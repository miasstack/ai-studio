---
name: latino-magic
description: "Latino Magic / Latina Magic apparel brand — product-on-model image production using ChatGPT browser. Tracks model roster, product checklist, workflow rules, and all project paths."
metadata: 
  node_type: memory
  type: project
  originSessionId: 19013318-2462-4c94-955d-2a7057d706d8
---

# Latino Magic / Latina Magic — Apparel Brand

An apparel brand with Latina cultural identity. Primary task: generate product-on-model lookbook/catalog images using ChatGPT browser, preserving model identity.

**Related:** [[Mia Suprema]] — Mia appears as models `woman-mia-pink` and `woman-white` in this project. Same public-language rules apply: never call her AI/synthetic/virtual/fake/avatar/bot in any public-facing copy.

---

## Key Paths

| Resource | Path |
|---|---|
| Project root | `/Users/damoneden/Desktop/lm product  workshop` |
| Production checklist | `/Users/damoneden/Desktop/lm product  workshop/PRODUCTION_CHECKLIST.md` |
| Batch prompts | `/Users/damoneden/Desktop/lm product  workshop/chatgpt_upload_batches/PROMPTS.md` |
| Batch manifest | `/Users/damoneden/Desktop/lm product  workshop/chatgpt_upload_batches/MANIFEST.md` |
| Upload-ready batch folders | `/Users/damoneden/Desktop/lm product  workshop/chatgpt_upload_batches/` |
| Accepted outputs | `/Users/damoneden/Desktop/lm product  workshop/generated model product photos/usable/` |
| Rejected outputs | `/Users/damoneden/Desktop/lm product  workshop/generated model product photos/bad/` |
| Model sheets | `/Users/damoneden/Desktop/lm product  workshop/model sheets/` |
| Product pics | `/Users/damoneden/Desktop/lm product  workshop/product pics/` |
| Product sheets | `/Users/damoneden/Desktop/lm product  workshop/product sheets/` |
| GitHub handoff doc | `/Users/damoneden/Documents/codex stuff/latino-magic-github-handoff/README.md` |
| Mia active character sheet | `/Users/damoneden/Documents/codex stuff/assets/mia/mia-active-character-sheet.png` |
| AGENTS.md rules | `/Users/damoneden/Documents/codex stuff/AGENTS.md` |

---

## Browser / Automation Workflow

**Tool:** ChatGPT browser ONLY (no Higgsfield, Nano Banana, Flow, image APIs as substitutes unless user explicitly changes this).

**Browser:** CloakBrowser (stealth Chromium, bypasses Cloudflare/reCAPTCHA)
- CloakBrowser install: `/Users/damoneden/Documents/codex stuff/CloakBrowser`
- Persistent profile: `/Users/damoneden/Documents/codex stuff/cloak-profiles/main`
- Launcher script: `/Users/damoneden/Documents/codex stuff/scripts/open_cloak_workspace.py`
- Run: `PYTHONPATH="/Users/damoneden/Documents/codex stuff/CloakBrowser" python3 "/Users/damoneden/Documents/codex stuff/scripts/open_cloak_workspace.py"`
- Opens Higgsfield, Spotify, ChatGPT, and Google tabs on launch

**Important:** Keep browser work on a separate desktop/space from the user's active workspace. Never take over their active Chrome session. Brave must not be used.

**Why:** [[CloakBrowser]] — user wants to multitask while generation runs elsewhere.

---

## Model Roster

| Model ID | Source file | Description |
|---|---|---|
| male-jcent | `model sheets/latin magic j cent sheet.png` | Male model, blue tracksuit/source pose sheet |
| woman-A | `model sheets/ChatGPT Image May 16, 2026, 03_38_21 AM.png` | Blonde curvy white activewear sheet |
| woman-B | `model sheets/ChatGPT Image May 16, 2026, 03_42_56 AM.png` | Blonde curvy turnaround sheet |
| woman-C | `model sheets/ChatGPT Image May 16, 2026, 03_49_10 AM.png` | Blonde dress/turnaround sheet |
| woman-HF | `model sheets/hf_20260516_062150_4c913436-a1ee-407e-8f33-7de029e79786.png` | Multi-view female sheet (Higgsfield-generated) |
| woman-mia-pink | `model sheets/mia pink 2.png` | Mia in pink outfit — same identity rules as Mia Suprema |
| woman-white | `model sheets/mia white winner.png` | Mia in white activewear |
| woman-1 | `model sheets/model 1.png` | Brunette/tan female turnaround |
| woman-2 | `model sheets/model 2.png` | Curly dark-haired female turnaround |
| woman-3 | `model sheets/model 3.png` | Blonde curvy activewear |
| woman-4 | `model sheets/model 4.png` | Blonde curvy activewear |

**Note:** `model sheets/mia set 4/` folder exists but is excluded from production unless user explicitly adds it.

---

## Product Categories

