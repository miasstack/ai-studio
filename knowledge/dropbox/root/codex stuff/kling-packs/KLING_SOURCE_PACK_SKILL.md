# Kling Source Pack Skill

## Purpose

This skill turns a YouTube Short, TikTok, Instagram Reel, or local video file into a clean Kling-ready reference pack.

Each pack must contain only:

```text
creator-handle-or-title - platform - videoid-or-shortcode/
  original-video.mp4
  first-frame.png
```

This workflow only prepares the source clip and its first frame.

## What The Agent Must Be Able To Do

The agent needs these capabilities:

- Read and write files in the target pack folder.
- Run shell commands.
- Access the internet.
- Download media from YouTube, TikTok, Instagram, or third-party downloader pages.
- Control a browser when a platform blocks direct download.
- Run `ffmpeg`, `ffprobe`, and `yt-dlp`.
- Optionally access Google Drive through a connector or browser session if cloud Drive upload is requested.

For Codex, useful tools are:

- Terminal/shell access.
- Codex Browser, Chrome automation, Playwright, or Computer Use for browser fallback.
- Google Drive connector only when the user explicitly wants cloud Drive upload.

For Claude Desktop, useful MCP servers are:

- Filesystem MCP for local files.
- Playwright MCP or Browser MCP for browser control.
- Shell/command MCP if the client does not already provide terminal execution.
- Google Drive MCP only when cloud Drive upload is required.

The exact browser MCP does not matter. The requirement is browser control with authenticated-session support when needed.

## Install/Bootstrap

Before running the workflow, verify the command-line tools:

```bash
command -v ffmpeg
command -v ffprobe
command -v yt-dlp || python3 -m yt_dlp --version
```

Install on macOS with Homebrew:

```bash
brew install ffmpeg yt-dlp
python3 -m pip install --upgrade yt-dlp
```

Install Playwright support if the host agent needs browser automation:

```bash
npm install -g playwright
npx playwright install chromium
```

Install a Playwright MCP server for Claude-style clients if no browser MCP exists:

```bash
npm install -g @playwright/mcp
```

Then configure the MCP server in the client. Configuration differs by app, so the skill should say "use an available browser-capable MCP" rather than hard-coding one provider.

## Destination

Set a project pack folder before running the skill. Example:

```text
/path/to/kling-packs
```

If the user gives a Dropbox, Google Drive, or local folder, use that destination. For a cloud-only folder, upload through an available cloud connector or through a browser session. If neither is available, complete the local pack and report that cloud upload is blocked.

## Folder Naming Contract

Every folder name must start with the source handle or readable title, then platform:

```text
creator-handle-or-title - platform - videoid-or-shortcode
```

Examples:

```text
mari_aminah - tiktok - 7613486879467506975
arabellamaexx - instagram - DYcZ-gHuviS
EmmOfficiaI - youtube - dZR_NRfaE5A
ILMM 9_16 - local - MP4
```

Rules:

- Use `youtube`, `tiktok`, `instagram`, or `local` as the platform.
- Use the creator handle when available.
- Include the video id, shortcode, or local file extension.
- Avoid timestamp-only names.
- Avoid folders that start with random downloader codes.
- If the source handle cannot be recovered, use `unavailable-source - platform - code`.

## Runbook

1. Parse the user input.
2. Determine whether the source is YouTube, TikTok, Instagram, or local.
3. Fetch metadata and recover the creator handle/title where possible.
4. Create the final folder using the naming contract.
5. Download the highest available source video into a temporary path.
6. Normalize the video into `original-video.mp4`.
7. Validate `original-video.mp4` with `ffprobe`.
8. Extract `first-frame.png` from the normalized video.
9. Visually verify that the frame matches the requested source.
10. Remove or move raw helper files so the delivered folder contains only the required files.
11. If cloud upload is requested, upload only `original-video.mp4` and `first-frame.png`.
12. Report the folder path and any quality caveats.

## Download Strategy

Start with `yt-dlp`:

```bash
python3 -m yt_dlp \
  -f "bv*+ba/b" \
  --merge-output-format mp4 \
  --remux-video mp4 \
  -o "/tmp/kling-source-download.%(ext)s" \
  "SOURCE_URL"
```

YouTube Shorts:

