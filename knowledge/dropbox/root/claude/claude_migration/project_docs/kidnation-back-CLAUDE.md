# CLAUDE.md - KidNation Backend

> Single source of truth for Claude Code working in the kidnation-back repo.

---

## Project Overview

- **App name:** KidNation
- **Client:** US-based startup, co-founded by Chris "Ludacris" Bridges
- **Description:** Backend API for KidNation - an AI-powered edutainment mobile app for kids. Handles content management, AI generation pipelines, user profiles, subscriptions, and media processing.
- **This repo:** Eclipt-AI/kidnation-back (branch: `development`)
- **ClickUp space:** External > KidNation (folder ID: 901512978046)

### Sister Repos

- **Mobile app:** Eclipt-AI/kidnation-mobile (branch: `dev`) - Flutter, BLoC + get_it, iOS/Android
- **Admin panel:** Eclipt-AI/kidnation-admin (branch: `main`) - React + Redux Toolkit. Calls this backend's API for content management and media upload.

---

## Tech Stack

- **Framework:** NestJS (^9.4.3) with TypeScript
- **Runtime:** Node.js
- **Package manager:** pnpm
- **Database:** PostgreSQL via TypeORM (^0.3.20)
- **Queue:** Bull (^4.16.0) + Redis
- **Scheduler:** @nestjs/schedule (^4.1.1)
- **AI - Text:** OpenAI (^4.78.0) using `gpt-4o` for all text generation
- **AI - Images:** OpenAI Image Edit API for story illustrations, Ideogram for video/song thumbnails
- **AI - Audio:** OpenAI `whisper-1` for transcription, `gpt-4o-mini-tts` for voiceover (default voice: "alloy")
- **Media storage:** AWS S3 (aws-sdk ^2.1630.0)
- **Content source:** Dropbox SDK (^10.34.0)
- **Media processing:** fluent-ffmpeg + ffprobe-static + sharp (^0.34.5)
- **Auth:** Firebase Admin SDK (^12.1.1) - auth only, no Firestore
- **API docs:** Swagger (@nestjs/swagger ^7.3.1)
- **Validation:** class-validator + class-transformer + zod
- **Infrastructure:** Docker Compose (dev only, no prod environment yet), GitHub Actions CI
- **Firebase project (dev):** kidnation-mobile
- **Firebase project (prod):** None yet

---

## Module Structure

NestJS modules in `src/modules/`. Each module has its own controller, service, and entity files.

| Module | Purpose |
|---|---|
| `account` | User account management |
| `admin` | Admin panel operations, content management |
| `aiPrompts` | AI prompt templates and management (admin-configurable) |
| `category` | Content categories |
| `dropbox` | Dropbox integration for content import |
| `firebase` | Firebase Admin SDK integration (auth) |
| `home` | Home page data, sections |
| `ideogram` | Ideogram AI thumbnail generation for video/song uploads |
| `imageAi` | AI image processing coordination |
| `leaderboard` | Game leaderboards (Word Ninja) |
| `media` | Media file management, upload pipeline with AI processing |
| `music` | Songs and audio content |
| `openai` | OpenAI module (gpt-4o for text, Image Edit API for story illustrations) |
| `profile` | User profiles (multiple child profiles per account) |
| `profileGameProgress` | Game progress tracking per profile |
| `profilePlayLists` | User playlists per profile |
| `profileStories` | AI-generated stories per profile |
| `revenueCat` | RevenueCat webhook + subscription verification |
| `scripts` | Admin scripts and data operations |
| `section` | Content sections / groupings |
| `videos` | Video content management |
| `wordsNinja` | Word Ninja game data (words, levels, categories) |

---

## Services

| Service | File | Purpose |
|---|---|---|
| `openAi.service` | `src/services/openAi.service.ts` | OpenAI gpt-4o text generation. Story text, titles, descriptions, Word Ninja words, image prompts |
| `openAISpeachToText.service` | `src/services/openAISpeachToText.service.ts` | Audio: whisper-1 for transcription/subtitles, gpt-4o-mini-tts for voiceover (voice: "alloy") |
| `s3.service` | `src/services/s3.service.ts` | AWS S3 upload/download for media files |
| `email.service` | `src/services/email.service.ts` | Email sending |
| `fileDownload.axios.service` | `src/services/fileDownload.axios.service.ts` | File download via Axios |

