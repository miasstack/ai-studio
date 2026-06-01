# Dog Vids: Golden Retriever Hay Truck Rescue — Full Replication Guide

This document lets another LLM pick up and finish (or fully redo) the pipeline for this video.

---

## Project Overview

**Goal**: Generate a YouTube Shorts video (~90s) assembled from 13 AI-generated clips telling a story about a golden retriever puppy accidentally left hanging from a hay truck, rescued by a woman with help from the adult dog.

**Pipeline**: Story idea → Kie.ai storyboard images → Google Flow (Veo 3 Lite) video clips → ffmpeg concat → catbox upload → video_log.md entry.

**Hard requirements**:
- Use `Nano Banana 2` only for still-image generation inside Google Flow.
- Use `Veo 3 Lite` only for every video clip in Flow.
- Generate only `1` video clip at a time in Flow. Do not batch-create multiple clips at once.
- Review each generated image or clip before moving to the next one.

**Current Google Flow UI note**:
- On `2026-04-19`, the Flow video model label shown in the UI is `Veo 3.1 - Lite`.
- Treat that as the current Lite variant and do not switch to any non-Lite video model.

---

## Story Bible

This is the locked narrative for the hay truck video. Do not improvise extra beats.

### Narrative order

1. Hook: a golden retriever puppy is hanging by a rope from the back of a hay truck that is actively driving down the road.
2. The adult golden retriever sees the puppy and runs behind the moving truck, barking in alarm.
3. The adult dog runs along the side of the moving truck to get the driver's attention.
4. Mia notices the adult dog, stops the truck, opens the door, and reacts: "What's wrong?"
5. Mia follows the adult dog to the back of the truck and discovers the puppy hanging there.
6. Mia reacts with concern and urgency, then runs back toward the front/cab area to get a step ladder.
7. Mia places the ladder against the hay stack and climbs up carefully.
8. Mia cuts the rope while securely embracing the puppy.
9. Ending: Mia is safely back down on the ground, and both dogs are licking on her and loving on her.

### Tight story rules

- Mia must **not** appear in the opening hook before the driver-attention beat.
- The reveal is that Mia discovers the puppy only after following the adult dog to the back.
- Do not skip the ladder retrieval/setup step.
- Do not show Mia holding the puppy before the rope-cut rescue beat.
- The final emotional release happens only after the rescue is complete.

### Dog-count rules

- Use exactly `2` dogs in this story:
  - `1` adult golden retriever helper
  - `1` golden retriever puppy in danger
- No extra dogs in the background.
- No dog duplication, morphing, or sudden breed/size changes.
- The adult dog should stay visually consistent from shot to shot.
- The puppy should stay visually consistent from shot to shot.

---

## Mia Character Bible

Mia is the recurring influencer/lead across scenarios. She is always the same woman, only with scenario-appropriate wardrobe changes.

### Identity and look

- Mia is a Latina influencer from Medellin, Colombia.
- Keep her face, hair color, brows, eyes, skin tone, and overall appearance consistent across the whole project.
- Use the same core character in every future scenario; only change outfit, setting, and task.
- For this scenario, Mia is dressed like a farmer: denim overalls, white tank top, brown work boots, hair tied back in a practical low bun.

### Voice and speech

- When Mia speaks English, it should sound like English spoken with a Latina Medellin accent.
- She can speak in Spanglish.
- She can also speak fully in Paisa Spanish when appropriate.
- Medellin/Paisa slang is allowed, but keep it natural and readable rather than exaggerated caricature.
- Keep dialogue short and clean so Flow does not garble it.

### Preferred dialogue beats for this story

- Driver-attention beat: `\"What's wrong?\"` or `\"Mijo, what happened?\"`
- Discovery beat: `\"Ay Dios mio.\"` or `\"Ve, no no no.\"`
- Rescue beat: `\"Ya, bebe, ya te tengo.\"`
- Ending beat: `\"Ay, que belleza.\"` or `\"Mis amores.\"`

If spoken dialogue comes out messy in Flow, prefer fewer words over more words.

### Character assets

