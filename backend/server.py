"""
AI Studio Backend
Wraps ComfyUI with a clean REST API + WebSocket progress streaming.

Run with:
    uvicorn server:app --host 0.0.0.0 --port 7860 --reload
"""

import asyncio
import base64
import json
import os
import tempfile
import uuid
from pathlib import Path
from typing import Optional

import aiofiles
from fastapi import FastAPI, HTTPException, UploadFile, WebSocket, WebSocketDisconnect, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from comfy_client import ComfyClient
from workflow_builder import build_workflow, ensure_default_templates

# FireRed / diffusers backend (loaded lazily — only if a diffusers model is requested)
_firered_available = False
try:
    import firered as _firered_module
    _firered_available = _firered_module.is_available()
except ImportError:
    _firered_module = None

# ------------------------------------------------------------------ #
# Config                                                               #
# ------------------------------------------------------------------ #

COMFY_HOST = os.getenv("COMFY_HOST", "127.0.0.1")
COMFY_PORT = int(os.getenv("COMFY_PORT", "8188"))
MODELS_CONFIG_PATH = Path(__file__).parent.parent / "models_config.json"
COMFY_OUTPUT_DIR = Path(os.getenv("COMFY_OUTPUT_DIR", "/kaggle/working/ComfyUI/output"))
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app = FastAPI(title="AI Studio", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

comfy = ComfyClient(host=COMFY_HOST, port=COMFY_PORT)

# In-memory job tracking (survives the process; persisted to disk too)
jobs: dict[str, dict] = {}

# WebSocket connections keyed by connection_id
ws_connections: dict[str, WebSocket] = {}


def load_models_config() -> dict:
    with open(MODELS_CONFIG_PATH) as f:
        return json.load(f)


# ------------------------------------------------------------------ #
# Startup                                                              #
# ------------------------------------------------------------------ #

@app.on_event("startup")
async def startup():
    ensure_default_templates()
    print("AI Studio backend started.")
    print(f"Connecting to ComfyUI at {COMFY_HOST}:{COMFY_PORT}")


# ------------------------------------------------------------------ #
# Models & LoRAs                                                       #
# ------------------------------------------------------------------ #

@app.get("/api/models")
async def get_models():
    config = load_models_config()
    return config["models"]


@app.get("/api/loras")
async def get_loras():
    """Return available LoRAs from ComfyUI (remote API) with local fallback."""
    # Try remote ComfyUI first
    if await comfy.is_alive():
        names = await comfy.list_loras()
        if names:
            return [{"name": n, "filename": Path(n).name, "size_mb": None} for n in names]

    # Fallback: scan local filesystem (Kaggle / local dev)
    lora_dir = Path(os.getenv("COMFY_DIR", "/kaggle/working/ComfyUI")) / "models" / "loras"
    loras = []
    if lora_dir.exists():
        for f in lora_dir.rglob("*"):
            if f.suffix.lower() in (".safetensors", ".ckpt", ".pt"):
                loras.append({
                    "name": str(f.relative_to(lora_dir.parent.parent)),
                    "filename": f.name,
                    "size_mb": round(f.stat().st_size / 1024 / 1024, 1),
                })
    return loras


@app.get("/api/status")
async def get_status():
    """Health check + ComfyUI connection status."""
    comfy_alive = await comfy.is_alive()
    queue = {}
    if comfy_alive:
        try:
            queue = await comfy.get_queue()
        except Exception:
            pass
    return {
        "studio": "ok",
        "comfyui": "connected" if comfy_alive else "disconnected",
        "queue_running": len(queue.get("queue_running", [])),
        "queue_pending": len(queue.get("queue_pending", [])),
        "firered": "ready" if _firered_available else "unavailable",
    }


# ------------------------------------------------------------------ #
# Generation                                                           #
# ------------------------------------------------------------------ #

class GenerateRequest(BaseModel):
    model_id: str
    positive_prompt: str
    negative_prompt: str = ""
    width: Optional[int] = None
    height: Optional[int] = None
    frames: Optional[int] = None
    fps: Optional[int] = None
    steps: Optional[int] = None
    cfg: Optional[float] = None
    seed: int = -1
    loras: list = Field(default_factory=list)
    # Images — all base64-encoded PNG
    init_image_b64:   Optional[str] = None   # reference image for i2v / i2i edit
    first_frame_b64:  Optional[str] = None   # pin first frame (LTX, etc.)
    last_frame_b64:   Optional[str] = None   # pin last frame


@app.post("/api/generate")
async def generate(req: GenerateRequest):
    config = load_models_config()
    models = config.get("models", {})
    if req.model_id not in models:
        raise HTTPException(status_code=404, detail=f"Model '{req.model_id}' not found")

    model_config = models[req.model_id]

    # ── Diffusers backend (FireRed, etc.) ──────────────────────────────
    if model_config.get("backend") == "diffusers":
        return await _generate_diffusers(req, model_config)

    params = {
        "positive_prompt": req.positive_prompt,
        "negative_prompt": req.negative_prompt,
        "seed": req.seed,
        "loras": req.loras,
    }
    if req.width is not None:
        params["width"] = req.width
    if req.height is not None:
        params["height"] = req.height
    if req.frames is not None:
        params["frames"] = req.frames
    if req.fps is not None:
        params["fps"] = req.fps
    if req.steps is not None:
        params["steps"] = req.steps
    if req.cfg is not None:
        params["cfg"] = req.cfg

    async def upload_b64_image(b64_data: str, prefix: str) -> str:
        """Upload a base64 image to ComfyUI (remote API) or local input dir as fallback."""
        img_bytes = base64.b64decode(b64_data)
        filename = f"{prefix}_{uuid.uuid4().hex[:8]}.png"

        # Try remote upload first
        try:
            if await comfy.is_alive():
                return await comfy.upload_image(filename, img_bytes)
        except Exception:
            pass

        # Fallback: write to local ComfyUI input dir
        input_dir = Path(os.getenv("COMFY_DIR", "/kaggle/working/ComfyUI")) / "input"
        input_dir.mkdir(parents=True, exist_ok=True)
        (input_dir / filename).write_bytes(img_bytes)
        return filename

    if req.init_image_b64:
        params["init_image"] = await upload_b64_image(req.init_image_b64, "init")
    if req.first_frame_b64:
        params["first_frame"] = await upload_b64_image(req.first_frame_b64, "first")
    if req.last_frame_b64:
        params["last_frame"] = await upload_b64_image(req.last_frame_b64, "last")

    try:
        workflow = build_workflow(model_config, params)
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not await comfy.is_alive():
        raise HTTPException(status_code=503, detail="ComfyUI is not running")

    try:
        prompt_id = await comfy.queue_prompt(workflow)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ComfyUI error: {e}")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "job_id": job_id,
        "prompt_id": prompt_id,
        "model_id": req.model_id,
        "status": "queued",
        "progress": 0,
        "outputs": [],
        "error": None,
    }

    # Fire-and-forget background tracker
    asyncio.create_task(_track_job(job_id, prompt_id))

    return {"job_id": job_id, "prompt_id": prompt_id, "status": "queued"}


