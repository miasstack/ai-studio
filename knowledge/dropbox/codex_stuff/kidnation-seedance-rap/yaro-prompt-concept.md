# Yaro Prompt Concept: KidNation Seedance Rap Videos

## Core Idea

Use the Yaro prompt style for KidNation music videos by combining tight
rap-video direction with kid-safe, school-centered visuals. Each prompt should
feel like a real music video scene: confident performance, clear lip sync,
camera movement, lyric-matched action, and strong visual rhythm.

For KidNation, replace adult trap-video imagery with bright educational
performance locations: classrooms, school hallways, playground courts, colorful
stages, desks, books, backpacks, flashcards, chalkboards, and call-and-response
group energy.

## Higgsfield / Seedance Setup

Use uploaded Higgsfield handles directly in prompts:

- `@jordansheet`
- `@narisheet`
- `@mellysheet`
- `@bjornsheet`
- `@salomesheet`
- `@arjunsheet`
- `@video_1` for the active acapella/lip-sync video

Do not write the character's normal name as the main identity lock when a sheet
handle is available. Use the handle first.

Always include this audio line:

```text
High-quality 3D render. Audio: Tight lip-sync performance matching the provided acapella track in @video_1.
```

## Audio Cutting Rules

Every Seedance clip must be cut from the original source audio, not edited into
shape after the fact.

Rules:

- Cut only at a natural vocal gap, breath, phrase ending, or section boundary.
- Never cut through an active word, adlib, or sustained "yah."
- Use whole-number durations only: `5 seconds`, `8 seconds`, `10 seconds`,
  `12 seconds`, `13 seconds`, etc.
- Do not use decimal-duration clips like `8.19 seconds`.
- Do not pad the end with silence to force a round duration.
- Do not manufacture empty space at the end of the acapella.
- If `10 seconds` is not clean, test nearby whole numbers.
- Going past `10 seconds` is allowed when it lands cleaner, but never exceed the
  platform limit for the current workflow.

## Prompt Structure

Write prompts as a single paste-ready block. Use direct visual instructions,
then line-by-line lyric actions. Use `CHANGE SCENE` where Seedance should switch
visual setups.

```text
PROMPT

Style & Mood: 3D Pixar-style animation, vibrant colors, clean cinematic
lighting, kid-safe urban music-video energy, polished school-performance world.

Narrative: @jordansheet is the lead performer in a colorful elementary
classroom turned into a mini rap stage. He performs directly to camera with
confident kid-rapper energy, readable mouth shapes, expressive eyebrows, and
natural beat-matched hand gestures.

LINE "[exact lyric]": [shot size], [action tied to lyric], [camera movement],
[prop or environment action], [expression].

CHANGE SCENE

LINE "[exact lyric]": [new setup], [new action], [visual payoff].

High-quality 3D render. Audio: Tight lip-sync performance matching the provided
acapella track in @video_1.
```

## Lyric Mapping Style

Each lyric should trigger visible action:

- "books on the desk" means books should visibly appear on or near a desk.
- "when I read" means the performer opens, points to, or reads from a book.
- "backpack packed" means the performer taps, zips, swings, or opens a backpack.
- "tools for success" means pencils, notebooks, flashcards, or school supplies
  pop into the visual rhythm.
- "person, place or thing" means big readable words can appear at the exact
  lyric moment: `PERSON`, `PLACE`, `THING`.
- "yah" should be treated like an adlib moment with a close-up, bounce, head
  nod, or camera punch-in.

## Text-On-Screen Rules

Use text only when the lyric benefits from it. Keep it big, simple, and timed
to the vocal.

Good:

```text
Huge clean 3D words appear one at a time behind him: PERSON, PLACE, THING.
Each word lands exactly when he says it, then pops away on the beat.
```

Avoid:

- Crowded captions.
- Long sentences on screen.
- Text that blocks the mouth during lip sync.
- Text that appears before the lyric is heard.

## KidNation Visual Rules

Keep the energy cool and aspirational, not babyish.

Use:

- confident kid-rapper poses
- school supplies as props
- colorful classroom lighting
- clean camera push-ins
- rhythmic hand gestures
- call-and-response choreography
- expressive close-ups for adlibs

Avoid:

