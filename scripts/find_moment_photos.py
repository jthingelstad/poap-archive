"""Find candidate originals in Photos for the moment photos Jamie posted to POAP.

POAP's moment media host is gone; the moments keep only the upload time. A photo is
usually taken before it is posted, so for each of Jamie's moments with media this
lists the photos taken in the hours before the upload (and a few minutes after), nearest
first, and exports copies of the top candidates for review. Photos is only read.

Run on the Mac that holds the Photos library, from the archive checkout:

    uv run --no-project --python 3.13 --with osxphotos -- \
        python -I scripts/find_moment_photos.py ~/Desktop/poap-moments

Options: --hours N (look back N hours, default 12), --top N (candidates exported per
moment, default 4), --download (let Photos fetch originals that live only in iCloud),
--library PATH (a .photoslibrary other than the one Photos last opened).
Writes <out>/candidates.csv and <out>/<moment id>/<rank>-<original name>.
"""

import argparse, collections, csv, datetime, json, os, sys
from zoneinfo import ZoneInfo

import osxphotos

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAMIE = {"0x111accebf9d70d9c06de2d38f9392522e82ecf29", "0xb81b70afee42e944b88d06a71e0531852c612056",
         "0x2bda946a7740b1ddb0fd5c226819170c4dd15720", "0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf"}
CENTRAL = ZoneInfo("America/Chicago")
AFTER = datetime.timedelta(minutes=5)

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--hours", type=float, default=12)
ap.add_argument("--top", type=int, default=4)
ap.add_argument("--download", action="store_true")
ap.add_argument("--library", help="path to a .photoslibrary (default: the last one Photos opened)")
args = ap.parse_args()
out = os.path.abspath(os.path.expanduser(args.out))
os.makedirs(out, exist_ok=True)


def rows(path):
    data = json.load(open(os.path.join(ROOT, path)))
    return data if isinstance(data, list) else next(v for v in data.values() if isinstance(v, list))


def when(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


names = {}
for d in rows("compass/created_drops.json"):
    names[d["id"]] = d.get("name") or ""
for t in rows("compass/collected.json"):
    names.setdefault(t["drop_id"], (t.get("drop") or {}).get("name") or "")

moments = sorted((m for m in rows("compass/moments.json")
                  if (m.get("author") or "").lower() in JAMIE and m.get("media")),
                 key=lambda m: m["created_on"])
db = osxphotos.PhotosDB(dbfile=os.path.expanduser(args.library)) if args.library else osxphotos.PhotosDB()
print(f"Photos library: {db.library_path}", file=sys.stderr)

table, found = [], collections.Counter()
for m in moments:
    posted = when(m["created_on"])
    start = posted - datetime.timedelta(hours=args.hours)
    photos = [p for p in db.photos(from_date=start, to_date=posted + AFTER) if not p.hidden]
    photos.sort(key=lambda p: abs((posted - p.date).total_seconds()))
    found[min(len(photos), 1)] += 1
    base = {"moment": m["id"], "drop": m["drop_id"], "drop_name": names.get(m["drop_id"], ""),
            "posted_central": posted.astimezone(CENTRAL).strftime("%Y-%m-%d %H:%M:%S"),
            "photos_posted": len(m["media"]), "note": (m.get("description") or "").strip()[:120]}
    if not photos:
        table.append({**base, "rank": "", "taken_central": "", "minutes_before": "", "file": "",
                      "uuid": "", "exported": "no candidates"})
        continue
    for rank, p in enumerate(photos[: args.top], 1):
        folder = os.path.join(out, m["id"])
        os.makedirs(folder, exist_ok=True)
        try:
            files = p.export(folder, f"{rank}-{p.original_filename}", use_photos_export=args.download)
            status = "yes" if files else ("missing (in iCloud; rerun with --download)" if p.ismissing else "no")
        except Exception as error:  # export failures are reported, never fatal
            status = f"error: {error}"
        table.append({**base, "rank": rank,
                      "taken_central": p.date.astimezone(CENTRAL).strftime("%Y-%m-%d %H:%M:%S"),
                      "minutes_before": round((posted - p.date).total_seconds() / 60, 1),
                      "file": p.original_filename, "uuid": p.uuid, "exported": status})

with open(os.path.join(out, "candidates.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(table[0]) if table else ["moment"])
    writer.writeheader()
    writer.writerows(table)
print(f"{len(moments)} moments with photos: {found[1]} have candidates, {found[0]} have none. "
      f"See {out}/candidates.csv", file=sys.stderr)
