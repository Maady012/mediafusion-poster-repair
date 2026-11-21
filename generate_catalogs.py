import urllib.request, json, os

UPSTREAM = "https://mediafusion.elfhosted.com/D-MfHFaq-W9IClcKI3Y8XoyFx9Ar2RSoDElE538VOoC82NRQvsxObGyUGys3RdaEscex--BLaz7E1SqK7HNe8bD_7WGgEFgUTHduEosulJlMHJL7iOYYKyTX5BxTFysVyckB87lFxPT6Mx7dMv-xps1MU5Ih7MO6fqYV9fhrGJXU3xOxa2fNVtFBcwtpVkmOjzs6mxKFAFt7UMMPhP3e79LFTaoAw_36PGAVDW30OPlPN00yNXZbaBrgHRIsr66cKo"

# 1. Fetch manifest
req = urllib.request.Request(f"{UPSTREAM}/manifest.json", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    manifest = json.loads(resp.read().decode("utf-8"))

manifest["id"] = "org.mediafusion.tamil.repaired"
manifest["name"] = "MediaFusion (Tamil HD Repaired)"
manifest["description"] = "MediaFusion Tamil & English catalogs with 100% repaired Metahub poster artwork"
manifest["resources"] = ["catalog"]

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("Manifest written")

# 2. Fetch all catalogs and patch posters
for cat in manifest.get("catalogs", []):
    ctype = cat["type"]
    cid = cat["id"]
    os.makedirs(f"catalog/{ctype}", exist_ok=True)
    cat_url = f"{UPSTREAM}/catalog/{ctype}/{cid}.json"
    print(f"Fetching {ctype}/{cid}...")
    try:
        r = urllib.request.Request(cat_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(r, timeout=20) as res:
            cat_data = json.loads(res.read().decode("utf-8"))
            metas = cat_data.get("metas", [])
            count = 0
            for item in metas:
                poster = item.get("poster", "")
                tt_id = item.get("id", "")
                if ("media-amazon.com" in poster or not poster) and tt_id.startswith("tt"):
                    item["poster"] = f"https://images.metahub.space/poster/medium/{tt_id}/img"
                    count += 1
            print(f"  Repaired {count}/{len(metas)} in {cid}")
            with open(f"catalog/{ctype}/{cid}.json", "w") as f:
                json.dump(cat_data, f)
    except Exception as e:
        print(f"  Error on {cid}: {e}")

