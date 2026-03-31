#!/bin/bash
# Start AI Studio pointing at Vast.ai instance 33876269
# ComfyUI runs on port 18188 (direct, no auth) at the static IP

cd "$(dirname "$0")/backend"

COMFY_HOST=50.173.30.254 \
COMFY_PORT=18188 \
  uvicorn server:app --host 0.0.0.0 --port 7860 --reload
