---
name: Canopy 2 Project
description: Fresh install of Canopy AI workspace platform, configured with Gemini as default adapter
type: project
tags: [ai-workspace, elixir, phoenix, sveltekit, tauri, game-development, gemini, google-api]
related:
  - project_unity_games.md
originSessionId: 55792257-f283-412f-8223-a8059ba32451
---

# Canopy 2 Project

Canopy (v2 / fresh install) is at `~/.canopy-app` — an Elixir/Phoenix + SvelteKit + Tauri AI workspace platform.

## Relationship to Other Projects

- **[Unity Games](project_unity_games.md)** — Canopy is configured with game dev skills (godot-gdscript-patterns, game-design-theory) to support the Unity games project. Both projects share the same game development context.

## Setup State
- Repo cloned from https://github.com/Miosa-osa/canopy (depth 1)
- DB: `canopy_dev` on local PostgreSQL (user: damoneden), migrations already up
- Backend deps built at `~/.canopy-app/backend/_build`
- Desktop npm deps installed at `~/.canopy-app/desktop/node_modules`
- Google/Gemini API key set in `~/.canopy-app/backend/.env` as `GEMINI_API_KEY`
- Default adapter: Gemini (cheapest model = gemini-pro via REST)
- Dev config patched: DB username uses `System.get_env("PGUSER") || "damoneden"`

**To start:** `cd ~/.canopy-app && make dev` (backend :9089, desktop :5200)

## Skills installed (at `~/.canopy-app/backend/.agents/skills/`)
- `godot-gdscript-patterns` (from wshobson/agents)
- `game-design-theory` (from pluginagentmarketplace/custom-plugin-game-developer)

**Why:** User wanted a fresh Canopy instance powered by Gemini (cheapest AI adapter) with game dev skills.

**How to apply:** When user asks about Canopy, refer to `~/.canopy-app`. Default adapter is Gemini — no Anthropic/OpenAI keys needed for basic agent operation.
