---
name: KidNation Project
description: Full architecture and context for KidNation — AI-powered kids edutainment app co-founded by Chris "Ludacris" Bridges. Three repos, all context needed to work across them.
type: project
tags: [app-development, flutter, nestjs, react, openai, firebase, aws-s3, postgresql, redis, edutainment, mobile-app, ai-features]
originSessionId: fb4781fa-5525-434f-88dc-126c2c8f3c76
---
# KidNation

**Client:** US-based startup, co-founded by Chris "Ludacris" Bridges
**Type:** AI-powered edutainment mobile app for kids
**ClickUp space:** External > KidNation (folder ID: 901512978046)
**Figma:** https://www.figma.com/design/u7TuU0FgWDzw4JvNMGlYyj/KidNation
**Local project folder:** ~/Desktop/kn app/ (contains all 4 CLAUDE.md files)

## Three Repos

| Repo | Branch | Stack | Purpose |
|---|---|---|---|
| Eclipt-AI/kidnation-back | `development` | NestJS + TypeScript + PostgreSQL + Redis | Backend API, all AI runs here |
| Eclipt-AI/kidnation-mobile | `dev` | Flutter 3.19.6 + BLoC + get_it | iOS/Android kid-facing app |
| Eclipt-AI/kidnation-admin | `main` | React + TypeScript + RTK Query | Content management, AI prompt config |

**Git:** Branch names come from ClickUp task IDs.

---

## Backend (kidnation-back)

- **NestJS** + TypeScript, pnpm
- **DB:** PostgreSQL via TypeORM, ~30+ migrations in `src/database/postgresql/`
- **Queue:** Bull + Redis for async AI jobs
- **Auth:** Firebase Admin SDK — auth only, no Firestore. Guards: `@IsPublic`, `@IsAdmin`, `@IsSuperAdmin`, `@IsRC`
- **AI Text:** OpenAI gpt-4o for everything (title/description/subtitles/story/word ninja words/image prompts)
- **AI Audio:** whisper-1 (transcription/subtitles), gpt-4o-mini-tts (voiceover, default voice "alloy")
- **AI Images:** OpenAI Image Edit API for story illustrations, Ideogram for video/song thumbnails
- **Storage:** AWS S3 via `s3.service.ts`
- **Content source:** Dropbox SDK

### Key Services
- `src/services/openAi.service.ts` — gpt-4o wrapper (generateResponse, generateWordsToVideo, generateStoryText, generateStoryTextV2)
- `src/services/openAISpeachToText.service.ts` — whisper + TTS
- `src/services/s3.service.ts` — S3 uploads/downloads

### Key Modules
account, admin, aiPrompts, category, dropbox, firebase, home, ideogram, imageAi, leaderboard, media, music, openai, profile, profileGameProgress, profilePlayLists, profileStories, revenueCat, scripts, section, videos, wordsNinja

### AI Pipelines

**Video/Song Upload Pipeline:**
1. Admin uploads via `POST /media-upload/single-video` or `/single-music`
2. Bull job queued, status at `GET /media-upload/{jobUid}`
3. Processor runs: Whisper → gpt-4o (title/desc/subtitles) → gpt-4o (Word Ninja words) → gpt-4o (image prompt) → Ideogram (thumbnail)
4. Results stored in PostgreSQL + S3

**Storyteller Pipeline:**
1. User picks hero, villain, setting, item, genre at `/pick-options`
2. gpt-4o generates 10-page story (prompt from AiPrompts table, age-based word counts: 3-5yo: 220-480 words, 6-8yo: 520-800, 9-11yo: 800-1200)
3. gpt-4o generates 10 image edit prompts
4. OpenAI Image Edit API edits hero/villain reference images for each page (consistent characters)
5. gpt-4o-mini-tts generates MP3 voiceover per page
6. Push notification on first image ready — user reads while rest generates
7. Stored in ProfileStories (jsonb) + S3

**Key detail:** ALL prompts are admin-configurable via AiPrompts table. No code changes needed to tune AI behavior.

