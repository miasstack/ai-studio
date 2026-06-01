# User Preferences & Working Style

## Identity
- User: Damon Eden (Damon@kidnation.com)
- Company: KidNation

## Critical Working Rules

- **Never use `hf_hub_download + shutil.move`** to download HuggingFace models — it moves symlinks not actual files. Always use `wget` directly to the target path.
- **User doesn't know Terminal.** Keep all instructions copy-paste simple with no explanation required.
- **Work autonomously** — minimize asking for permission. Just do it.
- **Don't summarize what you just did** at the end of responses.
- User wants Claude/Codex to figure things out and execute, not ask for guidance.

## Design Preferences

- UI prompt text must fit on-screen without horizontal overflow
- Prompt display must use a copyable box WITH full on-screen text wrapping
- High-polish, cute, non-generic visual quality always

## Design Stack (use together, not individually)

For KidNation UI design, visual direction, image/video prompts, character work, marketing:

1. `emil-design-eng` — interaction polish, refined component feel, motion judgment
2. `impeccable` — product/brand UI critique, layout, typography, color, anti-generic checks
3. `gpt-taste`, `high-end-visual-design`, `design-taste-frontend`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `stitch-design-taste`, `image-to-code`, `redesign-existing-projects` — visual taste and creative direction
4. For prompt engineering: combine above with `ai-prompt-builder`, `seedance2-director`, relevant `seedance-*` skill, `topview-skill`

**Do a deliberate preflight before showing results:** identify visual target → choose skill subset → generate/inspect reference → critique for cuteness, polish, clarity, brand fit, non-generic quality.
