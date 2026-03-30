# RunPod One-Time Setup

Do this once. After that, everything is controlled from the AI Studio website.

---

## Step 1 — Push your code to GitHub

```bash
cd ~/ai-studio
git init
git add .
git commit -m "initial"
git remote add origin https://github.com/YOUR_USER/ai-studio.git
git push -u origin main
```

Then open `runpod/startup.sh` and update the git clone line:
```bash
git clone --depth=1 https://github.com/YOUR_USER/ai-studio "$STUDIO_DIR"
```

---

## Step 2 — Create a RunPod Template

1. Go to **RunPod → Templates → New Template**
2. Fill in:
   - **Name:** `AI Studio`
   - **Container Image:** `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
   - **Container Start Command:**
     ```
     bash -c "git clone https://github.com/YOUR_USER/ai-studio /workspace/ai-studio 2>/dev/null || git -C /workspace/ai-studio pull; bash /workspace/ai-studio/runpod/startup.sh"
     ```
   - **Environment Variables:**
     - `AI_STUDIO_REPO` = `https://github.com/YOUR_USER/ai-studio`
   - **Expose HTTP Ports:** `7860, 8188`
   - **Expose TCP Ports:** `22`
   - **Volume Mount Path:** `/workspace`
3. Save. Copy the **Template ID**.

---

## Step 3 — Create a Network Volume (for models)

1. Go to **RunPod → Storage → New Network Volume**
2. **Name:** `ai-studio-models`
3. **Size:** 100–200GB depending on which models you want
4. **Region:** pick one close to you
5. Save. Copy the **Volume ID**.

> Models you download once stay on the volume between pod runs — you only pay the tiny storage fee (~$0.07/GB/month), not GPU time.

---

## Step 4 — Get your API Key

1. Go to **RunPod → Settings → API Keys**
2. Create a key with **Read + Write** permissions
3. Copy it

---

## Step 5 — Configure the AI Studio website

Open the AI Studio site and click **⚙** in the top-right:
- **API Key** → paste from Step 4
- **Template ID** → from Step 2
- **Volume ID** → from Step 3
- **GPU Type** → e.g. `NVIDIA A40` (good balance of price/VRAM)
- Save

That's it. From now on:
- **▶ Launch Pod** starts a GPU instance (~$0.40–$0.80/hr)
- Generate whatever you want
- **■ Stop Pod** kills the pod and stops GPU billing
- Storage fee (~few cents/day) is all that remains

---

## GPU recommendations by model

| Model | Min VRAM | Recommended GPU |
|-------|----------|-----------------|
| LTX 2B, Wan 1.3B | 10GB | RTX 3090, A4000 |
| FireRed 1.1, Wan I2V | 14–16GB | RTX 4090, A5000 |
| Wan 2.2 T2I/I2V | 20GB+ | A40, A6000, A100 |