- Main character sheet: `/Users/damoneden/dog vids/Mia charachter sheet 4_26.jpg`
- Face reference: `/Users/damoneden/dog vids/images/Golden_Retriever_Hay_Truck_Rescue_20260419_055043/face_ref.jpg`
- Farmer outfit reference: `/Users/damoneden/dog vids/images/Golden_Retriever_Hay_Truck_Rescue_20260419_055043/outfit_ref.jpg`

Always use the face and outfit references when generating or repairing this scenario.

---

## Repeatable Franchise Template

This channel concept should be reusable: a cute golden retriever helps solve a problem, and Mia responds.

### Core template

1. Establish a simple danger/problem in one strong visual.
2. The adult golden retriever notices it first.
3. The dog urgently alerts Mia.
4. Mia understands the problem.
5. Mia takes one clear action to solve it.
6. Emotional payoff with Mia and the dog(s).

### Template constants

- Mia is always the same influencer/character.
- Mia's voice is always Medellin Latina / Paisa-coded.
- The adult golden retriever is always cute, emotionally readable, and proactive.
- The plot should be understandable with the sound off.
- The final beat should feel sweet, relieved, and affectionate.

### Template variables

- Outfit: scenario-specific only
- Setting: scenario-specific only
- Problem to solve: scenario-specific only
- Rescue tool/action: scenario-specific only

Examples:
- farmer + hay truck
- firewoman + small fire rescue
- train conductor + track-side dog rescue
- construction worker + trapped puppy rescue

When making new scenarios, preserve the same story grammar and Mia identity.

---

## Current Status (as of session end)

- All 12 panel clips + 1 hook clip were submitted to Google Flow and generated.
- 14 download triggers were fired via JavaScript into the Flow tab (tab ID `1444145183`, project URL `https://labs.google/fx/tools/flow/project/6bbfdc14-4139-4815-be69-2aee59677377`).
- Files should be in `~/Downloads/` named `flow_clip_00_<guid>.mp4` through `flow_clip_13_<guid>.mp4`.

**Remaining tasks**:
1. Verify downloads completed in `~/Downloads/`
2. Map files to story order
3. ffmpeg concat
4. Upload to catbox/litterbox
5. Generate YouTube title
6. Append to `video_log.md`

---

## Story Panels and GUIDs

DOM order in Flow is **newest-first**. The 14 GUIDs in DOM order (index 0 = newest = hook):

| DOM index | Story role       | Panel image        | GUID |
|-----------|------------------|--------------------|------|
| 0  | Hook             | hook image          | `2d77a5e6-c0e9-4cc2-bb49-4fef13391487` |
| 1  | grid2_p6_BR      | `grid2_p6_BR.jpg`  | `e015dfdd-4435-4668-98a1-0bbdb2663546` |
| 2  | grid2_p5_BL      | `grid2_p5_BL.jpg`  | `e8b65ade-28cd-4b29-b0f8-a3be7804dfca` |
| 3  | grid2_p4_MR      | `grid2_p4_MR.jpg`  | `5cd73403-2736-4c24-95bd-f036a2934a97` |
| 4  | grid2_p3_ML      | `grid2_p3_ML.jpg`  | `e4306047-c66e-4ed9-a574-d15cb47f68e7` |
| 5  | grid2_p2_TR      | `grid2_p2_TR.jpg`  | `7e3ce91f-3f07-410f-b308-253e7654be31` |
| 6  | grid2_p1_TL      | `grid2_p1_TL.jpg`  | `d10fcfde-b6fc-4560-aa8b-cbf7892929bf` |
| 7  | grid1_p6_BR      | `grid1_p6_BR.jpg`  | `1c6c4178-0b6d-4cdb-a562-d6b09f1b5160` |
| 8  | grid1_p5_BL      | `grid1_p5_BL.jpg`  | `5ea4fdeb-4494-4370-92b1-0a95f5b08704` |
| 9  | grid1_p4_MR      | `grid1_p4_MR.jpg`  | `1961c16d-eb1a-406a-b33d-9b837743a7d9` |
| 10 | grid1_p3_ML      | `grid1_p3_ML.jpg`  | `f8293eb2-4b20-4391-9a18-0f225e576dd2` |
| 11 | grid1_p2_TR      | `grid1_p2_TR.jpg`  | `be6b5384-1456-4be7-a1ef-d93cc68ca04d` |
| 12 | grid1_p1_TL      | `grid1_p1_TL.jpg`  | `acce660d-2f2b-44ab-9834-46845d22b17d` |
| 13 | (extra/dup)      | unknown            | `3b869826-e296-40d3-8889-45fad4ec84f4` |

