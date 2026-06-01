# Codex Stuff Workspace

The `codex stuff` folder is Codex's primary workspace (equivalent to `~/.claude/` for Claude).
It lives in Dropbox and contains all of Codex's ongoing work.

## Folder Structure

### High-Value Clusters
| Folder | Contents |
|--------|----------|
| `kling-packs/` | Canonical reference packs for cloning/animation workflows. Each dated folder has `manifest.json`, source URL, first frame, source video, notes, generated Mia assets |
| `dog-storyboards/` | Storyboard and shot planning — dog-rescue and Mia/captain visual concepts |
| `dog-vids-favorites/` | Curated dog video reference clips, contact sheets, trims |
| `prepare-kling-reference-pack/` | Reusable skill for turning inspiration videos into Kling-ready source packs |
| `seedance-prompts-skill/` | Seedance prompt templates and references |
| `generate-a-video/` | Automation scripts and prompt/run pipeline for image/video gen |
| `kidnation-voices/` | KidNation dialogue generation, voice data, scripts |
| `treasure-town-demo/` | Playable/app prototype — Flutter/web/Unity for Treasure Town |
| `Open-Generative-AI/` | Larger app/code project — see `project_knowledge.md` |
| `creator-radar-mvp/` | Creator discovery tool prototype |
| `influur-clone/` | Influur clone prototype |
| `math-snake/` | Math Snake game |
| `kidnation-kart-racer-unity/` | Unity kart game |
| `kidnation-character-assets/` | KidNation character art pipeline |

### Contract Work
| Folder/File | Contents |
|-------------|----------|
| `contract-redraft/` | Contract redraft work |
| `danny-schofield-contract-review/` | Danny Schofield contract review |
| `*.docx` files | Montana 700 producer agreements (multiple artists) |
| `build_producer_agreement.py` | Script to build producer agreements from template |
| `update_template_producer_agreement.py` | Updates template format |

### Local Skills & Agents
| Folder | Contents |
|--------|----------|
| `skills/flow-scene-identity-anchoring/` | Recreate viral storyboards while preserving Mia identity |
| `.agents/` | Local agent definitions |
| `.claude/` | Claude config for this workspace |
| `.codex/` | Codex config for this workspace |
| `plugins/` | Local plugins |

### SEO & Marketing
| Folder/File | Contents |
|-------------|----------|
| `kidnation-landing-audit.md` | Full landing page audit with recommendations |
| `fundraising_campaign_plan_2026-05-08.md` | Fundraising campaign plan |
| `south_florida_code_violation_properties_*.csv/.xlsx/.json` | Real estate enrichment data |

### Media & References
- `transcripts/` — text transcripts (preferred over raw media for graphify)
- `scripts/` — reusable local automation
- `video_preview_frames/` — video preview frame extracts
- `video-preview/` — video preview files
- `reference_analysis/` — reference video analysis outputs
- Loose `flow-*`, `ship_t*`, `driver-attention-clip.png` etc. — working visual references, left in place to avoid breaking scripts

## Memory System
Codex uses a memory context system:
```
Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs])
Search: mem-search skill
```

## Graphify Config
```
.graphifyignore — in place
```
Strategy:
- Index whole workspace with `.graphifyignore` active
- For faster graphs: run on one cluster at a time (kling-packs/, dog-storyboards/, etc.)
- Highest signal files: `manifest.json`, `shot-notes.md`, `README.md`, prompt files, transcripts
- Raw videos/audio = optional; transcripts/contact sheets are better for the graph

## Key Characters
- **Mia** — primary content creator character used in Kling/Seedance videos
- **Jordan** — KidNation kart racer character (see `03-kidnation.md` for specs)
