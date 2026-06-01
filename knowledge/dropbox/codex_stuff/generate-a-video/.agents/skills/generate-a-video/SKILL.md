---
name: generate-a-video
description: Use when working inside this repo on the browser-based short-video workflow that selects an idea, generates story-grid images and videos through logged-in browser sessions, stitches clips with ffmpeg, logs finished outputs, and resumes failed runs.
---

# Generate-a-Video

Use this skill when the task involves the `generate-a-video` workflow in this repo.

## Goal

Create YouTube Shorts style videos from a simple editable idea list by using browser automation first, not APIs, whenever possible.

The intended flow is:

1. choose one idea from `data/video_ideas.txt`
2. create a run folder and run summary text file
3. generate three images in sequence
4. generate three videos from those images
5. stitch them together with `ffmpeg`
6. save the final file
7. append the result to `data/run_log.csv`
8. support resume if any step fails

## Project rules

- Prefer Playwright browser automation over paid APIs.
- Assume the user wants to reuse existing logged-in sessions.
- Keep scripts small and modular.
- Keep user-editable content in beginner-friendly text files.
- Keep fragile selectors and website details out of the main workflow logic.
- Add screenshot-on-failure behavior for browser steps.
- Save run state after each completed step.
- Avoid saving unnecessary stitched draft files.
- Make docs understandable for a non-coder.

## Where to look first

- `README.md`
  User-facing instructions.

- `PLAN.md`
  Beginner-friendly architecture explanation.

- `config/sites.json`
  Browser URLs, selectors, timeouts, download settings, and session file locations.

- `data/video_ideas.txt`
  Source of the actual video ideas.

- `scripts/run-workflow.js`
  Main orchestration entry point.

- `scripts/resume-run.js`
  Restart logic after partial failure.

## Editing guidance

- If the workflow breaks because a website changes, fix `config/sites.json` first before rewriting scripts.
- If prompt structure changes, update `data/video_ideas.txt` or `data/prompt_presets.txt`.
- If the order of workflow steps changes, update the step list in `scripts/lib/providers.js` and the README.
- Keep helper logic in `scripts/lib/` rather than growing one large script.

## When changing browser automation

- Preserve existing session reuse.
- Keep headless mode off by default unless the user asks otherwise.
- Use clear error messages.
- Save screenshots into the current run folder on failure.
- Retry transient browser actions before failing the run.

## When adding a new provider

- Add the provider config to `config/sites.json`.
- Reuse the shared browser helper functions.
- Keep provider-specific selectors in config, not hardcoded in orchestration.
- Keep output filenames predictable.

## Output expectations

At the end of a successful run there should be:

- a run folder in `runs/`
- downloaded images in `output/images/`
- downloaded clips in `output/clips/`
- a final stitched video in `output/final/`
- one appended row in `data/run_log.csv`

## User experience expectations

The user is not a developer. Prefer:

- simple commands
- plain-English docs
- easy file names
- safe defaults
- one clear next step at a time
