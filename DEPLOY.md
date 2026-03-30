# Deploy AI Studio — Cloudflare Pages + Access

One-time setup. Takes about 20 minutes.
After this: open your URL, click Launch Pod, click Open Studio. Done.

---

## Part 1 — Push to GitHub

```bash
cd ~/ai-studio
git init
git add .
git commit -m "initial"
```

Create a new **private** repo at github.com (click New → set Private), then:

```bash
git remote add origin https://github.com/YOUR_USER/ai-studio.git
git push -u origin main
```

---

## Part 2 — Deploy to Cloudflare Pages

1. Go to **dash.cloudflare.com** → sign up free if needed
2. Click **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
3. Authorize GitHub, select your `ai-studio` repo
4. Set build settings:
   - **Framework preset:** None
   - **Build command:** *(leave blank)*
   - **Build output directory:** `frontend`
5. Click **Save and Deploy**

Cloudflare gives you a URL like `ai-studio-abc.pages.dev` — that's your permanent control panel address.

> The `frontend/functions/api/runpod.js` file is automatically picked up as a serverless function — no extra config needed. It handles the RunPod API proxy.

---

## Part 3 — Lock it down with Cloudflare Access

This makes your site invisible to everyone except you.

1. In Cloudflare dashboard → **Zero Trust** (left sidebar)
   - Free plan is fine — click Start Free if prompted
2. **Access** → **Applications** → **Add an Application**
3. Choose **Self-hosted**
4. Fill in:
   - **Application name:** `AI Studio`
   - **Subdomain:** `ai-studio-abc` (match your Pages URL)
   - **Domain:** `pages.dev`
5. Click Next → **Add a policy**:
   - **Policy name:** `Owner only`
   - **Action:** Allow
   - **Include rule:** `Emails` → enter your email address
6. Click Next → Save

Now when you visit your Pages URL, Cloudflare shows a login screen. You click "Send me a code", get a one-time code in your email, enter it — and you're in. It remembers you for weeks.

Nobody else can even see the page exists.

---

## Part 4 — Configure the site

1. Visit your Pages URL (log in via email OTP)
2. The settings modal opens automatically on first visit
3. Fill in:
   - **RunPod API Key** — from runpod.io → Settings → API Keys
   - **Template ID** — from runpod/SETUP.md Part 2
   - **Volume ID** — from runpod/SETUP.md Part 3
   - **GPU Type** — e.g. `NVIDIA A40`
4. Save

---

## Every day after this

| What you want | What you do |
|---|---|
| Start a session | Open your Pages URL → ▶ Launch Pod |
| Use the studio | Wait ~60s → ↗ Open Studio (auto-opens) |
| End a session | Go back to Pages URL → ■ Stop Pod |
| Add money | Go to runpod.io → Billing |

That's it. You never need to touch RunPod's dashboard again.

---

## Deploying updates

Whenever you change code locally:

```bash
git add -A && git commit -m "update" && git push
```

Cloudflare auto-redeploys in ~30 seconds.