**Story order for concatenation** (skip index 13, the duplicate):
```
hook → grid1_p1_TL → grid1_p2_TR → grid1_p3_ML → grid1_p4_MR → grid1_p5_BL → grid1_p6_BR
     → grid2_p1_TL → grid2_p2_TR → grid2_p3_ML → grid2_p4_MR → grid2_p5_BL → grid2_p6_BR
```

In terms of downloaded filenames:
```
flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4   (hook)
flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4   (grid1_p1_TL)
flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4   (grid1_p2_TR)
flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4   (grid1_p3_ML)
flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4   (grid1_p4_MR)
flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4   (grid1_p5_BL)
flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4   (grid1_p6_BR)
flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4   (grid2_p1_TL)
flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4   (grid2_p2_TR)
flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4   (grid2_p3_ML)
flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4   (grid2_p4_MR)
flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4   (grid2_p5_BL)
flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4   (grid2_p6_BR)
```

## Known Problems In Current Source Images

The currently generated source images are not fully usable as-is. Important issues already identified:

- `hook.jpg` incorrectly shows Mia in the opening shot; she should not appear yet.
- The current visual story reveals Mia too early in parts of Grid 1 / the hook setup.
- Grid 2 sequencing is muddy, and the ladder/climb/cut order is not tight enough.
- Some shots risk introducing extra dogs or inconsistent dog placement.

Because of this, expect to regenerate at least some still images before trusting the current video clips.

---

## Step 1: Verify Downloads

Do not rely on a raw `flow_clip_*.mp4` count by itself, because `~/Downloads` may contain clips from older runs.

Verify the exact expected files instead:

```bash
cd ~/Downloads

expected=(
  "flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4"
  "flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4"
  "flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4"
  "flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4"
  "flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4"
  "flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4"
  "flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4"
  "flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4"
  "flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4"
  "flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4"
  "flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4"
  "flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4"
  "flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4"
  "flow_clip_13_3b869826-e296-40d3-8889-45fad4ec84f4.mp4"
)

missing=0
for f in "${expected[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "MISSING: $f"
    missing=1
  fi
done

ls -lh "${expected[@]}"
test "$missing" -eq 0 && echo "All expected Flow clips are present."
```

If you want a one-line count after that:

```bash
printf '%s\n' "${expected[@]}" | wc -l   # should be 14
```

If files are missing, re-trigger downloads by opening the Flow project tab and running:

```javascript
const guids = [
  '2d77a5e6-c0e9-4cc2-bb49-4fef13391487',
  'e015dfdd-4435-4668-98a1-0bbdb2663546',
  'e8b65ade-28cd-4b29-b0f8-a3be7804dfca',
  '5cd73403-2736-4c24-95bd-f036a2934a97',
  'e4306047-c66e-4ed9-a574-d15cb47f68e7',
  '7e3ce91f-3f07-410f-b308-253e7654be31',
  'd10fcfde-b6fc-4560-aa8b-cbf7892929bf',
  '1c6c4178-0b6d-4cdb-a562-d6b09f1b5160',
  '5ea4fdeb-4494-4370-92b1-0a95f5b08704',
  '1961c16d-eb1a-406a-b33d-9b837743a7d9',
  'f8293eb2-4b20-4391-9a18-0f225e576dd2',
  'be6b5384-1456-4be7-a1ef-d93cc68ca04d',
  'acce660d-2f2b-44ab-9834-46845d22b17d',
  '3b869826-e296-40d3-8889-45fad4ec84f4'
];
guids.forEach((guid, i) => {
  const a = document.createElement('a');
  a.href = `/fx/api/trpc/media.getMediaUrlRedirect?name=${guid}`;
  a.download = `flow_clip_${String(i).padStart(2,'0')}_${guid}.mp4`;
  document.body.appendChild(a);
  setTimeout(() => { a.click(); a.remove(); }, i * 500);
});
'Downloads triggered: ' + guids.length;
```

