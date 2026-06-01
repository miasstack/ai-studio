# Claude Skills — Migration Package

## Custom Slash Commands (reinstall via: /config → Commands)

These live in `~/.claude/commands/` on the original machine. Copy them to the same path on the new account.

| File | Slash Command | What it does |
|------|--------------|--------------|
| `generate-a-video.md` | `/generate-a-video` | Dog Vids YouTube Shorts pipeline — runs generate_video.py, critiques title, logs to video_log.md |
| `comfy_local.md` | `/comfy_local` | Controls local ComfyUI at localhost:8188 — Flux 2 Dev txt2img + WAN 2.2 i2v, with auto-critique loop |

## Installed Plugins (reinstall via: `claude plugins install <name>`)

| Plugin | Source | What it provides |
|--------|--------|-----------------|
| `document-skills@anthropic-agent-skills` | Anthropic marketplace | Word/Excel/PDF/PPTX creation skills |
| `example-skills@anthropic-agent-skills` | Anthropic marketplace | Example skill templates |
| `claude-api@anthropic-agent-skills` | Anthropic marketplace | Claude API / Anthropic SDK coding skill |
| `theone-skills@theone-training-skills` | theone-training-skills marketplace | Unity standards, PR review, and agent templates |

## How to reinstall commands on new account

1. Open Terminal
2. Run: `mkdir -p ~/.claude/commands`
3. Copy `generate-a-video.md` and `comfy_local.md` into `~/.claude/commands/`
4. Restart Claude Code — commands appear as `/generate-a-video` and `/comfy_local`
