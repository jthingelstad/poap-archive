"""Prototype of the time-capsule timeline: capsule/index.html, built from timeline/events.json.

One stream, two sides. Left: what Jamie collected from the world (tokens from drops Jamie
did not make). Right: what Jamie put into the world (the drops Jamie made, each fanning out
to its collectors). Down the middle: Jamie's writing and POAP's own milestones. Year
chapters open with the year's numbers and one of Jamie's sentences.

Privacy: this page uses only Jamie's own tokens, drops and writing. There are no collector
lists or addresses; other people appear as counts, or where Jamie's own titles and
descriptions already name them. Run: python3 -I scripts/build_capsule.py
"""
import collections, html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load = lambda p: json.load(open(os.path.join(ROOT, p)))
OUT = os.path.join(ROOT, "capsule", "index.html")
ESC = html.escape

CHAPTERS = {
    "2021": ("Getting hooked", "I think it is a very fun way to introduce people to some crypto / web3 technologies without having to spend any money.",
             "Weekly Thing 193, 2021-09-04", "https://weekly.thingelstad.com/archive/193/"),
    "2022": ("A company, a Merge, and the first traditions", "Photos stop time. Geo coordinates stop motion. POAPs are a time capsule of something of note.",
             "My Introduction to the POAP Community, 2022-06-04", "https://www.thingelstad.com/2022/06/04/my-introduction-to.html"),
    "2023": ("Telling POAP what to build", "I have personally introduced well over 100 people to crypto by giving out POAP tokens for various events.",
             "POAP Wishlist, 2023-01-14", "https://www.thingelstad.com/2023/01/14/poap-wishlist.html"),
    "2024": ("POAP ships the wishlist", "I gave it a try myself and I was excited to see that they had addressed everything I had wished for in this process!",
             "New POAP Onboarding Process, 2024-01-14", "https://www.thingelstad.com/2024/01/14/new-poap-onboarding.html"),
    "2025": ("Building on POAP", "I love that I was able to create an entire activity on the POAP platform.",
             "612 POAP Challenge: Collect them all!, 2025-05-31", "https://www.thingelstad.com/2025/05/31/poap-challenge-collect-them-now.html"),
    "2026": ("The last rally", "It is exactly the kind of project that can bring people into POAPs and have fun.",
             "Weekly Thing 342, 2026-03-08", "https://weekly.thingelstad.com/archive/342/"),
}

# POAP the company, from research/poap-company.md. Dates are the ones that document gives.
WORLD = [
    ("2022-01-19", "POAP Inc. announces a $10M seed round co-led by Archetype and Sapphire Sport."),
    ("2023-04-17", "Paid issuance begins for commercial issuers, at about $1 per POAP. Personal use stays free."),
    ("2026-01-01", "The POAP Airport Rally 2026 begins: GPS-minted POAPs at more than 100 airports."),
    ("2026-03-16", "POAP enters maintenance mode. No new issuers, no active development."),
    ("2026-07-31", "The last POAP drop is created, #229257. Jamie's working sunset date."),
    ("2026-08-03", "Isabel Gonzalez announces that POAP is winding down after five years."),
    ("2026-08-20", "poaparchive.com takes its final snapshot: 73,990 drops, 6,218,154 tokens."),
    ("2026-10-17", "This archive is captured."),
]

events = load("timeline/events.json")
created = {d["id"]: d for d in load("compass/created_drops.json")}
supply = collections.defaultdict(int)
for r in load("network/drop_supply.json"): supply[r["drop_id"]] += r["poap_count"]

# Writing that belongs on a card rather than in the spine.
mint_posts = {int(t): w for w in events if w["kind"] == "mint" for t in w.get("token_ids", [])}
drop_posts = collections.defaultdict(list)
for w in events:
    if w["kind"] == "drop-announcement":
        for d in w.get("drop_ids", []): drop_posts[int(d)].append(w)
moments = collections.Counter(e["drop_id"] for e in events if e["kind"] == "moment")
people_by_year = collections.defaultdict(set)
for e in events:
    if e["kind"] == "minted_by_other": people_by_year[e["date"][:4]].add(e["collector"])


