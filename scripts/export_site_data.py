"""Export the site data contract (DESIGN.md section 2) for poap.thingelstad.xyz.

Reads the captures in this archive and writes JSON only, into the directory given as the
first argument (default: export/). The site repository commits that directory as data/ and
reads nothing else from the archive. Artwork is not copied here; artwork.json lists every
source file with its hash and size so the site's media tool can publish it once.

Run: python3 -I scripts/export_site_data.py [/path/to/site/data]
"""
import collections, datetime, glob, hashlib, json, math, os, re, subprocess, sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "export")
load = lambda p: json.load(open(os.path.join(ROOT, p)))
JAMIE = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29", "0xb81b70afee42e944b88d06a71e0531852c612056",
         "0x2bda946a7740b1ddb0fd5c226819170c4dd15720", "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf"}
ZERO = "0x0000000000000000000000000000000000000000"
WALLETS = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29": "poap.thingelstad.eth",
           "0xb81b70afee42e944b88d06a71e0531852c612056": "thingelstad.onpoap.eth",
           "0x2bda946a7740b1ddb0fd5c226819170c4dd15720": "thingelstad.eth",
           "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf": "ens.thingelstad.eth"}

SERIES = [  # slug, label, color, name tests. Order is display order.
    ("612", "612 POAP Challenge", "#c23b22", ["612 POAP Challenge"]),
    ("birthday", "Jamie's birthdays", "#7b3fa0", ["Jamie Thingelstad's 5"]),
    ("weekly", "Weekly Thing", "#2a6f97", ["Weekly Thing", "Reading Things"]),
    ("family", "Family", "#2e8b57", ["Olson Family", "Magic Pines", "Thingelstad Valentines", "Cabin Christmas", "Thingelstad Ireland",
                                     "My mom", "Ice Fishing", "Lake Geneva", "First Computer Build", "Rosalin Chrest", "Father Son"]),
    ("sps", "SPS and TeamSPS", "#d9822b", ["SPS", "TeamSPS", "Women in Tech"]),
    ("minnebar", "Minnebar", "#138d75", ["Minnebar"]),
    ("t4g", "Things 4 Good", "#b8860b", ["Things 4 Good"]),
    ("met", "You've met Jamie", "#6c7a89", ["met thingelstad", "met poap.thingelstad", "met Jamie"]),
    ("community", "Community and crypto", "#8d6e63", []),
]

WORLD = [  # POAP the company, from research/poap-company.md
    ("2019-02-15", "POAP begins at ETHDenver 2019: about 100 ERC-721 badges for hackathon attendees."),
    ("2022-01-19", "POAP Inc. announces a $10M seed round co-led by Archetype and Sapphire Sport."),
    ("2023-04-17", "Paid issuance begins for commercial issuers, at about $1 per POAP. Personal use stays free."),
    ("2026-01-01", "The POAP Airport Rally 2026 begins: GPS-minted POAPs at more than 100 airports."),
    ("2026-03-16", "POAP enters maintenance mode. No new issuers, no active development."),
    ("2026-07-31", "The last POAP drop is created, #229257."),
    ("2026-08-03", "Isabel Gonzalez announces that POAP is winding down after five years."),
    ("2026-08-20", "poaparchive.com takes its final snapshot: 73,990 drops, 6,218,154 tokens."),
    ("2026-10-17", "This archive is captured."),
]


def iso(ts):
    if ts is None: return None
    if isinstance(ts, (int, float)): return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).isoformat()
    d = datetime.datetime.fromisoformat(ts if "T" in ts or " " in ts else ts + "T00:00:00")
    if d.tzinfo is None: d = d.replace(tzinfo=datetime.timezone.utc)
    return d.astimezone(datetime.timezone.utc).isoformat()


def series_of(name):
    for slug, _, _, tests in SERIES:
        if any(t.lower() in name.lower() for t in tests): return slug
    return "community"


def short(a): return a[:6] + "…" + a[-4:]


# Sources.
created = {d["id"]: d for d in load("compass/created_drops.json")}
collected = load("compass/collected.json")
tokens = load("compass/created_drop_tokens.json")
ens = load("network/ens.json")
events = load("timeline/events.json")
writing = load("writing/timeline.json")["rows"]
mint_posts = load("writing/mint-posts.json")["rows"]
supply = collections.defaultdict(int)
for r in load("network/drop_supply.json"): supply[r["drop_id"]] += r["poap_count"]
sizes = {}
for r in load("network/collector_sizes.json"): sizes[r["address"].lower()] = sizes.get(r["address"].lower(), 0) + r["poaps_owned"]

