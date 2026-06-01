# CLAUDE.md - KidNation

> This file is the single source of truth for Claude Code. Everything Claude Code needs to know about coding, architecture, and this project lives here.

---

## Project Overview

- **App name:** KidNation
- **Client:** US-based startup, co-founded by Chris "Ludacris" Bridges
- **Description:** AI-powered edutainment mobile app for kids. Streaming platform with videos, songs, playlists, AI story generator, Word Ninja game, and subscription-based access.
- **Platforms:** iOS, Android (fullscreen immersive mode, tablet support)
- **Frontend repo:** Eclipt-AI/kidnation-mobile (branch: `dev`)
- **Backend repo:** Eclipt-AI/kidnation-back (branch: `development`)
- **Admin panel repo:** Eclipt-AI/kidnation-admin (branch: `main`)
- **ClickUp space:** External > KidNation (folder ID: 901512978046)
- **Figma:** https://www.figma.com/design/u7TuU0FgWDzw4JvNMGlYyj/KidNation

---

## Tech Stack

### Frontend
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

### Backend
- **Framework:** NestJS (^9.4.3) with TypeScript
- **Runtime:** Node.js
- **Package manager:** pnpm
- **Database:** PostgreSQL via TypeORM (^0.3.20)
- **Queue:** Bull (^4.16.0) + Redis
- **Scheduler:** @nestjs/schedule (^4.1.1)
- **AI:** OpenAI (^4.78.0) using `gpt-4o` model for all text generation. Ideogram for AI thumbnail generation.
- **Media storage:** AWS S3 (aws-sdk ^2.1630.0)
- **Content source:** Dropbox SDK (^10.34.0)
- **Media processing:** fluent-ffmpeg + ffprobe-static + sharp (^0.34.5)
- **Auth:** Firebase Admin SDK (^12.1.1)
- **API docs:** Swagger (@nestjs/swagger ^7.3.1)
- **Validation:** class-validator + class-transformer + zod
- **Infrastructure:** Docker Compose (dev only, no prod environment yet), GitHub Actions CI

### Admin Panel
- **Repo:** Eclipt-AI/kidnation-admin (branch: `main`)
- **Framework:** React + TypeScript
- **State:** Redux Toolkit (RTK Query for API calls)
- **UI:** MUI (Material UI) + Ant Design + styled-components
- **Auth:** Firebase (client SDK)
- **Video:** video.js + HLS.js + react-hls-player
- **Forms:** react-hook-form + zod
- **Build:** Create React App (via craco)

---

## IMPORTANT: This project does NOT use flutter_base_project

KidNation was built independently. It does NOT use Riverpod, FirestoreRepositoryBase, RestApiBase, or any of the base project abstractions. Do not apply base project patterns here.

Key differences from base project:
- **BLoC + get_it/injectable** instead of Riverpod
- **PostgreSQL via REST API** instead of Firestore
- **NestJS backend** instead of Firebase Cloud Functions
- **RevenueCat** instead of Adapty
- **No flavors** configured (single Firebase project)

---

## Frontend Architecture

### Dependency Injection

Uses `get_it` + `injectable` for DI. Configuration in `lib/injection/`.

```dart
// lib/injection/injection.dart - configures all injectable dependencies
await configureDependencies();
await getIt.allReady();
```

Modules register their dependencies via `@injectable`, `@lazySingleton`, `@module` annotations.
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

App runs in immersive sticky mode (no system UI). Set in `main.dart`:
```dart
SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
```

### Custom Fonts

- SegoeUI (primary)
- fruit-ninja (Word Ninja game)
- super-boom (display)
- story_teller_new (story teller feature)
- calibri

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

## Backend Architecture

### Module Structure

NestJS modules in `src/modules/`. Each module has its own controller, service, and entity files.

