---
name: Who's Hot — TikTok Influencer CRM
description: TikTok influencer discovery and outreach CRM project. Single HTML file, no backend. Build spec saved here for future session.
type: project
---

# Who's Hot — TikTok Influencer Discovery CRM

**Project directory:** TBD (not started yet)
**Status:** Planned — user wants to build this in a future session

## What it is
A TikTok influencer discovery and outreach CRM dashboard. Finds trending creators by hashtag/niche, ranks by views/engagement, manages outreach campaigns with AI-generated pitches.

## Tech stack
- Pure HTML/CSS/JavaScript — single self-contained HTML file
- No backend, no database, no framework
- State stored in browser localStorage
- TikTok data via Apify API (actor: `clockworks~free-tiktok-scraper`)
- AI pitches via Anthropic Claude API (`claude-sonnet-4-20250514`) — called directly from browser

## 5 Tabs
1. **Discover** — Enter hashtags, scrape TikTok trending creators via Apify, poll for run completion, display results ranked by avg views with follower count + engagement rate. Button to add creator to CRM.
2. **CRM** — Table: name, handle, followers, engagement bar, niche, status (prospect/contacted/replied/closed), campaign assignment. Search + filter. Edit and Pitch buttons per row. CSV export.
3. **Pipeline** — Kanban board grouped by outreach status (4 columns).
4. **Compare** — Select up to 5 influencers, side-by-side stats, AI comparison report via Claude API.
5. **Settings** — Apify API key (localStorage, type=password), campaign manager, data export/clear.

## AI Features
- Pitch generator: DM, email, collab offer — calls `https://api.anthropic.com/v1/messages` directly
- Compare report: AI analysis of selected influencers

## Design
- Clean flat white UI
- Brand color: `#B8860B` (gold)
- Sans-serif font, fully responsive
- No external CSS frameworks

## Deployment options
- **Option A:** Standalone HTML file — open in browser or upload to any web host
- **Option B:** WordPress plugin — folder `xclusivox-crm` with `xclusivox-crm.php` (plugin header + iframe) and `dashboard.html`
- **Option C:** Any PHP/HTML host — upload HTML file directly

## Requirements
- Free Apify account (apify.com) — free tier ~$5/month credits, enough for daily discovery runs
- Anthropic API key (for AI pitches and compare reports)

**Why:** User wants to build this but is saving it for a later session.
**How to apply:** When user says "let's work on Who's Hot", load this spec and start building the HTML file.
