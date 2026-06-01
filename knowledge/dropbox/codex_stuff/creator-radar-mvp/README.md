# Creator Radar MVP

A TikTok-first MVP for finding creators and trends while they are still building.

This app is intentionally lean:

- search a niche or keyword
- pull TikTok-like results from a provider layer
- rank creators by a simple momentum score
- store searches locally in SQLite
- render the workflow in a local browser

## Why this exists

You do not need enterprise influencer SaaS pricing to prove the workflow.

This MVP is designed to work in 3 modes:

1. `sample` mode: zero setup, useful for UI and scoring validation
2. `apify` mode: live TikTok scraping through Apify actors
3. `auto` mode: use Apify if configured, otherwise fall back to sample data

## Files

- `server.py`: local HTTP server + API routes
- `services.py`: provider layer, scoring, persistence, parsing
- `fixtures/sample_results.json`: sample dataset for instant testing
- `web/`: static frontend

## Quick start

```bash
cd "/Users/damoneden/Documents/codex stuff/creator-radar-mvp"
python3 server.py
```

Then open:

`http://localhost:8080`

## Environment variables

Optional:

```bash
export DATA_SOURCE=auto
export APIFY_TOKEN=your_token_here
export APIFY_ACTOR_ID=clockworks/tiktok-scraper
export APIFY_RESULTS_PER_QUERY=30
```

Notes:

- `DATA_SOURCE=sample` uses the included fixture data
- `DATA_SOURCE=apify` requires `APIFY_TOKEN`
- `DATA_SOURCE=auto` uses Apify when configured, otherwise sample mode

## Apify actor recommendation

This MVP defaults to `clockworks/tiktok-scraper` because it supports:

- keyword search
- hashtag search
- profile scraping

It is configured conservatively to keep usage low.

## Gentle scraping strategy

The app intentionally does not try to brute-force TikTok.

Default behavior:

- one query at a time
- low result counts
- keyword + hashtag blending
- no comments scraping
- no media downloads
- no aggressive fanout

## What the scoring does

Each creator gets a momentum score from:

- video views
- engagement rate
- recency
- repeat appearance across the niche search

This is not meant to be academically perfect.
It is meant to be directionally useful for an MVP.

## Current limitations

- live mode depends on the selected Apify actor still working
- TikTok fields vary by actor, so some metrics may be missing
- trend scoring is heuristic, not production-calibrated
- no LLM layer yet

## Next steps

After this works end-to-end, the next high-value additions are:

1. LLM summaries of why each creator is popping
2. saved lists / bookmarks
3. repeated searches over time
4. niche expansion from the user query
5. a direct local scraper fallback if you want to try `TikTokApi` later
