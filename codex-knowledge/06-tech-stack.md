# Tech Stack & Infrastructure

## MCP Servers (Claude Code desktop)
| Server | Purpose |
|--------|---------|
| `blender` | Blender MCP — direct Blender control via `uvx blender-mcp` |
| `analytics-mcp` | Google Analytics via `~/.local/bin/analytics-mcp` |

**Google Analytics:** Project ID `analytics-api-498007`, credentials at `~/.config/gcloud/application_default_credentials.json`

## Cloud GPU
- **Vast.ai** — primary GPU provider for ComfyUI / image/video gen
  - Account: miasupremamusic@gmail.com (User ID: 456922)
  - Instance 34557960: RTX 4090, Finland, ~$0.447/hr
- **RunPod** — secondary GPU (API key rotated, get new one from dashboard)

## Key Tools & Scripts
- `blender_mcp_addon.py` — Blender MCP addon (in this repo root)
- `blender_start_mcp.py` — starts Blender MCP server
- `create_blockquest_characters.py` — BlockQuest character generator
- `build_producer_agreement.py` — music contract builder
- `update_template_producer_agreement.py` — contract template updater
- `ocr_vision.swift` / `ocr_vision.m` — OCR pipeline (macOS Vision framework)

## Video Generation Stack
- **Kling** — primary video gen, reference pack workflow
- **Seedance / Seedance 2** — video gen, has dedicated prompt skills
- **Flow** — video editing/composition tool
- **ComfyUI + Wan 2.2** — GPU-based video gen on Vast.ai
- **Remotion** — programmatic video with React (this repo)

## Image Generation
- `imagegen-frontend-mobile` / `imagegen-frontend-web` skills
- Adobe Firefly (MCP connected in cloud sessions)

## Graphify
Knowledge graph tool installed as a skill.
- `graphify-out/graph.json` — graph data (when present)
- `graphify-out/GRAPH_REPORT.md` — read this first for architecture questions
- `graphify-out/wiki/index.md` — wiki navigation (when present)
- Commands: `graphify query`, `graphify path`, `graphify explain`, `graphify update .`

## SEO Tools (via MCP or API)
- Ahrefs, DataForSEO, SEranking, Profound, Firecrawl, Google Search Console

## Environments
- **Desktop:** macOS, Claude Code desktop app, full Blender/Unity/Godot access
- **Cloud (this session):** Ubuntu Linux, Claude Code web, GitHub-connected, ephemeral container
- **Production:** GitHub repo `miasstack/ai-studio` as source of truth
