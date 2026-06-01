# Active Projects

## PROJECT 1: KidNation (Main Project)

A kids gaming platform with characters, a kart racer (Unity), and Treasure Town (playable demo).
See `03-kidnation.md` for full detail.

**Repos/Paths:**
- `kidnation-kart-racer-unity/` — Unity kart game
- `kidnation-character-assets/` — character art pipeline
- `treasure-town-demo/` — Flutter/web/Unity prototype

---

## PROJECT 2: AI Studio (This Repo — github.com/miasstack/ai-studio)

A Remotion-based video app using React to render videos.
See `08-remotion-rules.md` for the full component rules.

**Key facts:**
- Root file: `src/Root.tsx`
- Default: 1920×1080, 30fps, `id="MyComp"`
- Uses `<OffthreadVideo>`, `<Img>`, `<Audio>`, `<AbsoluteFill>`, `<Sequence>`, `<Series>`, `<TransitionSeries>`
- No `Math.random()` — use `random('seed')` from remotion
- No interactivity — Remotion components are frame-driven, not event-driven

---

## PROJECT 3: ComfyUI Wan 2.2 I2V on Vast.ai

**Goal:** Wan 2.2 I2V NSFW workflow on Vast.ai GPU — generate adult video from reference images via web UI.

**Instance:** ID 34557960 | IP 82.141.118.40 | SSH port 2545 | GPU: RTX 4090 Finland
**Cost:** ~$0.447/hr | **Status:** STOPPED (resume at cloud.vast.ai/instances/)
**Image:** `vastai/comfy:v0.18.2-cuda-12.9-py312`
**Jupyter token:** `2939116390aad9a262209b63bf2dfd917f8c835f1901a9cdf36e460e3ea35a04`

**Setup required after start:**
1. Install custom nodes: ComfyUI-WanVideoWrapper, rgthree-comfy, VideoHelperSuite, KJNodes, ComfyUI-Manager
2. Download base models (~33GB): Wan 2.2 I2V fp8 high+low, umt5_xxl clip, wan_2.1 vae
3. Upload LoRAs from Dropbox
4. Restart ComfyUI: `python main.py --disable-auto-launch --port 18188`
5. Upload `Wan 2.2 I2V NSFW.json` workflow

**Vast.ai Account:** miasupremamusic@gmail.com | User ID: 456922

---

## PROJECT 4: Open Generative AI

Larger app/code project in `Open-Generative-AI/`. Build artifacts ignored; source/docs indexable.
Has its own `project_knowledge.md` and `README.md`.

---

## PROJECT 5: Creator Radar MVP

Creator discovery tool prototype. `creator-radar-mvp/README.md` has details.

---

## PROJECT 6: Music Contracts (Montana 700)

Multiple producer agreements for: Kongo, K6WYA, John Gotit, CantRushTheVibe, 214Tony, QuinWithTheKeyz, Z4y.
Scripts: `build_producer_agreement.py`, `update_template_producer_agreement.py`

---

## PROJECT 7: Juhn Fan DNA Intelligence Report

- Artist: Juhn El All Star — Puerto Rican urban/trap
- 6.5M Spotify monthly listeners, 715K TikTok
- Top market: Santiago Chile (3.02x affinity), fastest growing: Mexico (+24% Q1 2026)
- US under-penetrated: 13.3% IG followers vs 5.4% streaming

---

## PROJECT 8: KidNation Fundraising

`fundraising_campaign_plan_2026-05-08.md` — full campaign plan.

---

## PROJECT 9: KidNation Landing Audit

`kidnation-landing-audit.md` — full audit of landing page with recommendations.

---

## INFRASTRUCTURE

**RunPod API:** used for GPU workloads (key rotated — get new key from RunPod dashboard)
**Graphify:** knowledge graph tool. When `graphify-out/graph.json` exists, read `GRAPH_REPORT.md` first before architecture questions.
