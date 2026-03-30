#!/bin/bash
# ============================================================
# AI Studio — RunPod Pod Startup Script
# Runs automatically when the pod starts via the RunPod template.
# ============================================================

set -e
WORK_DIR="/workspace"
STUDIO_DIR="$WORK_DIR/ai-studio"
COMFY_DIR="$WORK_DIR/ComfyUI"
LOG="$WORK_DIR/startup.log"

echo "=== AI Studio startup $(date) ===" | tee -a $LOG

# ── 1. Install system deps (cached after first run) ──────────────────
apt-get update -qq
apt-get install -y -qq ffmpeg libgl1-mesa-glx libglib2.0-0 git wget curl 2>/dev/null

# ── 2. Install / update ComfyUI ──────────────────────────────────────
if [ ! -d "$COMFY_DIR" ]; then
  echo "Cloning ComfyUI..." | tee -a $LOG
  git clone --depth=1 https://github.com/comfyanonymous/ComfyUI "$COMFY_DIR"
  pip install -q -r "$COMFY_DIR/requirements.txt"
fi

for d in checkpoints clip vae loras wan diffusion_models unet text_encoders; do
  mkdir -p "$COMFY_DIR/models/$d"
done
mkdir -p "$COMFY_DIR/input" "$COMFY_DIR/output"

# ── 3. Install / update custom nodes ─────────────────────────────────
CUSTOM="$COMFY_DIR/custom_nodes"
mkdir -p "$CUSTOM"

install_node() {
  local name=$1 url=$2
  if [ ! -d "$CUSTOM/$name" ]; then
    echo "Installing $name..." | tee -a $LOG
    git clone --depth=1 "$url" "$CUSTOM/$name"
    [ -f "$CUSTOM/$name/requirements.txt" ] && pip install -q -r "$CUSTOM/$name/requirements.txt"
  fi
}

install_node "ComfyUI-Manager"          "https://github.com/ltdrdata/ComfyUI-Manager"
install_node "ComfyUI-VideoHelperSuite" "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite"
install_node "ComfyUI-LTXVideo"         "https://github.com/Lightricks/ComfyUI-LTXVideo"
install_node "ComfyUI-WanVideoWrapper"  "https://github.com/kijai/ComfyUI-WanVideoWrapper"

# ── 4. Install / update AI Studio backend ────────────────────────────
GITHUB_REPO="${AI_STUDIO_REPO:-}"   # set in pod env vars: AI_STUDIO_REPO=https://github.com/YOU/ai-studio

if [ -d "$STUDIO_DIR/.git" ]; then
  echo "Updating AI Studio..." | tee -a $LOG
  git -C "$STUDIO_DIR" pull --ff-only 2>/dev/null || true
elif [ -n "$GITHUB_REPO" ]; then
  echo "Cloning AI Studio from $GITHUB_REPO..." | tee -a $LOG
  git clone --depth=1 "$GITHUB_REPO" "$STUDIO_DIR"
else
  echo "WARNING: AI_STUDIO_REPO env var not set and $STUDIO_DIR not found." | tee -a $LOG
  echo "Set AI_STUDIO_REPO in pod environment variables." | tee -a $LOG
fi

# Symlink network-volume model dirs into ComfyUI so models persist between pods
# Network volume is mounted at /workspace; ComfyUI expects models under /workspace/ComfyUI/models/
# We store actual model files at /workspace/models/ and symlink into ComfyUI
MODELS_STORE="$WORK_DIR/models"
mkdir -p "$MODELS_STORE"/{checkpoints,clip,vae,loras,wan,diffusion_models,text_encoders}

for subdir in checkpoints clip vae loras wan diffusion_models text_encoders; do
  target="$COMFY_DIR/models/$subdir"
  source="$MODELS_STORE/$subdir"
  if [ ! -L "$target" ] && [ -d "$target" ]; then
    # Move any existing files into the persistent store, then symlink
    cp -rn "$target/." "$source/" 2>/dev/null || true
    rm -rf "$target"
  fi
  [ -L "$target" ] || ln -s "$source" "$target"
done

# ── 5. Install Python deps ────────────────────────────────────────────
pip install -q fastapi "uvicorn[standard]" python-multipart aiohttp aiofiles websockets Pillow huggingface_hub

# FireRed deps (only if model dir exists on volume)
if [ -d "$WORK_DIR/models/FireRed-Image-Edit-1.1" ] || [ -d "$WORK_DIR/hf_cache/FireRed-Image-Edit-1.1" ]; then
  echo "Installing FireRed dependencies..." | tee -a $LOG
  pip install -q "transformers==4.57.6" accelerate peft sentencepiece
  pip install -q "git+https://github.com/huggingface/diffusers.git" 2>/dev/null || pip install -q "diffusers>=0.32.0"
fi

# ── 6. Start ComfyUI ─────────────────────────────────────────────────
echo "Starting ComfyUI on port 8188..." | tee -a $LOG
cd "$COMFY_DIR"
python main.py \
  --listen 0.0.0.0 \
  --port 8188 \
  --output-directory "$COMFY_DIR/output" \
  --input-directory  "$COMFY_DIR/input" \
  --disable-auto-launch \
  >> "$WORK_DIR/comfy.log" 2>&1 &

echo "Waiting for ComfyUI..." | tee -a $LOG
for i in $(seq 1 60); do
  curl -sf http://127.0.0.1:8188/system_stats > /dev/null 2>&1 && echo "ComfyUI ready." | tee -a $LOG && break
  sleep 3
done

# ── 7. Start AI Studio backend ────────────────────────────────────────
echo "Starting AI Studio on port 7860..." | tee -a $LOG

STUDIO_ENV="COMFY_HOST=127.0.0.1 COMFY_PORT=8188 COMFY_DIR=$COMFY_DIR COMFY_OUTPUT_DIR=$COMFY_DIR/output"

# FireRed model paths (if on network volume)
if [ -d "$WORK_DIR/hf_cache/FireRed-Image-Edit-1.1" ]; then
  STUDIO_ENV="$STUDIO_ENV FIRERED_MODEL_ID=$WORK_DIR/hf_cache/FireRed-Image-Edit-1.1"
  STUDIO_ENV="$STUDIO_ENV FIRERED_TRANSFORMER_ID=$WORK_DIR/hf_cache/Qwen-Image-Edit-Rapid-AIO-V19"
  STUDIO_ENV="$STUDIO_ENV HUGGINGFACE_HUB_CACHE=$WORK_DIR/hf_cache"
fi

env $STUDIO_ENV \
  python -m uvicorn server:app \
  --host 0.0.0.0 \
  --port 7860 \
  --workers 1 \
  >> "$WORK_DIR/studio.log" 2>&1 &

echo "AI Studio startup complete." | tee -a $LOG
echo "  ComfyUI:    http://localhost:8188" | tee -a $LOG
echo "  AI Studio:  http://localhost:7860" | tee -a $LOG

# Keep container alive
tail -f "$WORK_DIR/studio.log"
