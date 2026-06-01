# Graphify Corpus Map

This workspace is a mixed creative/code corpus. Use this map to understand the intended graph shape before indexing or querying.

## High-value clusters

- `kling-packs/` - canonical reference packs for cloning/animation workflows. Each dated folder usually contains `manifest.json`, source URL, first frame, source video, notes, and generated Mia assets.
- `dog-storyboards/` - storyboard and shot planning material, especially dog-rescue and Mia/captain visual concepts.
- `dog-vids-favorites/` - curated dog video reference clips, contact sheets, details, and trimmed selects.
- `prepare-kling-reference-pack/` - reusable skill/project for turning public inspiration videos into Kling-ready source packs.
- `skills/flow-scene-identity-anchoring/` - local skill for recreating viral storyboards while preserving Mia identity.
- `seedance-prompts-skill/` - Seedance prompt templates and references.
- `generate-a-video/` - automation scripts and prompt/run pipeline for image/video generation.
- `kidnation-voices/` - KidNation dialogue generation, voice data, and scripts. Generated audio output is intentionally ignored.
- `treasure-town-demo/` - playable/app prototype assets and Flutter/web/Unity experiments for Treasure Town.
- `Open-Generative-AI/` - larger app/code project. Build artifacts and dependencies are ignored; source/docs remain indexable.
- `creator-radar-mvp/`, `influur-clone/`, `math-snake/` - smaller app prototypes.
- `contract-redraft/` and top-level music agreement `.docx` files - contract/document redraft work.
- `transcripts/` - text transcripts that are cheaper and more graph-friendly than reprocessing raw media.
- `scripts/` and `plugins/textbelt-sms/` - reusable local automation and plugin work.

## Top-level loose assets

Loose `flow-*`, `ship_t*`, `driver-attention-clip.png`, `follow-dog-clip.png`, `latest-video-1.png`, and similar files are working visual references from Flow/Kling/storyboard sessions. They are intentionally left in place so existing scripts and absolute paths do not break.

## Graphify strategy

- Prefer indexing the whole workspace only after `.graphifyignore` is in place.
- For faster focused graphs, run Graphify on one cluster at a time, such as `kling-packs/`, `dog-storyboards/`, `generate-a-video/`, or `treasure-town-demo/`.
- Treat `manifest.json`, `shot-notes.md`, `README.md`, prompt files, and transcripts as the highest-signal source files.
- Treat raw videos and generated audio/video output as optional; transcripts and contact sheets usually give the graph more usable relationships per token.
