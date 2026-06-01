# Treasure Town Builders Chat Summary

## Goal

Build a much more game-like, kid-friendly version of Treasure Town Builders with real characters, real town exploration, and a more premium visual direction.

## Product Direction Agreed In This Chat

- Audience: kids ages 6-8.
- The experience should feel like a real sandbox town, not worksheets with buttons.
- The player should walk around town and enter different sections.
- Each town section should contain playable interactions.
- Rewards should visibly improve the town.
- When a section upgrades, the structure should get larger and feel more impressive.
- Visual inspiration shifted toward a polished survival/city-builder feel similar to Whiteout Survival, but adapted into an original kid-friendly style.

## Assets Used

KidNation character sheets and derived assets were incorporated into the prototype flow:

- Arjun
- Melli
- Jordan
- Nari
- Bjorn
- Salome

Existing local pixel/8-bit variants were reused from:

- `assets/characters/*-sprite-8bit.png`
- `assets/characters/*-portrait-8bit.png`

## Web Prototype Work Completed

The web demo in `treasure-town-demo/index.html` was iterated several times:

1. Flat browser prototype
2. More playful 2D sandbox version
3. Current Three.js-style 3D browser demo

### Current browser demo

- File: `index.html`
- Local run URL used during the session:
  - `http://localhost:8088/index.html`
- Current state:
  - 3D world feel
  - click-to-walk movement
  - follow camera
  - glowing districts
  - district entry prompts
  - mini-game overlays for number, word, and pattern activities

This browser version is still considered a stepping stone, not the final target.

## Flutter Work

A Flutter MVP scaffold was created earlier, including:

- `lib/main.dart`
- local save logic
- parent zone
- mini-game flow

But direction changed and Flutter was explicitly deprioritized in favor of a more premium-looking game approach.

## Unity Project Created

A Unity project scaffold was created here:

- `unity-treasure-town/`

### Key Unity files

- `unity-treasure-town/Assets/Scripts/TreasureTownGame.cs`
- `unity-treasure-town/Assets/Editor/TreasureTownAutoSetup.cs`
- `unity-treasure-town/Packages/manifest.json`
- `unity-treasure-town/ProjectSettings/ProjectVersion.txt`

### What the Unity prototype currently does

The Unity project is designed to auto-generate a playable snowy isometric town from code:

- snowy 3D world
- click-to-walk player movement
- follow camera
- district pads and helper characters
- district interactions
- number / word / pattern mini-games
- stars and build credits
- building upgrades
- structure scale increases as districts level up

### Important implementation detail

The Unity project was intentionally built to generate much of the scene procedurally from C# so it could be opened quickly without hand-building every object in the editor first.

## Unity Status / Blocker

Unity Hub is installed on the Mac, but during the last direct check:

- Unity Hub `Installs` showed: **No Unity version**
- Unity Hub `Projects` showed older projects with: **No Editor is available**

That means the Unity Editor itself was not available at the moment it was checked, so the Unity prototype could not actually be launched into Play Mode yet.

If Unity Editor has since been installed after that check, the next step is:

1. open Unity Hub
2. add/open `unity-treasure-town`
3. let the auto-setup script generate the scene
4. press Play

## README Updates

`README.md` was updated with:

- Unity project location
- Unity run instructions
- prototype summary

## Files Worth Looking At First Next Time

1. `unity-treasure-town/Assets/Scripts/TreasureTownGame.cs`
2. `unity-treasure-town/Assets/Editor/TreasureTownAutoSetup.cs`
3. `README.md`
4. `index.html`

## Recommended Next Steps

### If continuing in Unity

1. Verify a Unity 2022 LTS editor is actually installed and selectable in Hub.
2. Open `unity-treasure-town`.
3. Fix any import/compiler issues from first open.
4. Press Play and capture a working example.
5. Replace primitive buildings with more polished modular scene pieces.
6. Push visual style closer to:
   - snowy atmospheric lighting
   - cinematic fog
   - richer materials
   - larger upgrade silhouettes
   - stronger in-world effects

### Highest-value polish goals

- make the player avatar feel more alive
- make district interiors feel like places, not overlays
- make upgrades dramatically larger and more satisfying
- move toward a true premium mobile city-builder presentation

## Notes

- The browser demo is runnable now.
- The Unity project is scaffolded and ready for first open.
- The main unresolved dependency is the actual Unity Editor runtime availability.
