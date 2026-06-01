# KidNation — Full Context

## What It Is
KidNation is a kids gaming platform. Core products:
- **KidNation Kart Racer** — Unity kart game
- **Treasure Town** — playable prototype (Flutter/web/Unity)
- **Character pipeline** — 3D character assets and rigs

## Character Quality Gate

**Do not present any character asset until it has been A/B checked against the approved visual target.**

Steps required:
1. Run `kidnation-character-assets/tools/audit_character_quality.py` or equivalent contact sheet
2. Label asset honestly: visual target / 2D cutout / procedural Blender model / rigged base customization / Unity import / final rig
3. "A file exists" is NOT enough — visual bar comes first

**Rejection criteria (iterate internally, never show user):**
- Reads as a toy, blockout, clay doll, generic base model, or cutout masquerading as 3D

**Character: Jordan (primary)**
- Warm brown skin
- Large expressive eyes
- Braided hair with visible parting rows
- Red open jacket, white shirt, gold chain, dark jeans, gray sneakers

## Graphify Integration

When `graphify-out/graph.json` exists:
- Read `graphify-out/GRAPH_REPORT.md` for god nodes and community structure before architecture questions
- Use `graphify query`, `graphify path`, `graphify explain` for cross-module questions
- After modifying code files, run `graphify update .` to keep graph current

## KidNation UGC
- `kidnation-ugc/first-video-brief.md` — first video brief
- `kidnation-ugc/platform-recommendation.md` — platform strategy
- `kidnation-ugc/review-checklist.md` — review process

## KidNation Voices
- `kidnation-voices/` — dialogue generation, voice data, scripts
- Generated audio output is intentionally ignored in graphify

## Visual/Design Stack for KidNation

Always use the full design stack (see `01-user-preferences.md`):
- `emil-design-eng` + `impeccable` + taste skill pack for UI
- `ai-prompt-builder` + `seedance2-director` + relevant seedance skill for prompts
