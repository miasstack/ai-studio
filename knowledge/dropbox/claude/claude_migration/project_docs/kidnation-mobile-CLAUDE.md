# CLAUDE.md - KidNation Mobile (Frontend)

> Single source of truth for Claude Code working in the kidnation-mobile repo.

---

## Project Overview

- **App name:** KidNation
- **Client:** US-based startup, co-founded by Chris "Ludacris" Bridges
- **Description:** AI-powered edutainment mobile app for kids. Streaming platform with videos, songs, playlists, AI story generator, Word Ninja game, and subscription-based access.
- **Platforms:** iOS, Android (fullscreen immersive mode, tablet support)
- **This repo:** Eclipt-AI/kidnation-mobile (branch: `dev`)
- **ClickUp space:** External > KidNation (folder ID: 901512978046)
- **Figma:** https://www.figma.com/design/u7TuU0FgWDzw4JvNMGlYyj/KidNation

### Sister Repos

- **Backend:** Eclipt-AI/kidnation-back (branch: `development`) - NestJS + TypeScript + PostgreSQL + Redis + Bull queues. All AI runs server-side.
- **Admin panel:** Eclipt-AI/kidnation-admin (branch: `main`) - React + Redux Toolkit. Content management, AI prompt configuration, media upload.

---

## Tech Stack

- **Flutter:** 3.19.6 (managed via FVM)
- **Dart:** >=3.3.0 <4.0.0
- **Firebase project (dev):** kidnation-mobile
- **Firebase project (prod):** None yet. Only dev environment exists.
- **State management:** BLoC (flutter_bloc ^8.1.5) + get_it + injectable
- **Models:** Freezed + json_serializable
- **Navigation:** GoRouter (^14.1.2), routes defined in `lib/core/app_routes.dart`
- **Localization:** intl with ARB files (l10n.yaml)
- **Subscriptions:** RevenueCat (purchases_flutter ^8.1.0)
- **Analytics:** Firebase Analytics + Firebase Remote Config
- **Push notifications:** Firebase Messaging (14.9.2) + flutter_local_notifications
- **Game engine:** Flame (^1.17.0) + flame_bloc + flame_audio (for Word Ninja)
- **Audio:** just_audio (^0.9.38) + audio_service (^0.18.12)
- **Video:** better_player (custom fork: Ragnarokr45/kidNbetterplayer)
- **Auth:** Firebase Auth + Google Sign-In + Sign in with Apple
- **Environment:** envied (^0.5.4+1)
- **Other:** cached_network_image, carousel_slider, lottie, flutter_animate, vibration, wakelock_plus, fullscreen_window, connectivity_plus, screen_brightness, flutter_svg, spoiler_widget (custom fork)

---

## IMPORTANT: This project does NOT use flutter_base_project

KidNation was built independently. It does NOT use Riverpod, FirestoreRepositoryBase, RestApiBase, or any base project abstractions. Do not apply base project patterns here.

Key differences:
- **BLoC + get_it/injectable** instead of Riverpod
- **REST API to NestJS backend** instead of Firestore
- **RevenueCat** instead of Adapty
- **No flavors** configured (single Firebase project)

---

## Architecture

### Dependency Injection

Uses `get_it` + `injectable`. Configuration in `lib/injection/`.

```dart
await configureDependencies();
await getIt.allReady();
```

Modules register via `@injectable`, `@lazySingleton`, `@module` annotations.
Firebase services registered in `lib/injection/firebase_injection_module.dart`.

### State Management (BLoC)

Each feature uses BLoC pattern with `flutter_bloc`. BLoCs live in `lib/features/[feature]/presentation/`.

Pattern:
- Events define user actions
- States define UI states
- BLoC handles business logic
- BlocProvider wraps the widget tree
- BlocBuilder / BlocListener in widgets

### Navigation

Routes defined in `lib/core/app_routes.dart` as static string constants. GoRouter configured in `lib/core/router.dart`.

Key routes:
- `/login`, `/sign-up`, `/forgot-password`, `/confirm-email`
- `/on-board`, `/create-profile`, `/choose-profile`, `/blast-off`
- `/home`, `/home-search`
- `/videos`, `/search`, `/video-player`
- `/songs`, `/search-songs`, `/audio-player`
- `/playlists`, `/playlist`
- `/story-teller-on-board`, `/pick-options`, `/story-teller`, `/generating-story-finished`
- `/word-ninja`, `/ninja-on-board`, `/word-ninja-choose-difficulty-level`, `/word-ninja-choose-category`, `/results`
- `/profile`, `/profile-options`
- `/subscriptions`

### Fullscreen Mode

App runs in immersive sticky mode. Set in `main.dart`:
```dart
SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
```

### Custom Fonts

- SegoeUI (primary)
- fruit-ninja (Word Ninja game)
- super-boom (display)
- story_teller_new (story teller feature)
- calibri

---

## Folder Structure