```bash
python3 -m yt_dlp \
  -f "bv*+ba/b" \
  --merge-output-format mp4 \
  --remux-video mp4 \
  --extractor-args "youtube:player_client=android" \
  -o "/tmp/kling-source-download.%(ext)s" \
  "YOUTUBE_URL"
```

TikTok:

- Try `yt-dlp` first if it works cleanly.
- If direct TikTok download is blocked, low-quality, or watermarked, use a reputable third-party downloader/API.
- Prefer the highest-resolution clean stream.
- Compare file size and resolution before accepting a fallback.

Instagram:

- Try `yt-dlp` first.
- If blocked, use a browser-capable MCP with the logged-in browser session.
- A third-party downloader is acceptable if it gives a higher-quality or more compatible source.
- Do not trust Instagram UI downloads blindly; many need conversion before Finder/Kling will read them.

Local files:

- Copy or transcode from the user-provided source file.
- Still normalize to the final compatibility format.

## Compatibility Standard

The delivered video must work in Apple Finder/Quick Look and Kling.

Final `original-video.mp4` must be:

- MP4 container.
- H.264 video.
- `yuv420p` pixel format.
- AAC audio if audio exists.
- Faststart metadata.

Reject or convert:

- VP9.
- AV1.
- HEVC/H.265.
- 10-bit video.
- Odd Instagram/TikTok MP4 files that do not thumbnail in Finder.

Probe command:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,pix_fmt,width,height,profile \
  -of default=noprint_wrappers=1 original-video.mp4
```

Accept only:

```text
codec_name=h264
pix_fmt=yuv420p
```

If the video does not pass, transcode it.

## Normalize Video

Use this conversion for any questionable download:

```bash
ffmpeg -nostdin -y -i INPUT \
  -map 0:v:0 -map 0:a? \
  -c:v libx264 -preset medium -crf 18 \
  -pix_fmt yuv420p -profile:v high -level 4.1 \
  -c:a aac -b:a 160k \
  -movflags +faststart \
  original-video.mp4
```

If the source is already H.264/yuv420p MP4, still remux:

```bash
ffmpeg -nostdin -y -i INPUT \
  -map 0:v:0 -map 0:a? \
  -c copy -movflags +faststart \
  original-video.mp4
```

## Extract First Frame

Extract from the normalized video, not the raw download:

```bash
ffmpeg -nostdin -y -i original-video.mp4 \
  -vf "select=eq(n\\,0)" \
  -frames:v 1 first-frame.png
```

If the first frame looks blank, black, corrupt, or unrelated, verify the video and source URL. Do not silently substitute a later frame unless the user explicitly asks for a representative frame instead of the first frame.

## Final Folder Cleanup

The delivered folder should contain:

```text
original-video.mp4
first-frame.png
```

Do not leave these visible in the final folder:

- raw downloader files
- `.webm`
- `.mkv`
- incompatible `.mp4`
- metadata JSON
- cookies
- logs
- analysis frames
- nested `source/`, `delivery/`, or `generated/` folders

If raw files are needed temporarily, keep them outside the delivered folder or delete them after validation.

## Quality Checklist

Before telling the user the pack is done:

- Folder name starts with creator/title and platform.
- `original-video.mp4` exists.
- `first-frame.png` exists.
- `original-video.mp4` is H.264/yuv420p.
- The video is not a low-quality fallback unless clearly disclosed.
- The first frame was extracted from the final normalized video.
- The first frame visually matches the requested clip.
- The final folder contains no extra helper files.
- If cloud upload was requested, the cloud folder contains exactly the required deliverables.

## Troubleshooting

If Finder does not show a thumbnail:

- Re-run the compatibility probe.
- Transcode to H.264/yuv420p with `libx264`.
- Confirm the output file is the top-level `original-video.mp4`, not a raw backup.

If Instagram gives a weird MP4:

- Treat it as raw input.
- Transcode it.
- Verify the first frame afterward.

If TikTok direct download is blocked:

- Resolve the short URL in a browser.
- Try a third-party downloader/API.
- Use browser session/cookies only if necessary.

If Google Drive upload is requested but unavailable:

- Finish the local pack.
- Tell the user upload requires a Google Drive connector or browser session.

## Completion Message Template

Use a short completion message:

```text
Created the Kling source pack here:
/path/to/creator - platform - code

It contains `original-video.mp4` and `first-frame.png`. The video validates as H.264/yuv420p and should preview cleanly in Finder/Kling.
```
