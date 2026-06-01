# Claude Handoff — Full Context

## HOW TO USE THIS FILE
Paste this entire file into a new Claude Code session at the start. It gives Claude full memory of all ongoing projects and preferences.

---

## FEEDBACK (How to work with this user)
- Never use hf_hub_download + shutil.move to download HuggingFace models — it moves symlinks not actual files. Always use wget directly to the target path.
- User doesn't know Terminal. Keep instructions copy-paste simple.
- User wants Claude to work autonomously — minimize asking for permission.
- Don't summarize what you just did at the end of responses.

---

## PROJECT 1: ComfyUI Wan 2.2 I2V NSFW on Vast.ai

**Goal:** Get Wan 2.2 I2V NSFW workflow running on Vast.ai GPU, generate adult video content from reference images via a web UI.

### Current Instance (as of 2026-04-10)
- **Instance ID:** 34557960
- **IP:** 82.141.118.40
- **SSH port:** 2545
- **Jupyter port:** 2360 (internal 8080)
- **Jupyter token:** 2939116390aad9a262209b63bf2dfd917f8c835f1901a9cdf36e460e3ea35a04
- **GPU:** RTX 4090, Finland (Machine ID: 31087)
- **Cost:** ~$0.447/hr
- **Status: STOPPED** — resume at cloud.vast.ai/instances/ → click play button on instance 34557960
- **Image:** vastai/comfy:v0.18.2-cuda-12.9-py312

**The instance is EMPTY — nothing installed yet. Full setup still needed.**

### SSH Key (registered on Vast.ai account)
- Public key: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE0pwaLRZp9wDS8lhemLHb4/zXaurh8RSlIc82cRfj/j damoneden@MacBookAir.lan`
- Private key lives at `~/.ssh/vastai_key` on the original MacBook (may not be on this computer)
- If SSH doesn't work, use Jupyter terminal: cloud.vast.ai → Instances → ">_ Connect"

### Cloudflare Tunnel URLs
The vastai/comfy image creates Cloudflare tunnel URLs on startup — these **change every restart**. Find them by:
cloud.vast.ai/instances/ → ">_ Connect" button → look for ComfyUI and Jupyter links

---

## SETUP STEPS (run in order after starting instance)

### Step 1 — Open Jupyter Terminal
Go to cloud.vast.ai/instances/ → ">_ Connect" on instance 34557960 → open Jupyter → New Terminal

### Step 2 — Install Custom Nodes
```bash
cd /workspace/ComfyUI/custom_nodes
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper
git clone https://github.com/rgthree/rgthree-comfy
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
git clone https://github.com/kijai/ComfyUI-KJNodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
cd ComfyUI-WanVideoWrapper && pip install -r requirements.txt -q
cd ../ComfyUI-VideoHelperSuite && pip install -r requirements.txt -q
cd ../ComfyUI-KJNodes && pip install -r requirements.txt -q
```

### Step 3 — Download Base Models (~33GB, 20-40 min on Finland instance)
```bash
mkdir -p /workspace/ComfyUI/models/diffusion_models
mkdir -p /workspace/ComfyUI/models/clip
mkdir -p /workspace/ComfyUI/models/vae
mkdir -p /workspace/ComfyUI/models/loras/"wan 2.2"

wget -q --show-progress -O /workspace/ComfyUI/models/diffusion_models/Wan_2.2_I2V_HighNoise_10steps_fp8.safetensors \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2.2_I2V_HighNoise_10steps_fp8_e4m3fn.safetensors"

wget -q --show-progress -O /workspace/ComfyUI/models/diffusion_models/Wan_2.2_I2V_LowNoise_10steps_fp8.safetensors \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2.2_I2V_LowNoise_10steps_fp8_e4m3fn.safetensors"

wget -q --show-progress -O /workspace/ComfyUI/models/clip/umt5_xxl_fp8_e4m3fn_scaled.safetensors \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/umt5_xxl_fp8_e4m3fn_scaled.safetensors"

