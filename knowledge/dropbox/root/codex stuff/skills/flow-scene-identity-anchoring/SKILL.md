---
name: flow-scene-identity-anchoring
description: Use when recreating viral video storyboards in Google Flow while inserting Mia as the recurring human lead. This skill covers the workflow of analyzing a viral video, extracting key frames, creating a new outfit-specific Mia character sheet from the original Mia base sheet, and generating storyboard images in Flow by pairing the scene frame with the updated Mia character sheet as composition and identity references.
---

# Flow Scene + Identity Anchoring

Use this skill for Google Flow image generation when the shot needs:

- the original scene or viral frame composition to stay close
- Mia to remain the same person across images
- a scenario-specific outfit such as farmer, naval captain, firefighter, or conductor

This workflow is for **Flow image generation**, not generic image generation elsewhere.

## Source asset

The original Mia base character sheet for this workflow is stored here:

- [mia-original-character-sheet.jpg](/Users/damoneden/Documents/codex%20stuff/skills/flow-scene-identity-anchoring/assets/mia-original-character-sheet.jpg)

Always start new scenario outfit sheets from this base identity source.

## Blueprint workflow

Follow these steps in order for every new video:

1. Analyze a viral source video.
2. Extract the key frames that define the storyboard beats.
3. Start from the original Mia base character sheet.
4. Create a new scenario-specific Mia character sheet with the outfit appropriate for that video.
5. Treat that updated scenario-specific Mia character sheet as the identity source of truth for the whole storyboard.
6. In Flow, generate each storyboard image using:
   - the extracted key frame as the composition reference
   - the updated scenario-specific Mia character sheet as the identity reference
7. Drag both reference images into the Flow prompt box so they visibly appear as attached references before generation.
8. Mention the updated Mia character sheet explicitly in every Mia image prompt to preserve consistency.

## Core rule

For every new scenario, remake Mia's character sheet first in the scenario outfit before generating storyboard images or videos.

Then, for each Mia image:

1. attach the scene reference image
2. attach the outfit-specific Mia character sheet for every storyboard image in that scenario
3. drag both of those references into the prompt box so they are visibly attached inside the prompt input
4. explicitly say in the prompt which attachment is the composition reference and which attachment is the identity reference
5. generate `x4` in Flow and pick the best result

## Character sheet rule

- Use the **outfit-specific character sheet** as the identity reference for the first Mia shot in a scenario.
- Keep using that **same outfit-specific character sheet** as the identity reference for each subsequent storyboard image in the same scenario.
- Do not switch storyboard generation over to the latest Mia frame unless the user explicitly asks for a different method.
- For dog-only or environment-only shots, do not force the Mia sheet unless future continuity depends on it.

## Standard Flow setup

- Platform: Google Flow
- Mode: `Image`
- Model: `Nano Banana 2`
- Variants: `x4`
- Aspect ratio: match the target shot, often `9:16`

## Prompt pattern

Use wording like this and adapt only the shot details:

```text
Use the attached scene frame as the composition reference and use the attached captain character sheet as the identity reference for Mia.

Recreate this shot very close to the original reference: [describe the original scene composition and action].

Replace the original human with Mia only. Mia must match the attached character sheet exactly: same girl, same face, same body details, wearing [scenario outfit].

Photorealistic iPhone realism, no extra dogs, no extra people, no text, no watermark.
```

The important part is that the prompt explicitly names both roles:

- attached scene frame = composition reference
- attached scenario-specific Mia character sheet = identity reference

Those two references must also be visibly attached inside the Flow prompt box. If they are not shown inside the prompt box, the setup is not valid yet.

## Example: first Mia shot in a ship scenario

```text
Use the attached scene frame as the composition reference and use the attached captain character sheet as the identity reference for Mia.

Recreate this ship bridge alert shot very close to the original reference image: modern ship bridge interior, ocean visible through windows, captain chair, navigation screens, adult golden retriever standing urgently near the controls.

Replace the original male captain with Mia only. Mia must match the captain reference sheet exactly: same girl, same face, same body details, wearing the all white naval captain uniform from the sheet.

The dog is barking up at her and she is turning from the controls with alarm.

Photorealistic iPhone realism, no extra dogs, no extra people, no text, no watermark.
```

## Example: later Mia shot in the same storyboard

```text
Use the attached ship scene frame as the composition reference and use the attached captain character sheet as the identity reference for Mia.

Recreate this evacuation beat very close to the original reference: the side of the large red and white ship, a crane lowering an orange inflatable lifeboat with crew members already inside, open sea around them.

Add Mia naturally into the scene as the captain supervising the evacuation. Mia must still match the attached captain character sheet exactly: same girl, same face, same body details, same blonde hair, same all white naval captain uniform.

Keep exactly one adult golden retriever in the rescue.

Photorealistic iPhone realism, no extra dogs, no text, no watermark.
```

## Workflow rules

- Start by analyzing the viral source and extracting the storyboard frames before generating any Mia images.
- Build a new outfit-specific Mia character sheet for the scenario before any Mia storyboard image is made.
- Reuse that same updated character sheet for every Mia storyboard image in the same scenario.
- Do not count a Flow image setup as correct unless both the key frame and the updated character sheet are visibly attached inside the prompt box.
- Do not rewrite the story if the goal is to copy the viral structure closely.
- Keep the original frame logic and only swap the human lead to Mia unless the user says otherwise.
- For Mia storyboard shots, mention the attached character sheet in the prompt every time.
- If a result is close but not consistent enough, regenerate with the same character sheet and a clearer prompt before changing methods.
- Maintain a single source of truth for the current scenario outfit sheet.

## What success looks like

- same Mia face across all Mia shots
- outfit consistent with the scenario
- original scene composition still recognizable
- dog count and story logic stay clean
- no unnecessary extra people or props
