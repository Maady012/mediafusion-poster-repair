# MediaFusion Poster Repair Engine

Lightweight, zero-cost edge proxy that fixes broken 404 Amazon posters in MediaFusion South Indian / Tamil catalogs by routing poster metadata to Stremio's high-speed Metahub CDN (`images.metahub.space`).

## Deploy with Cloudflare Workers (1 Minute)
1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) -> **Workers & Pages** -> **Create Worker**.
2. Copy and paste the contents of `worker.js`.
3. Click **Deploy**.
4. Install `stremio://<your-worker-url>/manifest.json` into Nuvio or Stremio.

## Deploy with Vercel
1. Import this repository into Vercel.
2. Vercel automatically detects `vercel.json` and `api/index.py`.
3. Click **Deploy**.