| Module | Purpose |
|---|---|
| `account` | User account management |
| `admin` | Admin panel operations, content management |
| `aiPrompts` | AI prompt templates and management |
| `category` | Content categories |
| `dropbox` | Dropbox integration for content import |
| `firebase` | Firebase Admin SDK integration (auth) |
| `home` | Home page data, sections |
| `ideogram` | Ideogram AI thumbnail generation. Has its own Bull processor, controller, service, config, DTOs |
| `imageAi` | AI image processing coordination |
| `leaderboard` | Game leaderboards (Word Ninja) |
| `media` | Media file management (videos, audio, images) |
| `music` | Songs and audio content |
| `openai` | OpenAI module (gpt-4o for text, Image Edit API for story illustrations). Story generation, word extraction, title/description/subtitle generation, image prompt generation |
| `profile` | User profiles (multiple child profiles per account) |
| `profileGameProgress` | Game progress tracking per profile |
| `profilePlayLists` | User playlists per profile |
| `profileStories` | AI-generated stories per profile |
| `revenueCat` | RevenueCat webhook + subscription verification |
| `scripts` | Admin scripts and data operations |
| `section` | Content sections / groupings |
| `videos` | Video content management |
| `wordsNinja` | Word Ninja game data (words, levels, categories) |

### Backend Services

| Service | File | Purpose |
|---|---|---|
| `openAi.service` | `src/services/openAi.service.ts` | OpenAI gpt-4o wrapper. Functions: generateResponse, generateWordsToVideo, generateResponseWords, generateStoryText, generateStoryTextV2 |
| `openAISpeachToText.service` | `src/services/openAISpeachToText.service.ts` | Audio service: whisper-1 for transcription/subtitles, gpt-4o-mini-tts for voiceover (voice: "alloy") |
| `s3.service` | `src/services/s3.service.ts` | AWS S3 upload/download for media files |
| `email.service` | `src/services/email.service.ts` | Email sending |
| `fileDownload.axios.service` | `src/services/fileDownload.axios.service.ts` | File download via Axios |

### Authentication

Firebase Admin SDK for auth. Global `AuthGuard` applied via `APP_GUARD`.
- Public routes use `@IsPublic()` decorator
- Admin routes use `@IsAdmin()` decorator
- Super admin routes use `@IsSuperAdmin()` decorator
- RevenueCat webhook routes use `@IsRC()` decorator

### Database (PostgreSQL + TypeORM)

- PostgreSQL as primary database
- TypeORM with migration-based schema management
- Entities defined per module
- ~30+ migrations in `src/database/postgresql/`
- TypeORM provider module at `src/providers/database/postgresql/typeorm.module.ts`
- Datasource config at `src/utils/datasource.ts`

### Database Schema (PostgreSQL)

#### Account & Auth

**Account**
- `id` uuid PK
- `uids` text[]
- `emails` text[]
- `FCM_tokens` text[]
- `role` "AccountRole"
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `isSubscribedToEmail` boolean

**Admin**
- `id` uuid PK
- `emails` character varying
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone

**TokenEmails**
- `id` uuid PK
- `uid` character varying
- `adminEmails` character varying
- `isPatched` boolean
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone

#### Profiles

**Profile**
- `id` uuid PK
- `name` character varying(25)
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `preferredAge` character varying(255)
- `birthday` date
- `accountId` uuid FK -> Account
- `storyStatus` jsonb

**profile_images**
- `id` uuid PK
- `url` character varying
- `name` character varying

**ProfileMedia** (tracks user interaction with media)
- `id` uuid PK
- `isLiked` boolean
- `isLast` boolean
- `secondsWatched` integer
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profileId` uuid FK -> Profile
- `mediaId` uuid FK -> Media

**ProfileGameProgress**
- `id` uuid PK
- `levelDifficulty` "ProfileGameLevelDifficulty"
- `totalCompleted` integer
- `easyLevelsComplete` integer
- `mediumLevelsComplete` integer
- `hardLevelsComplete` integer
- `expertLevelsComplete` integer
- `masterLevelsComplete` integer
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profile_id` uuid FK -> Profile

**WordToProfileProgress** (join table)
- `wordId` uuid FK -> WordNinja
- `progressId` uuid FK -> ProfileGameProgress

#### Content

