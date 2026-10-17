"""Prototype of the network page: capsule/network.html.

A bipartite graph. One kind of node is a drop Jamie made (130), the other is a person who
minted one (639, with Jamie's wallets and the zero address removed). One edge per person
and drop. The layout is computed here with a force-directed pass in numpy and written as
static SVG, so the page is a picture first and interactive second.

People are named by primary ENS name where one is set, else by shortened address
(0x018a…3c47), as POAP itself did. Addresses and names are public on-chain; Jamie decided
this on 2026-10-17. Run: python3 -I scripts/build_network.py
"""
import collections, datetime, html, json, math, os
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load = lambda p: json.load(open(os.path.join(ROOT, p)))
OUT = os.path.join(ROOT, "capsule", "network.html")
ESC = html.escape
JAMIE = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29", "0xb81b70afee42e944b88d06a71e0531852c612056",
         "0x2bda946a7740b1ddb0fd5c226819170c4dd15720", "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf"}
ZERO = "0x0000000000000000000000000000000000000000"

SERIES = [  # (slug, label, color, name tests)
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
SERIES_OF = {s[0]: s for s in SERIES}


def series(name):
    for slug, _, _, tests in SERIES:
        if any(t.lower() in name.lower() for t in tests): return slug
    return "community"


iso = lambda ts: datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).isoformat() if isinstance(ts, (int, float)) else ts

created = {d["id"]: d for d in load("compass/created_drops.json")}
tokens = load("compass/created_drop_tokens.json")
ens = load("network/ens.json")
sizes = collections.defaultdict(int)
for r in load("network/collector_sizes.json"): sizes[r["address"].lower()] += r["poaps_owned"]

holds = collections.defaultdict(dict)  # person -> drop -> first mint time
for t in tokens:
    a = t["collector_address"].lower()
    if a in JAMIE or a == ZERO or not t["minted_on"]: continue
    holds[a][t["drop_id"]] = min(holds[a].get(t["drop_id"], iso(t["minted_on"])), iso(t["minted_on"]))
people = sorted(holds, key=lambda a: (-len(holds[a]), a))  # deterministic, most drops first
pidx = {a: i for i, a in enumerate(people)}
drops = sorted(created, key=lambda i: (series(created[i]["name"]), created[i]["start_date"]))
didx = {d: i for i, d in enumerate(drops)}
mints = collections.Counter(d for a in people for d in holds[a])
edges = [(pidx[a], didx[d]) for a in people for d in holds[a]]

# Layout: drops start on a circle grouped by series, people at the mean of their drops.
N = len(drops) + len(people)
pos = np.zeros((N, 2))
rng = np.random.default_rng(612)
for i, d in enumerate(drops):
    ang = 2 * math.pi * i / len(drops)
    pos[i] = [0.55 * math.cos(ang), 0.55 * math.sin(ang)]
for a in people:
    j = len(drops) + pidx[a]
    pos[j] = pos[[didx[d] for d in holds[a]]].mean(axis=0) * 1.3 + rng.normal(0, 0.05, 2)
E = np.array([(len(drops) + p, d) for p, d in edges])
k = 1.0 / math.sqrt(N)
deg = np.bincount(np.concatenate([E[:, 0], E[:, 1]]), minlength=N).astype(float)
for step in range(400):
    temp = 0.08 * (1 - step / 400) + 0.002
    diff = pos[:, None, :] - pos[None, :, :]
    dist = np.sqrt((diff ** 2).sum(-1)) + 1e-6
    rep = (diff / dist[..., None]) * (k * k / dist)[..., None]
    disp = rep.sum(axis=1)
    ev = pos[E[:, 0]] - pos[E[:, 1]]
    el = np.sqrt((ev ** 2).sum(-1)) + 1e-6
    att = ev / el[:, None] * (el * el / k)[:, None]
    np.add.at(disp, E[:, 0], -att)
    np.add.at(disp, E[:, 1], att)
    disp -= pos * 0.6 * (1 + np.log1p(deg))[:, None]  # gravity, stronger on hubs
    ln = np.sqrt((disp ** 2).sum(-1)) + 1e-6
    pos += disp / ln[:, None] * np.minimum(ln, temp)[:, None]