# Artwork manifest: one source file per drop, from either artwork folder.
artwork = {}
for folder in ("created-drops/artwork", "collection/drop-artwork"):
    for path in sorted(glob.glob(os.path.join(ROOT, folder, "*.*"))):
        drop_id = int(os.path.basename(path).split(".")[0])
        if drop_id in artwork: continue
        data = open(path, "rb").read()
        with Image.open(path) as im:
            width, height = im.size
            animated = getattr(im, "n_frames", 1) > 1
            fmt = im.format.lower()
        ext = {"jpeg": "jpg"}.get(fmt, fmt)
        artwork[drop_id] = {"drop": drop_id, "source": os.path.relpath(path, ROOT), "key": f"art/{drop_id}.{ext}",
                            "mime": Image.MIME[im.format], "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                            "width": width, "height": height, "animated": animated}

# Writing attached to drops and tokens.
posts_by_drop = collections.defaultdict(list)
post_by_token = {}
for w in writing:
    row = {"title": w.get("title") or "", "url": w["url"], "date": iso(w["date"])[:10], "kind": w["kind"]}
    if w["kind"] == "mint":
        for t in w.get("token_ids", []): post_by_token[int(t)] = row
    elif w["kind"] in ("drop-announcement", "announcement", "essay"):
        for d in w.get("drop_ids", []): posts_by_drop[int(d)].append(row)
commentary = {int(r["token_id"]): (r.get("commentary") or "").strip() for r in mint_posts if r.get("token_id")}

# People and mints.
holds = collections.defaultdict(dict)
for t in tokens:
    a = t["collector_address"].lower()
    if a in JAMIE or a == ZERO or not t["minted_on"]: continue
    when = iso(t["minted_on"])
    if t["drop_id"] not in holds[a] or when < holds[a][t["drop_id"]]: holds[a][t["drop_id"]] = when
people = sorted(holds, key=lambda a: (-len(holds[a]), a))
mint_count = collections.Counter(d for a in people for d in holds[a])
collectors_of = collections.defaultdict(list)
for a in people:
    for d, when in holds[a].items(): collectors_of[d].append((when, a))
own_token = {p["drop_id"]: p["id"] for p in collected if p["drop_id"] in created}
bdays = sorted(d for d in created if series_of(created[d]["name"]) == "birthday")
name_of = lambda a: ens.get(a, {}).get("ens_primary") or None

# drops.json
drops = []
for d in sorted(created.values(), key=lambda d: d["start_date"] or ""):
    c = collectors_of[d["id"]]
    drops.append({
        "id": d["id"], "name": d["name"], "slug": d["fancy_id"], "series": series_of(d["name"]),
        "date": (d["start_date"] or "")[:10], "end": (d["end_date"] or "")[:10], "created": iso(d["created_date"]),
        "city": (d.get("city") or "").strip() or None, "country": (d.get("country") or "").strip() or None,
        "virtual": bool(d.get("virtual")), "private": d.get("private") == "true", "description": (d.get("description") or "").strip(),
        "url": d.get("drop_url") or None, "artwork": artwork.get(d["id"], {}).get("key"), "animated": artwork.get(d["id"], {}).get("animated", False),
        "supply": supply.get(d["id"], 0), "mints": mint_count[d["id"]], "collectors": len(c),
        "first_mint": min(c)[0] if c else None, "last_mint": max(c)[0] if c else None,
        "reserved": (d.get("email_claims_stats") or {}).get("reserved", 0),
        "own_token": own_token.get(d["id"]),
        "posts": sorted(posts_by_drop.get(d["id"], []), key=lambda r: r["date"]),
    })

# tokens.json: everything Jamie holds, flagged by whether the drop is Jamie's own.
toks = []
for p in sorted(collected, key=lambda p: iso(p["minted_on"])):
    dr = p["drop"]; a = artwork.get(p["drop_id"], {})
    toks.append({
        "id": p["id"], "minted": iso(p["minted_on"]), "wallet": WALLETS.get(p["collector_address"].lower(), p["collector_address"].lower()),
        "chain": p["chain"], "own_drop": p["drop_id"] in created, "transfers": p.get("transfer_count", 0),
        "drop": {"id": p["drop_id"], "name": dr["name"], "slug": dr.get("fancy_id"), "date": (dr.get("start_date") or "")[:10],
                 "city": (dr.get("city") or "").strip() or None, "country": (dr.get("country") or "").strip() or None,
                 "virtual": bool(dr.get("virtual")), "description": (dr.get("description") or "").strip(), "url": dr.get("drop_url") or None,
                 "artwork": a.get("key"), "animated": a.get("animated", False), "supply": supply.get(p["drop_id"], 0)},
        "post": post_by_token.get(p["id"]), "commentary": commentary.get(p["id"]) or None,
    })

# people.json and mints.json
finish_612 = {a: holds[a][190903] for a in people if 190903 in holds[a]}
ppl = [{"address": a, "ens": name_of(a), "label": name_of(a) or short(a), "avatar": ens.get(a, {}).get("avatar_small"),
        "total": sizes.get(a), "drops": [{"id": d, "minted": w} for d, w in sorted(holds[a].items(), key=lambda x: x[1])],
        "birthdays": sum(1 for d in bdays if d in holds[a]), "finished_612": finish_612.get(a)} for a in people]
mints = [{"person": a, "drop": d, "minted": w} for a in people for d, w in sorted(holds[a].items(), key=lambda x: x[1])]

# events.json: the timeline plus POAP's milestones.
# Mint posts are attached to tokens. POAP Moments are left out of the time capsule
# entirely (Jamie, 2026-10-17: an add-on that was never fully adopted).
evs = [e for e in events if e["kind"] not in ("mint", "moment")]
for date, title in WORLD: evs.append({"date": iso(date), "side": "world", "kind": "milestone", "title": title})
evs.sort(key=lambda e: e["date"])

# writing.json: the writing rows that stand on their own, and the advice table from ESSAYS.md.
advice = []
for line in open(os.path.join(ROOT, "writing/ESSAYS.md")):
    cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
    if len(cells) == 5 and cells[0].isdigit():
        advice.append({"n": int(cells[0]), "suggestion": cells[1], "source": cells[2], "words": cells[3].strip('"'), "shipped": cells[4]})
wr = {"items": [{**w, "date": iso(w["date"])} for w in writing if w["kind"] != "mint"], "advice": advice}

# series.json
ser = [{"slug": s, "label": l, "color": c, "drops": [d["id"] for d in drops if d["series"] == s]} for s, l, c, _ in SERIES]

# layout.json: force-directed positions for the bipartite graph (drops and people).
dorder = [d["id"] for d in drops]
didx = {d: i for i, d in enumerate(dorder)}; pidx = {a: i for i, a in enumerate(people)}
N = len(dorder) + len(people)
pos = np.zeros((N, 2)); rng = np.random.default_rng(612)
for i in range(len(dorder)):
    ang = 2 * math.pi * i / len(dorder); pos[i] = [0.55 * math.cos(ang), 0.55 * math.sin(ang)]
for a in people:
    j = len(dorder) + pidx[a]
    pos[j] = pos[[didx[d] for d in holds[a]]].mean(axis=0) * 1.3 + rng.normal(0, 0.05, 2)
E = np.array([(len(dorder) + pidx[a], didx[d]) for a in people for d in holds[a]])
k = 1.0 / math.sqrt(N)
deg = np.bincount(np.concatenate([E[:, 0], E[:, 1]]), minlength=N).astype(float)
for step in range(400):
    temp = 0.08 * (1 - step / 400) + 0.002
    diff = pos[:, None, :] - pos[None, :, :]
    dist = np.sqrt((diff ** 2).sum(-1)) + 1e-6
    disp = ((diff / dist[..., None]) * (k * k / dist)[..., None]).sum(axis=1)
    ev = pos[E[:, 0]] - pos[E[:, 1]]
    el = np.sqrt((ev ** 2).sum(-1)) + 1e-6
    att = ev / el[:, None] * (el * el / k)[:, None]
    np.add.at(disp, E[:, 0], -att); np.add.at(disp, E[:, 1], att)
    disp -= pos * 0.6 * (1 + np.log1p(deg))[:, None]
    ln = np.sqrt((disp ** 2).sum(-1)) + 1e-6
    pos += disp / ln[:, None] * np.minimum(ln, temp)[:, None]
pos -= pos.mean(axis=0); pos /= np.abs(pos).max() * 1.08
xy = (pos * 500 + 500).round(1)
layout = {"size": 1000, "drops": {d: [float(xy[i, 0]), float(xy[i, 1])] for d, i in didx.items()},
          "people": {a: [float(xy[len(dorder) + i, 0]), float(xy[len(dorder) + i, 1])] for a, i in pidx.items()}}

# Metadata.
try: commit = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
except Exception: commit = None
meta = {"archive": "jthingelstad/poap-archive", "commit": commit, "exported": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "captured": "2026-10-17", "wallets": WALLETS,
        "counts": {"drops": len(drops), "tokens": len(toks), "tokens_from_others": sum(1 for t in toks if not t["own_drop"]),
                   "people": len(ppl), "mints": len(mints), "events": len(evs), "writing": len(wr["items"]), "advice": len(advice),
                   "artwork": len(artwork)}}

os.makedirs(OUT, exist_ok=True)
for name, data in [("drops", drops), ("tokens", toks), ("people", ppl), ("mints", mints), ("events", evs), ("writing", wr),
                   ("series", ser), ("layout", layout), ("artwork", sorted(artwork.values(), key=lambda a: a["drop"])),
                   ("export", meta)]:
    with open(os.path.join(OUT, f"{name}.json"), "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False); f.write("\n")
print(json.dumps(meta["counts"]), "->", OUT)