# ------------------------------------------------------------------ #
# Diffusers backend (FireRed, etc.)                                    #
# ------------------------------------------------------------------ #

async def _generate_diffusers(req: GenerateRequest, model_config: dict):
    """Handle generation for models with backend='diffusers' (e.g. FireRed)."""
    if _firered_module is None:
        raise HTTPException(status_code=503, detail="Diffusers not installed. Run: pip install diffusers transformers accelerate")
    if not _firered_available:
        raise HTTPException(status_code=503, detail="No CUDA GPU available for diffusers backend")
    if not req.init_image_b64:
        raise HTTPException(status_code=400, detail=f"{model_config['name']} requires an input image (Image Edit mode)")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "job_id": job_id,
        "prompt_id": None,
        "model_id": req.model_id,
        "status": "running",
        "progress": 10,
        "outputs": [],
        "error": None,
    }
    await _broadcast(job_id, {"type": "progress", "progress": 10, "job_id": job_id})

    asyncio.create_task(_run_diffusers_job(job_id, req, model_config))
    return {"job_id": job_id, "status": "running"}


async def _run_diffusers_job(job_id: str, req: GenerateRequest, model_config: dict):
    try:
        await _broadcast(job_id, {"type": "progress", "progress": 20, "job_id": job_id})

        # Run blocking inference in thread pool to avoid blocking the event loop
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: _firered_module.infer(
                image_b64=req.init_image_b64,
                prompt=req.positive_prompt,
                negative_prompt=req.negative_prompt or "deformed, blurry, bad anatomy, noisy",
                steps=req.steps or model_config.get("defaults", {}).get("steps", 4),
                guidance=req.cfg or model_config.get("defaults", {}).get("cfg", 1.0),
                seed=req.seed if req.seed != -1 else -1,
            )
        )

        # Save output image to a temp file so it can be served
        import tempfile, base64 as b64mod
        output_dir = Path(os.getenv("COMFY_DIR", "/kaggle/working/ComfyUI")) / "output"
        output_dir.mkdir(parents=True, exist_ok=True)
        fname = f"firered_{job_id[:8]}.png"
        fpath = output_dir / fname
        img_bytes = b64mod.b64decode(result["image_b64"])
        fpath.write_bytes(img_bytes)

        outputs = [{"type": "image", "filename": fname, "subfolder": "", "url": f"/api/output/{fname}"}]
        jobs[job_id]["status"] = "complete"
        jobs[job_id]["progress"] = 100
        jobs[job_id]["outputs"] = outputs
        await _broadcast(job_id, {"type": "complete", "job_id": job_id, "outputs": outputs})

    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["error"] = str(e)
        await _broadcast(job_id, {"type": "error", "job_id": job_id, "message": str(e)})


