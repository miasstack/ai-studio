---
name: Sodatone / Artist Radar project
description: A&R talent discovery tool tracking emerging artists across platforms — located at /Users/damoneden/artist-radar
type: project
originSessionId: 8c50781d-f6d7-42b6-9751-925a7e00a607
---
A Sodatone lookalike A&R discovery tool that finds unsigned artists blowing up across streaming and social platforms.

**Why:** Help find talent before labels do — track growth velocity across TikTok, Spotify, YouTube, Instagram, SoundCloud, Last.fm.

**How to apply:** Work inside `/Users/damoneden/artist-radar/`. SQLite DB at `radar.db`. All keys in `config.py` (no .env).

## What's already built (April 2026)
- `spotify_collector.py` — new releases, follower snapshots, major label filter
- `youtube_collector.py` — channel growth, video velocity alerts
- `tiktok_scraper.py` — basic scraper (trending sounds, artist search via public endpoints)
- `chartmetric_collector.py` — trending artists via Chartmetric API (email/password auth)
- `label_filter.py` — comprehensive major label blocklist (UMG, Sony, Warner + all subs)
- `database.py` — SQLite schema: artists, spotify_snapshots, youtube_snapshots, tiktok_snapshots, alerts
- `report.py` — CLI daily report
- `run.py` — scheduler (runs every 6 hrs, --watch mode)

## API keys already configured (in config.py)
- Spotify: client_id=da7e584536be4df0b5dfcc816e5d4c79
- YouTube: AIzaSyDaQi997g7EcIy6_ETM-0CoZmJnl675Aq0
- Chartmetric: email/password auth (ecmg.corp@gmail.com)

## What's missing (to reach Sodatone parity)
1. **Web dashboard UI** — Flask/FastAPI + HTML with artist cards ranked by momentum
2. **Momentum score** — cross-platform weighted velocity score per artist
3. **Cross-platform identity** — link same artist across Spotify/YouTube/TikTok
4. **Last.fm collector** — listener counts, scrobble trends (free API)
5. **SoundCloud collector** — plays, followers for indie/underground
6. **Instagram** — follower growth (requires Meta business account)
7. **Better TikTok** — existing scraper may break; consider pyktok or official Research API

## Free APIs available to add
- Last.fm: free API key, `/artist.getInfo` → listeners + play counts
- SoundCloud: mostly deprecated official API but client_id can be extracted
- Deezer: no auth needed, `/search` + `/artist/{id}`
- MusicBrainz: no auth, comprehensive artist metadata
- Shazam: unofficial reverse-engineered endpoints for chart data
- Reddit: OAuth free tier for music community monitoring