---

## Step 2: Move Clips to Working Directory

```bash
DEST="/Users/damoneden/dog vids/clips/hay_truck"
mkdir -p "$DEST"
cp ~/Downloads/flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4 "$DEST/"
cp ~/Downloads/flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4 "$DEST/"
cp ~/Downloads/flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4 "$DEST/"
cp ~/Downloads/flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4 "$DEST/"
cp ~/Downloads/flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4 "$DEST/"
cp ~/Downloads/flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4 "$DEST/"
cp ~/Downloads/flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4 "$DEST/"
cp ~/Downloads/flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4 "$DEST/"
cp ~/Downloads/flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4 "$DEST/"
cp ~/Downloads/flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4 "$DEST/"
cp ~/Downloads/flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4 "$DEST/"
cp ~/Downloads/flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4 "$DEST/"
cp ~/Downloads/flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4 "$DEST/"
cp ~/Downloads/flow_clip_13_3b869826-e296-40d3-8889-45fad4ec84f4.mp4 "$DEST/"
```

---

## Step 3: Build ffmpeg Concat List

Create `/Users/damoneden/dog vids/clips/hay_truck/concat.txt`:

```
file 'flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4'
file 'flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4'
file 'flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4'
file 'flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4'
file 'flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4'
file 'flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4'
file 'flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4'
file 'flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4'
file 'flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4'
file 'flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4'
file 'flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4'
file 'flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4'
file 'flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4'
```

---

## Step 4: ffmpeg Concatenation

```bash
cd "/Users/damoneden/dog vids/clips/hay_truck"
mkdir -p "/Users/damoneden/dog vids/output"
ffmpeg -f concat -safe 0 -i concat.txt -c copy \
  "/Users/damoneden/dog vids/output/hay_truck_rescue_$(date +%Y%m%d_%H%M%S).mp4"
```

If clips have mismatched codecs/resolutions, re-encode:
```bash
ffmpeg -f concat -safe 0 -i concat.txt \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -crf 18 -preset fast -c:a aac \
  "/Users/damoneden/dog vids/output/hay_truck_rescue_$(date +%Y%m%d_%H%M%S).mp4"
```

---

## Step 5: Upload to Catbox

```bash
OUTPUT_FILE="/Users/damoneden/dog vids/output/hay_truck_rescue_TIMESTAMP.mp4"  # use actual filename
curl -F "reqtype=fileupload" -F "fileToUpload=@$OUTPUT_FILE" https://catbox.moe/user/api.php
```

This returns a URL like `https://files.catbox.moe/xxxxxx.mp4`. Save it.

Alternatively use litterbox for 72h expiry:
```bash
curl -F "reqtype=fileupload" -F "time=72h" -F "fileToUpload=@$OUTPUT_FILE" https://litterbox.catbox.moe/resources/internals/api.php
```

---

## Step 6: Review The Final Video

There is no dedicated Codex video-review skill installed for this project, so use local video tools directly.

Check file metadata:

```bash
ffprobe -v error -show_entries format=duration,size:stream=index,codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 \
  "/Users/damoneden/dog vids/output/hay_truck_rescue_TIMESTAMP.mp4"
```

Export a few frames for spot-checking:

```bash
mkdir -p "/Users/damoneden/dog vids/output/review_frames"
ffmpeg -i "/Users/damoneden/dog vids/output/hay_truck_rescue_TIMESTAMP.mp4" \
  -vf "fps=1/8,scale=540:-1" \
  "/Users/damoneden/dog vids/output/review_frames/frame_%03d.jpg"
```

What to check:
- The hook clip comes first.
- There are 13 story clips total in the final render.
- No duplicate extra clip from `flow_clip_13_...` appears in the concat.
- Resolution is vertical and consistent through the whole video.
- There are no black frames, broken transitions, or obvious codec glitches.