**Media** (generic media entity)
- `id` uuid PK
- `mediaType` "MediaType"
- `url` character varying
- `thumbnailUrl` character varying
- `subtitleUrl` character varying
- `title` character varying
- `description` character varying
- `accessType` "MediaAccessType"
- `levelDifficulty` "MusicLevelDifficulty"
- `isPublished` boolean
- `categories` "MusicCategories"
- `duration` integer
- `likes` integer
- `views` integer
- `maxAge` integer
- `minAge` integer
- `sections` "MediaSectionsMedia"
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profileId` uuid FK
- `thumbnailPrompt` text

**Music**
- `id` uuid PK
- `url` character varying
- `levelDifficulty` "MusicLevelDifficulty"
- `isPublished` boolean
- `musicLength` character varying
- `subtitleUrl` character varying
- `isTopScreen` boolean
- `isRecommendation` boolean
- `description` character varying
- `thumbnail` character varying
- `mediaType` "MediaForAudio"
- `duration` double precision
- `maxAge` integer
- `minAge` integer
- `sections` text[]
- `category` "MusicCategories"
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profileId` uuid FK
- `viewsCount` integer
- `accessType` "MediaAccessType"

**Video**
- `id` uuid PK
- `url` character varying
- `levelDifficulty` "ProfileAndInternalLevelDifficulty"
- `isPublished` boolean
- `thumbnail` character varying
- `title` character varying
- `mediaType` "media"
- `isTopScreen` boolean
- `isRecommendation` boolean
- `isFeatured` boolean
- `thumbnailWeight` character varying
- `maxAge` integer
- `minAge` integer
- `duration` double precision
- `sections` text[]
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `extra_id` uuid
- `viewsCount` integer
- `accessType` "MediaAccessType"

#### Categories & Keywords

**KeywordCategories**
- `id` uuid PK
- `keywordCategory` "KeywordCategory"
- `isPublished` boolean
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone

**KeywordOptions**
- `id` uuid PK
- `optionName` character varying
- `description` character varying
- `isPublished` boolean
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `categoryId` uuid FK -> KeywordCategories

**Category**
- `id` uuid PK
- `url` character varying
- `name` character varying
- `description` character varying
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone

#### AI & Stories

**AiPrompts**
- `id` uuid PK
- `title` character varying
- `aiPrompts` "EAiPrompts"
- `isCurrent` boolean
- `format` character varying
- `imageGenerationPrompt` character varying
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone

**ProfileStories**
- `id` uuid PK
- `storyText` jsonb
- `keyword` jsonb
- `description` character varying
- `title` character varying
- `text` text
- `subscriptionTime` timestamp with time zone
- `upgradeablePoints` integer
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `ageCategory` "AgeCategory"

**ProfileSubscription** (story-to-profile relationship)
- `id` uuid PK
- `isRead` boolean
- `isFavorite` boolean
- `temporary` boolean
- `profile_id` uuid FK -> Profile
- `story_id` uuid FK -> ProfileStories

#### Games

**WordNinja**
- `id` uuid PK
- `levelDifficulty` "ProfileWordsLevelDifficulty"
- `category` "CategoryWord"
- `Word` character varying
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `mediaId` uuid FK
- `videoId` uuid FK

**question**
- `id` uuid PK
- `isLiked` boolean
- `questionText` character varying
- `levelDifficulty` "QuestionLevelDifficulty"
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone (false zone)
- `profileId` uuid FK -> Profile

#### Playlists

