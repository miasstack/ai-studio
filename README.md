# AI Studio

A clean UI for AI video/image generation, running on top of ComfyUI with Kaggle GPU backend.

## Project Structure

```
ai-studio/
├── frontend/
│   └── index.html          ← The UI (serves from FastAPI)
├── backend/
│   ├── server.py           ← FastAPI backend
│   ├── comfy_client.py     ← ComfyUI API wrapper
│   ├── workflow_builder.py ← Builds ComfyUI workflow JSON
│   ├── requirements.txt
│   └── workflows/          ← ComfyUI API-format JSON templates
│       ├── ltx_t2v.json
│       ├── ltx_i2v.json
│       └── wan_t2v.json
├── models_config.json      ← Model definitions & param mappings
└── kaggle/
    └── ai_studio_notebook.ipynb  ← Run this on Kaggle
```

## Quick Start (Kaggle)

1. Upload `ai_studio_notebook.ipynb` to Kaggle
2. Upload `backend/` files as a Kaggle dataset named `ai-studio-backend`
3. Run all cells — the studio URL prints at the end of Cell 11

## Adding a New Model

1. Build/test the workflow in ComfyUI
2. Export as **API format** JSON (Settings → Save → API Format)
3. Drop the file in `backend/workflows/your_model.json`
4. Add an entry to `models_config.json`:

```json
"your-model-id": {
  "id": "your-model-id",
  "name": "Display Name",
  "category": "video",
  "mode": "t2v",
  "label": "Text → Video",
  "workflow_file": "your_model.json",
  "param_nodes": {
    "positive_prompt": {"node_id": "NODE_ID", "field": "text"},
    "negative_prompt": {"node_id": "NODE_ID", "field": "text"},
    "steps": {"node_id": "NODE_ID", "field": "steps"},
    "seed": {"node_id": "NODE_ID", "field": "seed"}
  },
  "lora_insert_after_node": "1",
  "defaults": {"width": 768, "height": 512, "frames": 97, "steps": 30, "cfg": 3.0},
  "resolutions": ["768x512", "512x768"],
  "vram_gb": 10
}
```

Node IDs come from the exported API JSON — just open it and find which node
handles prompts, steps, etc.

## Using Your Associate's Workflow

1. In ComfyUI, go to **Settings → Save (API Format)** to export the workflow JSON
2. In the Kaggle notebook Cell 8, set `ASSOCIATE_WORKFLOW_PATH` to the file
3. Add a model entry in `models_config.json` pointing to it
4. The UI will show it as a selectable model

## LoRA Support

LoRAs placed in `ComfyUI/models/loras/` appear automatically in the UI.
The LoRA injector inserts LoraLoader nodes into the workflow chain after the
base model loader node (`lora_insert_after_node` in config).

## Local Development

```bash
cd backend
pip install -r requirements.txt
# Point at a running ComfyUI instance:
COMFY_HOST=127.0.0.1 COMFY_PORT=8188 COMFY_DIR=/path/to/ComfyUI \
  uvicorn server:app --reload --port 7860
# Open http://localhost:7860
```
