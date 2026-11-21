from http.server import BaseHTTPRequestHandler
import urllib.request
import json

UPSTREAM = "https://mediafusion.elfhosted.com/D-MfHFaq-W9IClcKI3Y8XoyFx9Ar2RSoDElE538VOoC82NRQvsxObGyUGys3RdaEscex--BLaz7E1SqK7HNe8bD_7WGgEFgUTHduEosulJlMHJL7iOYYKyTX5BxTFysVyckB87lFxPT6Mx7dMv-xps1MU5Ih7MO6fqYV9fhrGJXU3xOxa2fNVtFBcwtpVkmOjzs6mxKFAFt7UMMPhP3e79LFTaoAw_36PGAVDW30OPlPN00yNXZbaBrgHRIsr66cKo"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = UPSTREAM + self.path
        try:
            req = urllib.request.Request(target_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()

            if "/catalog/" in self.path and self.path.endswith(".json"):
                try:
                    catalog_data = json.loads(data.decode("utf-8"))
                    metas = catalog_data.get("metas", [])
                    for m in metas:
                        poster = m.get("poster", "")
                        mid = m.get("id", "")
                        if ("m.media-amazon.com" in poster or not poster) and mid.startswith("tt"):
                            m["poster"] = f"https://images.metahub.space/poster/medium/{mid}/img"
                    data = json.dumps(catalog_data).encode("utf-8")
                except Exception:
                    pass
            elif self.path == "/manifest.json":
                try:
                    manifest = json.loads(data.decode("utf-8"))
                    manifest["name"] = "MediaFusion (Tamil HD Repaired)"
                    data = json.dumps(manifest).encode("utf-8")
                except Exception:
                    pass

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode("utf-8"))