**ProfilePlayList**
- `id` uuid PK
- `title` character varying
- `type` "PlayListTypes"
- `additionalText` character varying
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profileId` uuid FK -> Profile

**profile_playlist_music** (join table)
- `playlist_id` uuid FK -> ProfilePlayList
- `music_id` uuid FK -> Music

**profile_playlist_videos** (join table)
- `playlist_id` uuid FK -> ProfilePlayList
- `video_id` uuid FK -> Video

#### Activity & Other

**ActivityStatus**
- `id` uuid PK
- `isRead` boolean
- `isFavorite` boolean
- `profile_id` uuid FK -> Profile
- `story_id` uuid FK
- `temporary` boolean

**ProfilePlaylistLists**
- `id` uuid PK
- `createdAt` timestamp with time zone
- `updatedAt` timestamp with time zone
- `profileId` uuid FK -> Profile

**profile_migrations**
- migration tracking table

### Job Queue (Bull + Redis)

Bull queues for async processing. Used for media upload pipeline (AI generation runs as background jobs).
Configured in `app.module.ts` via `BullModule.forRootAsync`.

Key processors:
- `src/modules/media/processor/media-upload-processor.ts` - Processes uploaded videos/audio through the AI pipeline
- `src/modules/ideogram/processor/` - Processes Ideogram image generation requests

### Scheduled Tasks

`@nestjs/schedule` for cron jobs. `ScheduleModule.forRoot()` in app module.

### AI Pipelines

KidNation uses AI in two distinct flows:

#### 1. Video/Song Upload Pipeline

When a video or audio file is uploaded via the admin panel:

1. **Admin uploads** via `POST /media-upload/single-video` or `POST /media-upload/single-music` (or bulk via `POST /media-upload/from-csv`)
2. **Job is queued** in Bull + Redis. Admin can check status via `GET /media-upload/{jobUid}` and `GET /media-upload/jobs/pending`
3. **Bull processor runs** (`media-upload-processor.ts`):
   - OpenAI Whisper transcribes audio to text (`openAISpeachToText.service.ts`)
   - OpenAI (`gpt-4o`) generates: title, description, subtitles from transcription
   - OpenAI (`gpt-4o`) generates Word Ninja words from transcription (`generateWordsToVideo`)
   - OpenAI (`gpt-4o`) generates an image prompt for the thumbnail
   - Ideogram generates thumbnail image from that prompt (`ideogram.service.ts`)
4. **AI prompts are configurable** in the admin panel. The `AiPrompts` table stores prompt templates with `imageGenerationPrompt` field. Admins can change prompts without code changes.
5. **Results stored:** Media metadata in PostgreSQL, files in S3

#### 2. Storyteller Pipeline

AI-generated children's picture books. Fully async, progressive delivery.

**Step 1: User picks options (Flutter app)**
- User navigates to `/pick-options` route
- Options are uploaded from admin panel and stored in `KeywordCategories` + `KeywordOptions` tables
- Each hero/villain option contains a personality prompt (also from admin panel)
- User selects hero, villain, setting, special item, genre
- User's age determines word count limits and reading level

**Step 2: Story text generation (OpenAI gpt-4o)**
- Backend receives selected options + their personality prompts + user age
- Story generation system prompt is stored in admin panel (`AiPrompts` table) and sent to OpenAI
- Prompt enforces strict structure: exactly 10 pages, age-appropriate word counts, hero flaw arc, villain present on 6+ pages, climax on page 7
- Word count rules by age:
  - Ages 3-5: 220-480 total, 18-45 per page
  - Ages 6-8: 520-800 total, 45-85 per page
  - Ages 9-11: 800-1200 total, 75-130 per page
- Output: JSON with 10 page objects (`{ pageNumber, text }`)
- Code: `generateStoryTextV2(keywords, prompt)` in `openAi.service.ts`

**Step 3: Image prompt generation (OpenAI gpt-4o)**
- Second OpenAI request generates 10 image EDIT prompts (one per page)
- Prompt for this request is also stored in admin panel
- Each prompt describes the exact scene to illustrate, with identity locks for hero/villain reference images
- Prompts include camera angles, lighting, emotion cues, anti-text rules, physical staging rules
- Output: JSON with 10 prompt objects (`{ pageNumber, imagePrompt }`)

**Step 4: Image generation (OpenAI Image Edit API)**
- Image prompts are used by OpenAI image EDIT API (NOT Ideogram, NOT image generation from scratch)
- The API edits reference images of the selected hero/villain to match each scene
- This preserves consistent character appearance across all 10 pages
- Images generated in parallel

**Step 5: Voiceover generation (OpenAI gpt-4o-mini-tts)**
- OpenAI `gpt-4o-mini-tts` model generates audio narration for each page
- Default voice: "alloy"
- Output: MP3 files

**Step 6: Progressive delivery**
- As soon as the first image is returned, a push notification is sent to the user
- User can start reading immediately while remaining images generate in background
- Frontend routes: `/pick-options` -> `/story-teller` -> `/generating-story-finished`

**Step 7: Storage**
- Story metadata stored in `ProfileStories` table (storyText as jsonb, keyword as jsonb)
- Story-to-profile link stored in `ProfileSubscription` table
- Generated images and audio stored in S3

**Key detail: All prompts are admin-configurable.** The story generation prompt and image prompt generation prompt are both stored in the `AiPrompts` table and editable via the admin panel. This means the AI behavior can be tuned without code changes.

#### OpenAI Service Functions

**`src/services/openAi.service.ts` (text generation)**

| Function | Model | Purpose |
|---|---|---|
| `generateResponse(prompt)` | gpt-4o | Base function. Single prompt -> text response |
| `generateWordsToVideo(transcription, videoCategory)` | gpt-4o | Generates 15 Word Ninja words from video transcription. Returns JSON with word + difficulty + category |
| `generateResponseWords(transcription, levelDifficulty, category)` | gpt-4o | Extracts keywords with difficulty levels from transcription. Returns JSON |
| `generateStoryText(keywords, prompt)` | gpt-4o | Story generation v1. Generates pages sequentially (one API call per page) |
| `generateStoryTextV2(keywords, prompt)` | gpt-4o | Story generation v2. Generates all 10 pages in one call, split by "PageBreak" |

**`src/services/openAISpeachToText.service.ts` (audio)**

| Function | Model | Purpose |
|---|---|---|
| `transcribeAudio(audioFilePath)` | whisper-1 | Transcribes audio file to text (English) |
| `speechToTextFromUrl(fileUrl)` | whisper-1 | Downloads file, converts to audio, transcribes |
| `subtitleAudio(audioFilePath)` | whisper-1 | Generates SRT subtitles from audio |
| `speechToText(audioFilePath)` | whisper-1 | Translates audio to English text (private) |
| `textToSpeech(text, voice)` | gpt-4o-mini-tts | Generates MP3 voiceover. Default voice: "alloy". Returns file path |
| `textToSpeechAsBuffer(text, voice)` | gpt-4o-mini-tts | Same but returns Buffer. Prefixes "spell " for Word Ninja word spelling |

---

## Folder Structure

### Frontend (`kidnation-mobile`)

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

### Backend (`kidnation-back`)

```
src/
  authentication/       # Auth guard, service, controller
  common/
    constants/          # App constants (isAdminKey, wordNinjaUid, etc.)
    decorators/         # Custom decorators (@IsPublic, @IsAdmin, etc.)
    entity/             # Shared entities (question.entity.ts)
    enums/              # All enums (MediaCategory, levelDifficulty, games, etc.)
    errors/             # Custom error classes
    guards/             # Route guards
    interfaces/         # Shared interfaces
    mappers/            # Data mappers
    parsers/            # Data parsers
    repository/         # Shared repository patterns
    transformers/       # Data transformers
    types/              # Shared types
  database/
    postgresql/         # TypeORM migrations
  dto/                  # Data transfer objects
  modules/              # Feature modules (see Backend Modules table above)
  providers/
    database/           # TypeORM provider module
  services/             # Shared services (OpenAI, S3, email, etc.)
  utils/                # Utilities (datasource config, etc.)
  app.module.ts         # Root module
  main.ts               # Entry point