### OpenAI Service Functions (`src/services/openAi.service.ts`)

| Function | Model | Purpose |
|---|---|---|
| `generateResponse(prompt)` | gpt-4o | Base function. Single prompt -> text response |
| `generateWordsToVideo(transcription, videoCategory)` | gpt-4o | Generates 15 Word Ninja words from video transcription. JSON output |
| `generateResponseWords(transcription, levelDifficulty, category)` | gpt-4o | Extracts keywords with difficulty levels. JSON output |
| `generateStoryText(keywords, prompt)` | gpt-4o | Story generation v1. Sequential page-by-page |
| `generateStoryTextV2(keywords, prompt)` | gpt-4o | Story generation v2. All 10 pages in one call, "PageBreak" separator |

### Audio Service Functions (`src/services/openAISpeachToText.service.ts`)

| Function | Model | Purpose |
|---|---|---|
| `transcribeAudio(audioFilePath)` | whisper-1 | Transcribes audio file to text (English) |
| `speechToTextFromUrl(fileUrl)` | whisper-1 | Downloads file, converts to audio, transcribes |
| `subtitleAudio(audioFilePath)` | whisper-1 | Generates SRT subtitles from audio |
| `speechToText(audioFilePath)` | whisper-1 | Translates audio to English text (private) |
| `textToSpeech(text, voice)` | gpt-4o-mini-tts | Generates MP3 voiceover. Default voice: "alloy". Returns file path |
| `textToSpeechAsBuffer(text, voice)` | gpt-4o-mini-tts | Returns Buffer. Prefixes "spell " for Word Ninja word spelling |

---

## Authentication

Firebase Admin SDK for auth. Global `AuthGuard` applied via `APP_GUARD`.

| Decorator | Purpose |
|---|---|
| `@IsPublic()` | Public routes, no auth required |
| `@IsAdmin()` | Admin-only routes |
| `@IsSuperAdmin()` | Super admin routes |
| `@IsRC()` | RevenueCat webhook routes |

---

## AI Pipelines

### 1. Video/Song Upload Pipeline

When a video or audio file is uploaded via the admin panel:

1. **Admin uploads** via `POST /media-upload/single-video` or `POST /media-upload/single-music` (or bulk via `POST /media-upload/from-csv`)
2. **Job queued** in Bull + Redis. Status check: `GET /media-upload/{jobUid}` and `GET /media-upload/jobs/pending`
3. **Bull processor** (`src/modules/media/processor/media-upload-processor.ts`) runs:
   - OpenAI Whisper transcribes audio to text
   - OpenAI gpt-4o generates: title, description, subtitles from transcription
   - OpenAI gpt-4o generates Word Ninja words from transcription
   - OpenAI gpt-4o generates an image prompt for the thumbnail
   - Ideogram generates thumbnail image from that prompt
4. **AI prompts are admin-configurable** via `AiPrompts` table
5. **Results stored:** Media metadata in PostgreSQL, files in S3

### 2. Storyteller Pipeline

AI-generated children's picture books with progressive delivery.

1. **User picks options** (hero, villain, setting, item, genre). Each has personality prompts from admin panel.
2. **Story text** generated by OpenAI gpt-4o. System prompt from admin panel. Enforces 10-page structure with age-based word counts (3-5: 220-480, 6-8: 520-800, 9-11: 800-1200). Output: JSON with 10 pages.
3. **Image prompts** generated by second OpenAI gpt-4o call. Prompt from admin panel. 10 scene descriptions with identity locks for hero/villain.
4. **Images** generated by OpenAI Image Edit API. Edits reference images of hero/villain per scene. Consistent characters across pages.
5. **Voiceover** generated by OpenAI gpt-4o-mini-tts. Default voice: "alloy".
6. **Progressive delivery**: push notification sent on first image. User reads while rest generates.
7. **Storage**: `ProfileStories` (storyText as jsonb), images/audio in S3, profile link in `ProfileSubscription`.

**Key: All prompts are admin-configurable** via the `AiPrompts` table. No code changes needed to tune AI behavior.

**Ideogram = video/song thumbnails. OpenAI Image Edit = story illustrations.** Different AI for different purposes.

