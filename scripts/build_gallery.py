"""Build index.html: a local, offline gallery of Jamie's POAP collection and the drops Jamie created.

Reads only files already in this repo. Run from anywhere: python3 -I scripts/build_gallery.py
"""
import collections, datetime, glob, html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load = lambda p: json.load(open(os.path.join(ROOT, p)))
esc = html.escape


def art(folder, drop_id):
    hits = [f for f in glob.glob(os.path.join(ROOT, folder, f"{drop_id}.*"))]
    return os.path.relpath(hits[0], ROOT) if hits else ""


def day(s):
    return (s or "")[:10]


collected = sorted(load("compass/collected.json"), key=lambda p: p["minted_on"] or 0, reverse=True)
created = sorted(load("compass/created_drops.json"), key=lambda d: d["start_date"] or "", reverse=True)
tokens = load("compass/created_drop_tokens.json")
moments = load("compass/moments.json")
minted = collections.Counter(t["drop_id"] for t in tokens)
moment_count = collections.Counter(m["drop_id"] for m in moments)
holders = len({t["collector_address"] for t in tokens})


def card(img, title, lines, href=None):
    body = f'<img loading="lazy" src="{esc(img)}" alt="">' if img else '<div class="noimg"></div>'
    name = f'<a href="{esc(href)}">{esc(title)}</a>' if href else esc(title)
    return f'<figure>{body}<figcaption><b>{name}</b>' + "".join(f"<span>{esc(l)}</span>" for l in lines if l) + "</figcaption></figure>"


def place(d):
    return ", ".join(x for x in (d.get("city"), d.get("country")) if x)


coll_cards = []
for p in collected:
    d = p["drop"]
    when = datetime.datetime.fromtimestamp(p["minted_on"], datetime.timezone.utc).strftime("%Y-%m-%d") if p["minted_on"] else ""
    coll_cards.append(card(art("collection/drop-artwork", d["id"]), d["name"],
                           [f"Minted {when} · #{p['id']} · {p['chain']}", place(d)], f"compass/collected.json#{p['id']}"))

made_cards = []
for d in created:
    made_cards.append(card(art("created-drops/artwork", d["id"]), d["name"],
                           [f"{day(d['start_date'])} · drop {d['id']}", f"{minted[d['id']]} minted" + (f" · {moment_count[d['id']]} moments" if moment_count[d['id']] else ""), place(d)]))

page = f"""<!doctype html><meta charset="utf-8"><title>Jamie's POAP Archive</title>
<style>
body{{font:15px/1.4 -apple-system,system-ui,sans-serif;margin:2rem;background:#fafaf7;color:#222}}
h1{{margin:0}} h2{{margin-top:2.5rem;border-bottom:1px solid #ddd}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:1.2rem}}
figure{{margin:0;text-align:center}} img,.noimg{{width:150px;height:150px;border-radius:50%;object-fit:cover;background:#eee}}
figcaption{{display:flex;flex-direction:column;font-size:12px;color:#666}} figcaption b{{font-size:13px;color:#222;margin:.3rem 0}}
a{{color:inherit}}
</style>
<h1>Jamie's POAP Archive</h1>
<p>Captured {datetime.date.today()} after the POAP protocol sunset (2026-07-31).
{len(collected)} tokens collected · {len(created)} drops created · {len(tokens)} tokens minted from them by {holders} collectors.</p>
<h2>Drops Jamie created or curated ({len(created)})</h2><div class="grid">{''.join(made_cards)}</div>
<h2>Collected ({len(collected)})</h2><div class="grid">{''.join(coll_cards)}</div>
"""
open(os.path.join(ROOT, "index.html"), "w").write(page)
print(f"index.html: {len(collected)} collected, {len(created)} created")
