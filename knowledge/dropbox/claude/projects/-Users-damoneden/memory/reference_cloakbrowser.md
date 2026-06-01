---
name: reference-cloakbrowser
description: CloakBrowser installed — stealth Chromium drop-in Playwright replacement for bypassing bot detection
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6e245e70-9253-40f4-828f-c6d1369fa16c
---

CloakBrowser is installed and ready to use (Python `cloakbrowser` v0.3.29, npm `cloakbrowser` global).

**What it is:** Stealth Chromium with 49 C++ source-level patches. Passes Cloudflare Turnstile, reCAPTCHA v3 (0.9 score), FingerprintJS. Drop-in Playwright replacement.

**Binary:** Auto-downloads ~200MB to `~/.cloakbrowser` on first run. macOS Gatekeeper fix if needed: `xattr -cr ~/.cloakbrowser/chromium-*/Chromium.app`

**Python quick start:**
```python
from cloakbrowser import launch
browser = launch(humanize=True, proxy="http://user:pass@host:8080", geoip=True)
page = browser.new_page()
page.goto("https://protected-site.com")
browser.close()
```

**Persistent profile (survives incognito detection):**
```python
from cloakbrowser import launch_persistent_context
ctx = launch_persistent_context("./profile", humanize=True)
```

**Async:**
```python
from cloakbrowser import launch_async
browser = await launch_async(humanize=True)
```

**JS:**
```javascript
import { launch } from 'cloakbrowser';
const browser = await launch({ humanize: true });
```

**Key options:** `humanize=True`, `proxy="http://..."`, `geoip=True` (needs `pip install cloakbrowser[geoip]`), `args=["--fingerprint=42069"]` (pin seed), `headless=False`

**Best production config:**
```python
browser = launch(proxy="http://residential-proxy:port", geoip=True, headless=False, humanize=True)
```

**Use cases:** Scraping TikTok/IG/Spotify for TradeKraft, bypassing anti-bot for Who's Hot CRM, automating platform interactions for Mia content pipeline.