async def _track_job(job_id: str, prompt_id: str):
    """Background task: track a ComfyUI job and update jobs dict."""
    jobs[job_id]["status"] = "running"
    try:
        async for event in comfy.stream_progress(prompt_id):
            etype = event["type"]
            if etype == "progress":
                pct = int(event["value"] / max(event["max"], 1) * 100)
                jobs[job_id]["progress"] = pct
                await _broadcast(job_id, {"type": "progress", "progress": pct, "job_id": job_id})
            elif etype == "done":
                history = await comfy.get_history(prompt_id)
                outputs = _extract_outputs(history, prompt_id)
                jobs[job_id]["status"] = "complete"
                jobs[job_id]["progress"] = 100
                jobs[job_id]["outputs"] = outputs
                await _broadcast(job_id, {"type": "complete", "job_id": job_id, "outputs": outputs})
                return
            elif etype == "error":
                jobs[job_id]["status"] = "error"
                jobs[job_id]["error"] = event.get("message")
                await _broadcast(job_id, {"type": "error", "job_id": job_id, "message": event.get("message")})
                return
    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["error"] = str(e)
        await _broadcast(job_id, {"type": "error", "job_id": job_id, "message": str(e)})


def _extract_outputs(history: dict, prompt_id: str) -> list:
    outputs = []
    job_history = history.get(prompt_id, {})
    for node_id, node_output in job_history.get("outputs", {}).items():
        for img in node_output.get("images", []):
            outputs.append({
                "type": "image",
                "filename": img["filename"],
                "subfolder": img.get("subfolder", ""),
                "url": f"/api/output/{img['filename']}?subfolder={img.get('subfolder', '')}",
            })
        for vid in node_output.get("videos", []):
            outputs.append({
                "type": "video",
                "filename": vid["filename"],
                "subfolder": vid.get("subfolder", ""),
                "url": f"/api/output/{vid['filename']}?subfolder={vid.get('subfolder', '')}",
            })
    return outputs


async def _broadcast(job_id: str, message: dict):
    dead = []
    for cid, ws in ws_connections.items():
        try:
            await ws.send_json(message)
        except Exception:
            dead.append(cid)
    for cid in dead:
        ws_connections.pop(cid, None)


# ------------------------------------------------------------------ #
# Job status                                                           #
# ------------------------------------------------------------------ #

@app.get("/api/job/{job_id}")
async def get_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]


@app.get("/api/jobs")
async def list_jobs():
    return list(jobs.values())


@app.post("/api/cancel")
async def cancel():
    await comfy.interrupt()
    return {"status": "interrupted"}


# ------------------------------------------------------------------ #
# Output file serving                                                  #
# ------------------------------------------------------------------ #

@app.get("/api/output/{filename}")
async def serve_output(filename: str, subfolder: str = ""):
    try:
        data = await comfy.get_image_bytes(filename, subfolder, "output")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    ext = Path(filename).suffix.lower()
    media_types = {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp", ".mp4": "video/mp4", ".webm": "video/webm",
        ".gif": "image/gif",
    }
    media_type = media_types.get(ext, "application/octet-stream")
    return StreamingResponse(iter([data]), media_type=media_type)


# ------------------------------------------------------------------ #
# WebSocket for live progress                                          #
# ------------------------------------------------------------------ #

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cid = str(uuid.uuid4())
    ws_connections[cid] = websocket
    try:
        while True:
            # Keep alive; client can also send pings
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        ws_connections.pop(cid, None)


# ------------------------------------------------------------------ #
# RunPod GraphQL proxy (avoids CORS from the browser)                 #
# ------------------------------------------------------------------ #

class RunPodProxyRequest(BaseModel):
    query: str
    apiKey: str

@app.post("/api/runpod")
async def runpod_proxy(req: RunPodProxyRequest):
    """Proxy RunPod GraphQL requests to avoid browser CORS restrictions."""
    import aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.runpod.io/graphql",
            json={"query": req.query},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {req.apiKey}",
            },
        ) as resp:
            data = await resp.json()
            return JSONResponse(content=data, status_code=resp.status)


# ------------------------------------------------------------------ #
# Custom workflow upload                                               #
# ------------------------------------------------------------------ #

@app.post("/api/workflow/upload")
async def upload_workflow(
    name: str = Form(...),
    file: UploadFile = File(...)
):
    """Upload a custom ComfyUI API-format workflow JSON."""
    content = await file.read()
    try:
        workflow_json = json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    workflows_dir = Path(__file__).parent / "workflows"
    workflows_dir.mkdir(exist_ok=True)
    safe_name = "".join(c for c in name if c.isalnum() or c in "-_") + ".json"
    path = workflows_dir / safe_name
    async with aiofiles.open(path, "w") as f:
        await f.write(json.dumps(workflow_json, indent=2))

    return {"status": "ok", "workflow_file": safe_name}


# ------------------------------------------------------------------ #
# Serve frontend                                                       #
# ------------------------------------------------------------------ #

if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=7860, reload=False)
