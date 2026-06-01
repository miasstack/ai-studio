---
name: Dog Vids project
description: YouTube Shorts auto-generation pipeline using Kie AI and Kinovi APIs
type: project
---

YouTube Shorts generation pipeline for the "Dog Vids" channel, located at `/Users/damoneden/dog vids`.

**Why:** Automate the full Shorts production workflow — image gen → video gen → combine → publish.

**How to apply:** When working in this project, understand the full pipeline and file layout before suggesting changes.

## File layout
- `generate_video.py` — main pipeline script (Python 3)
- `prompts.txt` — video idea presets (user fills in; script randomly selects one per run)
- `.env` — API keys (KIE_API_KEY, KINOVI_API_KEY, ANTHROPIC_API_KEY)
- `requirements.txt` — pip deps: anthropic, python-dotenv, requests
- `video_log.md` — running log of all generated videos (date, idea, title, catbox link)
- `videos/` — final combined MP4s saved here (never intermediate clips)
- `.temp/` — scratch space for intermediate clips (auto-cleaned after each run)
- `~/.claude/commands/generate-a-video.md` — Claude Code skill (invoke with /generate-a-video)

## Character — Mia
- Character sheet saved as `mia_reference.jpg` in project root
- Base description in `prompts.txt` under `[MIA]` block: "a beautiful young woman in her mid-20s with long flowing wavy blonde hair, striking grey-green eyes, tan complexion, full lips, and defined brows"
- Each idea has a `MIA_OUTFIT` field — her outfit changes per video context
- Use `[MIA]` token anywhere in prompts — script auto-replaces with full description + outfit
- Mia sheet is uploaded to catbox once and URL cached in `mia_cache.json`
- Mia sheet URL is always passed as first reference image in every Kie AI call
- For Grid 1: references are [mia_url, hook_img_url]; for Grid 2: [mia_url, grid1_img_url]

## Pipeline steps
1. Randomly select a filled-in idea from prompts.txt
2. Generate Hook Image → Kie AI Nanobanana 2, 2K, 9:16
3. Generate Grid 1 Image (Hook as reference) → same model
4. Generate Grid 2 Image (Grid 1 as reference) → same model
5. Submit Hook Video (4s, keyframe mode) + Grid 1 Video (15s, reference mode) + Grid 2 Video (15s, reference mode) to Kinovi Seedance 2.0 concurrently
6. Poll all 3 in parallel via ThreadPoolExecutor
7. Download clips, combine Hook→Grid1→Grid2 with ffmpeg -c copy
8. Upload final MP4 to catbox.moe (anonymous)
9. Generate title via Claude claude-opus-4-6 using TITLE_EXAMPLES from prompts.txt as style reference
10. Append row to video_log.md; save final video to videos/

## APIs
- Kie AI create: POST https://api.kie.ai/api/v1/jobs/createTask
- Kie AI poll: GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=...  (resultJson → resultUrls[0])
- Kinovi create: POST https://kinovi.ai/api/v1/jobs/createTask
- Kinovi poll: GET https://kinovi.ai/api/v1/jobs/recordInfo?taskId=...  (output[0].url)
- Catbox: POST https://catbox.moe/user/api.php (anonymous, reqtype=fileupload)
