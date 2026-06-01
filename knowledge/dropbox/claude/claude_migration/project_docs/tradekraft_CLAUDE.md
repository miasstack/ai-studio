# TradeKraft — Music Virality Platform

## What This Is
TradeKraft is an autonomous music marketing platform that takes a song and builds + executes a complete viral release campaign. It is built for an A&R professional who receives finished songs and needs to plan and execute releases across Latin, hip-hop, EDM, R&B, and pop genres.

## Core Philosophy
- The machine does 95% of the work. A human approves and fires.
- Every campaign is genre-aware — Latin gets a different playbook than EDM.
- All organic outreach feeds a paid retargeting machine via tracking pixels.
- No spray-and-blast. Everything is targeted and human-sounding.

## Primary User
An A&R professional who receives finished songs from artists and manages their release campaigns. No existing curator/blog/sync relationships — cold pitching everything. May eventually productize this as a service to other managers/labels.

## Campaign Inputs
**Pre-release (new artist):**
- Audio file + artist name
- Genre
- Release date
- Facebook Business Manager access
- TikTok Ads Manager access

**Post-release (song already out):**
- Spotify artist/track link
- Everything else auto-discovered

## What the Machine Auto-Discovers from a Spotify Link
- Monthly listeners, follower count, trajectory
- Top markets where fans already are
- Similar/comparable artists (used for targeting)
- Existing playlist placements
- All social profiles (YouTube, Instagram, TikTok, Facebook, SoundCloud, Audiomack, Twitter/X)
- Audience demographics and size per platform

## Core Modules

### 1. Artist Intelligence Profile
Aggregates all available data on the artist across every platform. Flags missing or unsynced profiles. Similar to Sodatone/Chartmetric in scope.

### 2. Smart Link + Pixel Engine
- Generates a custom landing page per song (not just a Linktree — a real campaign page)
- Artist photo, song player, streaming links, email capture
- Facebook Pixel + TikTok Pixel embedded
- Every visitor gets cookied for retargeting
- Builds Custom Audiences and Lookalike Audiences in both ad platforms
- One link used everywhere so all traffic is tracked

### 3. Playlist Pitching Engine
Targets curators across ALL platforms:
- Spotify (editorial + UGC)
- Apple Music
- Amazon Music
- Deezer
- YouTube playlists
- Tidal
- SoundCloud
- Audiomack
- Pandora
- iHeartRadio
Scrapes curator contact info, scores by genre fit, drafts personalized pitches, tracks responses.

### 4. Press + Blog Engine
- Identifies relevant publications by genre
- Pitches premieres pre-release
- Pitches reviews post-release
- Latin: Remezcla, Sounds & Colours
- Hip-hop: DJBooth, 2DopeBoyz, HipHopDX, Pigeons & Planes
- EDM: Dancing Astronaut, Your EDM, EDMTunes
- R&B/Pop: Ones To Watch, Earmilk

### 5. Sync Licensing Engine
- Identifies music supervisors at production companies, ad agencies, studios, game studios
- Matches by song mood/tempo/genre
- Drafts pitches with full metadata and licensing info

### 6. Social Recon + Seeding Engine
- Maps relevant Reddit communities
- Identifies YouTube videos where target fans congregate
- Finds Discord servers, Facebook groups
- Drafts native-feeling posts and comments
- Queues everything for human approval before posting (platform ToS protection)

### 7. Influencer Engine
- Finds TikTok/YouTube/Instagram creators in the right niche
- Scores by engagement rate and audience fit
- Identifies which creators in which niches are likely to organically pick up the sound
- Drafts DM outreach scripts

### 8. Pre-Save Campaign
- Builds pre-release momentum
- Drives saves on release day to trigger algorithmic playlists
- Email capture on landing page feeds this

### 9. College Radio Engine
- Database of college radio stations and music directors
- Submits to relevant stations by genre and market

### 10. Analytics Watcher
- Monitors all platforms daily
- Tracks streaming trajectory, social growth, playlist adds, press mentions
- Identifies what is gaining traction
- Tells other agents to double down or pivot

## Genre Routing
| Genre | Key Platforms | Key Markets | Notes |
|---|---|---|---|
| Latin | YouTube + Spotify | Mexico, Colombia, Miami, Spain | Reggaeton, trap, cumbia have different sub-playbooks |
| Hip-Hop | Audiomack + SoundCloud + Spotify | US, UK, Nigeria | Rap Caviar is the holy grail |
| EDM | Beatport + Spotify | Europe, Australia | DJ support matters |
| R&B/Pop | Spotify + Apple Music | US, UK | Mood/aesthetic creator focus |

## Campaign Timeline Structure
- T-30 days: Artist profile audit, smart link creation, pixel setup, pre-save campaign launch
- T-14 days: Playlist pitches go out, press premiere pitches go out, influencer seeding begins
- T-7 days: Social content queue loaded, college radio submissions, sync pitches go out
- Release day: All streaming links live, social content fires, pre-save converts
- T+7 to T+30: Analytics monitoring, retargeting ads launch, double down on what's working

## Tech Stack (to be determined during build)
- Claude Agent SDK for multi-agent orchestration
- Spotify API for artist/track data
- Facebook Marketing API for pixel and audience setup
- TikTok Marketing API for pixel and audience setup
- Web scraping for curator/blog/influencer discovery
- Simple web UI for intake and campaign dashboard

## Project Directory Structure (planned)
- /agents — individual agent definitions
- /tools — API integrations and scrapers
- /templates — pitch templates, content templates by genre
- /ui — campaign dashboard and intake form
- /data — curator databases, blog lists, sync supervisor lists
