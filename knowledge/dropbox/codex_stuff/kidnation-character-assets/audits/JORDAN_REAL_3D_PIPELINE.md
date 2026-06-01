# Jordan Real 3D Pipeline

Status: local procedural Blender passes are rejected.

The latest candidate, `jordan_proper_v3`, is a real Blender/FBX/GLB export with a transform rig, but it does not pass the KidNation visual gate. It still reads as a procedural doll/blockout next to the approved Jordan cutout and character sheet.

Do not import the following as final character art:

- `hero3d/jordan_from_sheet_v1`
- `hero3d/jordan_proper_v2`
- `hero3d/jordan_proper_v3`

Use them only as process artifacts or rigging tests.

## Why The Current Loop Failed

The approved Arjun look came from a polished visual target/cutout path. The local Blender scripts can build riggable forms, but they are not producing production-quality KidNation character geometry from scratch. The missing piece is a true source mesh, not another Blender-control skill.

## Correct Next Pipeline

1. Generate or obtain a high-quality Jordan source mesh from the existing Jordan sheet/cutout.
2. Import the mesh into Blender.
3. Clean topology, fix hair/clothing volumes, preserve the exact Jordan identity.
4. Auto-rig or hand-rig in Blender.
5. Export Unity FBX/GLB.
6. Run the audit contact sheet before showing or importing into the game.

## GPT Image Prompt For Better Source Input

Use the attached Jordan cutout and Jordan turnaround sheet as strict identity references. Create a clean orthographic 3D character turnaround of the exact same KidNation character, Jordan: warm brown skin, large expressive brown eyes, thick black eyebrows, visible cornrow braids with neat scalp parting rows, short hanging braids behind the ears, red open jacket, white shirt, gold chain, dark blue jeans, gray sneakers. Full-body neutral A-pose, arms slightly away from body, feet flat, child proportions, cute premium animated-film 3D style, soft studio lighting, clean white background. Preserve the face shape, hair silhouette, jacket silhouette, and outfit colors exactly. No text, no logos, no extra accessories, no clay look, no toy look, no flat cutout look.

Deliverables needed from image generation:

- Front orthographic full-body PNG.
- Left side orthographic full-body PNG.
- Back orthographic full-body PNG.
- 3/4 front beauty render PNG.
- One combined turnaround sheet PNG.

These images should then go into an image-to-3D or professional character generation tool before Blender cleanup.

## Candidate External Steps To Test

- Image-to-3D source mesh: TRELLIS/Hunyuan3D/Meshy/Tripo/Rodin-style workflow or a commercial character tool.
- Auto-rigging: AutoRig.online, Kinemo, Neural4D, or Blender Rigify after mesh cleanup.

The quality gate remains the final judge. A file existing is not enough.
