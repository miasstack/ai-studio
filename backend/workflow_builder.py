"""
Builds ComfyUI API-format workflow JSON from user parameters.

Adding a new model:
  1. Export workflow from ComfyUI as "API format" JSON
  2. Save in backend/workflows/<name>.json
  3. Add entry in models_config.json
  4. Fill in param_nodes to map logical params → node IDs

LoRA injection inserts LoraLoader nodes inline in the model chain.
First/last frame injection adds guide nodes for models that support it (e.g. LTX).
"""

import copy
import json
import os
import random
from pathlib import Path

WORKFLOWS_DIR = Path(__file__).parent / "workflows"


def load_template(workflow_file: str) -> dict:
    path = WORKFLOWS_DIR / workflow_file
    if not path.exists():
        raise FileNotFoundError(
            f"Workflow template not found: {path}\n"
            f"Export your workflow from ComfyUI (API format) and save it there."
        )
    with open(path) as f:
        return json.load(f)


def apply_params(workflow: dict, param_nodes: dict, params: dict) -> dict:
    """Patch workflow node inputs per the models_config param_nodes mapping."""
    wf = copy.deepcopy(workflow)
    for param_name, mapping in param_nodes.items():
        if param_name not in params:
            continue
        node_id = str(mapping["node_id"])
        field = mapping["field"]
        if node_id in wf and "inputs" in wf[node_id]:
            wf[node_id]["inputs"][field] = params[param_name]
    return wf


def inject_loras(workflow: dict, loras: list, after_node: str) -> dict:
    """
    Insert LoraLoader nodes after `after_node` and rewire downstream consumers.
    loras: [{"name": str, "strength_model": float, "strength_clip": float}]
    """
    if not loras:
        return workflow

    wf = copy.deepcopy(workflow)
    max_id = max(int(k) for k in wf.keys())
    after_node_str = str(after_node)

    prev_model_ref = [after_node_str, 0]
    prev_clip_ref  = [after_node_str, 1]
    new_lora_ids = []

    for lora in loras:
        max_id += 1
        lora_id = str(max_id)
        wf[lora_id] = {
            "inputs": {
                "lora_name": lora["name"],
                "strength_model": lora.get("strength_model", 1.0),
                "strength_clip":  lora.get("strength_clip",  1.0),
                "model": prev_model_ref,
                "clip":  prev_clip_ref,
            },
            "class_type": "LoraLoader",
            "_meta": {"title": f"LoRA: {lora['name']}"},
        }
        prev_model_ref = [lora_id, 0]
        prev_clip_ref  = [lora_id, 1]
        new_lora_ids.append(lora_id)

    # Rewire downstream nodes that were connected to after_node outputs 0 and 1
    for node_id, node in wf.items():
        if node_id in new_lora_ids:
            continue
        for key, val in node.get("inputs", {}).items():
            if isinstance(val, list) and len(val) == 2 and str(val[0]) == after_node_str:
                if val[1] == 0:
                    node["inputs"][key] = prev_model_ref
                elif val[1] == 1:
                    node["inputs"][key] = prev_clip_ref

    return wf


def inject_first_last_frames(
    workflow: dict,
    model_config: dict,
    first_frame_filename: str | None,
    last_frame_filename:  str | None,
    total_frames: int,
) -> dict:
    """
    Inject LTXVAddGuide nodes for first-frame and/or last-frame conditioning.
    Works for LTX Video; can be extended for other models by changing the
    model_config['first_frame_node'] value.

    The guide node takes:
      pipeline/model, conditioning (positive), image, index, strength
    and outputs updated conditioning.

    We chain:
      positive_encode → [LTXVAddGuide frame=0] → [LTXVAddGuide frame=-1] → sampler
    """
    if not first_frame_filename and not last_frame_filename:
        return workflow

    node_type = model_config.get("first_frame_node", "LTXVAddGuide")
    positive_node_id = str(model_config.get("first_frame_positive_node_id", "6"))

    wf = copy.deepcopy(workflow)
    max_id = max(int(k) for k in wf.keys())

    # Find sampler node — it's the one consuming the positive conditioning
    # We look for any node that has an input pointing to [positive_node_id, 0]
    sampler_node_id = None
    sampler_positive_input_key = None
    for nid, node in wf.items():
        for key, val in node.get("inputs", {}).items():
            if isinstance(val, list) and len(val) == 2 and str(val[0]) == positive_node_id and val[1] == 0:
                sampler_node_id = nid
                sampler_positive_input_key = key

    if sampler_node_id is None:
        # Can't inject — return unchanged
        return wf

    # Find model node id — first_frame_node also needs a model/pipeline input
    # We look for the node that feeds MODEL output [*, 0] into the sampler
    model_node_ref = None
    for key, val in wf[sampler_node_id].get("inputs", {}).items():
        if isinstance(val, list) and len(val) == 2 and val[1] == 0 and key.lower() in ("model", "pipeline", "ltxv_model"):
            model_node_ref = val
            break

    current_cond_ref = [positive_node_id, 0]

    def add_guide_node(filename: str, frame_index: int) -> str:
        nonlocal max_id
        max_id += 1
        nid = str(max_id)

        inputs = {
            "conditioning": current_cond_ref,
            "image": _load_image_ref(wf, filename, max_id + 1000),
            "index": frame_index,
            "strength": 1.0,
        }
        if model_node_ref:
            inputs["pipeline"] = model_node_ref

        wf[nid] = {
            "inputs": inputs,
            "class_type": node_type,
            "_meta": {"title": f"Guide Frame {frame_index}"},
        }
        return nid

    if first_frame_filename:
        guide_id = add_guide_node(first_frame_filename, 0)
        current_cond_ref = [guide_id, 0]

    if last_frame_filename:
        last_idx = max(total_frames - 1, 1)
        guide_id = add_guide_node(last_frame_filename, last_idx)
        current_cond_ref = [guide_id, 0]

    # Rewire sampler's positive input to the last guide node output
    wf[sampler_node_id]["inputs"][sampler_positive_input_key] = current_cond_ref

    return wf


