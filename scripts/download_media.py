import json, os, sys, time, urllib.request
ROOT = sys.argv[1]
def get(url):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "jamie-poap-archive/1.0"}), timeout=120)
            return r.read(), r.headers.get("content-type", "")
        except Exception as e: err = e; time.sleep(2 ** i)
    raise err
EXT = {"image/png": "png", "image/gif": "gif", "image/jpeg": "jpg", "image/webp": "webp", "image/svg+xml": "svg", "video/mp4": "mp4"}
def fetch(url, dest_noext, log):
    if not url: return
    try:
        b, ct = get(url); ext = EXT.get(ct.split(";")[0], url.rsplit(".", 1)[-1][:4])
        open(f"{dest_noext}.{ext}", "wb").write(b); log.append({"url": url, "file": os.path.relpath(f"{dest_noext}.{ext}", ROOT), "bytes": len(b)})
    except Exception as e: log.append({"url": url, "error": str(e)}); print("fail", url, e)
log = []
os.makedirs(f"{ROOT}/created-drops/artwork", exist_ok=True)
for d in json.load(open(f"{ROOT}/compass/created_drops.json")):
    fetch(d.get("image_url"), f"{ROOT}/created-drops/artwork/{d['id']}", log)
    if d.get("animation_url"): fetch(d["animation_url"], f"{ROOT}/created-drops/artwork/{d['id']}-animation", log)
os.makedirs(f"{ROOT}/collections/images", exist_ok=True)
for c in json.load(open(f"{ROOT}/compass/collections.json")):
    fetch(c.get("logo_image_url"), f"{ROOT}/collections/images/{c['id']}-logo", log)
    fetch(c.get("banner_image_url"), f"{ROOT}/collections/images/{c['id']}-banner", log)
# collected drops: original drop artwork too (token metadata images can be resized)
os.makedirs(f"{ROOT}/collection/drop-artwork", exist_ok=True)
for p in json.load(open(f"{ROOT}/compass/collected.json")):
    d = p["drop"]
    if not any(os.path.exists(f"{ROOT}/collection/drop-artwork/{d['id']}.{e}") for e in ("png","gif","jpg","webp","svg")):
        fetch(d.get("image_url"), f"{ROOT}/collection/drop-artwork/{d['id']}", log)
json.dump(log, open(f"{ROOT}/compass/media_log.json", "w"), indent=2)
print(len([l for l in log if "file" in l]), "saved,", len([l for l in log if "error" in l]), "failed")
