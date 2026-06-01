---
name: Vast.ai ComfyUI model download approach
description: Use wget to download HuggingFace models directly, never hf_hub_download + shutil.move which moves symlinks not actual data
type: feedback
---

Always use `wget -O /target/path.safetensors "https://huggingface.co/..."` to download models to Vast.ai instances. Never use `hf_hub_download()` + `shutil.move()` — HF hub creates symlinks into a blob cache, and shutil.move moves the symlink leaving a broken link.

**Why:** We had to re-download ~33GB of models because the first attempt with hf_hub_download + shutil.move left broken symlinks with the blobs gone.

**How to apply:** Any time downloading HuggingFace models to ComfyUI model directories on Vast.ai (or any server), use wget or curl with `-o /direct/path/filename.safetensors`.
