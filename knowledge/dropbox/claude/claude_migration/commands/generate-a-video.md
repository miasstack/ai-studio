Run the Dog Vids YouTube Shorts generation pipeline.

## Steps

1. Run the generation script with the Bash tool:
   ```
   cd "/Users/damoneden/dog vids" && python3 generate_video.py
   ```
   Stream all output to the user as it appears so they can follow progress.

2. When the script finishes, find the line starting with `PIPELINE_RESULT:` in the output and parse the JSON that follows it. Extract:
   - `idea` — the idea name
   - `title_examples` — list of example titles
   - `catbox_url` — the public video link
   - `saved_path` — local file path
   - `timestamp` — date/time string

3. Generate a brand-new YouTube Shorts title for this video. Use `title_examples` as your style and tone reference. Match the exact format, energy, and length of those examples. Output ONLY the title — no explanation.

4. Append a row to `/Users/damoneden/dog vids/video_log.md` using the Edit tool:
   ```
   | {timestamp} | {idea} | {your generated title} | [{catbox_url}]({catbox_url}) |
   ```

5. Display the final results clearly to the user:

   ---
   **Title:** {your generated title}
   **Video:** {catbox_url}
   **Saved:** {saved_path}
   ---

## Critique loop — always do this on the title

After generating the video and before showing the user, run three passes on the title:

**Pass 1 — Generate**
Create the YouTube Shorts title as normal using `title_examples` as your style guide.

**Pass 2 — Critique**
Score your own title 1–10 on these things:
- Would a complete stranger stop scrolling for this? (the hook)
- Is it specific enough to feel real, not generic?
- Does it match the energy and format of the example titles?
- Is it the right length (short = punchy, not a full sentence)?

Write down what's weak about it.

**Pass 3 — Improve**
If score is 7 or lower: write 2 more title options fixing the weak spots. Pick the strongest one.
If score is 8+: keep it.

Show the user only the final chosen title. Don't explain the process unless they ask.

## Error handling
If the script exits with an error:
- Missing .env keys → remind user to fill in `/Users/damoneden/dog vids/.env`
- Missing dependencies → run `pip3 install -r "/Users/damoneden/dog vids/requirements.txt"`
- ffmpeg not found → `brew install ffmpeg`
- API error → show the raw error so the user can act on it

Do not re-run the script unless the user explicitly asks.