def _load_image_ref(wf: dict, filename: str, hint_id: int) -> list:
    """
    Find or create a LoadImage node for filename; return [node_id, 0].
    """
    # Check if a LoadImage node for this filename already exists
    for nid, node in wf.items():
        if node.get("class_type") == "LoadImage" and node.get("inputs", {}).get("image") == filename:
            return [nid, 0]

    # Create one
    new_id = str(max(int(k) for k in wf.keys()) + 1)
    wf[new_id] = {
        "inputs": {"image": filename, "upload": "image"},
        "class_type": "LoadImage",
        "_meta": {"title": f"Load {filename}"},
    }
    return [new_id, 0]


def build_workflow(model_config: dict, params: dict) -> dict:
    """
    Main entry point. Returns a ComfyUI API-format workflow.

    params keys (all optional; fall back to model defaults):
      positive_prompt, negative_prompt
      width, height, frames, fps
      steps, cfg, seed
      loras: [{"name": str, "strength_model": float, "strength_clip": float}]
      init_image:         filename (for i2v — init image in ComfyUI /input)
      first_frame:        filename (pinned first frame)
      last_frame:         filename (pinned last frame)
    """
    template = load_template(model_config.get("workflow_file", "custom.json"))

    # Merge defaults → user params
    merged = {**model_config.get("defaults", {}), **params}

    if "seed" not in merged or merged["seed"] == -1:
        merged["seed"] = random.randint(0, 2**32 - 1)

    workflow = apply_params(template, model_config.get("param_nodes", {}), merged)

    # LoRA injection
    after_node = model_config.get("lora_insert_after_node")
    loras = params.get("loras", [])
    if loras and after_node:
        workflow = inject_loras(workflow, loras, after_node)

    # First/last frame injection (video models only)
    if model_config.get("supports_first_frame") or model_config.get("supports_last_frame"):
        first_frame = params.get("first_frame")
        last_frame  = params.get("last_frame")
        if first_frame or last_frame:
            workflow = inject_first_last_frames(
                workflow,
                model_config,
                first_frame if model_config.get("supports_first_frame") else None,
                last_frame  if model_config.get("supports_last_frame")  else None,
                merged.get("frames", 97),
            )

    return workflow


# ------------------------------------------------------------------ #
# Default workflow templates                                          #
# ------------------------------------------------------------------ #