```
lib/
  core/
    audio_player/       # Audio playback logic
    channels/           # Platform channels
    env/                # Environment config (envied)
    error/              # Error handling
    interceptors/       # Dio interceptors
    logger/             # Logging
    media/              # Media utilities
    models/             # Core data models
    network/            # Network layer (Dio)
    notifications/      # Push notification setup
    search/             # Search functionality
    storage/            # Secure storage, clear on reinstall
    styles/             # App theme, colors, text styles
    utils/              # Utility functions
    widgets/            # Shared widgets
    app_constants.dart  # App-wide constants
    app_routes.dart     # Route path definitions
    router.dart         # GoRouter configuration
    index.dart          # Core barrel file
  features/
    activities/         # Interactive activities
    analytics/          # Analytics tracking
    auth/               # Authentication (login, signup, forgot password)
    home/               # Home screen
    main/               # Main shell / bottom navigation
    playlists/          # Playlists feature
    profile/            # User profiles (create, choose, options)
    songs/              # Songs / audio content
    story_teller/       # AI story generator
    subscriptions/      # RevenueCat subscriptions
    videos/             # Video content
  injection/
    injection.dart              # DI configuration
    injection_module.dart       # Manual modules
    firebase_injection_module.dart  # Firebase DI
  l10n/                # Localization ARB files
  app.dart             # App widget
  firebase_options.dart # Firebase config
  main.dart            # Entry point
  providers.dart       # Top-level providers
```

### Assets

```
assets/
  icons/
  images/
  images/ninja/
  images/ninja/letters/
  bottom-navigation/
  story_teller/
  fonts/
  audio/
  videos/
  story_teller_mock/
  animations/
  splash.png
```

---

## Backend API Context

The Flutter app talks to the NestJS backend via REST API (Dio). Key endpoint groups:

- `/media-upload/` - Video/audio upload with AI processing (admin only)
- `/profile/` - User profiles CRUD
- `/videos/` - Video content listing, search
- `/music/` - Music/audio content
- `/home/` - Home page sections and data
- `/account/` - Account management
- `/leaderboard/` - Word Ninja game leaderboards
- `/category/` - Content categories
- `/section/` - Content sections

All endpoints require Firebase Auth token (Bearer) except public routes.

---

## Key Flows

### Storyteller (AI Story Generation)
1. User picks options at `/pick-options` (hero, villain, setting, item, genre)
2. App sends selections to backend
3. Backend generates 10-page story (OpenAI gpt-4o), image prompts, illustrations (OpenAI Image Edit), and voiceover (gpt-4o-mini-tts)
4. Push notification sent when first image is ready
5. User reads at `/story-teller` while remaining images generate
6. Finished story at `/generating-story-finished`

### Word Ninja (Flame Game)
1. Game built with Flame engine + flame_bloc
2. Words generated server-side from video transcriptions
3. Progress tracked per profile in backend
4. Leaderboard shared across users

### Subscriptions (RevenueCat)
1. `purchases_flutter` handles native store interaction
2. Backend verifies via RevenueCat webhooks
3. Access control based on subscription status

---

## Key Commands

```bash
# Code generation (after changing Freezed models or injectable)
fvm dart run build_runner build -d
fvm dart run build_runner watch -d

# Localization
fvm flutter gen-l10n

# Run app
fvm flutter run

# Analyze
fvm dart analyze
```

---

## Current State

- **Version:** 2.0.11+209
- **Primary developer:** Andrii
- **Known tech debt:**
  - `pubspec.yaml` description still "A new Flutter project"
  - No flavors configured
  - Custom package forks (better_player, turn_page_transition, spoiler_widget)

---

## Rules for Claude Code

### Code Style
- Use BLoC pattern for state management. Do NOT use Riverpod.
- Use `get_it` + `@injectable` for dependency injection.
- Routes are string constants in `lib/core/app_routes.dart`.
- Feature-based folder structure: `data/`, `domain/`, `presentation/` per feature.
- No em dashes in comments. Use periods or commas.
- App runs fullscreen. Do not add system UI elements.

### Code Generation
- Run `fvm dart run build_runner build -d` after changing Freezed models or injectable annotations.
- Run `fvm flutter gen-l10n` after changing localization strings.

### Security
- Never put secrets or API keys in client-side code.
- All AI calls go through the NestJS backend. Never call OpenAI from the client.
- All media uploads go through the backend. Never upload to S3 from the client.

### Patterns
- Do not introduce new packages without noting it clearly.
- Follow existing BLoC patterns. Look at similar features before creating new ones.
- For payments: always use RevenueCat.
- Always consider both iOS and Android.
- Test on both phone and tablet form factors.

### Git
- This repo: `Eclipt-AI/kidnation-mobile` (branch: `dev`)
- Branch names come from ClickUp task IDs.

### When Unsure
- If unsure about a pattern, say so. Do not guess.
- If the task is ambiguous, ask. Do not assume.