def thumb(path, alt=""):
    if not path: return '<span class="art none"></span>'
    return f'<img class="art" loading="lazy" src="../{ESC(path)}" alt="{ESC(alt)}">'


def place(e):
    if e.get("virtual"): return "virtual"
    return e.get("city") or ""


def collector_card(e):
    post = mint_posts.get(e["token_id"])
    bits = [place(e)]
    if supply.get(e["drop_id"]): bits.append(f"one of {supply[e['drop_id']]:,}")
    meta = " · ".join(b for b in bits if b)
    link = f' <a class="post" href="{ESC(post["url"])}">post</a>' if post else ""
    return (f'<div class="card collected" data-date="{e["date"][:10]}">{thumb(e["artwork"], e["drop_name"])}'
            f'<div><b>{ESC(e["drop_name"])}</b><span>{e["date"][:10]} · {ESC(meta)}{link}</span></div></div>')


def issuer_card(e):
    d = created[e["drop_id"]]
    span = ""
    if e["first_mint"]:
        span = f'minted {e["first_mint"][:10]}' + (f' to {e["last_mint"][:10]}' if e["last_mint"][:10] != e["first_mint"][:10] else "")
    bits = [place(e), f'<a href="network.html">{e["minted"]} minted by {e["collectors"]} people</a>', span]
    if moments.get(e["drop_id"]): bits.append(f'{moments[e["drop_id"]]} moments')
    links = "".join(f' <a class="post" href="{ESC(w["url"])}">post</a>' for w in drop_posts.get(e["drop_id"], [])[:2])
    desc = (d.get("description") or "").strip()
    if len(desc) > 220: desc = desc[:220].rsplit(" ", 1)[0] + " …"
    desc = ESC(desc)
    return (f'<div class="card issued" id="drop-{e["drop_id"]}" data-date="{e["date"][:10]}">{thumb(e["artwork"], e["drop_name"])}'
            f'<div><b>{ESC(e["drop_name"])}</b><span>{" · ".join(b for b in bits if b)}{links}</span>'
            f'<p>{desc}</p></div></div>')


def group_card(cls, title, items, summary):
    inner = "".join(items)
    return (f'<details class="card group {cls}"><summary><b>{ESC(title)}</b><span>{ESC(summary)}</span></summary>{inner}</details>')


def spine_card(e):
    kind = {"essay": "essay", "weekly-thing": "Weekly Thing", "announcement": "note", "world": "POAP"}[e["kind"]]
    if e["kind"] == "world":
        return f'<div class="spine world"><i>POAP</i><b>{ESC(e["title"])}</b><span>{e["date"][:10]}</span></div>'
    return (f'<div class="spine {e["kind"]}"><i>{kind}</i><a href="{ESC(e["url"])}">{ESC(e["title"])}</a>'
            f'<span>{e["date"][:10]}</span></div>')


# Build the per-year streams.
is_612 = lambda e: "612 POAP Challenge" in (e.get("drop_name") or "")
years = collections.defaultdict(lambda: {"left": [], "spine": [], "right": [], "n": collections.Counter()})
for e in events:
    y = e["date"][:4]; Y = years[y]
    if e["kind"] == "collected" and e["drop_id"] not in created:
        Y["left"].append(e); Y["n"]["collected"] += 1
    elif e["kind"] == "drop_created":
        # Place a drop at its event date so the story reads in human order.
        e = {**e, "date": e["drop_start"] or e["date"]}
        years[e["date"][:4]]["right"].append(e); years[e["date"][:4]]["n"]["issued"] += 1
    elif e["kind"] in ("essay", "weekly-thing", "announcement"):
        Y["spine"].append(e); Y["n"]["writing"] += 1
    elif e["kind"] == "minted_by_other":
        Y["n"]["mints"] += 1
    elif e["kind"] == "transfer" and e["date"][:7] == "2023-02" and e["to"] == "0x111accebf9d70d9c06de2d38f9392522e82ecf29":
        Y["n"]["moved"] += 1
