---
name: TradeKraft Music Virality Platform
description: Autonomous music marketing platform — full spec, architecture, and current build status
type: project
---

TradeKraft is an autonomous music marketing platform that takes a song and executes a complete viral release campaign. Project directory: ~/TradeKraft. Full spec in ~/TradeKraft/CLAUDE.md.

**Why:** User is an A&R professional who receives finished songs and manages releases. No existing curator/blog/sync relationships. Needs to break artists across Latin, hip-hop, EDM, R&B, pop. May productize as a service later.

**How to apply:** When working on TradeKraft, always open ~/TradeKraft/CLAUDE.md first for full context. Build on the other computer using browser-based Claude Code at claude.ai/code.

## Current Status
- Full platform spec designed across one conversation
- Project directory created at ~/TradeKraft
- CLAUDE.md written with complete spec
- No code written yet — ready to start Phase 1

## Core Architecture — 10 Agents
1. Artist Intelligence Profile (aggregates all platform data, similar to Sodatone/Chartmetric)
2. Smart Link + Pixel Engine (landing page per song + Facebook/TikTok pixels for retargeting)
3. Playlist Pitching Engine (all platforms: Spotify, Apple, Amazon, Deezer, YouTube, Tidal, SoundCloud, Audiomack, Pandora, iHeartRadio)
4. Press + Blog Engine (genre-specific publications, premiere + review pitching)
5. Sync Licensing Engine (music supervisors at production companies, ad agencies, game studios)
6. Social Recon + Seeding Engine (Reddit, YouTube comments, Discord — queued for human approval)
7. Influencer Engine (TikTok/YouTube/Instagram creators, scored by fit)
8. Pre-Save Campaign (release day save spike to trigger Spotify algorithm)
9. College Radio Engine (music directors by genre and market)
10. Analytics Watcher (monitors all platforms, tells other agents to pivot or double down)

## Key Design Decisions
- Human approves before any comment/post fires (protects against platform ToS bans)
- Genre detection routes to different playbooks (Latin vs hip-hop vs EDM vs R&B/Pop)
- Smart link with pixels is the traffic hub — ALL organic work feeds the paid retargeting machine
- Intake: audio file + artist name (pre-release) OR Spotify link (already out)

## Build Plan
- Phase 1: Artist intelligence profile + smart link generator (foundation)
- Phase 2: Outreach automation (playlist pitching, press, sync, influencers)
- Phase 3: Analytics watcher + paid ads integration
