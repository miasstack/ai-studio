---
name: ComfyUI Wan 2.2 I2V NSFW on Vast.ai
description: Status of ComfyUI Wan 2.2 I2V NSFW workflow setup on Vast.ai instance, including what's installed, what's working, and what still needs to be done.
type: project
tags: [ai-generation, video-generation, comfyui, vastai, nsfw, wan2.2, lora, diffusion-models, content-pipeline]
related:
  - feedback_vastai_workflow.md
  - reference_character_sheet_prompt.md
originSessionId: fb4781fa-5525-434f-88dc-126c2c8f3c76
---
# ComfyUI Wan 2.2 I2V NSFW — Vast.ai Setup State

**Goal:** Get the Wan 2.2 I2V NSFW workflow fully running on Vast.ai, then automate it into a content generation pipeline.

**Why:** User wants to test generation works manually before building automation.

**How to apply:** When continuing this project, reference this to avoid re-doing completed work.

## Relationship to Other Projects

- **[Vast.ai download feedback](feedback_vastai_workflow.md)** — Critical lesson learned: always use wget for model downloads on this instance, never hf_hub_download + shutil.move.
- **[Higgsfield Character Sheet Prompt](reference_character_sheet_prompt.md)** — Both this project and the Higgsfield prompt are part of the same AI content generation workflow. Character sheets from Higgsfield feed as reference images into Wan 2.2 I2V.

---

## Current Instance (as of 2026-03-31)

- **Instance ID:** 33876269
- **IP:** 50.173.30.254
- **GPU:** RTX 4090, Oregon US
- **Cost:** $0.303/hr GPU
- **Portal:** `https://attraction-oscar-shaw-amino.trycloudflare.com/#/apps`
- **ComfyUI:** `https://likelihood-kenneth-leon-socket.trycloudflare.com/?token=f11e3a9959336bcb4a825d2cc90f1bfb09a8e479359d5bb96f4591b92d1d8340`
- **Jupyter:** `https://entrance-salvation-disposal-tennessee.trycloudflare.com`
- **Jupyter Token:** `f11e3a9959336bcb4a825d2cc90f1bfb09a8e479359d5bb96f4591b92d1d8340`
- **ComfyUI Caddy auth:** Use `?token=f11e3a9959336bcb4a825d2cc90f1bfb09a8e479359d5bb96f4591b92d1d8340` in URL to bypass login

**NOTE:** Cloudflare tunnel URLs change on restart. Find new ones via the portal or Vast.ai console.

---

## Installed Custom Nodes

All installed in `/workspace/ComfyUI/custom_nodes/`:
- `ComfyUI-WanVideoWrapper` (provides `WanImageToVideo`)
- `rgthree-comfy` (provides `Power Lora Loader (rgthree)`)
- `ComfyUI-VideoHelperSuite` (provides `VHS_VideoCombine`)
- `ComfyUI-KJNodes` (provides `PathchSageAttentionKJ`)
- `ComfyUI-Manager`

---

## Models — Downloaded via wget (see [download feedback](feedback_vastai_workflow.md))

- `diffusion_models/Wan_2.2_I2V_HighNoise_10steps_fp8.safetensors` (~14GB)
- `diffusion_models/Wan_2.2_I2V_LowNoise_10steps_fp8.safetensors` (~14GB)
- `clip/umt5_xxl_fp8_e4m3fn_scaled.safetensors` (~5GB)
- `vae/wan_2.1_vae.safetensors` (~0.4GB)

**Important:** First download attempt used `hf_hub_download` + `shutil.move` which moved symlinks, not actual files. Re-downloaded using wget directly to `/workspace/ComfyUI/models/*/filename`.

---

## LoRAs

All in `/workspace/ComfyUI/models/loras/`:
- Root level: `NSFW-22-H-e8.safetensors`, `NSFW-22-L-e8.safetensors`
- Subdirectory `wan 2.2/`: DR34ML4Y high/low, wan22-cunilingus high/low, reverse_suspended_congress high/low, WAN-2.2-I2V-Handjob high/low, WAN-2.2-I2V-POV-Titfuck high/low, Sensual_fingering high/low, BouncyWalk02 high/low, Pornmaster Slow Twerk high/low

Local files NOT yet uploaded (not in workflow so not needed for test):
- `Qv_8bEmM86wrtPnwibRrj_pytorch_lora_weights.safetensors`
- `m14-highnoise.safetensors` / `m14-lownoise.safetensors`

---

## Workflow

- File: `Wan 2.2 I2V NSFW.json` (local at `/Users/damoneden/Desktop/mias-storage-backup/`)
- Uploaded to instance at: `/workspace/ComfyUI/user/default/workflows/Wan_2.2_I2V_NSFW.json`
- Node 214 (LoadImage) needs an input image — use `test_input.png` (already uploaded to ComfyUI input dir) or upload a real image via `/upload/image`

### How to queue via browser JS (after loading workflow):
```javascript
fetch('/api/userdata/workflows%2FWan_2.2_I2V_NSFW.json')
  .then(r => r.json())
  .then(async wf => {
    await window.app.loadGraphData(wf);
    const loadImg = window.app.graph._nodes.find(n => n.type === 'LoadImage');
    if (loadImg) loadImg.widgets[0].value = 'test_input.png';
    await new Promise(r => setTimeout(r, 500));
    const p = await window.app.graphToPrompt();
    const resp = await fetch('/prompt', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({prompt: p.output, client_id: window.app.api.clientId, extra_data: {extra_pnginfo: {workflow: p.workflow}}})
    });
    const data = await resp.json();
    console.log(data);
  });
```

---

## Test Generation Status (2026-03-31)

- **Prompt ID:** `3a556313-5552-4b63-86e2-d9283b0565f3`
- **Status at session end:** Running, `[0%][80%]` — actively processing
- **Input image:** `test_input.png` (64x64 solid color test image)

**If generation completed:** Check history at `GET /history/3a556313-5552-4b63-86e2-d9283b0565f3`, look for GIF output in node 135 (VHS_VideoCombine)

---

## Next Steps

1. Verify test generation produced output GIF
2. Upload a real NSFW reference image for proper test
3. Build automation pipeline (API wrapper at port 8288 / `forgot-marie-autos-formal.trycloudflare.com`)
4. The API wrapper accepts workflow payloads — integrate with whatever front-end automation system
