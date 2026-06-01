# Generate a Video

This project creates one short video at a time using browser automation.

It is built to reuse your existing logged-in browser sessions where possible, instead of pushing you toward APIs.

## What it does

The workflow:

1. picks a random idea from `data/video_ideas.txt`
2. creates a run folder in `runs/`
3. generates a Hook image
4. generates a Grid 1 image using the Hook image as a reference
5. generates a Grid 2 image using the Grid 1 image as a reference
6. generates a Hook video, Grid 1 video, and Grid 2 video
7. stitches the three videos together with `ffmpeg`
8. saves the final result in `output/final/`
9. logs the completed result in `data/run_log.csv`

## Project layout

- `PLAN.md`
  Plain-English architecture overview.

- `.agents/skills/generate-a-video/SKILL.md`
  Repo skill for future Codex work in this project.

- `data/video_ideas.txt`
  The main place you edit ideas and prompts.

- `data/prompt_presets.txt`
  Shared prompt notes and reusable style language.

- `config/sites.json`
  Website URLs, selectors, timeouts, downloads, and session file paths.
  The Google image provider is currently pointed at your Flow project URL.

- `runs/`
  One folder per run, including the run text document and resume state.

- `output/images/`
  Downloaded images.

- `output/clips/`
  Downloaded video clips.

- `output/final/`
  Final stitched videos.

## First setup

### 1. Open this project folder

Use the folder:

`/Users/damoneden/Documents/codex stuff/generate-a-video`

### 2. Install dependencies

```bash
npm install
```

### 3. Create your local environment file

```bash
cp .env.example .env
```

You do not need to paste API keys here for this prototype.

### 4. Save your browser sessions

This opens real browser windows so you can log in once and save the session locally.

```bash
npm run save:image-session
npm run save:video-session
```

If you are already logged in during the first run, that is fine too.

## How to run the workflow

### Full workflow

```bash
npm run generate
```

### Resume the most recent unfinished run

```bash
npm run resume
```

### Run only the first setup step

```bash
npm run prepare
```

## Where you edit ideas and prompts

### Main idea list

Edit:

`data/video_ideas.txt`

Each idea contains:

- Name
- Title
- Hook Image Prompt
- Hook Video Prompt
- Grid 1 Image Prompt
- Grid 1 Video Prompt
- Grid 2 Image Prompt
- Grid 2 Video Prompt

### Shared prompt notes

Edit:

`data/prompt_presets.txt`

Use this for reusable style reminders, tone rules, or output preferences.

## How browser automation is set up

This project separates fragile website details from the workflow logic.

If a website changes its layout, the first place to check is:

`config/sites.json`

That file contains:

- page URLs
- selectors
- timeouts
- session file locations
- download behavior

For this project, the Google image step is currently aimed at your Flow page:

`https://labs.google/fx/tools/flow/project/a631a8e8-6524-4314-9cd4-351355fe8dc5`

## If the automation breaks

Do these in order:

1. Open `config/sites.json`
2. Update the selector that no longer matches the website
3. Try the workflow again
4. If a run already started, use `npm run resume`

If a browser step fails, the project saves a screenshot in that run folder to help debugging.

## What gets saved during a run

Each run creates its own folder in `runs/`.

That folder includes:

- `run.txt`
  Human-readable summary of that run.

- `idea.json`
  The selected idea in machine-readable format.

- `state.json`
  Resume progress for that run.

- failure screenshots when needed

## What this first version assumes

- You want browser automation first.
- You are logged in to the tools you already use.
- You are okay updating selectors when websites change.
- You want the workflow kept simple and modular.

## Useful commands

```bash
npm run generate
npm run resume
npm run prepare
npm run stitch -- --run-id=YOUR_RUN_ID
```
