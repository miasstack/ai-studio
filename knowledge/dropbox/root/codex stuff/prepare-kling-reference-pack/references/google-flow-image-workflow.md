# Google Flow Image Workflow

Use this when the user wants Google Flow to generate or refine the Mia still.

## When to Prefer Flow

Prefer Flow when:

- The user explicitly wants Google Flow
- Face drift is the main failure mode
- You want iterative edits on the same base image instead of rerolling the whole shot

## Access Checks

Before relying on Flow, confirm these prerequisites in the browser:

- The user is 18+
- The account has Flow access in a supported region
- The account has a qualifying subscription
- Use a desktop Chromium-based browser when possible

If Flow access is blocked, fall back to another image generator and say so clearly.

## Recommended Flow Strategy

1. Open `https://labs.google/flow`.
2. Open the current pack project or create a new project named after the pack slug.
3. In the prompt box, switch to image creation.
4. Pick the model intentionally:
   - `Nano Banana Pro`: best default when Mia's face needs tighter control and professional-grade edits
   - `Imagen 4`: alternate high-quality image generation path
   - `Nano Banana 2`: fast base pass when speed matters more than precision
5. Paste the Mia prompt from `generated/mia-prompt.md`.
6. Generate the first image.
7. Review the face against the Mia character sheet before doing anything else.
8. If the face is close but not locked:
   - Open the image
   - Use `Select` to isolate the face, eyes, lips, hairline, or brows
   - Prompt only the needed fix, such as "keep Mia's almond hazel-grey eyes, fuller nude lips, and softer oval-heart face from the character sheet"
9. If the feature needs more explicit direction, use `Draw` to mark the exact region and regenerate.
10. Keep edits local and specific. Do not reroll the entire image unless composition or wardrobe is also wrong.

## Prompting Advice For Flow

- Keep the shot description and the face-lock instructions in the same prompt.
- Prioritize Mia's face over the source creator's expression.
- Use "comparable outfit" language rather than "same outfit."
- If the first pass is compositionally good, prefer iterative edits over starting fresh.

## What Flow Can Do Here

- Create images directly inside a project
- Edit an image without losing the original version
- Keep prior versions in history
- Add generated images back into the prompt as ingredients for later work

## Maintenance Note

Flow changes quickly. If model names, credit rules, or UI labels differ from this file, trust the current official Flow help center and adapt the workflow.
