# Master Project Context — Claude Team Migration

Paste this file (or the individual project files) at the start of a new Claude Code session to restore full context.

---

## HOW TO WORK WITH THIS USER

- Never use `hf_hub_download` + `shutil.move` for HuggingFace models — it moves symlinks not actual files. Use `wget` directly to the target path.
- User is not a Terminal expert. Keep instructions copy-paste simple.
- Work autonomously — minimize asking for permission.
- Don't summarize what you just did at the end of responses.

---

## ACTIVE PROJECTS

### 1. ComfyUI Wan 2.2 I2V NSFW on Vast.ai
Full setup guide: `project_comfyui_vastai.md`  
Also see: `feedback_vastai_workflow.md`  
Also see: full step-by-step in `claude_handoff.md` → PROJECT 1

### 2. Juhn Fan DNA Intelligence Report
See: `project_juhn_fan_dna.md`  
SOP for any artist: `Artist_FanDNA_SOP.md`

### 3. TradeKraft Music Virality Platform
See: `project_tradekraft.md`  
Project dir: `~/TradeKraft/`  
CLAUDE.md: `tradekraft_CLAUDE.md`

### 4. Who's Hot — TikTok Influencer CRM
See: `project_whos_hot.md`  
Status: spec complete, ready to build

### 5. KidNation App (co-founded with Ludacris)
See: `project_kidnation.md`  
CLAUDE files: `kidnation_CLAUDE.md`, `kidnation-mobile-CLAUDE.md`, `kidnation-back-CLAUDE.md`, `kidnation-admin-CLAUDE.md`  
Project dir: `~/Desktop/kn app/`

### 6. Dog Vids YouTube Shorts Pipeline
Skill: `/generate-a-video` (see skills folder)  
Log: `dog_vids_video_log.md`  
Replication guide: `dog_vids_REPLICATION_GUIDE.md`  
Pipeline dir: `~/dog vids/`

### 7. Canopy 2
See: `project_canopy2.md`  
Install: `~/.canopy-app/`

### 8. Unity Games
See: `project_unity_games.md`

---

## REFERENCE

- Higgsfield character sheet prompt: `reference_character_sheet_prompt.md`
- Memory index: `MEMORY.md`