### Database Schema (key tables)
- **Account** — uids[], emails[], FCM_tokens[], role
- **Profile** — name, birthday, preferredAge, accountId FK, storyStatus (jsonb)
- **Media** — mediaType, url, thumbnailUrl, subtitleUrl, title, description, accessType, levelDifficulty, isPublished, categories, sections, thumbnailPrompt
- **Music** — url, levelDifficulty, isPublished, isTopScreen, isRecommendation, category, sections[], accessType
- **Video** — url, levelDifficulty, thumbnail, title, isFeatured, isTopScreen, isRecommendation, sections[], accessType
- **AiPrompts** — title, aiPrompts (EAiPrompts enum), isCurrent, format, imageGenerationPrompt
- **ProfileStories** — storyText (jsonb), keyword (jsonb), ageCategory
- **ProfileSubscription** — profile_id FK, story_id FK, isRead, isFavorite
- **WordNinja** — Word, levelDifficulty, category, mediaId FK, videoId FK
- **KeywordCategories / KeywordOptions** — Storyteller option picker data

---

## Mobile App (kidnation-mobile)

- **Flutter 3.19.6** via FVM, Dart >=3.3.0
- **State:** BLoC (flutter_bloc) + get_it + injectable. NO Riverpod.
- **Navigation:** GoRouter, routes in `lib/core/app_routes.dart`
- **Models:** Freezed + json_serializable
- **Subscriptions:** RevenueCat (purchases_flutter)
- **Auth:** Firebase Auth + Google Sign-In + Apple Sign-In
- **Video:** better_player (custom fork: Ragnarokr45/kidNbetterplayer)
- **Audio:** just_audio + audio_service
- **Game engine:** Flame + flame_bloc (Word Ninja game)
- **Analytics:** Firebase Analytics + Remote Config
- **Push:** Firebase Messaging + flutter_local_notifications
- **App mode:** fullscreen immersive sticky (no system UI)
- **Custom fonts:** SegoeUI (primary), fruit-ninja, super-boom, story_teller_new, calibri

### Features
lib/features/: activities, analytics, auth, home, main, playlists, profile, songs, story_teller, subscriptions, videos

### Code Rules
- BLoC only (no Riverpod)
- Routes = string constants in app_routes.dart
- Feature structure: data/ + domain/ + presentation/
- Run `fvm dart run build_runner build -d` after Freezed/injectable changes
- Run `fvm flutter gen-l10n` after l10n changes
- No em dashes in comments
- Must work fullscreen on both phone and tablet, iOS and Android

---

## Admin Panel (kidnation-admin)

- **React + TypeScript**, Create React App via craco, yarn
- **State:** Redux Toolkit + RTK Query for all API calls (no raw fetch/axios)
- **UI:** MUI v5 + Ant Design v5 + styled-components
- **Forms:** react-hook-form + zod
- **Auth:** Firebase client SDK
- **Video:** video.js + HLS.js + react-hls-player

### RTK Query API files (src/store/rtk-api/)
admin.api.ts, ai-prompts.api.ts, books.api.ts, home.api.ts, media-upload.api.ts, media.api.ts, profiles.api.ts, users.api.ts

### Pages
AIPrompts, AdminsPage, Authorization, BooksPage, ContentPage, FeaturedPage, HomePage, MusicPage, ProfileActivityPage, ProfilePage, StoryTeller, UserPage, UsersPage

---

## Current State

- **Version:** 2.0.11+209 (mobile)
- **Primary developer:** Andrii
- **No production environment yet** — only dev Firebase project (kidnation-mobile)
- **Known tech debt:**
  - ~30+ migrations could be squashed (backend)
  - All OpenAI calls use gpt-4o — could use gpt-4o-mini for simpler tasks (cost saving)
  - No flavors configured
  - Custom package forks (better_player, turn_page_transition, spoiler_widget)

**Why:** Co-founder is Chris "Ludacris" Bridges. Project is in active development with Andrii as primary dev.
**How to apply:** When working on any KidNation task, always check which repo it belongs to and follow that repo's patterns. Never Riverpod on mobile, never raw fetch on admin, all AI goes through backend.