```

### Admin Panel (`kidnation-admin`)

```
src/
  assets/               # Static assets
  components/           # Shared React components
  helpers/              # Utility functions
  hooks/                # Custom React hooks
  pages/
    AIPrompts/          # AI prompt management (configurable prompts for content generation)
    AdminsPage/         # Admin user management
    Authorization/      # Login/auth
    BooksPage/          # Story books management
    ContentPage/        # Content management
    FeaturedPage/       # Featured content curation
    HomePage/           # Dashboard
    MusicPage/          # Music/audio content management + upload
    ProfileActivityPage/# Profile activity tracking
    ProfilePage/        # Profile management
    StoryTeller/        # Story teller configuration
    UserPage/           # Single user view
    UsersPage/          # Users list
  services/
    firebase.ts         # Firebase client SDK
    logout.ts           # Logout logic
    withAdmin.tsx        # Admin HOC wrapper
  shared/               # Shared types, constants
  store/
    models/             # TypeScript interfaces (users, music, video, etc.)
    reducers/           # Redux slices
    rtk-api/            # RTK Query API definitions
      admin.api.ts      # Admin endpoints
      ai-prompts.api.ts # AI prompts CRUD
      books.api.ts      # Books/stories endpoints
      home.api.ts       # Home page config
      media-upload.api.ts  # Media upload (video/audio + AI pipeline)
      media.api.ts      # Media CRUD
      profiles.api.ts   # Profile endpoints
      users.api.ts      # User endpoints
    api.ts              # Base API config
    store.ts            # Redux store setup
  styles/               # Global styles
  App.tsx               # Root component
  index.tsx             # Entry point
