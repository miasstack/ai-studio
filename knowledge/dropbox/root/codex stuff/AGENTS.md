<claude-mem-context>
# Memory Context

# [codex stuff] recent context, 2026-05-11 11:05am EDT

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 4 obs (1,324t read) | 48,147t work | 97% savings

### Apr 28, 2026
7 4:55p 🟣 Kling Reference Pack Created for TikTok Video 7632084992499272973 (Mia)
12 7:29p 🟣 Music Video Storyboard Request: 6-Kid Dance Scene with Melly
13 7:35p ⚖️ UI Preference: Prompt Text Must Fit On-Screen Without Horizontal Overflow
14 7:42p ⚖️ Prompt Display Must Use Copyable Box WITH Full On-Screen Text Wrapping

Access 48k tokens of past work via get_observations([IDs]) or mem-search skill.
</claude-mem-context>

## graphify

This project is configured for graphify. When graphify-out/graph.json exists, use the knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)

## KidNation Character Quality Gate

When working on KidNation character renders, Blender files, Unity rigs, or kart driver assets:

- Do not present a character asset to the user until it has been A/B checked against the approved visual target or character sheet.
- Use `kidnation-character-assets/tools/audit_character_quality.py` or an equivalent contact sheet before user review.
- Label every asset honestly as one of: visual target, 2D cutout, procedural Blender model, rigged base customization, Unity import, or final rig.
- Never treat "a Blender/FBX/GLB file exists" as enough. The visual bar comes first: face shape, eye style, hair silhouette, outfit silhouette, material quality, body proportions, and character identity.
- If the render reads as a toy, blockout, clay doll, generic base model, or cutout masquerading as 3D, reject it internally and iterate before showing it.
- For Jordan specifically, the target is the existing Jordan sheet/cutout: warm brown skin, large expressive eyes, braided hair with visible parting rows, red open jacket, white shirt, gold chain, dark jeans, and gray sneakers.

## Design, Cute Visuals, And Prompt Engineering Stack

For KidNation UI design, cute/high-polish visual direction, image prompts, video prompts, character presentation, marketing screens, or frontend polish, use the local skill stack together instead of relying on a single design pass:

- Use `emil-design-eng` for interaction polish, refined component feel, motion judgment, and the tiny details that make screens feel intentional.
- Use `impeccable` for product/brand UI critique, layout, typography, color, accessibility, responsive behavior, and anti-generic design checks.
- Use the installed `taste-skill` pack for visual taste and creative direction, especially `gpt-taste`, `high-end-visual-design`, `design-taste-frontend`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `brandkit`, `stitch-design-taste`, `image-to-code`, and `redesign-existing-projects`.
- For prompt engineering for images or videos, combine this design stack with the existing prompt/video skills such as `ai-prompt-builder`, `seedance2-director`, the relevant `seedance-*` skill, and `topview-skill` when applicable.
- For the planned weekend design work on May 16-17, 2026, treat this as the default creative stack.

Do a deliberate preflight before showing results: identify the intended visual target, choose the relevant subset of skills, generate or inspect a reference when useful, then critique the output against the target for cuteness, polish, clarity, brand fit, and non-generic quality.
