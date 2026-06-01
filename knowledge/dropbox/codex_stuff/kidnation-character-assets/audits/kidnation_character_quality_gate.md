# KidNation Character Quality Gate

## Root Cause

- The approved-looking Arjun asset is a high-fidelity visual target/cutout, not evidence that the procedural Blender character pipeline reached that quality.
- The failed Jordan v3 was built with a generic primitive/capsule Blender script instead of the Arjun-specific visual-target-first workflow.
- I treated 'real 3D export exists' as a sufficient milestone. That is wrong. The gate must be visual identity first, then rig/export.

## Stop Conditions Before User Review

- A new render must be shown in a contact sheet beside the approved visual target and the character sheet/cutout.
- It must preserve the character's face shape, eye style, hair silhouette, outfit silhouette, materials, and body proportions.
- If it looks like a toy, blockout, clay doll, or generic base model, it is internally rejected and not shown as progress.
- The report must label the asset honestly: visual target, cutout, procedural model, rigged base, or final rig.

## Current Audit Items

### Arjun visual target
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-character-assets/hero3d/arjun_visual_targets/renders/arjun_visual_target_v1.png`
- Kind: AI/2D visual target
- Verdict: PASS visual bar
- Notes: This is the style bar the user means by 'Arjun looked amazing'.

### Arjun current cutout
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-kart-racer-unity/Assets/Resources/CharacterCutouts/arjun-cutout.png`
- Kind: 2D cutout
- Verdict: PASS visual bar
- Notes: High-fidelity render/cutout, not proof of a matching 3D rig.

### Arjun Blender hero
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-character-assets/hero3d/arjun/renders/arjun_hero_fullbody.png`
- Kind: procedural Blender
- Verdict: FAIL vs visual bar
- Notes: Useful process reference, but it does not match the polished Arjun target.

### Arjun Quaternius rig
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-character-assets/hero3d/arjun_v2_quaternius/renders/arjun_quaternius_fullbody.png`
- Kind: rigged base customization
- Verdict: FAIL vs visual bar
- Notes: Rig-ready direction, but still not close to the approved look.

### Jordan reference
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-kart-racer-unity/Assets/Resources/CharacterCutouts/jordan-cutout.png`
- Kind: 2D reference/cutout
- Verdict: TARGET
- Notes: This is the Jordan identity target: face, braids, jacket, chain, jeans, shoes.

### Jordan v3 Blender
- Path: `/Users/damoneden/Kidnation Dropbox/damon eden/code folder/codex stuff/kidnation-character-assets/hero3d/jordan_focus_v3/jordan_v3_blender_render.png`
- Kind: procedural Blender
- Verdict: REJECT
- Notes: Too stiff, toy-like, wrong material quality, wrong body and hair language.

### Jordan target-locked v1
- Path: `/Users/damoneden/Documents/codex stuff/kidnation-character-assets/hero3d/jordan_target_locked_v1/renders/jordan_target_locked_front.png`
- Kind: procedural Blender
- Verdict: REJECT
- Notes: More Jordan-specific details, but still a toy/blockout and not close to the reference quality.