```

---

## Environment Variables

### Backend (.env.development / .env.production)

```
# PostgreSQL
POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DATABASE

# Firebase Admin
FIREBASE_CLIENT_EMAIL, FIREBASE_PRIVATE_KEY, FIREBASE_API_KEY, FIREBASE_WEP_API_KEY, FIREBASE_PROJECT_ID, FIREBASE_STORAGE_BUCKET

# AWS S3
AWS_REGION, AWS_ACCESS_KEY_ID, AWS_S3_BUCKET_NAME, AWS_SECRET_ACCESS_KEY

# OpenAI
OPENAI_API_KEY, OPENAI_ORG_ID, OPENAI_PROJECT_ID

# Redis
REDIS_IMAGE, REDIS_CONTAINER_NAME, REDIS_PORT, REDIS_PASSWORD, REDIS_DATA_VOLUME, REDIS_RESTART_POLICY
```

### Frontend

Environment managed via `envied` package. Config in `lib/core/env/`.

---

## Key Commands

### Frontend

```bash
# Code generation (after changing Freezed models or injectable)
fvm dart run build_runner build -d
# Watch mode:
fvm dart run build_runner watch -d

# Localization
fvm flutter gen-l10n

# Run app
fvm flutter run

# Analyze
fvm dart analyze
```

### Backend

```bash
# Install dependencies
cd kidnation-back && pnpm install

# Run with Docker (development)
pnpm run start:docker:development:build

# Run without Docker (development)
pnpm run start:dev

# Run production Docker
pnpm run start:docker:production:build

# Run migrations
pnpm run migration:run

# Generate migration
pnpm run migration:generate --name=migration_name

# Create empty migration
pnpm run migration:create --name=migration_name

# Revert last migration
pnpm run migration:revert

# Lint
pnpm run lint

# Format
pnpm run format

# Test
pnpm run test
pnpm run test:e2e