---

## Database (PostgreSQL + TypeORM)

- ~30+ migrations in `src/database/postgresql/`
- TypeORM provider module at `src/providers/database/postgresql/typeorm.module.ts`
- Datasource config at `src/utils/datasource.ts`
- Environment: `.env.${NODE_ENV}` files

### Schema

#### Account & Auth

**Account** - id (uuid PK), uids (text[]), emails (text[]), FCM_tokens (text[]), role ("AccountRole"), createdAt, updatedAt, isSubscribedToEmail (boolean)

**Admin** - id (uuid PK), emails (character varying), createdAt, updatedAt

**TokenEmails** - id (uuid PK), uid, adminEmails, isPatched (boolean), createdAt, updatedAt

#### Profiles

**Profile** - id (uuid PK), name (varchar 25), createdAt, updatedAt, preferredAge (varchar 255), birthday (date), accountId (uuid FK -> Account), storyStatus (jsonb)

**profile_images** - id (uuid PK), url, name

**ProfileMedia** - id (uuid PK), isLiked, isLast, secondsWatched (integer), createdAt, updatedAt, profileId (FK -> Profile), mediaId (FK -> Media)

**ProfileGameProgress** - id (uuid PK), levelDifficulty ("ProfileGameLevelDifficulty"), totalCompleted, easyLevelsComplete, mediumLevelsComplete, hardLevelsComplete, expertLevelsComplete, masterLevelsComplete, createdAt, updatedAt, profile_id (FK -> Profile)

**WordToProfileProgress** (join) - wordId (FK -> WordNinja), progressId (FK -> ProfileGameProgress)

#### Content

**Media** - id (uuid PK), mediaType ("MediaType"), url, thumbnailUrl, subtitleUrl, title, description, accessType ("MediaAccessType"), levelDifficulty ("MusicLevelDifficulty"), isPublished, categories ("MusicCategories"), duration, likes, views, maxAge, minAge, sections ("MediaSectionsMedia"), createdAt, updatedAt, profileId (FK), thumbnailPrompt (text)

**Music** - id (uuid PK), url, levelDifficulty, isPublished, musicLength, subtitleUrl, isTopScreen, isRecommendation, description, thumbnail, mediaType ("MediaForAudio"), duration (double), maxAge, minAge, sections (text[]), category ("MusicCategories"), createdAt, updatedAt, profileId (FK), viewsCount, accessType

**Video** - id (uuid PK), url, levelDifficulty ("ProfileAndInternalLevelDifficulty"), isPublished, thumbnail, title, mediaType, isTopScreen, isRecommendation, isFeatured, thumbnailWeight, maxAge, minAge, duration (double), sections (text[]), createdAt, updatedAt, extra_id, viewsCount, accessType

#### Categories & Keywords

**KeywordCategories** - id (uuid PK), keywordCategory ("KeywordCategory"), isPublished, createdAt, updatedAt

**KeywordOptions** - id (uuid PK), optionName, description, isPublished, createdAt, updatedAt, categoryId (FK -> KeywordCategories)

**Category** - id (uuid PK), url, name, description, createdAt, updatedAt

#### AI & Stories

**AiPrompts** - id (uuid PK), title, aiPrompts ("EAiPrompts"), isCurrent (boolean), format, imageGenerationPrompt, createdAt, updatedAt

**ProfileStories** - id (uuid PK), storyText (jsonb), keyword (jsonb), description, title, text (text), subscriptionTime (timestamp), upgradeablePoints (integer), createdAt, updatedAt, ageCategory ("AgeCategory")

**ProfileSubscription** - id (uuid PK), isRead, isFavorite, temporary, profile_id (FK -> Profile), story_id (FK -> ProfileStories)

#### Games

**WordNinja** - id (uuid PK), levelDifficulty ("ProfileWordsLevelDifficulty"), category ("CategoryWord"), Word, createdAt, updatedAt, mediaId (FK), videoId (FK)

**question** - id (uuid PK), isLiked, questionText, levelDifficulty ("QuestionLevelDifficulty"), createdAt, updatedAt, profileId (FK -> Profile)

#### Playlists

