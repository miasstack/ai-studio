# Mia Still Prompt Template

Use this template after reviewing `source/first-frame.png`, `analysis/shot-notes.md`, and the Mia character sheet asset.

## Mia Identity Anchors

Keep these traits stable unless the user explicitly asks for a variation:

- Long blonde hair with a center part and soft, polished waves
- Glam beauty styling with sculpted brows, defined lashes, contoured cheeks, and full neutral lips
- Curvy hourglass figure with pronounced hips and bust
- Soft tan complexion and polished influencer/editorial finish
- Facial identity driven by the character sheet, not by the source creator

## Face Lock Notes

When the face starts drifting, explicitly restate the character sheet traits:

- Oval-to-heart face shape with soft, sculpted cheekbones
- Almond-shaped light hazel/grey-green eyes
- Thick arched brows with a clean glam shape
- Slim refined nose
- Full nude-toned lips with a defined cupid's bow
- Smooth warm tan skin and symmetrical polished beauty look
- Blonde hair framing the face with a clean center part

## Prompt Formula

```text
Create a polished photorealistic still of Mia, keeping her identity locked to the attached character sheet: oval-heart face shape, soft sculpted cheekbones, almond-shaped light hazel/grey-green eyes, thick arched brows, slim refined nose, full nude lips with a defined cupid's bow, warm tan skin, long center-parted blonde waves, glam makeup, and curvy hourglass proportions. Match the source frame's exact camera perspective, crop, pose direction, lens feel, lighting direction, and scene mood. Recreate the same fashion category and overall styling energy, but redesign the outfit so it feels original, premium, and comparable rather than copied. Keep the background and color palette consistent with the source frame's look. Preserve realistic anatomy, hands, fabric behavior, and natural skin detail. Output as a clean single frame for later image-to-video use.
```

## Fill-In Additions

Append specific details for:

- Crop and body visibility
- Camera height and angle
- Head turn and gaze
- Outfit silhouette, materials, and color palette
- Background setting
- Emotional tone

## Guardrails

- Say "comparable outfit" or "inspired by the silhouette" rather than "same exact outfit."
- Avoid named brand logos unless the user explicitly wants them and has rights to use them.
- Keep Mia recognizable to the character sheet instead of blending toward the source creator's face.
- If the source frame is weak or blurry, improve clarity while keeping composition intact.
- If the output starts drifting, restate the blonde hair color, center part, glam face, and hourglass body shape explicitly.
- Prioritize matching Mia's face over matching the source creator's exact expression.

## Flow-Specific Tip

If working in Google Flow:

- Start with `Nano Banana Pro` when you expect face drift.
- If the first pass has the right composition but the wrong face, use Flow's edit tools on the face region instead of changing the whole image.
- Keep a good base image in project history and refine forward from it.
