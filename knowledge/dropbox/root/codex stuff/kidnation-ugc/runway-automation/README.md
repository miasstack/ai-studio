# Runway Automation Starter

This is a semi-automated Playwright helper for your Runway clip workflow.

What it does:

- opens Runway in a real browser
- saves your login session after the first run
- uploads the configured clip file(s)
- pastes the prompt for each clip
- pauses before generation so you can review the setup

Why it pauses:

Runway's UI changes often, and fully blind automation is fragile. This version automates the repetitive setup while still keeping you in control before each render.

## Setup

1. In this folder, install dependencies:

```bash
npm install
```

2. Copy the example config:

```bash
cp runway.config.example.json runway.config.json
```

3. Edit `runway.config.json`:

- set the real file paths for `ugcclip1`, `ugcclip2`, and `ugcclip3`
- paste each clip prompt
- update selectors if Runway's page needs more specific targets

## First run

Save a logged-in session:

```bash
npm run save-session
```

The script will open Runway, wait for you to log in, then save the session locally.

## Normal run

```bash
npm run
```

For each clip, the script will:

1. load the page
2. upload the configured files
3. paste the prompt
4. stop so you can review and hit Generate

After you submit a clip and the page is ready again, press Enter in the terminal to move to the next clip.

## Selector notes

The default selectors are intentionally simple:

- `promptInput`: defaults to `textarea`
- `referenceUploadInput`: defaults to `input[type='file']`
- `audioUploadInput`: defaults to `input[type='file']`

If Runway uses different elements for your exact tool, inspect the page and replace these selectors in `runway.config.json`.