- Male tracksuits: blue, green, baby-blue windbreaker
- Women's tracksuits: baby-blue, blue, green
- Women's activewear: black/gold, red, pink, green, black/white leggings, white leggings
- Women's bathing suits: baby-blue bikini, pink bikini, black bikini, red/white letters bikini, one-piece baby-blue swimsuit
- Women's casual/baby tee: Bandidas tee (crop tee), black/yellow Spanish text shirt ("Lujuriosa, Atrevida, Tentadora, Impredecible, Necesaria, Ardiente")

---

## Hard Rules

1. **Identity preservation:** Preserve each model's face, hair, skin tone, body shape, curves, waist/hip ratio, proportions, posture feel. Curvy bodies must stay curvy. No slimming, reshaping, glamour-filtering, or body replacement.
2. **Product precision:** Preserve color, garment cut, logo placement, monogram scale, waistband/band text, cuffs, zipper, trim, top/bottom pairing. No changed colorway, no invented accessories.
3. **Only root-level model sheets** — no nested folders like `mia set 4/` unless explicitly added.
4. **Male model wears male clothes only.**
5. **ChatGPT browser is the tool** — not APIs, not Higgsfield, not Nano Banana, not Flow.
6. **Rotate female models** — don't default to woman-1 and woman-2 when other models fit.
7. **Expression cue:** Eyes engaged with camera, lifted chin, relaxed mouth or soft smirk, slight eyebrow attitude. Inspired by Savage X Fenty / Fashion Nova / PrettyLittleThing product imagery. No blank mannequin faces.
8. **Checklist discipline:** Only mark `[x]` after a real ChatGPT browser output has been downloaded and visually accepted. Files in `bad/` do not count.

---

## Current Status (as of 2026-05-27)

### Done
- Male: blue tracksuit (front/set), green tracksuit (front), baby-blue windbreaker
- Women's tracksuits: baby-blue (front + side/rear), blue (front + side), green (front)
- Women's activewear: black/gold, red, pink, green (rear + front), white leggings + Bandidas tee, Bandidas tee + red/black leggings
- Women's bathing suits: baby-blue bikini rear only
- Women's baby tee: Bandidas tee covered via leggings combo

### Pending (next batch queue order)
1. Black/yellow Spanish text shirt + green/yellow track pants — woman-3 or woman-4 (batch 16)
2. Bandidas tee + green/yellow track pants — woman-4 or woman-A (batch 17)
3. Bandidas tee + green/yellow bikini bottoms beach look — woman-HF or woman-mia-pink (confirm bikini bottom ref first)
4. Black/white leggings front/catalog — woman-white or woman-B (batch 11)
5. Baby-blue bikini front/catalog — woman-2 or woman-C (batch 04)
6. Pink bikini front/catalog — woman-3 or woman-A (batch 05)
7. Black bikini front/catalog — woman-4 or woman-HF (batch 07)
8. Red/white letters bikini front/catalog — woman-1 or woman-B (batch 12)
9. One-piece baby-blue swimsuit — woman-C or woman-white (batch 08)
10. Blue men windbreaker product-forward shot — male-jcent (batch 09)
11. Green male tracksuit side/back alternate — male-jcent (batch 10)

Upload-ready folders exist for batches 03–17. Use `PROMPTS.md` for matching prompts. Prefer batches 16 and 17 (rotated models) over older woman-1 repeats for next women's runs.

---

## Higgsfield Character Sheet Prompt

For generating new model sheets (multi-view turnarounds) from a reference image, use Higgsfield (Nano Banana Pro) with this prompt:

> Create a professional character reference sheet based strictly on the uploaded reference image. Use a clean, neutral plain background and present the sheet as a technical model turnaround while matching the exact visual style of the reference (same realism level, rendering approach, texture, color treatment, and overall aesthetic). Arrange the composition into two horizontal rows. Top row: four full-body standing views placed side-by-side in this order: front view, left profile view (facing left), right profile view (facing right), back view. Bottom row: three highly detailed close-up portraits aligned beneath the full-body row in this order: front portrait, left profile portrait (facing left), right profile portrait (facing right). Maintain perfect identity consistency across every panel. Keep the subject in a relaxed A-pose and with consistent scale and alignment between views, accurate anatomy, and clear silhouette; ensure even spacing and clean panel separation, with uniform framing and consistent head height across the full-body lineup and consistent facial scale across the portraits. Lighting should be consistent across all panels (same direction, intensity, and softness), with natural, controlled shadows that preserve detail without dramatic mood shifts. Output a crisp, print-ready reference sheet look, sharp details.

**Why:** [[Higgsfield Character Sheet Prompt]] — this is how woman-HF was created and how new model sheets can be generated when adding new models to the roster.

---

## What Happened Last (2026-05-27)

- Batch 03 was attempted in user's active Chrome — user redirected away correctly
- Brave was opened by mistake — must not use Brave
- CloakBrowser launched with the open_cloak_workspace.py script
- User paused and may resume when stepping away from computer
- `cloak-profiles/main` may not be fully signed into ChatGPT image/upload features — user may need to log in once before generation continues