for date, title in WORLD:
    years[date[:4]]["spine"].append({"date": date, "kind": "world", "title": title})
years["2023"]["spine"].append({"date": "2023-02-28", "kind": "announcement", "title": f"Moved {years['2023']['n']['moved']} POAPs into poap.thingelstad.eth, a wallet made just for collecting",
                               "url": "https://www.thingelstad.com/2023/03/04/isolating-crypto-assets.html"})
# Jamie's own collected copies of own drops are the issuer story; count them for the header.
own_collected = sum(1 for e in events if e["kind"] == "collected" and e["drop_id"] in created)

# Render.
totals = {"collected": sum(1 for e in events if e["kind"] == "collected"), "issued": len(created),
          "mints": sum(1 for e in events if e["kind"] == "minted_by_other"),
          "people": len({e["collector"] for e in events if e["kind"] == "minted_by_other"}),
          "writing": sum(1 for e in events if e["side"] == "writer" and e["kind"] != "mint")}

parts = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>A POAP Time Capsule</title>
<style>
:root{{--bg:#f7f5ef;--ink:#1d1b16;--mute:#6b665b;--line:#e3dfd3;--left:#2f6f8f;--right:#b4552d;--spine:#7a6f3e;--card:#fffdf8}}
@media(prefers-color-scheme:dark){{:root{{--bg:#16150f;--ink:#efe9da;--mute:#a39c8c;--line:#2d2a21;--left:#7fb6d3;--right:#e58c5e;--spine:#cbbd7a;--card:#1f1d16}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,system-ui,"Segoe UI",sans-serif}}
a{{color:inherit}}header{{padding:3rem 1rem 1rem;max-width:1180px;margin:0 auto}}h1{{font-size:2.4rem;margin:0 0 .3rem;letter-spacing:-.02em}}
.dek{{color:var(--mute);max-width:52rem;margin:0 0 1rem}}.totals{{display:flex;flex-wrap:wrap;gap:1.4rem;margin:1rem 0}}.totals div{{font-size:.85rem;color:var(--mute)}}.totals b{{display:block;font-size:1.6rem;color:var(--ink)}}
nav{{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:2}}nav div{{max-width:1180px;margin:0 auto;padding:.5rem 1rem;display:flex;gap:1rem;align-items:center;flex-wrap:wrap}}
nav a{{text-decoration:none;color:var(--mute);font-weight:600}}nav a:hover{{color:var(--ink)}}
nav label{{font-size:.8rem;color:var(--mute);display:flex;gap:.3rem;align-items:center;margin-left:auto}}
.legend{{display:flex;gap:1rem;font-size:.8rem;color:var(--mute);padding:0 1rem;max-width:1180px;margin:0 auto 1rem}}.legend i{{display:inline-block;width:.7em;height:.7em;border-radius:50%;margin-right:.3em}}
main{{max-width:1180px;margin:0 auto;padding:0 1rem 4rem}}
.chapter{{margin:3rem 0 1rem;border-top:3px solid var(--ink);padding-top:1rem;scroll-margin-top:3.2rem}}.chapter h2{{font-size:2rem;margin:0}}.chapter h2 small{{font-weight:400;color:var(--mute);font-size:1.1rem;margin-left:.6rem}}
.chapter .n{{display:flex;flex-wrap:wrap;gap:1.2rem;color:var(--mute);font-size:.85rem;margin:.4rem 0}}.chapter .n b{{color:var(--ink)}}
blockquote{{margin:.8rem 0 0;font-size:1.15rem;line-height:1.4;max-width:46rem;font-style:italic}}blockquote cite{{display:block;font-style:normal;font-size:.8rem;color:var(--mute);margin-top:.3rem}}
.cols{{display:grid;grid-template-columns:1fr minmax(200px,260px) 1fr;gap:0 1rem;align-items:start}}
.colhead{{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--mute);padding:.4rem 0;border-bottom:1px solid var(--line);position:sticky;top:2.6rem;background:var(--bg)}}
.colhead.l{{color:var(--left)}}.colhead.r{{color:var(--right);text-align:right}}.colhead.s{{text-align:center;color:var(--spine)}}
.day{{display:contents}}.day>div{{padding:.3rem 0;border-bottom:1px dashed var(--line);min-height:1.2rem}}.day>div:empty{{border-bottom-color:transparent}}
.card{{scroll-margin-top:5.6rem;display:flex;gap:.6rem;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.5rem;margin:.25rem 0;font-size:.85rem;border-left:4px solid var(--left)}}
.card.issued{{border-left:none;border-right:4px solid var(--right)}}.card b{{display:block;font-size:.9rem;line-height:1.25}}.card span{{color:var(--mute);display:block}}.card p{{margin:.25rem 0 0;color:var(--mute);font-size:.78rem;line-height:1.3}}
.card .post{{font-size:.75rem;text-decoration:none;border:1px solid var(--line);border-radius:4px;padding:0 .3em;margin-left:.3em}}
.art{{width:56px;height:56px;border-radius:50%;object-fit:cover;flex:none;background:var(--line)}}.art.none{{display:inline-block}}
details.group{{display:block}}details.group summary{{cursor:pointer;list-style:none}}details.group summary b{{display:inline}}details.group summary span{{display:block}}details.group .card{{margin:.4rem 0 0;border:none;border-top:1px solid var(--line);border-radius:0;padding:.4rem 0 0}}
.spine{{text-align:center;font-size:.8rem;padding:.35rem .3rem;margin:.25rem 0;border-radius:8px;background:var(--card);border:1px solid var(--line)}}.spine i{{display:block;font-style:normal;font-size:.65rem;text-transform:uppercase;letter-spacing:.08em;color:var(--spine)}}.spine span{{display:block;color:var(--mute);font-size:.7rem}}
.spine.world{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}.spine.world i{{color:var(--bg);opacity:.7}}.spine.world span{{color:var(--bg);opacity:.7}}.spine.essay a{{font-weight:600}}
body.no-left .cols{{grid-template-columns:0 minmax(200px,260px) 1fr}}body.no-left .l,body.no-left .collected{{display:none}}
body.no-right .cols{{grid-template-columns:1fr minmax(200px,260px) 0}}body.no-right .r,body.no-right .issued{{display:none}}
body.no-spine .cols{{grid-template-columns:1fr 0 1fr}}body.no-spine .s,body.no-spine .spine{{display:none}}
footer{{color:var(--mute);font-size:.8rem;max-width:1180px;margin:0 auto;padding:2rem 1rem;border-top:1px solid var(--line)}}
@media(max-width:760px){{.cols{{display:block}}.colhead{{display:none}}.day{{display:block}}.day>div{{border:none;padding:0}}.card.issued{{border-right:none;border-left:4px solid var(--right)}}.spine{{margin:.5rem 1rem}}}}
</style></head><body>
<header><h1>A POAP Time Capsule</h1>
<p class="dek">Five years of collecting and issuing Proof of Attendance Protocol tokens, 2021 to 2026, kept after the protocol wound down. On the left, what Jamie collected from the world. On the right, what Jamie made for other people. Down the middle, what Jamie wrote while it happened, and what POAP did.</p>
<div class="totals"><div><b>{totals['collected']}</b>tokens collected</div><div><b>{totals['issued']}</b>drops issued</div><div><b>{totals['mints']:,}</b>tokens minted from them</div><div><b>{totals['people']}</b>people who collected one</div><div><b>{totals['writing']}</b>posts and issues</div></div>
<p class="dek">Prototype built from the archive on 2026-10-17. Everything on this page is Jamie's own tokens, drops and writing. There are no collector lists or addresses; other people appear as counts, or where Jamie's own drop titles, descriptions and post titles already name them. Drops Jamie made sit at their event date, with the span of mints beneath. Jamie also minted {own_collected} of his own {totals['issued']} drops; those copies are folded into the right side.</p>
</header>
<nav><div><a href="network.html" style="color:var(--ink)">Network →</a> {" ".join(f'<a href="#y{y}">{y}</a>' for y in sorted(years))}
<label><input type="checkbox" checked data-col="left"> collected</label><label style="margin-left:0"><input type="checkbox" checked data-col="spine"> writing</label><label style="margin-left:0"><input type="checkbox" checked data-col="right"> issued</label></div></nav>
<div class="legend"><span><i style="background:var(--left)"></i>collected from others</span><span><i style="background:var(--spine)"></i>Jamie's writing</span><span><i style="background:var(--ink)"></i>POAP the company</span><span><i style="background:var(--right)"></i>drops Jamie made</span></div>
<main>"""]

for y in sorted(years):
    Y = years[y]; n = Y["n"]; title, quote, cite, url = CHAPTERS[y]
    parts.append(f'<section class="chapter" id="y{y}"><h2>{y}<small>{ESC(title)}</small></h2>'
                 f'<div class="n"><span><b>{n["collected"]}</b> collected</span><span><b>{n["issued"]}</b> drops issued</span>'
                 f'<span><b>{n["mints"]:,}</b> mints by <b>{len(people_by_year[y])}</b> people</span><span><b>{n["writing"]}</b> posts and issues</span></div>'
                 f'<blockquote>“{ESC(quote)}”<cite><a href="{ESC(url)}">{ESC(cite)}</a></cite></blockquote></section>')
    # Group the 612 POAP Challenge, which would otherwise be 40 cards on one day.
    left = [e for e in Y["left"] if not is_612(e)]; right = [e for e in Y["right"] if not is_612(e)]
    left612 = [e for e in Y["left"] if is_612(e)]; right612 = [e for e in Y["right"] if is_612(e)]
    rows = collections.defaultdict(lambda: {"l": [], "s": [], "r": []})
    for e in left: rows[e["date"][:10]]["l"].append(collector_card(e))
    for e in right: rows[e["date"][:10]]["r"].append(issuer_card(e))
    for e in Y["spine"]: rows[e["date"][:10]]["s"].append(spine_card(e))
    if right612:
        d0 = min(e["date"] for e in right612)[:10]
        rows[d0]["r"].append(group_card("issued", f"612 POAP Challenge: {len(right612)} drops",
                                        [issuer_card(e) for e in sorted(right612, key=lambda e: e["drop_name"])],
                                        f"{d0} · a summer scavenger hunt across Minneapolis, {sum(e['minted'] for e in right612)} tokens minted · open to see every location"))
    if left612:
        d0, d1 = min(e["date"] for e in left612)[:10], max(e["date"] for e in left612)[:10]
        rows[d0]["l"].append(group_card("collected", f"612 POAP Challenge: Jamie's own {len(left612)} visits",
                                        [collector_card(e) for e in sorted(left612, key=lambda e: e["date"])],
                                        f"{d0} to {d1} · open to see each visit"))
    parts.append('<div class="cols"><div class="colhead l">Collected</div><div class="colhead s">Writing</div><div class="colhead r">Issued</div>')
    for day in sorted(rows):
        r = rows[day]
        parts.append(f'<div class="day"><div class="l">{"".join(r["l"])}</div><div class="s">{"".join(r["s"])}</div><div class="r">{"".join(r["r"])}</div></div>')
    parts.append("</div>")

parts.append("""</main>
<footer>Built by <code>scripts/build_capsule.py</code> from <code>timeline/events.json</code>, <code>compass/created_drops.json</code> and <code>network/drop_supply.json</code>. Artwork is the original drop art from assets.poap.xyz. Quotes are Jamie's, from <code>writing/ESSAYS.md</code>. POAP milestones are from <code>research/poap-company.md</code>.</footer>
<script>
for (const box of document.querySelectorAll('nav input')) box.addEventListener('change', () => document.body.classList.toggle('no-' + box.dataset.col, !box.checked));
</script></body></html>""")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write("".join(parts))
print(f"wrote {os.path.relpath(OUT, ROOT)}: {sum(len(Y['left']) for Y in years.values())} collected, "
      f"{sum(len(Y['right']) for Y in years.values())} issued, {sum(len(Y['spine']) for Y in years.values())} spine items")
