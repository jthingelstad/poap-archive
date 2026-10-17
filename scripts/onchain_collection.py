import json, os, sys, time, urllib.request, urllib.parse
OUT = sys.argv[1]
ADDRS = sys.argv[2:]
POAP = "0x22c1f6050e56d2876009903609a2cc3fef83b415"
def get(url, raw=False):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "jamie-poap-archive/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                b = r.read(); return (b, r.headers.get("content-type","")) if raw else json.loads(b)
        except Exception as e:
            err = e; time.sleep(2 ** i)
    raise err
os.makedirs(f"{OUT}/metadata", exist_ok=True); os.makedirs(f"{OUT}/artwork", exist_ok=True)
index = []
for addr in ADDRS:
    params = {"type": "ERC-721"}
    while True:
        d = get(f"https://gnosis.blockscout.com/api/v2/addresses/{addr}/nft?" + urllib.parse.urlencode(params))
        for it in d["items"]:
            if it["token"]["address_hash"].lower() != POAP: continue
            tid = it["id"]; md = it.get("metadata") or {}
            url = md.get("external_url") or ""
            try:
                if "api.poap.tech/metadata" in url: md = get(url)
            except Exception as e: print("metadata fail", tid, e)
            json.dump({"chain_item": it, "metadata": md}, open(f"{OUT}/metadata/{tid}.json", "w"), indent=2)
            img = md.get("image_url") or it.get("image_url"); fn = None
            if img:
                try:
                    b, ct = get(img, raw=True)
                    ext = {"image/png":"png","image/gif":"gif","image/jpeg":"jpg","image/webp":"webp"}.get(ct.split(";")[0], "bin")
                    fn = f"artwork/{tid}.{ext}"; open(f"{OUT}/{fn}", "wb").write(b)
                except Exception as e: print("image fail", tid, e)
            attrs = {a.get("trait_type"): a.get("value") for a in md.get("attributes", []) if isinstance(a, dict)}
            index.append({"token_id": tid, "owner": addr, "name": md.get("name"), "event_id": url.split("/metadata/")[-1].split("/")[0] if "/metadata/" in url else None,
                          "date": attrs.get("startDate") or attrs.get("start_date"), "city": attrs.get("city"), "country": attrs.get("country"),
                          "event_url": attrs.get("eventURL") or attrs.get("event_url"), "image": fn, "image_url": img})
        if not d.get("next_page_params"): break
        params = {"type": "ERC-721", **{k: v for k, v in d["next_page_params"].items()}}
    print(addr, "done, running total", len(index))
json.dump(index, open(f"{OUT}/collection.json", "w"), indent=2)
