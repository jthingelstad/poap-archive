"""Network side of the time capsule: who collected Jamie's drops, their ENS names, which of
Jamie's collected events they also attended, and supply for every drop in play.

Writes network/*.json. Run: python3 -I scripts/network_harvest.py
"""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compass_harvest_lib import q, paged

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "network"); os.makedirs(OUT, exist_ok=True)
load = lambda p: json.load(open(os.path.join(ROOT, p)))
JAMIE = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29", "0xb81b70afee42e944b88d06a71e0531852c612056",
         "0x2bda946a7740b1ddb0fd5c226819170c4dd15720", "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf"}

def save(name, data):
    json.dump(data, open(f"{OUT}/{name}.json", "w"), indent=2); print(name, len(data))

created_tokens = load("compass/created_drop_tokens.json")
collected = load("compass/collected.json")
created_ids = sorted({t["drop_id"] for t in created_tokens} | {d["id"] for d in load("compass/created_drops.json")})
collected_ids = sorted({p["drop_id"] for p in collected})
people = sorted({t["collector_address"].lower() for t in created_tokens} - JAMIE)

# 1. supply per chain for every drop Jamie made or collected
ids = sorted(set(created_ids) | set(collected_ids))
stats = []
for i in range(0, len(ids), 100):
    stats += q('query($d:[bigint!]){ drops_stats_by_chain(where:{drop_id:{_in:$d}}){ drop_id chain poap_count transfer_count } }', {"d": ids[i:i+100]})["drops_stats_by_chain"]
save("drop_supply", stats)

# 2. which of Jamie's collected events the people in Jamie's network also hold
co = []
for i in range(0, len(people), 50):
    co += paged("poaps", {"collector_address": {"_in": people[i:i+50]}, "drop_id": {"_in": collected_ids}}, "id drop_id collector_address chain minted_on")
save("co_attendance", co)

# 3. each person's overall collection size
sizes = []
for i in range(0, len(people), 100):
    sizes += q('query($a:[String!]){ collectors_stats_by_chain(where:{address:{_in:$a}}){ address chain poaps_owned } }', {"a": people[i:i+100]})["collectors_stats_by_chain"]
save("collector_sizes", sizes)

# 4. ENS names (reverse records) via ensdata.net, cached so re-runs are cheap
cache_p = f"{OUT}/ens.json"
ens = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
for n, a in enumerate(people + sorted(JAMIE)):
    if a in ens: continue
    try:
        r = urllib.request.urlopen(urllib.request.Request(f"https://api.ensdata.net/{a}", headers={"User-Agent": "jamie-poap-archive/1.0"}), timeout=30)
        d = json.loads(r.read()); ens[a] = {k: d.get(k) for k in ("ens_primary", "avatar_small", "url", "twitter", "github")}
    except urllib.error.HTTPError as e:
        ens[a] = {"ens_primary": None} if e.code == 404 else ens.get(a)
        if e.code == 429: time.sleep(10)
    except Exception: pass
    if n % 50 == 0: json.dump(ens, open(cache_p, "w"), indent=1); print("ens", n, "/", len(people))
    time.sleep(0.25)
ens = {k: v for k, v in ens.items() if v is not None}
save("ens", ens)
