---
name: "seedance-prompts"
description: "Use when the user wants help writing, refining, or batch-generating Seedance prompts for image-to-video or text-to-video creation, especially when they want cleaner cinematic motion, ad-style product shots, music-video visuals, character actions, camera direction, or stronger prompt structure."
---

# Seedance Prompts

Turn rough creative ideas into compact, production-ready Seedance prompts.

## Quick start

- If the user gives a vague idea, convert it into: subject + action + environment + camera + lighting + mood + output constraints.
- If the user gives a long messy prompt, tighten it by removing duplicate adjectives and contradictions.
- If the user wants multiple options, provide 3 prompt variants: safe, bolder, and most cinematic.
- Keep the final prompt concrete and visual. Prefer what the camera can see over abstract storytelling language.

## Workflow

1. Identify the core shot:
   subject, action, setting, time of day, tone.
2. Add motion:
   body movement, environmental movement, camera movement.
3. Add look:
   lighting, color palette, lens feel, texture, realism/stylization.
4. Add production constraints:
   duration, aspect ratio, pacing, continuity, no text/logos if needed.
5. Rewrite into one clean prompt plus optional negative guidance.

## Prompt formula

Use this structure by default:

`[subject], [action], in [setting], [time/lighting], [camera movement], [visual style], [mood], [quality/output constraints]`

Example shape:

`A lone female singer in a silver jacket walks through a rain-soaked Mexico City street at night, neon reflections on the pavement, slow dolly-in camera, cinematic low-key lighting, moody and romantic, realistic textures, smooth motion, high detail, no text or watermark`

## What to emphasize

- Specific physical actions: walking, turning, laughing, reaching, dancing, lip-syncing, pouring, opening, driving.
- Specific camera language: dolly-in, slow push, tracking shot, handheld, orbit, overhead, locked wide, macro close-up.
- Specific light: golden hour, overcast daylight, practical neon, soft studio key, rim light, hard flash.
- Specific atmosphere: dust, mist, rain, smoke, reflections, lens bloom, shallow depth of field.

## What to avoid

- Stacking too many styles at once.
- Contradictory directions like `minimalist` plus `maximalist`.
- Abstract words with no visual meaning like `amazing`, `epic`, `cool`.
- Overwriting. One strong image beats five competing ones.

## Output modes

Choose the lightest mode that matches the request:

- `single`: one polished prompt
- `three-ways`: three distinct prompt options
- `treatment`: one hero prompt plus a short visual rationale
- `shot-list`: 5 to 10 short prompts for a sequence

## Default rewrite rules

- Make the subject explicit.
- Make the main action explicit.
- Name the setting.
- Add one camera move.
- Add one lighting direction.
- Add one mood direction.
- End with clean quality constraints.

## Reusable templates

Load `references/templates.md` when the user wants category-specific prompt starters.

## PDF reference

If the user wants inspiration from the bundled prompt collection, use `references/400-ready-to-use-prompts.pdf` as the source document and adapt ideas into concise Seedance-friendly prompts rather than copying blindly.
