Control the local ComfyUI instance at localhost:8188 to generate images and videos.

## Setup facts
- ComfyUI base: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics`
- Controller script: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/comfy_controller.py`
- Python venv: `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/.venv/bin/python`
- Device: MPS (Apple Silicon) — generation is slower than GPU; be patient
- Text-to-image: Flux 2 Dev (`flux2-dev.safetensors` in `diffusion_models/`)
- Image-to-video: WAN 2.2 i2v models (in `models/` — auto-discovered)
- Do NOT download any new models

## Step 1 — ensure ComfyUI is running

```bash
curl -s --max-time 3 http://localhost:8188/system_stats
```

If that fails (no response or error), tell the user:
> "Please open the ComfyUI Desktop app and wait for it to finish loading, then run the command again."
Do not proceed until ComfyUI responds.

## Step 2 — discover available models

Run this before every generation to find what's installed:

```bash
"/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/.venv/bin/python" \
  "/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/comfy_controller.py" discover
```

This prints JSON with available model names per loader type. Use this to verify the right models exist before proceeding.

**Required model files** (place in `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/models/`):

| Model | Folder | Filename |
|---|---|---|
| Flux 2 Dev UNET | `diffusion_models/` | `flux2-dev.safetensors` |
| Flux text encoders | `text_encoders/` | `t5xxl_fp16.safetensors`, `clip_l.safetensors` |
| Flux VAE | `vae/` | `ae.safetensors` |
| WAN i2v high-noise | `diffusion_models/` | `Wan_2.2_I2V_HighNoise_10steps_fp8.safetensors` |
| WAN i2v low-noise | `diffusion_models/` | `Wan_2.2_I2V_LowNoise_10steps_fp8.safetensors` |
| WAN T5 encoder | `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` |
| WAN VAE | `vae/` | `wan_2.1_vae.safetensors` |

## Step 3a — text-to-image (Flux 2 Dev)

```bash
"/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/.venv/bin/python" \
  "/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/comfy_controller.py" txt2img \
  "YOUR PROMPT HERE" \
  --width 1024 --height 1024 --steps 20
```

Common aspect ratios for Shorts:
- Portrait 9:16 → `--width 576 --height 1024`
- Square 1:1 → `--width 1024 --height 1024`
- Landscape 16:9 → `--width 1024 --height 576`

The script prints `RESULT: /path/to/output.png` when done. Show the user that path.

## Step 3b — image-to-video (WAN 2.2 i2v)

```bash
"/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/.venv/bin/python" \
  "/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/comfy_controller.py" img2vid \
  "/path/to/source_image.png" \
  "motion description prompt" \
  --frames 81 --fps 16 --steps 30
```

- `--frames 81` = ~5 seconds at 16fps (keep under 97 for memory)
- The script copies the image into ComfyUI's input folder automatically
- Prints `RESULT: /path/to/output.webp` when done

## Step 4 — use output in the Dog Vids pipeline

Generated images land in `/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/output/`.

To use a generated image as a frame in the Dog Vids pipeline, copy it:
```bash
cp "/Users/damoneden/Kidnation Dropbox/damon eden/comfy flics/output/comfy_flux_XXXXX.png" \
   "/Users/damoneden/dog vids/images/"
```

## Troubleshooting

**Workflow errors / node not found:**
- Run `discover` again and check if the required nodes exist (e.g. `WanVideoModelLoader`, `CLIPTextEncodeFlux`, `FluxGuidance`).
- If a node is missing, the custom node that provides it may not be installed in ComfyUI Manager.
- Check ComfyUI Manager → "Missing Nodes" and install them.

**Out of memory (MPS):**
- Reduce `--steps` to 10–15
- Reduce resolution: `--width 768 --height 768`
- For video: reduce `--frames` to 49

**WAN workflow node names changed:**
- The WAN API nodes (`WanVideoModelLoader`, `WanImageToVideoConditioningWithEmbeds`, `VAEDecodeVideo`) depend on the ComfyUI version.
- If they fail, run `discover` and check which WAN-related nodes are actually listed, then edit `comfy_controller.py` → `build_wan_workflow()` to match the correct node names.

**Slow generation:**
- Expected on MPS. Flux 2 Dev at 1024×1024 takes ~3–8 min. WAN video at 81 frames takes 15–30 min.
- Stream output to the user so they know it's still running.

## Critique loop — always do this after generating

After every generation, run three passes before showing the user the final result:

**Pass 1 — Generate**
Run the generation command as normal. Get the output file.

**Pass 2 — Critique**
Look at the result (Read the image file if it's an image; note the video path if it's video). Then ask yourself:
- Does it match what the user actually asked for?
- Is the subject clear and well-framed?
- Are there obvious flaws (blurry faces, wrong anatomy, weird artifacts)?
- For video: does it have natural motion or does it look frozen/static?
- Score it 1–10. Write down exactly what's wrong.

**Pass 3 — Improve**
If the score is 7 or lower:
- Rewrite the prompt to fix the specific issues from Pass 2 (more detail, different wording, clearer action)
- Adjust settings if needed (more steps, different resolution, different LoRA strength)
- Run generation again with the improved prompt
- Show the user BOTH outputs and explain what changed and why the second is better

If the score is 8 or higher, show the result and briefly say why it worked well.

Don't tell the user "I'm running the critique loop" — just do it and show the better result.