pos -= pos.mean(axis=0)
pos /= np.abs(pos).max() * 1.08
W = 1000
xy = (pos * W / 2 + W / 2).round(1)

# Stories.
n_drops = {a: len(holds[a]) for a in people}
known = [a for a in people if a in sizes]
one_total = sum(1 for a in known if sizes[a] == 1)
five_total = sum(1 for a in known if sizes[a] <= 5)
unknown = len(people) - len(known)
bdays = [d for d in drops if series(created[d]["name"]) == "birthday"]
bday_loyalty = collections.Counter(sum(1 for d in bdays if d in holds[a]) for a in people)
finish = sorted((holds[a][190903], a) for a in people if 190903 in holds[a])
regulars = [a for a in people if n_drops[a] >= 10]
series_order = [s[0] for s in SERIES]
matrix = [[sum(1 for d in holds[a] if series(created[d]["name"]) == s) for s in series_order] for a in regulars]
series_totals = collections.Counter(series(created[d]["name"]) for d in drops)
tiers = [("30 or more", 30, 10 ** 9), ("10 to 29", 10, 29), ("5 to 9", 5, 9), ("2 to 4", 2, 4), ("1", 1, 1)]
tier_counts = [(label, sum(1 for a in people if lo <= n_drops[a] <= hi)) for label, lo, hi in tiers]

short = lambda a: a[:6] + "…" + a[-4:]
label = lambda a: ens.get(a, {}).get("ens_primary") or short(a)
link = lambda a: f"https://app.ens.domains/{ens[a]['ens_primary']}" if ens.get(a, {}).get("ens_primary") else f"https://gnosisscan.io/address/{a}"
# Data for the page's JavaScript.
data = {
    "drops": [{"id": d, "name": created[d]["name"], "series": series(created[d]["name"]), "date": (created[d]["start_date"] or "")[:10],
               "mints": mints[d], "x": float(xy[didx[d], 0]), "y": float(xy[didx[d], 1])} for d in drops],
    "people": [{"n": n_drops[a], "total": sizes.get(a, 0), "name": label(a), "addr": a, "url": link(a),
                "x": float(xy[len(drops) + pidx[a], 0]), "y": float(xy[len(drops) + pidx[a], 1])} for a in people],
    "edges": edges,
    "series": {s[0]: {"label": s[1], "color": s[2]} for s in SERIES},
}

svg = [f'<svg viewBox="0 0 {W} {W}" xmlns="http://www.w3.org/2000/svg" id="graph">', '<g id="edges">']
for p, d in edges:
    x1, y1 = xy[len(drops) + p]; x2, y2 = xy[d]
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" data-p="{p}" data-d="{d}"/>')
svg.append('</g><g id="people">')
for i, a in enumerate(people):
    x, y = xy[len(drops) + i]
    r = 1.6 + 0.45 * math.log1p(sizes.get(a, 1))
    svg.append(f'<circle class="p" cx="{x}" cy="{y}" r="{r:.1f}" data-i="{i}"><title>{ESC(label(a))}</title></circle>')
svg.append('</g><g id="drops">')
for i, d in enumerate(drops):
    x, y = xy[i]
    r = 4 + 1.1 * math.sqrt(mints[d])
    svg.append(f'<circle class="d" cx="{x}" cy="{y}" r="{r:.1f}" fill="{SERIES_OF[series(created[d]["name"])][2]}" data-i="{i}"><title>{ESC(created[d]["name"])}</title></circle>')
svg.append("</g></svg>")

legend = "".join(f'<button class="lg" data-s="{s}"><i style="background:{c}"></i>{ESC(l)} <small>{series_totals[s]}</small></button>' for s, l, c, _ in SERIES)
tiers_html = "".join(f'<div class="bar"><span>{ESC(l)} of Jamie\'s drops</span><b style="width:{100 * n / len(people):.1f}%"></b><em>{n}</em></div>' for l, n in tier_counts)
matrix_html = "".join(
    f'<tr><td><a href="{ESC(link(a))}" title="{a}">{ESC(label(a))}</a></td><td>{n_drops[a]}</td>' + "".join(f'<td class="c{min(c, 5)}">{c or ""}</td>' for c in row) + f'<td>{sizes.get(a, "?")}</td></tr>'
    for i, (a, row) in enumerate(zip(regulars, matrix)))
