---
name: TradeKraft Music Virality Platform
description: Autonomous music marketing platform — full spec, architecture, and current build status
type: project
tags: [music-industry, ai-agents, marketing, autonomous, a-and-r, spotify, tiktok, influencers, playlist-pitching, sync-licensing]
related:
  - project_whos_hot.md
  - project_juhn_fan_dna.md
originSessionId: fb4781fa-5525-434f-88dc-126c2c8f3c76
---
TradeKraft is an autonomous music marketing platform that takes a song and executes a complete viral release campaign. Project directory: ~/TradeKraft. Full spec in ~/TradeKraft/CLAUDE.md.

**Why:** User is an A&R professional who receives finished songs and manages releases. No existing curator/blog/sync relationships. Needs to break artists across Latin, hip-hop, EDM, R&B, pop. May productize as a service later.

**How to apply:** When working on TradeKraft, always open ~/TradeKraft/CLAUDE.md first for full context. Build on the other computer using browser-based Claude Code at claude.ai/code.

## Relationships to Other Projects

- **[Who's Hot CRM](project_whos_hot.md)** — TradeKraft's Influencer Engine (Agent 7) overlaps directly with Who's Hot. Who's Hot discovers and ranks TikTok creators; TradeKraft automates the outreach. These two tools are complementary and could be integrated.
- **[Juhn Fan DNA Report](project_juhn_fan_dna.md)** — The output of TradeKraft's Artist Intelligence Profile (Agent 1) is exactly what the Juhn Fan DNA report represents. The Juhn data is a live example of what this agent should produce for any artist.

## Current Status
- Full platform spec designed across one conversation
- Project directory created at ~/TradeKraft
- CLAUDE.md written with complete spec
- No code written yet — ready to start Phase 1

## Core Architecture — 10 Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | Artist Intelligence Profile | Aggregates all platform data (like Sodatone/Chartmetric). Output looks like [Juhn Fan DNA report](project_juhn_fan_dna.md). |
| 2 | Smart Link + Pixel Engine | Landing page per song + Facebook/TikTok pixels for retargeting |
| 3 | Playlist Pitching Engine | All platforms: Spotify, Apple, Amazon, Deezer, YouTube, Tidal, SoundCloud, Audiomack, Pandora, iHeartRadio |
| 4 | Press + Blog Engine | Genre-specific publications, premiere + review pitching |
| 5 | Sync Licensing Engine | Music supervisors at production companies, ad agencies, game studios |
| 6 | Social Recon + Seeding Engine | Reddit, YouTube comments, Discord — queued for human approval |
| 7 | Influencer Engine | TikTok/YouTube/Instagram creators, scored by fit. See also: [Who's Hot CRM](project_whos_hot.md) |
| 8 | Pre-Save Campaign | Release day save spike to trigger Spotify algorithm |
| 9 | College Radio Engine | Music directors by genre and market |
| 10 | Analytics Watcher | Monitors all platforms, tells other agents to pivot or double down |

## Key Design Decisions
- Human approves before any comment/post fires (protects against platform ToS bans)
- Genre detection routes to different playbooks (Latin vs hip-hop vs EDM vs R&B/Pop)
- Smart link with pixels is the traffic hub — ALL organic work feeds the paid retargeting machine
- Intake: audio file + artist name (pre-release) OR Spotify link (already out)

## Build Plan
- Phase 1: Artist intelligence profile + smart link generator (foundation)
- Phase 2: Outreach automation (playlist pitching, press, sync, influencers)
- Phase 3: Analytics watcher + paid ads integration