If something looks wrong, go back to `concat.txt` before uploading.

---

## Step 7: Generate YouTube Title

Style reference from `TITLE_EXAMPLES` in `prompts.txt`:
- "She Had No Idea What Was Hanging From Her Truck"
- "The Dogs Knew Before She Did"
- "She Stopped The Truck Just In Time"

Generate a title in this style: short, punchy, emotional, and easy to read in a YouTube Shorts feed. Focus on the dog's loyalty or the rescue moment. An emoji is optional, not required.

---

## Step 8: Log to video_log.md

Append to `/Users/damoneden/dog vids/video_log.md`:
```
| 2026-04-19 HH:MM | Golden Retriever Hay Truck Rescue | {TITLE} | [{URL}]({URL}) |
```

Match the existing table exactly:
- Keep the human-readable idea name `Golden Retriever Hay Truck Rescue`
- Include a timestamp, not just the date
- Preserve the four-column Markdown table format

---

## Full Pipeline Reference (for future ideas)

### Tools Used
- **Kie.ai**: Storyboard grid image generation (6-panel grids, 9:16 aspect ratio)
- **Google Flow (Veo 3 Lite)**: Free video generation at `https://labs.google/fx/tools/flow`
  - 10 credits per clip, ~8s clips
  - Use `Veo 3 Lite` only; do not switch models mid-project
  - Generate one clip, wait for it to finish, review it, then move to the next clip
  - Ingredients mode: attach up to 3 reference images per clip
  - `+` button opens ingredient picker; search by filename
- **ffmpeg**: Concatenation (`-f concat -safe 0`)
- **catbox.moe**: Free file hosting via curl API

### Key JavaScript for Flow

**Set prompt text** (inject once per page load, then call `window._setPrompt("text")`):
```javascript
window._setPrompt = function(text) {
  const div = document.querySelectorAll('[contenteditable="true"]')[0];
  div.focus();
  const fiberKey = Object.keys(div).find(k => k.startsWith('__reactFiber'));
  let f = div[fiberKey];
  let editor = null;
  for (let i = 0; i < 25; i++) {
    f = f.return;
    if (!f) break;
    try {
      if (f.memoizedState && f.memoizedState.memoizedState && f.memoizedState.memoizedState.editor) {
        editor = f.memoizedState.memoizedState.editor;
        break;
      }
    } catch(e) {}
  }
  if (!editor) return 'ERROR: editor not found';
  const currentLen = editor.children[0].children[0].text.length;
  if (currentLen > 0) {
    editor.selection = {anchor:{path:[0,0],offset:0}, focus:{path:[0,0],offset:currentLen}};
    editor.deleteFragment();
  }
  editor.insertText(text);
  return editor.children[0].children[0].text.slice(0, 80);
};
```

**Download all generated clips** (after generation is complete):
```javascript
// Get GUIDs from the Flow page DOM first, then:
guids.forEach((guid, i) => {
  const a = document.createElement('a');
  a.href = `/fx/api/trpc/media.getMediaUrlRedirect?name=${guid}`;
  a.download = `flow_clip_${String(i).padStart(2,'0')}_${guid}.mp4`;
  document.body.appendChild(a);
  setTimeout(() => { a.click(); a.remove(); }, i * 500);
});
```

**Extract GUIDs from current Flow project page**:
```javascript
// Videos are in DOM newest-first
document.querySelectorAll('[data-media-id], video[src*="labs.google"]')
// Or look for GUIDs in network requests / page source
```

### Policy Notes
- Do NOT use character names (e.g. "Mia") — Flow will reject with "prominent people" policy violation
- Use "a woman" instead of any named character
- Avoid any text that implies real identifiable people

### Ingredient Reference Images
For this project, uploaded to Flow:
- `face_ref.jpg` — character face reference
- `outfit_ref.jpg` — character outfit reference
- Per-scene panel images: `grid1_p1_TL.jpg` through `grid2_p6_BR.jpg`

Each clip generation uses 3 ingredients: `{panel image}` + `face_ref.jpg` + `outfit_ref.jpg`

