# Generate-a-Video Plan

## What this project is

This project is a simple browser-automation workflow for making one short video at a time.

It is designed for someone who is not a programmer:

- video ideas live in easy-to-edit text files
- browser steps are broken into small scripts
- fragile website selectors are kept in one config file
- every run saves its own notes and state so it can resume after a failure

The first version prefers your existing logged-in browser sessions instead of asking you to sign up for extra APIs.

## What the workflow does

The workflow name is `generate-a-video`.

For each run, it will:

1. pick one idea from your idea list
2. create a run folder
3. save a text summary for that run
4. generate a Hook image
5. generate a Grid 1 image using the Hook image as the reference image
6. generate a Grid 2 image using the Grid 1 image as the reference image
7. generate three videos from those images
8. stitch the videos together with `ffmpeg`
9. save the final video locally
10. write the finished result to a running log

## Why the project is split into small parts

Websites like Runway and Google tools can change their layout. If everything lived in one giant script, it would be hard to fix later.

This project keeps things modular:

- one part chooses the idea
- one part creates the run folder
- one part handles image generation
- one part handles video generation
- one part stitches the clips
- one part logs the result
- one part resumes failed work

That makes it easier to repair one piece without rebuilding everything.

## Files being created

### Main project files

- `README.md`
  Explains how to run the project in plain English.

- `.env.example`
  Shows the environment settings you may want later, without storing secrets in chat.

- `package.json`
  Gives you simple terminal commands like `npm run setup` and `npm run generate`.

## Skill file

- `.agents/skills/generate-a-video/SKILL.md`
  A repo skill so Codex can understand this project later without you needing to re-explain the whole workflow.

## Editable data files

- `data/video_ideas.txt`
  Your easy-to-edit list of video ideas. Each idea contains all prompts needed for one full run.

- `data/prompt_presets.txt`
  Optional shared prompt notes, style reminders, and reusable language.

- `data/run_log.csv`
  The running history of completed outputs.

## Config files

- `config/sites.json`
  Stores URLs, selectors, timeouts, and download settings for the browser automation.

- `config/sites.example.json`
  A backup example copy you can refer to if you need to restore the config later.

## Automation scripts

- `scripts/prepare-run.js`
  Picks an idea and creates a run folder.

- `scripts/generate-image.js`
  Runs one image-generation step in the browser.

- `scripts/generate-video.js`
  Runs one video-generation step in the browser.

- `scripts/stitch-video.js`
  Uses `ffmpeg` to combine the finished clips.

- `scripts/log-run.js`
  Adds the finished result to the CSV log.

- `scripts/run-workflow.js`
  Runs the full workflow from start to finish.

- `scripts/resume-run.js`
  Resumes a failed or interrupted run.

- `scripts/save-session.js`
  Saves logged-in browser sessions for the image site and the video site.

## Support code

The `scripts/lib/` folder contains small helper files for:

- paths
- file handling
- parsing ideas
- saving run state
- browser actions
- reusable provider logic

These are the building blocks that keep the project organized.

## How failure recovery works

Every run gets its own folder inside `runs/`.

That folder stores:

- the selected idea
- a plain-English text summary
- the current workflow state
- the output file paths already completed

If the browser crashes or a website times out, the run can continue later from the last unfinished step instead of starting over.

## What will likely need your input later

The biggest thing that may need a quick adjustment is the website selector config in `config/sites.json`.

That is normal with browser automation.

The good news is that this project keeps those fragile details in one place, so updates should be much easier.