**ProfilePlayList** - id (uuid PK), title, type ("PlayListTypes"), additionalText, createdAt, updatedAt, profileId (FK -> Profile)

**profile_playlist_music** (join) - playlist_id (FK), music_id (FK)

**profile_playlist_videos** (join) - playlist_id (FK), video_id (FK)

#### Other

**ActivityStatus** - id (uuid PK), isRead, isFavorite, profile_id (FK), story_id (FK), temporary

**ProfilePlaylistLists** - id (uuid PK), createdAt, updatedAt, profileId (FK)

---

## Folder Structure

```
src/
  authentication/       # Auth guard, service, controller
  common/
    constants/          # App constants (isAdminKey, wordNinjaUid, etc.)
    decorators/         # @IsPublic, @IsAdmin, @IsSuperAdmin, @IsRC
    entity/             # Shared entities (question.entity.ts)
    enums/              # All enums (MediaCategory, levelDifficulty, games, etc.)
    errors/             # Custom error classes
    guards/             # Route guards
    interfaces/         # Shared interfaces
    mappers/            # Data mappers
    parsers/            # Data parsers
    repository/         # Shared repository patterns
    transformers/       # Data transformers
    types/              # Shared types (textToSpeachType, etc.)
  database/
    postgresql/         # TypeORM migrations (~30+)
  dto/                  # Data transfer objects
  modules/              # Feature modules (see Module Structure above)
  providers/
    database/           # TypeORM provider module
  services/             # Shared services (OpenAI, S3, email, etc.)
  utils/                # Utilities (datasource config, convertDifficulty, etc.)
  app.module.ts         # Root module
  main.ts               # Entry point
```

---

## Environment Variables (.env.development)

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
- `imageGenerationService.enum.ts` - Which AI service for images
- `keyword.enum.ts` - Content keywords
- `levelDifficulty.enum.ts` / `internalLevelDifficulty.ts` - Game difficulty levels
- `media.enum.ts` - Media types
- `mediaAccessStatus.enum.ts` - Free vs premium access
- `mediaSections.enum.ts` - Content sections
- `playListTypes.enum.ts` - Playlist types

---

## Key Commands

```bash
# Install
pnpm install

# Run with Docker (development)
pnpm run start:docker:development:build

# Run without Docker
pnpm run start:dev

# Migrations
pnpm run migration:run
pnpm run migration:generate --name=migration_name
pnpm run migration:create --name=migration_name
pnpm run migration:revert

# Lint / Format / Test
pnpm run lint
pnpm run format
pnpm run test
pnpm run test:e2e

# Clean
pnpm run clean
```

---

## Current State

- **Version:** 0.0.1
- **Primary developer:** Andrii
- **Known tech debt:**
  - No production environment yet
  - ~30+ migrations that could be squashed
  - All OpenAI calls use gpt-4o. Could use gpt-4o-mini for simpler tasks to reduce cost.

---

## Rules for Claude Code

### Code Style
- TypeScript with NestJS conventions.
- One module per feature in `src/modules/`.
- Entities use TypeORM decorators (`@Entity`, `@Column`, `@PrimaryGeneratedColumn`).
- Validation via class-validator decorators on DTOs.
- Use `@nestjs/schedule` for cron jobs, Bull for async queues.
- Environment config via `@nestjs/config` with `.env.{NODE_ENV}` files.
- Firebase Admin SDK for auth only. Data lives in PostgreSQL.

### Database
- All schema changes require a TypeORM migration. Never modify the DB manually.
- Generate migrations: `pnpm run migration:generate --name=descriptive_name`
- Test migrations locally before pushing.

### Security
- All API keys stay in backend `.env` files.
- Firebase Admin credentials, OpenAI, AWS, Ideogram keys are server-side only.
- RevenueCat webhook verification happens server-side.

### Patterns
- Do not introduce new packages without noting it clearly.
- Follow existing NestJS module patterns. Look at similar modules before creating new ones.
- For AI features: always route through OpenAI service. Never expose API keys to clients.
- For media: always use S3 service.

### Git
- This repo: `Eclipt-AI/kidnation-back` (branch: `development`)
- Branch names come from ClickUp task IDs.

### When Unsure
- If unsure about a pattern, say so. Do not guess.
- If the task is ambiguous, ask. Do not assume.