---

## File Locations

| File | Path |
|------|------|
| Prompts & ideas | `/Users/damoneden/dog vids/prompts.txt` |
| Video log | `/Users/damoneden/dog vids/video_log.md` |
| Output videos | `/Users/damoneden/dog vids/output/` |
| Storyboard images | `/Users/damoneden/dog vids/` (root, various grids) |
| This guide | `/Users/damoneden/dog vids/REPLICATION_GUIDE.md` |

---

## Immediate Next Action

Run these commands in sequence:

```bash
# 1. Check downloads
cd ~/Downloads
ls -lh flow_clip_*2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4 \
       flow_clip_*e015dfdd-4435-4668-98a1-0bbdb2663546.mp4 \
       flow_clip_*e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4 \
       flow_clip_*5cd73403-2736-4c24-95bd-f036a2934a97.mp4 \
       flow_clip_*e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4 \
       flow_clip_*7e3ce91f-3f07-410f-b308-253e7654be31.mp4 \
       flow_clip_*d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4 \
       flow_clip_*1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4 \
       flow_clip_*5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4 \
       flow_clip_*1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4 \
       flow_clip_*f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4 \
       flow_clip_*be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4 \
       flow_clip_*acce660d-2f2b-44ab-9834-46845d22b17d.mp4 \
       flow_clip_*3b869826-e296-40d3-8889-45fad4ec84f4.mp4

# 2. Move to working dir
mkdir -p "/Users/damoneden/dog vids/clips/hay_truck"
cp ~/Downloads/flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"
cp ~/Downloads/flow_clip_13_3b869826-e296-40d3-8889-45fad4ec84f4.mp4 "/Users/damoneden/dog vids/clips/hay_truck/"

# 3. Create concat list (story order — skip _13_ which is a duplicate)
cd "/Users/damoneden/dog vids/clips/hay_truck"
cat > concat.txt << 'EOF'
file 'flow_clip_00_2d77a5e6-c0e9-4cc2-bb49-4fef13391487.mp4'
file 'flow_clip_12_acce660d-2f2b-44ab-9834-46845d22b17d.mp4'
file 'flow_clip_11_be6b5384-1456-4be7-a1ef-d93cc68ca04d.mp4'
file 'flow_clip_10_f8293eb2-4b20-4391-9a18-0f225e576dd2.mp4'
file 'flow_clip_09_1961c16d-eb1a-406a-b33d-9b837743a7d9.mp4'
file 'flow_clip_08_5ea4fdeb-4494-4370-92b1-0a95f5b08704.mp4'
file 'flow_clip_07_1c6c4178-0b6d-4cdb-a562-d6b09f1b5160.mp4'
file 'flow_clip_06_d10fcfde-b6fc-4560-aa8b-cbf7892929bf.mp4'
file 'flow_clip_05_7e3ce91f-3f07-410f-b308-253e7654be31.mp4'
file 'flow_clip_04_e4306047-c66e-4ed9-a574-d15cb47f68e7.mp4'
file 'flow_clip_03_5cd73403-2736-4c24-95bd-f036a2934a97.mp4'
file 'flow_clip_02_e8b65ade-28cd-4b29-b0f8-a3be7804dfca.mp4'
file 'flow_clip_01_e015dfdd-4435-4668-98a1-0bbdb2663546.mp4'
EOF

# 4. Concat
mkdir -p "/Users/damoneden/dog vids/output"
ffmpeg -f concat -safe 0 -i concat.txt -c copy \
  "/Users/damoneden/dog vids/output/hay_truck_rescue_$(date +%Y%m%d_%H%M%S).mp4"

# 5. Upload (replace FILENAME with actual output filename)
curl -F "reqtype=fileupload" \
  -F "fileToUpload=@/Users/damoneden/dog vids/output/FILENAME.mp4" \
  https://catbox.moe/user/api.php
```

Then append to `/Users/damoneden/dog vids/video_log.md`:
```
| 2026-04-19 HH:MM | Golden Retriever Hay Truck Rescue | {GENERATED_TITLE} | [{CATBOX_URL}]({CATBOX_URL}) |
```
