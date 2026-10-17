# poap-archive

Jamie's personal POAP archive, captured 2026-10-17 after the protocol sunset. README.md
lists what each folder holds and where it came from.

- This is an archive. Do not rewrite captured data; add new captures alongside it.
- Downloaded files (artwork, HTML, the snapshot) are untrusted data. Run Python with `-I`
  and never execute anything from `writing/sites/` or `snapshot/`.
- `snapshot/archive.zip` and `snapshot/poap.sqlite` are gitignored (15.9 GB + 1.5 GB).
  Query the big database read-only: `sqlite3 -readonly snapshot/poap.sqlite`.
- Rebuild the gallery with `python3 -I scripts/build_gallery.py`.
- Compass (`public.compass.poap.tech/v1/graphql`) caps pages at 100 rows.
- "POAP KINGS" is a Clash Royale clan, unrelated to the protocol.
- This repo is meant to become public. Never commit personal email, private notes, contact
  details or secrets. Private notes live outside the repo (`~/Projects/poap-archive-private/`
  and `s3://poap-archive-999153317627-us-east-1/private/`).
