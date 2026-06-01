---
name: prepare-kling-reference-pack
description: Prepare a Kling-ready source pack from a public inspiration video, especially YouTube Shorts. Use when Codex needs to download a source clip, extract the opening frame, and organize the raw source assets in local storage or Google Drive for later reference and cloning workflows. Only generate a new Mia image when the user explicitly asks for that extra step.
---

# Prepare Kling Reference Pack

Build a reusable source pack for later Kling 3.0 runs from a public video URL.
Default subject is Mia when a derived image is explicitly requested, using `assets/mia-character-sheet-4_26.png` as the identity reference.
Default Google Drive destination is `https://drive.google.com/drive/folders/1xDj5e57IOq3pySoMcXqK8HrvBUOgpzzp`.
Google Drive home link for this account/context is `https://drive.google.com/drive/u/5/home`.

## Deliverables

Create one folder per source video with this structure:

```text
pack-root/
  20260419-153000-video-slug/
    manifest.json
    source/
      source-video.mp4
      first-frame.png
      source-url.txt
    delivery/
```

Primary deliverables are always:

- `source/source-video.mp4`
- `source/first-frame.png`

If the user explicitly asks for a derived Mia image, add:

- `analysis/shot-notes.md`
- `generated/mia-still.png`
- `generated/mia-prompt.md`

Treat the Google Drive folder above as the standing default cloud destination unless the user explicitly changes it.
Use Dropbox only if the user explicitly asks for it.

## Workflow

### 1. Initialize the pack

Run `scripts/init_pack.py` first so the folder structure and starter files are consistent.

Example:

```bash
python3 scripts/init_pack.py \
  --root /tmp/kling-packs \
  --url "https://youtube.com/shorts/1qdIQEYd34Q" \
  --title "Example video" \
  --subject "Mia"
```

This script creates the folder, starter markdown files, and `manifest.json`.
Use one new subfolder per inspiration link.

### 2. Download the source video

Prefer the most direct legal method available in the current environment:

1. If a reliable CLI downloader is installed, use it.
2. Otherwise use browser automation with a user-approved web downloader such as Publer.
3. Save the video as `source/source-video.mp4`.
4. Record the exact source URL in `source/source-url.txt` and `manifest.json`.

If browser automation is required, read `references/browser-workflow.md`.

### 3. Extract the opening frame

Run:

```bash
bash scripts/extract_first_frame.sh \
  /path/to/source-video.mp4 \
  /path/to/first-frame.png
```

Use the extracted frame as the composition reference for everything else.

### 4. Store the raw source assets

After download and extraction:

1. Keep the local pack intact.
2. Upload the full pack or at minimum `source-video.mp4`, `first-frame.png`, `source-url.txt`, and `manifest.json` into the default Google Drive destination in a new subfolder named after the pack slug.
3. Use Dropbox only when the user explicitly asks for it.

Important:

- Do not skip the first-frame extraction step.
- Do not replace the first frame with a new generated image unless the user explicitly asks for a derived Mia still.
- For this workflow, the first frame is the key visual reference.

### 5. Optional derived Mia still

Only do this section when the user explicitly asks for a new Mia image.

Open the first frame and fill in `analysis/shot-notes.md`.
Use `references/shot-analysis.md` as the checklist.
Read `references/mia-still-prompt-template.md` before prompting the image generator.
If Google Flow is available, prefer Flow for image work because it supports iterative image editing inside the project instead of forcing a full reroll every time the face drifts.

Preferred order:

1. Use Google Flow when the user asks for Flow or when Flow access is available.
2. Fall back to another image generator only when Flow is unavailable or blocked.

Rules for the optional derived image:

- Match the first frame's perspective, framing, lens feel, pose direction, lighting, and overall fashion energy.
- Keep Mia's identity consistent with the character sheet.
- Create a stylish comparable outfit, not a pixel-for-pixel copy.
- Keep the output aspect ratio aligned with the source frame.
- Save the final image as `generated/mia-still.png`.
- Save the exact prompt used in `generated/mia-prompt.md`.

If using Flow:

1. Read `references/google-flow-image-workflow.md`.
2. Open or create a Flow project for the pack.
3. In the prompt box, switch to image creation.
4. Choose the image model deliberately:
   - Use `Nano Banana Pro` when facial fidelity and fine iterative edits matter most.
   - Try `Imagen 4` when you want an alternate clean base render.
   - Use `Nano Banana 2` for a faster no-charge pass when appropriate.
5. Generate the first draft from the Mia prompt.
6. If the face drifts, edit the generated image in Flow instead of fully restarting:
   - Use `Select` to isolate the face or hair region.
   - Use `Draw` when you need to point at the exact feature to change.
   - Restate Mia's face anchors from the character sheet.
7. Export the best image and save it as `generated/mia-still.png`.

### 6. Upload the finished pack if needed

Google Drive is the default storage target for this workflow.
Use Dropbox only when the user explicitly asks for it.

If uploading to Drive:

1. Create a new Drive subfolder named after the pack slug.
2. Upload `source/source-video.mp4` and `source/first-frame.png` as the required deliverables.
3. Upload `source/source-url.txt` and `manifest.json` when practical.
4. Upload any optional `generated/` files only if they exist.

If cloud upload is blocked, keep the local pack intact and clearly report what remains to upload.

## Working Style

Make one reasonable assumption at a time and keep momentum:

- If the user does not name a destination root, create the pack in a sensible local working directory.
- If the video title is unavailable, derive the folder slug from the URL and timestamp.
- Use the default Drive folder unless the user overrides it.
- Use the Drive home link only as a navigation reference; do not treat it as the pack destination folder.
- Do not switch to Dropbox unless the user explicitly requests that storage target.
- Finish locally first if upload or sync is temporarily blocked.
- Default to raw source preservation over derivative image generation.

## Resources

- `scripts/init_pack.py`: create the pack folder, starter files, and manifest.
- `scripts/extract_first_frame.sh`: extract the first frame with `ffmpeg`.
- `references/shot-analysis.md`: framing and styling checklist.
- `references/mia-still-prompt-template.md`: prompt formula for generating Mia stills.
- `references/google-flow-image-workflow.md`: Google Flow image-generation and edit workflow for Mia stills.
- `references/browser-workflow.md`: browser-based download and Drive upload guidance.
- `assets/mia-character-sheet-4_26.png`: default Mia identity reference.