- weapons
- alcohol
- cash flexing
- clubs
- intimidating crime imagery
- sexualized styling
- random extra characters
- generic characters that do not match the uploaded KidNation sheets

## Audio-to-Video Clip Pipeline

Seedance requires `@video_1` to be a **video file**, not a raw audio file.
Even though the clip has no visual content, it must be wrapped as an MP4 with
a black video track. The audio is what Seedance reads for lip-sync locking.

### Step 1 — Analyze the source audio

```bash
# Get song duration
ffprobe -v quiet -show_entries format=duration -of csv=p=0 vocals.mp3

# Find major section boundaries (true silence gaps)
ffmpeg -i vocals.mp3 -af "silencedetect=noise=-35dB:duration=0.2" -f null - 2>&1 | grep silence

# Get BPM for beat-grid clip planning
python3 -c "import librosa; y,sr=librosa.load('vocals.mp3',sr=None); t,_=librosa.beat.beat_track(y=y,sr=sr); print(float(t))"
```

**Clip length math:** At ~134 BPM, 5 bars = 8.96s ≈ 9s. Use 9-second clips as
the default. Never exceed 11 seconds (AI gets unstable past ~10s).
Always use whole-number durations: `7`, `9`, `10`, `11` — never `8.19`.

### Step 2 — Build the clip plan

Map lyrics to timestamps using the beat grid. Cut only at:
- natural vocal gaps / breath points
- phrase endings (end of a line)
- section boundaries (verse → chorus transitions)

Never cut through an active word, adlib, or sustained vocal.

### Step 3 — Generate video-wrapped clips

```bash
# Single clip: black video track + trimmed audio = Seedance-ready MP4
ffmpeg -y \
  -f lavfi -i "color=black:size=1920x1080:rate=30" \
  -ss START_SECONDS -t DURATION_SECONDS -i vocals.mp3 \
  -map 0:v -map 1:a \
  -shortest \
  -c:v libx264 -crf 23 -preset fast \
  -c:a aac -b:a 192k \
  clip_name.mp4
```

Use `generate_clips.py` in the project folder to batch-generate all clips
for a song. Edit the `CLIPS` list to adjust start times and durations.

### Step 4 — Calibrate timestamps

Timestamps from BPM analysis are estimates. **Listen to each generated clip**
before submitting to Seedance. If a lyric is cut mid-word:
1. Open `generate_clips.py`
2. Adjust that clip's `start_sec` by ±2-4 seconds
3. Re-run the script — it regenerates all clips

## Clip Asset Checklist

For each Seedance scene, prepare:

- [ ] `clip_XX_name.mp4` — black video + trimmed acapella audio
- [ ] Clip confirmed by listening — right lyrics, no mid-word cuts
- [ ] Matching instrumental clip for editing sync (kept separate)
- [ ] Character handle uploaded: `@jordansheet`, `@narisheet`, etc.
- [ ] `@video_1` = the acapella clip MP4 for this scene
- [ ] Paste-ready Yaro prompt (single block, no special chars)
- [ ] Duration is a whole number in seconds

## Example Clip Prompt

```text
PROMPT

Style & Mood: 3D Pixar-style animation, vibrant colors, clean cinematic
lighting, kid-safe urban music-video energy, polished elementary classroom
performance.

Narrative: @jordansheet is alone in a colorful classroom turned into a mini
rap stage. He performs like a confident young rapper, facing camera with tight
lip sync, expressive eyebrows, rhythmic shoulder bounce, and clean beat-matched
hand gestures.

LINE "Person, place or thing": medium close-up of @jordansheet pointing to
three floating 3D words that appear behind him one by one: PERSON, PLACE,
THING. Each word pops on the exact lyric, with bright classroom colors and
sharp readable lettering.

CHANGE SCENE

LINE "yah": quick punch-in close-up on @jordansheet's mouth and face as he
delivers the adlib with a confident head nod, then the camera snaps back to
the classroom stage.

CHANGE SCENE

LINE "That's a noun all day": @jordansheet plants his feet, points to the
camera, and the classroom lights pulse on the beat while the chalkboard behind
him glows with a clean noun-symbol pattern, no extra text blocking his face.

High-quality 3D render. Audio: Tight lip-sync performance matching the provided
acapella track in @video_1.
```