wget -q --show-progress -O /workspace/ComfyUI/models/vae/wan_2.1_vae.safetensors \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors"
```

### Step 4 — Upload LoRAs from Dropbox
LoRA files are in this Dropbox shared folder:
**https://www.dropbox.com/scl/fo/h32gdpjdvuc6xv69vm4rh/AIt6GuO26Kew-ACWsaMhFow?rlkey=34r1p3yu3j6gvi477du1or6js&dl=0**

Files confirmed in that folder:
- `DR34ML4Y_I2V_14B_HIGH.safetensors`
- `DR34ML4Y_I2V_14B_LOW.safetensors`
- `m14-highnoise.safetensors`
- `m14-lownoise.safetensors`
- `Qv_8bEmM86wrtPnwibRrj_pytorch_lora_weights.safetensors`
- `wan22-cunilingus-I2V-72epoc-low.safetensors`
- `wan22-cunilingus-I2V-106epoc-high.safetensors`
- `Wan 2.2 I2V NSFW.json` (the workflow file)
- `download_models.sh` (may have useful wget commands)

To upload LoRAs to the instance: download from Dropbox, then upload via ComfyUI's web UI or scp.

Target paths on instance:
- `/workspace/ComfyUI/models/loras/` (root LoRAs)
- `/workspace/ComfyUI/models/loras/wan 2.2/` (sub-folder LoRAs)

Additional LoRAs known to exist (from prior session, not confirmed in Dropbox):
- NSFW-22-H-e8.safetensors
- NSFW-22-L-e8.safetensors
- reverse_suspended_congress high+low
- WAN-2.2-I2V-Handjob high+low
- WAN-2.2-I2V-POV-Titfuck high+low
- Sensual_fingering high+low
- BouncyWalk02 high+low
- Pornmaster Slow Twerk high+low

### Step 5 — Restart ComfyUI
```bash
pkill -f comfyui || true
cd /workspace/ComfyUI
python main.py --disable-auto-launch --disable-xformers --port 18188 --enable-cors-header &
```

### Step 6 — Upload Workflow
Upload `Wan 2.2 I2V NSFW.json` from Dropbox (same folder above) to ComfyUI via the web UI.

### Step 7 — Test Generation
Upload a test image and queue a generation. Check node 135 (VHS_VideoCombine) for GIF output.

---

## Vast.ai API — Useful JS Commands (run from cloud.vast.ai in browser console)

```javascript
// Check instance status
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/v0/instances/?owner=me', false);
xhr.setRequestHeader('Accept', 'application/json');
xhr.send();
JSON.parse(xhr.responseText).instances.map(i => ({ id: i.id, status: i.actual_status, ip: i.public_ipaddr }))

// Start instance
const xhr2 = new XMLHttpRequest();
xhr2.open('PUT', '/api/v0/instances/34557960/', false);
xhr2.setRequestHeader('Content-Type', 'application/json');
xhr2.send(JSON.stringify({ state: 'running' }));
xhr2.responseText

// Stop instance
const xhr3 = new XMLHttpRequest();
xhr3.open('PUT', '/api/v0/instances/34557960/', false);
xhr3.setRequestHeader('Content-Type', 'application/json');
xhr3.send(JSON.stringify({ state: 'stopped' }));
xhr3.responseText
```

---

## PROJECT 2: Juhn Fan DNA Intelligence Report
- Full PDF: ~/Desktop/Juhn_Fan_DNA_Intelligence_Report.pdf (on original Mac)
- SOP for any artist: ~/Desktop/Artist_FanDNA_SOP.md (on original Mac)
- Artist: Juhn El All Star — Puerto Rican urban/trap
- Key stats: 6.5M Spotify monthly listeners, 715K TikTok
- Top market: Santiago Chile (3.02x affinity), fastest growing: Mexico (+24% Q1 2026)
- US under-penetrated: 13.3% of IG followers but only 5.4% of streaming

---

## VAST.AI ACCOUNT
- Account: miasupremamusic@gmail.com
- User ID: 456922
- Instance 34557960 costs ~$0.447/hr when running
- Stop when not in use: cloud.vast.ai/instances/ → pause button
- Add credits at: cloud.vast.ai/billing/
