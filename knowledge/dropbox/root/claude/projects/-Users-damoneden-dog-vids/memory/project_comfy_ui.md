---
name: ComfyUI local setup
description: Local ComfyUI Desktop install on Mac, WAN 2.2 i2v LoRA pipeline, model locations and what's missing
type: project
originSessionId: c28de4a2-fa9f-4ba9-8650-2e07820ca04a
---
ComfyUI is installed as a desktop app at `/Applications/ComfyUI.app`. User data moved to `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/` (was on Desktop, moved by user to Dropbox for backup).

**Why:** Building a pipeline for adult content (Mia Suprema character) using WAN 2.2 i2v + custom LoRAs. Mac MPS is too slow for 14B models — runs on RunPod cloud GPU. AI Studio (`~/ai-studio`) is the UI; frontend served locally at localhost:8080.

## Key paths
- Models: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/models/`
- Workflows: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/user/default/workflows/`
- Output: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/output/`
- Controller script: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/comfy_controller.py`
- Skill command: `~/.claude/commands/comfy_local.md`
- Python venv: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/.venv/bin/python`
- API (local only): `http://localhost:8188`
- AI Studio frontend: `~/ai-studio/frontend/index.html`
- RunPod API key: `~/ai-studio/.env` → `RUNPOD_API_KEY`
- RunPod network volume: `js7r7jbbln` (Mia's Storage, 250GB, EUR-NO-1)

## Models installed ✅ (in Dropbox comfy flics/models/)
- **VAE**: `vae/wan_2.1_vae.safetensors`, `vae/ae.safetensors` (Flux)
- **Text encoders**: `text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `text_encoders/clip_l.safetensors`, `text_encoders/t5/t5xxl_fp16.safetensors`, `text_encoders/qwen/qwen_2.5_vl_7b_fp8_scaled.safetensors`
- **LoRAs** in `models/loras/wan 2.2/`:
  - DR34ML4Y_I2V_14B_HIGH/LOW (primary Mia LoRAs)
  - m14-highnoise/lownoise, wan22-cunilingus H/L
  - NSFW-22-H/L, BouncyWalk02 H/L, Sensual_fingering H/L
  - WAN-2.2-I2V-Handjob H/L, Orgasm-HIGH, POV-Titfuck-LOW
  - reverse_suspended_congress H/L, oral-insertion H/L
  - LongCat_distill, Pornmaster-SlowTwerk H/L, Wan21_T2V, Qv_lora

## Still missing ❌
- `Wan_2.2_I2V_HighNoise_10steps_fp8.safetensors` → `diffusion_models/` (0 bytes on RunPod volume, need real source)
- `Wan_2.2_I2V_LowNoise_10steps_fp8.safetensors` → `diffusion_models/` (same)
- WAN2.2-Pussy H/L, WAN-Orgasm-LOW, WAN-POV-Titfuck-HIGH, Wan21_T2V — failed to download from pod (still on network volume `js7r7jbbln`)

## Workflow
- `wan22_i2v_mia.json` — DR34ML4Y LoRAs, dual-pass KSamplerAdvanced, VHS_VideoCombine MP4 output
- `Wan 2.2 I2V NSFW.json`, `LongCat img2video.json`, `wan2.2-text-2-img.json` — downloaded from RunPod

## RunPod setup
- Network volume `js7r7jbbln` has all models at `/workspace/ComfyUI/models/`
- To spin up: create pod with `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`, mount volume, run startup.sh
- Pod backend runs on port 7860, ComfyUI on 8188
- Public URL format: `https://<pod-id>-7860.proxy.runpod.net`