def _ltx_t2v() -> dict:
    return {
      "1": {"inputs": {"ckpt_name": "ltx-video-2b-v0.9.5.safetensors"}, "class_type": "LTXVLoader", "_meta": {"title": "LTX Loader"}},
      "2": {"inputs": {"clip_name": "t5xxl_fp16.safetensors", "type": "ltxv"}, "class_type": "CLIPLoader", "_meta": {"title": "T5 Clip"}},
      "6": {"inputs": {"text": "cinematic video", "clip": ["2", 0]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Positive"}},
      "7": {"inputs": {"text": "worst quality, blurry", "clip": ["2", 0]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Negative"}},
      "5": {"inputs": {"width": 768, "height": 512, "video_frames": 97, "batch_size": 1}, "class_type": "LTXVEmptyLatentVideo"},
      "3": {"inputs": {"model": ["1", 0], "positive": ["6", 0], "negative": ["7", 0],
              "latent_image": ["5", 0], "noise_seed": 42, "steps": 30, "cfg": 3.0,
              "sampler_name": "euler", "scheduler": "ltv_uniform"}, "class_type": "LTXVSampler"},
      "9": {"inputs": {"samples": ["3", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
      "10": {"inputs": {"frame_rate": 24, "loop_count": 0, "filename_prefix": "ltx_video",
               "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19,
               "save_metadata": True, "pingpong": False, "save_output": True, "images": ["9", 0]},
             "class_type": "VHS_VideoCombine"}
    }


def _ltx_i2v() -> dict:
    """LTX image-to-video: LoadImage feeds into LTXVImgToVideo node."""
    return {
      "1": {"inputs": {"ckpt_name": "ltx-video-2b-v0.9.5.safetensors"}, "class_type": "LTXVLoader"},
      "2": {"inputs": {"clip_name": "t5xxl_fp16.safetensors", "type": "ltxv"}, "class_type": "CLIPLoader"},
      "20": {"inputs": {"image": "init_image.png", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference Image"}},
      "6": {"inputs": {"text": "cinematic video", "clip": ["2", 0]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Positive"}},
      "7": {"inputs": {"text": "worst quality, blurry", "clip": ["2", 0]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Negative"}},
      "5": {"inputs": {"width": 768, "height": 512, "video_frames": 97, "batch_size": 1,
              "image": ["20", 0]}, "class_type": "LTXVEmptyLatentVideo"},
      "3": {"inputs": {"model": ["1", 0], "positive": ["6", 0], "negative": ["7", 0],
              "latent_image": ["5", 0], "noise_seed": 42, "steps": 30, "cfg": 3.0,
              "sampler_name": "euler", "scheduler": "ltv_uniform"}, "class_type": "LTXVSampler"},
      "9": {"inputs": {"samples": ["3", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
      "10": {"inputs": {"frame_rate": 24, "loop_count": 0, "filename_prefix": "ltx_i2v",
               "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19,
               "save_metadata": True, "pingpong": False, "save_output": True, "images": ["9", 0]},
             "class_type": "VHS_VideoCombine"}
    }


def _wan_t2v() -> dict:
    return {
      "1": {"inputs": {"model_path": "models/wan/Wan2.1-T2V-1.3B"}, "class_type": "WanVideoModelLoader"},
      "6": {"inputs": {"text": "a beautiful landscape", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Positive"}},
      "7": {"inputs": {"text": "worst quality", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Negative"}},
      "5": {"inputs": {"width": 832, "height": 480, "video_frames": 81, "batch_size": 1}, "class_type": "WanVideoEmptyLatent"},
      "3": {"inputs": {"model": ["1", 0], "positive": ["6", 0], "negative": ["7", 0],
              "latents": ["5", 0], "steps": 30, "guidance_scale": 6.0, "seed": 42}, "class_type": "WanVideoSampler"},
      "9": {"inputs": {"samples": ["3", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
      "10": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "wan_video",
               "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19,
               "save_metadata": True, "pingpong": False, "save_output": True, "images": ["9", 0]},
             "class_type": "VHS_VideoCombine"}
    }


def _wan_i2v() -> dict:
    return {
      "1": {"inputs": {"model_path": "models/wan/Wan2.1-I2V-14B-480P"}, "class_type": "WanVideoModelLoader"},
      "20": {"inputs": {"image": "init_image.png", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference Image"}},
      "6": {"inputs": {"text": "a beautiful landscape", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Positive"}},
      "7": {"inputs": {"text": "worst quality", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Negative"}},
      "5": {"inputs": {"width": 832, "height": 480, "video_frames": 81, "batch_size": 1,
              "image": ["20", 0]}, "class_type": "WanVideoEmptyLatent"},
      "3": {"inputs": {"model": ["1", 0], "positive": ["6", 0], "negative": ["7", 0],
              "latents": ["5", 0], "steps": 30, "guidance_scale": 6.0, "seed": 42}, "class_type": "WanVideoSampler"},
      "9": {"inputs": {"samples": ["3", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
      "10": {"inputs": {"frame_rate": 16, "loop_count": 0, "filename_prefix": "wan_i2v",
               "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19,
               "save_metadata": True, "pingpong": False, "save_output": True, "images": ["9", 0]},
             "class_type": "VHS_VideoCombine"}
    }


def _sdxl_t2i() -> dict:
    return {
      "1": {"inputs": {"ckpt_name": "sd_xl_base_1.0.safetensors"}, "class_type": "CheckpointLoaderSimple", "_meta": {"title": "Load SDXL"}},
      "2": {"inputs": {"text": "a beautiful image", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Positive"}},
      "3": {"inputs": {"text": "worst quality, blurry, watermark", "clip": ["1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "Negative"}},
      "4": {"inputs": {"width": 1024, "height": 1024, "batch_size": 1}, "class_type": "EmptyLatentImage"},
      "5": {"inputs": {"model": ["1", 0], "positive": ["2", 0], "negative": ["3", 0],
              "latent_image": ["4", 0], "seed": 42, "steps": 30, "cfg": 7.0,
              "sampler_name": "euler", "scheduler": "karras", "denoise": 1.0}, "class_type": "KSampler"},
      "6": {"inputs": {"samples": ["5", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
      "7": {"inputs": {"filename_prefix": "sdxl_image", "images": ["6", 0]}, "class_type": "SaveImage"}
    }


def ensure_default_templates():
    WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
    templates = {
        "ltx_t2v.json": _ltx_t2v,
        "ltx_i2v.json": _ltx_i2v,
        "wan_t2v.json": _wan_t2v,
        "wan_i2v.json": _wan_i2v,
        "sdxl_t2i.json": _sdxl_t2i,
    }
    for filename, generator in templates.items():
        path = WORKFLOWS_DIR / filename
        if not path.exists():
            with open(path, "w") as f:
                json.dump(generator(), f, indent=2)
