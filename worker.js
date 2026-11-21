const UPSTREAM = "https://mediafusion.elfhosted.com/D-MfHFaq-W9IClcKI3Y8XoyFx9Ar2RSoDElE538VOoC82NRQvsxObGyUGys3RdaEscex--BLaz7E1SqK7HNe8bD_7WGgEFgUTHduEosulJlMHJL7iOYYKyTX5BxTFysVyckB87lFxPT6Mx7dMv-xps1MU5Ih7MO6fqYV9fhrGJXU3xOxa2fNVtFBcwtpVkmOjzs6mxKFAFt7UMMPhP3e79LFTaoAw_36PGAVDW30OPlPN00yNXZbaBrgHRIsr66cKo";

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const targetUrl = UPSTREAM + url.pathname + url.search;

    const resp = await fetch(targetUrl, {
      headers: { "User-Agent": "Mozilla/5.0" }
    });

    if (url.pathname.includes("/catalog/") && url.pathname.endsWith(".json")) {
      const data = await resp.json();
      if (data && data.metas) {
        for (const item of data.metas) {
          const poster = item.poster || "";
          const id = item.id || "";
          if ((poster.includes("m.media-amazon.com") || !poster) && id.startsWith("tt")) {
            item.poster = `https://images.metahub.space/poster/medium/${id}/img`;
          }
        }
      }
      return new Response(JSON.stringify(data), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }

    if (url.pathname === "/manifest.json") {
      const manifest = await resp.json();
      manifest.name = "MediaFusion (Tamil HD Repaired)";
      return new Response(JSON.stringify(manifest), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }

    return resp;
  }
};
