# CLAUDE.md - KidNation Admin Panel

> Single source of truth for Claude Code working in the kidnation-admin repo.

---

## Project Overview

- **App name:** KidNation Admin
- **Description:** Web admin panel for KidNation. Content management, media upload with AI processing, AI prompt configuration, user management, analytics.
- **This repo:** Eclipt-AI/kidnation-admin (branch: `main`)
- **ClickUp space:** External > KidNation (folder ID: 901512978046)

### Sister Repos

- **Backend API:** Eclipt-AI/kidnation-back (branch: `development`) - NestJS + TypeScript + PostgreSQL. This admin panel calls the backend API for all data operations and AI processing.
- **Mobile app:** Eclipt-AI/kidnation-mobile (branch: `dev`) - Flutter. End-user facing app that consumes the same backend API.

---

## Tech Stack

- **Framework:** React + TypeScript
- **Build:** Create React App (via craco)
- **State management:** Redux Toolkit (RTK Query for API calls)
- **UI:** MUI (Material UI ^5.15.20) + Ant Design (^5.21.2) + styled-components
- **Forms:** react-hook-form (^7.52.0) + zod for validation
- **Auth:** Firebase client SDK (^10.12.2)
- **Video playback:** video.js + HLS.js + react-hls-player
- **Package manager:** yarn (yarn.lock present)
- **Routing:** react-router-dom (^6.24.0)

---

## Architecture

### API Layer (RTK Query)

All API calls go through RTK Query in `src/store/rtk-api/`. The admin panel does NOT talk to the database directly. Everything goes through the NestJS backend API.

| API File | Endpoints |
|---|---|
| `admin.api.ts` | Admin user management |
| `ai-prompts.api.ts` | AI prompt CRUD (story generation prompts, image prompts) |
| `books.api.ts` | Stories/books management |
| `home.api.ts` | Home page configuration |
| `media-upload.api.ts` | Media upload pipeline (video/audio + AI processing) |
| `media.api.ts` | Media CRUD (videos, music, content) |
| `profiles.api.ts` | Profile management |
| `users.api.ts` | User management |

### Media Upload Pipeline

The admin panel triggers AI processing on the backend when uploading content:

1. Admin uploads video/audio via `POST /media-upload/single-video` or `POST /media-upload/single-music`
2. Bulk upload supported via `POST /media-upload/from-csv`
3. Backend queues the job (Bull + Redis) and runs AI pipeline:
   - OpenAI Whisper transcribes audio
   - OpenAI gpt-4o generates title, description, subtitles, Word Ninja words, image prompt
   - Ideogram generates thumbnail from the image prompt
4. Admin can check job status via `GET /media-upload/{jobUid}`
5. Pending jobs listed via `GET /media-upload/jobs/pending`

### AI Prompt Configuration

The admin panel manages AI prompts that control how content is generated:

- **Story generation prompt** - System prompt sent to OpenAI for generating 10-page children's stories
- **Image prompt generation prompt** - System prompt for generating image edit prompts from story text
- **Content generation prompts** - Prompts used during video/song upload for title/description/thumbnail generation

All prompts stored in the `AiPrompts` table and editable through the `AIPrompts` page.

### Auth

Firebase client SDK for admin authentication. Token sent as Bearer in all API requests via `prepareHeaders` in RTK Query config.

---

## Folder Structure

```
src/
  assets/               # Static assets
  components/           # Shared React components
  helpers/              # Utility functions
  hooks/                # Custom React hooks
  pages/
    AIPrompts/          # AI prompt management (configurable prompts for all AI pipelines)
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
    firebase.ts         # Firebase client SDK init
    logout.ts           # Logout logic
    withAdmin.tsx        # Admin HOC wrapper
  shared/               # Shared types, constants
  store/
    models/             # TypeScript interfaces (users, music, video, etc.)
    reducers/           # Redux slices
    rtk-api/            # RTK Query API definitions (see API Layer above)
    api.ts              # Base API config (base URL, auth headers)
    store.ts            # Redux store setup
  styles/               # Global styles
  App.tsx               # Root component
  App.scss              # Root styles
  index.tsx             # Entry point
```

---

## Key Commands

```bash
# Install
yarn install

# Development
yarn start

# Build
yarn build

# Lint
yarn lint
```

---

## Backend API Base URL

Configured in `src/store/api.ts` via `baseQueryConfig`. Points to the NestJS backend.

Key API groups this admin panel calls:
- `/media-upload/` - Upload video/audio with AI processing
- `/admin/` - Admin management
- `/media/` - Content CRUD
- `/profile/` - Profile management
- `/account/` - Account management
- `/home/` - Home page section config
- `/category/` - Category management

---

## Rules for Claude Code

### Code Style
- React + TypeScript. Functional components with hooks.
- RTK Query for all API calls. Do not use raw fetch/axios.
- MUI + Ant Design for UI components. Check which library existing pages use before adding components.
- styled-components for custom styling.
- react-hook-form for all forms.

### Patterns
- Do not introduce new packages without noting it clearly.
- Follow existing page patterns. Look at similar pages before creating new ones.
- All data comes from the backend API. Never hardcode data.
- AI prompts are managed through the AIPrompts page. Never hardcode prompts.

### Security
- Firebase token is automatically attached to all API requests via RTK Query config.
- Never store secrets in frontend code.

### Git
- This repo: `Eclipt-AI/kidnation-admin` (branch: `main`)
- Branch names come from ClickUp task IDs.

### When Unsure
- If unsure about a pattern, say so. Do not guess.
- If the task is ambiguous, ask. Do not assume.