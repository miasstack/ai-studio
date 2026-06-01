# Jordan Character Process Root Cause And Rebuild Plan

## What Went Wrong

The accepted Arjun look came from the high-fidelity visual target/cutout path:

- `kidnation-character-assets/hero3d/arjun_visual_targets/renders/arjun_visual_target_v1.png`
- `kidnation-kart-racer-unity/Assets/Resources/CharacterCutouts/arjun-cutout.png`

Those are polished 2D visual assets. They are not proof that the current procedural Blender or rig-generation scripts can create a matching production-quality 3D model.

The bad Jordan v3 render came from a new procedural Blender script that focused on "3D file exists" instead of matching the approved visual bar. That was the process failure.

## Evidence

The audit contact sheet is here:

- `kidnation-character-assets/audits/kidnation_character_quality_gate.png`

It shows:

- Arjun visual target/cutout passes the style bar.
- Arjun procedural Blender and Quaternius rig outputs fail the style bar.
- Jordan v3 fails.
- Jordan target-locked v1 improves identity details but still fails.

## New Gate

No KidNation character asset should be shown to the user until it passes this internal gate:

- A/B contact sheet beside the approved visual target and character sheet/cutout.
- Honest label: visual target, 2D cutout, procedural Blender model, rigged base customization, Unity import, or final rig.
- Face shape, eye style, hair silhouette, outfit silhouette, materials, body proportions, and identity must be visibly close.
- If it reads as a toy, blockout, clay doll, generic base model, or cutout pretending to be 3D, it is rejected internally.

## OODA Execution Plan

Observe:
Audit every candidate beside the Jordan sheet/cutout and the accepted Arjun visual target.

Orient:
The current local Blender scripting approach cannot reach the Arjun visual-target fidelity by itself. It can make riggable blockouts, not Pixar-quality production character meshes.

Decide:
Stop presenting procedural Blender blockouts as candidates. For the final Jordan character, use either:

- A professional sculpt/image-to-3D workflow that can generate real geometry from the Jordan sheet, then clean and rig it in Blender.
- A deliberately scoped Unity-ready stylized low-poly rig, clearly labeled as a game rig and not expected to match the visual target exactly.

Act:
The next real attempt should start from the Jordan reference and use a true 3D character pipeline:

1. Generate or sculpt high-quality Jordan head/hair/clothing geometry from the existing sheet.
2. Retopologize/simplify for Unity.
3. Add armature and weights.
4. Render front, side, back, and in-kart previews.
5. Run the audit gate before user review.
6. Import into Unity only after the visual gate passes.

## Current Status

`jordan_target_locked_v1` was created as a controlled test and rejected. It should not be imported into Unity or used as a final character.
