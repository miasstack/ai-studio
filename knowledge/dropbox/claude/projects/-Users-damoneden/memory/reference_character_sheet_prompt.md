---
name: Higgsfield Character Sheet Prompt
description: The character sheet prompt template used in Higgsfield (Nano Banana Pro) to generate multi-view reference sheets from an uploaded reference image
type: reference
tags: [ai-generation, prompt-engineering, higgsfield, character-sheet, video-reference, image-generation]
related:
  - project_comfyui_vastai.md
originSessionId: fb4781fa-5525-434f-88dc-126c2c8f3c76
---
# Higgsfield Character Sheet Prompt

**Tool:** Higgsfield (Nano Banana Pro)
**Purpose:** Generate multi-view character reference sheets from an uploaded reference image. These reference sheets can then be used as input images for [ComfyUI Wan 2.2 I2V](project_comfyui_vastai.md) to maintain character consistency across video generation.

## Prompt Template

Create a professional character reference sheet based strictly on the uploaded reference image. Use a clean, neutral plain background and present the sheet as a technical model turnaround while matching the exact visual style of the reference (same realism level, rendering approach, texture, color treatment, and overall aesthetic). Arrange the composition into two horizontal rows. Top row: four full-body standing views placed side-by-side in this order: front view, left profile view (facing left), right profile view (facing right), back view. Bottom row: three highly detailed close-up portraits aligned beneath the full-body row in this order: front portrait, left profile portrait (facing left), right profile portrait (facing right). Maintain perfect identity consistency across every panel. Keep the subject in a relaxed A-pose and with consistent scale and alignment between views, accurate anatomy, and clear silhouette; ensure even spacing and clean panel separation, with uniform framing and consistent head height across the full-body lineup and consistent facial scale across the portraits. Lighting should be consistent across all panels (same direction, intensity, and softness), with natural, controlled shadows that preserve detail without dramatic mood shifts. Output a crisp, print-ready reference sheet look, sharp details.