# Clean
pnpm run clean
```

---

## Key Enums

Located in `src/common/enums/`:

- `MediaCategory.enum.ts` - Content categories
- `accountSubscriptionStatus.enum.ts` - Subscription statuses
- `age-categories.enum.ts` - Age group categories
- `aiPrompts.enum.ts` - AI prompt types
- `completeLevels.ts` - Completion levels
- `games.enum.ts` - Game types
- `ideogramAspectRatio.enum.ts` - Ideogram image aspect ratios
- `imageGenerationService.enum.ts` - Which AI service to use for images
- `keyword.enum.ts` - Content keywords
- `levelDifficulty.enum.ts` / `internalLevelDifficulty.ts` - Game difficulty levels
- `media.enum.ts` - Media types
- `mediaAccessStatus.enum.ts` - Free vs premium access
- `mediaSections.enum.ts` - Content sections
- `playListTypes.enum.ts` - Playlist types

---

## Modules In Use

- [x] RevenueCat (subscriptions via purchases_flutter)
- [x] OpenAI gpt-4o (title/description/subtitle generation, Word Ninja word extraction, story text generation, image prompt generation)
- [x] OpenAI Image Edit API (story page illustrations - edits hero/villain reference images per scene)
- [x] OpenAI Whisper (whisper-1 for speech-to-text transcription and SRT subtitles)
- [x] OpenAI TTS (gpt-4o-mini-tts for story voiceover and Word Ninja word spelling, default voice: "alloy")
- [x] Ideogram (AI thumbnail generation for video/song uploads - NOT for stories)
- [x] Firebase Auth (Google Sign-In + Apple Sign-In)
- [x] Firebase Analytics
- [x] Firebase Remote Config
- [x] Firebase Messaging (push notifications)
- [x] Local Notifications (flutter_local_notifications)
- [x] Flame game engine (Word Ninja)
- [x] AWS S3 (media storage)
- [x] Dropbox (content import)
- [x] Docker (backend deployment)

---

## Current State

- **Version:** 2.0.11+209
- **Last shipped features:** Subscription fixes, profile updates
- **Primary developer:** Andrii
- **Known issues / tech debt:**
  - No production environment yet. Only dev Firebase project (`kidnation-mobile`) exists.
  - Backend repo has ~30+ migrations that could be squashed
  - `pubspec.yaml` description is still "A new Flutter project"
  - No flavors configured (single Firebase project)
  - Some custom package forks (better_player, turn_page_transition, spoiler_widget)
  - All OpenAI calls use `gpt-4o`. Could use a lighter model (gpt-4o-mini) for simpler tasks like title/description generation to reduce cost.

---

## Rules for Claude Code

### Code Style (Frontend)
- Use BLoC pattern for state management. Do NOT use Riverpod.
- Use `get_it` + `@injectable` for dependency injection.
- Routes are string constants in `lib/core/app_routes.dart`.
- Feature-based folder structure. Each feature has `data/`, `domain/`, `presentation/`.
- No em dashes in comments or documentation. Use periods or commas.
- App runs in fullscreen immersive mode. Do not add system UI elements.

### Code Style (Backend)
- TypeScript with NestJS conventions.
- One module per feature in `src/modules/`.
- Entities use TypeORM decorators (`@Entity`, `@Column`, `@PrimaryGeneratedColumn`, etc.).
- Validation via class-validator decorators on DTOs.
- Use `@nestjs/schedule` for cron jobs, Bull for async queues.
- Environment config via `@nestjs/config` with `.env.{NODE_ENV}` files.
- Firebase Admin SDK for auth only. Data lives in PostgreSQL.

### Code Generation (Frontend)
- Run `fvm dart run build_runner build -d` after changing Freezed models or injectable annotations.
- Run `fvm flutter gen-l10n` after changing localization strings.

### Security
- Never put secrets in client-side code. All API keys stay in backend `.env` files.
- Firebase Admin credentials are server-side only.
- OpenAI, AWS, and Ideogram keys are server-side only.
- RevenueCat webhook verification happens server-side.

### Patterns
- Do not introduce new packages without noting it clearly in your output.
- Follow existing BLoC patterns. Look at similar features before creating new ones.
- For payments: always use RevenueCat. Never raw StoreKit/BillingClient.
- For AI features: always route through the NestJS backend. Never call OpenAI from the client.
- For media: always use S3 via the backend service. Never upload from the client directly.

### Database
- All schema changes require a TypeORM migration. Never modify the DB manually.
- Generate migrations: `pnpm run migration:generate --name=descriptive_name`
- Test migrations locally before pushing.

### Git
- Frontend: `Eclipt-AI/kidnation-mobile` (branch: `dev`)
- Backend: `Eclipt-AI/kidnation-back` (branch: `development`)
- Admin panel: `Eclipt-AI/kidnation-admin` (branch: `main`)
- GitHub branch names come from ClickUp task IDs.

### Platform
- Always consider both iOS and Android.
- App runs fullscreen. UI must work without system status bar.
- Test on both phone and tablet form factors.

### When Unsure
- If unsure about a pattern, say so. Do not guess.
- If the task is ambiguous, ask. Do not assume.