finish_html = "".join(f'<li><a href="{ESC(link(a))}" title="{a}">{ESC(label(a))}</a>, {t[:10]}</li>' for t, a in finish)
all_five = [a for a in people if all(d in holds[a] for d in bdays)]
all_five_html = ", ".join(f'<a href="{ESC(link(a))}" title="{a}">{ESC(label(a))}</a>' for a in all_five)

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The POAP Network</title>
<style>
:root{{--bg:#f7f5ef;--ink:#1d1b16;--mute:#6b665b;--line:#e3dfd3;--card:#fffdf8;--edge:#1d1b16;--person:#9a9385}}
@media(prefers-color-scheme:dark){{:root{{--bg:#16150f;--ink:#efe9da;--mute:#a39c8c;--line:#2d2a21;--card:#1f1d16;--edge:#efe9da;--person:#7d766a}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,system-ui,"Segoe UI",sans-serif}}a{{color:inherit}}
header,main,footer{{max-width:1180px;margin:0 auto;padding:0 1rem}}header{{padding-top:2.5rem}}h1{{font-size:2.4rem;margin:0 0 .3rem;letter-spacing:-.02em}}
.dek{{color:var(--mute);max-width:52rem}}nav{{display:flex;gap:1rem;margin:.6rem 0 1rem}}nav a{{text-decoration:none;color:var(--mute);font-weight:600}}
.totals{{display:flex;flex-wrap:wrap;gap:1.4rem;margin:1rem 0}}.totals div{{font-size:.85rem;color:var(--mute)}}.totals b{{display:block;font-size:1.6rem;color:var(--ink)}}
.legend{{display:flex;flex-wrap:wrap;gap:.4rem;margin:.5rem 0 1rem}}.lg{{font:inherit;font-size:.8rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:.2rem .7rem .2rem .5rem;cursor:pointer}}
.lg i{{display:inline-block;width:.7em;height:.7em;border-radius:50%;margin-right:.4em}}.lg small{{color:var(--mute)}}.lg.on{{outline:2px solid var(--ink)}}
.wrap{{display:grid;grid-template-columns:1fr 300px;gap:1rem;align-items:start}}@media(max-width:860px){{.wrap{{display:block}}}}
#graph{{width:100%;height:auto;background:var(--card);border:1px solid var(--line);border-radius:12px}}
#edges line{{stroke:var(--edge);stroke-opacity:.07;stroke-width:.6}}#edges line.hi{{stroke-opacity:.6;stroke-width:1.2}}
.p{{fill:var(--person);fill-opacity:.75;cursor:pointer}}.p.hi{{fill:var(--ink);fill-opacity:1}}.p.dim,.d.dim{{opacity:.12}}#edges line.dim{{stroke-opacity:.015}}
.d{{stroke:var(--card);stroke-width:1;cursor:pointer}}.d.hi{{stroke:var(--ink);stroke-width:2}}
.panel{{position:sticky;top:1rem;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem;font-size:.9rem;min-height:12rem}}.panel h3{{margin:0 0 .3rem;font-size:1.05rem}}.panel p{{margin:.3rem 0;color:var(--mute)}}.panel ul{{padding-left:1.1rem;margin:.3rem 0}}.panel li{{margin:.15rem 0}}
.panel .tl{{display:inline-block;margin-top:.5rem;font-size:.8rem}}.panel .who{{font-size:.75rem;line-height:1.5;max-height:14rem;overflow:auto}}
h2{{margin:2.5rem 0 .5rem;font-size:1.5rem}}section p{{max-width:52rem;color:var(--mute)}}
.bar{{display:grid;grid-template-columns:14rem 1fr 3rem;align-items:center;gap:.6rem;margin:.3rem 0;font-size:.85rem}}.bar b{{display:block;height:1.1rem;background:var(--ink);border-radius:3px;min-width:2px}}.bar em{{font-style:normal;color:var(--mute)}}
table{{border-collapse:collapse;font-size:.8rem;margin-top:.5rem}}th,td{{padding:.2rem .45rem;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}}th{{font-weight:600;color:var(--mute)}}td:first-child,th:first-child{{text-align:left}}
td.c1{{background:rgba(42,111,151,.12)}}td.c2{{background:rgba(42,111,151,.25)}}td.c3{{background:rgba(42,111,151,.4)}}td.c4{{background:rgba(42,111,151,.55)}}td.c5{{background:rgba(42,111,151,.7);color:#fff}}
.tw{{overflow-x:auto}}footer{{color:var(--mute);font-size:.8rem;padding:2rem 1rem;border-top:1px solid var(--line);margin-top:3rem}}
</style></head><body>
<header><h1>The POAP Network</h1>
<nav><a href="index.html">Timeline</a><a href="network.html">Network</a></nav>
<p class="dek">Every person who minted one of Jamie's drops, and the drops that connect them. Big colored circles are the {len(drops)} drops Jamie made, sized by how many people minted them and colored by series. Small gray dots are the {len(people)} people, sized by how many POAPs they hold in total. A line is one person minting one drop. Click anything.</p>
<div class="totals"><div><b>{len(people)}</b>people</div><div><b>{len(drops)}</b>drops</div><div><b>{len(edges):,}</b>person-to-drop links</div><div><b>{one_total}</b>people whose only POAP is one of Jamie's</div><div><b>{len(regulars)}</b>people with ten or more</div></div>
<p class="dek">People are shown by their primary ENS name where they set one ({sum(1 for a in people if ens.get(a, {}).get("ens_primary"))} of {len(people)}) and by shortened wallet address otherwise, the way POAP showed them. Names link to ENS, addresses to Gnosisscan. Everything here is on the public chain.</p>
</header>
<main>
<div class="legend">{legend}<button class="lg" id="clear">clear</button></div>
<div class="wrap">{"".join(svg)}
<aside class="panel" id="panel"><h3>Pick a drop or a person</h3><p>Click a colored circle to light up everyone who minted it and every other drop they hold. Click a gray dot to see one person's path through Jamie's drops. Click a series in the legend to see its cluster.</p></aside></div>

<section><h2>The on-ramp</h2>
<p>Most people in this graph are here because of one drop. For {one_total} of them, Jamie's drop is the only POAP they have ever minted; {five_total} hold five or fewer in total. (Collection sizes are known for {len(known)} of the {len(people)}; the other {unknown} returned nothing from Compass.)</p>
{tiers_html}</section>

<section><h2>The regulars</h2>
<p>{len(regulars)} people hold ten or more of Jamie's drops. Rows are people in order of drops held, columns are series, cells are how many drops of that series they hold.</p>
<div class="tw"><table><tr><th>Collector</th><th>Drops</th>{"".join(f"<th>{ESC(SERIES_OF[s][1])}</th>" for s in series_order)}<th>POAPs in total</th></tr>{matrix_html}</table></div>
<p>Birthday loyalty across the five birthday drops: {bday_loyalty[5]} people came to all five ({all_five_html}), {bday_loyalty[4]} to four, {bday_loyalty[3]} to three, {bday_loyalty[2]} to two, {bday_loyalty[1]} to one.</p></section>

<section><h2>The 612 finishers</h2>
<p>{len(finish)} people besides Jamie collected all 31 locations of the 612 POAP Challenge and received the Collected Them All! token, in this order:</p>
<ol>{finish_html}</ol></section>
</main>
<footer>Built by <code>scripts/build_network.py</code> from <code>compass/created_drop_tokens.json</code>, <code>network/collector_sizes.json</code> and <code>network/ens.json</code>. Names are primary ENS records from ensdata.net on 2026-10-17. Layout is a force-directed pass computed at build time; the picture is static SVG and the highlighting is a little inline script.</footer>
<script>
const D={json.dumps(data, separators=(",", ":"))};
const panel=document.getElementById('panel'), lines=[...document.querySelectorAll('#edges line')], P=[...document.querySelectorAll('.p')], DR=[...document.querySelectorAll('.d')];
const byP=D.people.map(()=>[]), byD=D.drops.map(()=>[]);
D.edges.forEach(([p,d],i)=>{{byP[p].push([d,i]);byD[d].push([p,i]);}});
function reset(){{for(const el of [...lines,...P,...DR]) el.classList.remove('hi','dim');document.querySelectorAll('.lg').forEach(b=>b.classList.remove('on'));}}
function dimAll(){{for(const el of [...lines,...P,...DR]) el.classList.add('dim');}}
function showDrop(i){{reset();dimAll();const d=D.drops[i];DR[i].classList.replace('dim','hi');
  const others=new Map();for(const [p,e] of byD[i]){{P[p].classList.replace('dim','hi');lines[e].classList.replace('dim','hi');for(const [d2] of byP[p]) if(d2!==i) others.set(d2,(others.get(d2)||0)+1);}}
  for(const d2 of others.keys()) DR[d2].classList.remove('dim');
  const top=[...others].sort((a,b)=>b[1]-a[1]).slice(0,6).map(([d2,n])=>`<li>${{n}} also hold <a href="#" data-drop="${{d2}}">${{D.drops[d2].name}}</a></li>`).join('');
  const who=byD[i].map(([p])=>p).sort((a,b)=>D.people[b].n-D.people[a].n).map(p=>`<a href="#" data-person="${{p}}" title="${{D.people[p].addr}}">${{D.people[p].name}}</a>`).join(', ');
  panel.innerHTML=`<h3>${{d.name}}</h3><p>${{D.series[d.series].label}} · ${{d.date}} · ${{d.mints}} people minted it</p><ul>${{top}}</ul><p class="who">${{who}}</p><a class="tl" href="index.html#drop-${{d.id}}">See it on the timeline →</a>`;}}
function showPerson(i){{reset();dimAll();const p=D.people[i];P[i].classList.replace('dim','hi');
  const ds=byP[i].map(([d,e])=>{{lines[e].classList.replace('dim','hi');DR[d].classList.remove('dim');return d;}}).sort((a,b)=>D.drops[a].date<D.drops[b].date?-1:1);
  panel.innerHTML=`<h3><a href="${{p.url}}" title="${{p.addr}}">${{p.name}}</a></h3><p>holds ${{p.n}} of Jamie's drops · ${{p.total||'?'}} POAPs in total</p><ul>${{ds.map(d=>`<li><a href="#" data-drop="${{d}}">${{D.drops[d].name}}</a> <small>${{D.drops[d].date}}</small></li>`).join('')}}</ul>`;}}
function showSeries(s){{reset();dimAll();const set=new Set();D.drops.forEach((d,i)=>{{if(d.series===s){{DR[i].classList.replace('dim','hi');for(const [p,e] of byD[i]){{P[p].classList.remove('dim');lines[e].classList.remove('dim');set.add(p);}}}}}});
  document.querySelector(`.lg[data-s="${{s}}"]`).classList.add('on');
  panel.innerHTML=`<h3>${{D.series[s].label}}</h3><p>${{D.drops.filter(d=>d.series===s).length}} drops · ${{set.size}} people hold at least one</p>`;}}
DR.forEach((el,i)=>el.addEventListener('click',()=>showDrop(i)));P.forEach((el,i)=>el.addEventListener('click',()=>showPerson(i)));
document.querySelectorAll('.lg[data-s]').forEach(b=>b.addEventListener('click',()=>showSeries(b.dataset.s)));
document.getElementById('clear').addEventListener('click',()=>{{reset();panel.innerHTML='<h3>Pick a drop or a person</h3>';}});
panel.addEventListener('click',e=>{{if(e.target.dataset.drop){{e.preventDefault();showDrop(+e.target.dataset.drop);}}if(e.target.dataset.person){{e.preventDefault();showPerson(+e.target.dataset.person);}}}});
</script></body></html>"""
open(OUT, "w").write(page)
print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(people)} people, {len(drops)} drops, {len(edges)} edges; on-ramp {one_total}; regulars {len(regulars)}; finishers {len(finish)}")
