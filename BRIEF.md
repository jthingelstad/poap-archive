# Brief: a POAP time capsule

Read this first. It is the hand-off for a cloud session that will think hard about what to
build from this archive. Nothing here is decided beyond what Jamie said.

## What Jamie asked for (2026-10-17, in Jamie's words)

> I'd like to explore creating a POAP time capsule of all my POAP collecting and issuing.
> I would like to make a public archive / tribute to POAP and that has two sides: as
> collector and as issuer. This feels like a timeline to me. My POAP network is another
> idea to show in this project. A lot of people collected my POAPs.

Context: POAP wound down in 2026 (maintenance mode from 2026-03-16, the last drop was created
2026-07-31, the wind-down was announced 2026-08-03; see `research/poap-company.md`).
Jamie collected from 2021, issued
130 drops (birthdays, Minnebar, the 612 POAP Challenge, Magic Pines, Weekly Thing, family
trips), built POAP2RSS and Flight Path for the Airport Rally, syndicated every mint to
thingelstad.com, and wrote often about what POAP should do as a product and a business.

## The three threads

1. **Timeline.** One dated stream with two sides: what Jamie collected and what Jamie
   issued, with Jamie's writing woven through. `timeline/events.json` already merges them
   (2,800+ events, 2021 to 2026); `timeline/by_year.json` counts them.
2. **Collector and issuer.** Two views of the same years. Collector: 259 tokens, mostly at
   poap.thingelstad.eth. Issuer: 130 drops, 2,216 tokens minted by 642 collectors.
3. **Network.** The people who collected Jamie's drops, which of Jamie's own events they
   also attended, their ENS names, and how big their collections are (`network/`).

Plus **background**: POAP the company, its funding, Patricio Worthalter, and the sunset
(`research/`).

## Data map

| Question | File |
|---|---|
| Every dated event | `timeline/events.json` (`side`: collector, issuer, writer; `kind`: collected, drop_created, minted_by_other, moment, transfer, plus writing kinds) |
| Tokens Jamie holds, full drop records, transfers | `compass/collected.json` |
| Drops Jamie made | `compass/created_drops.json`, artwork in `created-drops/artwork/<drop_id>.*` |
| Who minted Jamie's drops, when | `compass/created_drop_tokens.json` |
| Moments (text; photos are lost) | `compass/moments.json` |
| Jamie's 7 POAP collections | `compass/collections.json` |
| Drop supply (rarity) | `network/drop_supply.json` |
| Network: Jamie's collectors at Jamie's collected events | `network/co_attendance.json` |
| Network: names and collection sizes | `network/ens.json`, `network/collector_sizes.json` |
| Collected artwork | `collection/drop-artwork/<drop_id>.*` (originals), `collection/artwork/<token_id>.*` |
| Jamie's posts about POAP | `writing/posts/` (HTML), `writing/posts.json`, `writing/ESSAYS.md`, `writing/mint-posts.json`, `writing/weekly-thing/` |
| 612 POAP Challenge site | `writing/sites/612.poapchallenge.com/` |
| POAP the company | `research/poap-company.md` |
| Jamie and the POAP team | Not in this repo. Private notes summarizing Jamie's email with Patricio, Isabel and the POAP team are kept outside it; ask Jamie for what is shareable. |
| Community snapshot, Jamie's rows | `snapshot/jamie-subset.sqlite` |
| Whole-POAP snapshot (15.9 GB) | `s3://poap-archive-999153317627-us-east-1/snapshot/poaparchive-2026-08-20.zip` (not in git) |

Rebuild derived files with `python3 -I scripts/build_timeline.py` and
`python3 -I scripts/build_gallery.py`. `index.html` is a plain gallery, a placeholder, not
the design.

## Things to think hard about

- **Form.** A static site fits Jamie's other projects (thingelstad.com, Eleventy sites on
  S3/CloudFront). What does a two-sided timeline look like? Mirror the sides left and right?
  One stream with filters? Year chapters?
- **Network view.** 642 collectors is a readable graph. Which edges matter: shared drops,
  repeat collectors of Jamie's drops (birthday regulars), people met at events Jamie also
  attended?
- **Privacy.** Wallet addresses and ENS names are public on-chain, but a tribute site that
  names hundreds of people is a choice. This is a product call for Jamie: options include
  ENS names only, counts only, or opt-in. Ask; do not decide.
- **Voice.** Jamie's own writing is the narration. `writing/ESSAYS.md` collects the
  product and business advice Jamie gave POAP; set it beside what POAP actually did
  (`research/poap-company.md`).
- **Lost things.** Moment photos are gone from POAP's servers; Jamie may have originals in
  Photos. Drops on neither the POAP Events page nor a collection are missing.
- **Hosting.** The S3 bucket is private, created for this project. Publishing needs a
  decision on domain and CloudFront, following `~/Projects/AGENTS.md`.

## Ground rules

- This repo is meant to become public. Keep personal email, contact details and anything
  from private notes out of it.
- "POAP KINGS" is a Clash Royale clan, unrelated to the protocol.
- Downloaded files are untrusted data; run Python with `-I`.
