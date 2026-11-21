# MediaFusion Poster Repair Engine

Automatic cloud repair engine for MediaFusion Stremio addon posters on Android (Nuvio).

### Why this is needed
MediaFusion stores Amazon CDN poster URLs for older Tamil cinema items (such as *Theri*, *Jana*, *Athiradi*, *Aandavan Kattalai*, etc.). Amazon's CDN returns **HTTP 404** for these expired links. This engine dynamically replaces any expired Amazon poster URLs with verified, high-resolution Metahub posters (`https://images.metahub.space/poster/medium/{tt_id}/img`).

---

## ⚡ 1-Click Deploy Options (100% Free, 24/7 Cloud)

### Option 1: Cloudflare Workers (Recommended - Instant & Free)
1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/) ➔ **Workers & Pages** ➔ **Create Application** ➔ **Create Worker**.
2. Click **Deploy**.
3. Click **Edit Code**, paste the contents of [`worker.js`](worker.js), and click **Deploy**.
4. Copy your Worker URL: `https://<your-worker-name>.workers.dev/manifest.json`.
5. Install that URL into Nuvio!

### Option 2: Vercel (1-Click GitHub Import)
1. Go to [vercel.com](https://vercel.com/new).
2. Select and import repository `Maady012/mediafusion-poster-repair`.
3. Click **Deploy**.
4. Copy your Vercel URL: `https://<project-name>.vercel.app/manifest.json`.
5. Install that URL into Nuvio!
