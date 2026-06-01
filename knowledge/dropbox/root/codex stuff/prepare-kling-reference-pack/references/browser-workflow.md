# Browser Workflow

Use these notes when a direct CLI workflow is unavailable.

## Downloading the Source Clip

Preferred order:

1. Use a direct downloader if the environment already has one.
2. Otherwise use browser automation with a user-approved downloader site such as Publer.

Practical browser flow:

1. Open the downloader page.
2. Paste the public video URL.
3. Trigger the conversion or fetch step.
4. Wait for the final download control to appear.
5. Save the file directly into `source/source-video.mp4`.

If you are using Playwright code, rely on the page download event so the file lands in the right path instead of the default downloads folder.

## Uploading the Finished Pack to Google Drive

The Drive connector is useful for finding the right folder URL and reading metadata, but arbitrary `.mp4` and `.png` uploads may still require browser automation.
Default destination folder: `https://drive.google.com/drive/folders/1xDj5e57IOq3pySoMcXqK8HrvBUOgpzzp`

Practical browser flow:

1. Open the destination Drive folder URL.
2. Create a subfolder named after the pack slug if needed.
3. Use file upload or folder upload.
4. At minimum upload `source-video.mp4` and `mia-still.png`.
5. Upload the rest of the pack contents when possible.
6. Verify the uploaded files are visible before reporting success.

If folder upload is unsupported in the browser session, upload the files one by one:

- `source-video.mp4`
- `first-frame.png`
- `mia-still.png`
- `shot-notes.md`
- `mia-prompt.md`
- `manifest.json`
