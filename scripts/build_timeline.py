"""Merge every dated thing in the archive into timeline/events.json, one row per event.

Sides: "collector" (tokens Jamie minted or received), "issuer" (drops Jamie made, mints
of them, moments on them), "writer" (posts and Weekly Thing items, from writing/timeline.json
when present). Run: python3 -I scripts/build_timeline.py
"""
import collections, datetime, glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load = lambda p: json.load(open(os.path.join(ROOT, p)))
JAMIE = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29", "0xb81b70afee42e944b88d06a71e0531852c612056",
         "0x2bda946a7740b1ddb0fd5c226819170c4dd15720", "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf"}


def iso(ts):
    """Any timestamp in the sources -> UTC ISO 8601, so string order is time order."""
    if ts is None: return None
    if isinstance(ts, (int, float)): return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).isoformat()
    d = datetime.datetime.fromisoformat(ts if "T" in ts or " " in ts else ts + "T00:00:00")
    if d.tzinfo is None: d = d.replace(tzinfo=datetime.timezone.utc)
    return d.astimezone(datetime.timezone.utc).isoformat()


def art(folder, drop_id):
    hits = glob.glob(os.path.join(ROOT, folder, f"{drop_id}.*"))
    return os.path.relpath(hits[0], ROOT) if hits else None


def drop_info(d):
    return {"drop_id": d["id"], "drop_name": d["name"], "drop_start": d.get("start_date"), "city": d.get("city") or None,
            "country": d.get("country") or None, "virtual": d.get("virtual")}


events = []
collected = load("compass/collected.json")
for p in collected:
    events.append({"date": iso(p["minted_on"]), "side": "collector", "kind": "collected", "token_id": p["id"], "chain": p["chain"],
                   **drop_info(p["drop"]), "artwork": art("collection/drop-artwork", p["drop_id"])})

created = load("compass/created_drops.json")
tokens = load("compass/created_drop_tokens.json")
by_drop = collections.defaultdict(list)
for t in tokens: by_drop[t["drop_id"]].append(t)
for d in created:
    mints = sorted(t["minted_on"] for t in by_drop[d["id"]] if t["minted_on"])
    events.append({"date": iso(d.get("created_date")), "side": "issuer", "kind": "drop_created", **drop_info(d),
                   "minted": len(by_drop[d["id"]]), "collectors": len({t["collector_address"] for t in by_drop[d["id"]]}),
                   "first_mint": iso(mints[0]) if mints else None, "last_mint": iso(mints[-1]) if mints else None,
                   "artwork": art("created-drops/artwork", d["id"])})
for t in tokens:
    if t["collector_address"].lower() in JAMIE: continue
    events.append({"date": iso(t["minted_on"]), "side": "issuer", "kind": "minted_by_other", "token_id": t["id"],
                   "drop_id": t["drop_id"], "collector": t["collector_address"].lower(), "chain": t["chain"]})

drop_names = {d["id"]: d["name"] for d in created} | {p["drop_id"]: p["drop"]["name"] for p in collected}
for m in load("compass/moments.json"):
    events.append({"date": iso(m["created_on"]), "side": "issuer" if m["drop_id"] in {d["id"] for d in created} else "collector",
                   "kind": "moment", "moment_id": m["id"], "drop_id": m["drop_id"], "drop_name": drop_names.get(m["drop_id"]),
                   "author": (m["author"] or "").lower(), "by_jamie": (m["author"] or "").lower() in JAMIE,
                   "description": m.get("description"), "media_count": len(m.get("media") or [])})

for t in load("compass/transfers.json"):
    if t["from_address"] == "0x0000000000000000000000000000000000000000": continue  # mints are covered above
    events.append({"date": iso(t["timestamp"]), "side": "collector", "kind": "transfer", "token_id": t["poap_id"],
                   "drop_id": (t.get("poap") or {}).get("drop_id"), "drop_name": ((t.get("poap") or {}).get("drop") or {}).get("name"),
                   "from": t["from_address"], "to": t["to_address"], "chain": t["chain"], "tx": t["tx_hash"]})

writing_p = os.path.join(ROOT, "writing/timeline.json")
if os.path.exists(writing_p):
    for w in json.load(open(writing_p))["rows"]:
        events.append({**w, "date": iso(w["date"]), "side": "writer"})

events = [e for e in events if e["date"]]
events.sort(key=lambda e: e["date"])
os.makedirs(os.path.join(ROOT, "timeline"), exist_ok=True)
json.dump(events, open(os.path.join(ROOT, "timeline/events.json"), "w"), indent=1)

summary = collections.defaultdict(collections.Counter)
for e in events: summary[e["date"][:4]][e["kind"]] += 1
json.dump({y: dict(c) for y, c in sorted(summary.items())}, open(os.path.join(ROOT, "timeline/by_year.json"), "w"), indent=2)
print(len(events), "events")
for y, c in sorted(summary.items()): print(y, dict(c))
