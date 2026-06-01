# Treasure Town Builders Prototypes

Treasure Town Builders is an educational town-building game for ages 6-8. Kids choose a KidNation builder, walk around a friendly town, solve short game-like learning challenges, earn stars and build credits, and restore buildings little by little.

## Unity 3D Prototype

The current high-end prototype direction lives in:

```text
unity-treasure-town/
```

This Unity version targets a polished snowy isometric city-builder feel: cinematic camera, winter lighting, glowing districts, KidNation character billboards, and buildings that visibly get larger as town sections improve.

### Run in Unity

This project is pinned to Unity `2022.3.50f1`.

1. Install Unity Editor `2022.3.50f1` from Unity Hub.
2. In Unity Hub, choose **Add project from disk**.
3. Select:

   ```text
   /Users/damoneden/Documents/codex stuff/treasure-town-demo/unity-treasure-town
   ```

4. Let Unity import the project.
5. The editor auto-creates:

   ```text
   Assets/Scenes/TreasureTown.unity
   ```

6. Open that scene and press **Play**.

If the scene does not auto-create, use the Unity menu:

```text
Treasure Town > Rebuild Demo Scene
```

If you prefer the terminal and Unity Hub supports headless installs on your machine, this project version can be installed with:

```sh
'/Applications/Unity Hub.app/Contents/MacOS/Unity Hub' -- --headless install --version 2022.3.50f1
```

### Unity Gameplay Included

- Snowy 3D town generated from C#.
- Click-to-walk KidNation character.
- Follow camera with isometric/cinematic angle.
- Six district structures.
- Glowing district entry pads.
- Helper characters in each district.
- Number, word, and pattern mini-games.
- Stars and build credits.
- Each district structure grows larger as its level improves.
- Local progress via `PlayerPrefs`.

## What Is Included

- Web town hub map with six buildable areas.
- KidNation character picker using the local 8-bit character assets.
- Three playable mini-game types:
  - Number Bridge: move the exact number of stones into the bridge.
  - Word Garden: plant letter seeds in the right order.
  - Pattern Parade: choose the next visual parade piece.
- Rewards and progression:
  - Stars for successful rounds.
  - Build credits for town restoration.
  - Building stages that upgrade as each area earns credits.
- Parent Zone:
  - Simple grown-up gate before settings.
  - Progress snapshot.
  - Easy, Standard, and Challenge difficulty bands.
  - Music, SFX, and voice prompt toggles.
  - Local progress reset.
- Local save state through `shared_preferences`.
- Browser prototype preserved in `web_demo/index.html`.

## Initial Brainstorm Coverage

The Flutter MVP keeps the important brainstorm ideas:

- Learning feels like play, not a worksheet.
- Sessions work in short 5-10 minute bursts.
- One clear task per screen.
- Large touch targets for iPhone portrait.
- Gentle wrong-answer feedback with a clear next action.
- Visual rewards tied to town restoration.
- Math, reading, logic, and early SEL tone through helping characters.
- No ads, chat, online accounts, or pressure loops.

The SEL-only mini-game concepts, avatar accessories, live events, deeper story chapters, and online systems remain post-MVP, matching the original scope.

## Run on iPhone Simulator

1. Install Flutter and Xcode.
2. From this folder, generate platform shells if they are not present yet:

   ```sh
   flutter create --platforms=ios,web .
   ```

3. Install packages:

   ```sh
   flutter pub get
   ```

4. Open an iPhone simulator:

   ```sh
   open -a Simulator
   ```

5. List devices and copy the iPhone device id:

   ```sh
   flutter devices
   ```

6. Run the app:

   ```sh
   flutter run -d "iPhone 15"
   ```

   If your simulator has a different name, use that name from `flutter devices`.

## Run on Flutter Web

```sh
flutter pub get
flutter run -d chrome
```

For a release web build:

```sh
flutter build web
```

## Browser Prototype

The original playable browser prototype is available at:

```text
web_demo/index.html
```

The Flutter app uses that prototype as the reference for color, characters, town-building feel, and mini-game direction.
