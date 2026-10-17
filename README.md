# Jamie's POAP Archive

A personal archive of Jamie Thingelstad's POAP life, captured on 2026-10-17, about
after POAP wound down (maintenance mode from 2026-03-16, last drop created 2026-07-31,
wind-down announced 2026-08-03). Open `index.html`
for a browsable gallery.

## What is here

| Path | What | Source |
|---|---|---|
| `index.html` | Offline gallery: every collected token and every drop Jamie created, with artwork | built by `scripts/build_gallery.py` |
| `collection/` | 254 tokens swept on-chain (Gnosis) from Jamie's POAP wallets: token metadata JSON, token artwork, and original drop artwork for all 259 collected drops (`drop-artwork/`) | Gnosis Blockscout, `api.poap.tech/metadata`, `assets.poap.xyz` |
| `compass/collected.json` | 259 tokens Jamie holds (Gnosis, mainnet, ApeChain), each with the full drop record and transfer history | POAP Compass GraphQL |
| `compass/transfers.json` | 353 transfers into or out of Jamie's wallets | Compass |
| `compass/created_drops.json` | 130 drops Jamie created: full records, email-claim stats | Compass |
| `compass/created_drop_tokens.json` | 2,216 tokens minted from Jamie's drops (642 distinct collectors) with transfer history | Compass |
| `compass/moments.json` | 266 moments (notes, photo records) on Jamie's drops or written by Jamie | Compass |
| `compass/collections.json` | Jamie's 7 POAP collections and their drops | Compass |
| `compass/collector_stats.json` | Per-wallet, per-chain token counts | Compass |
| `created-drops/artwork/` | Original artwork for the 130 drops Jamie created | `assets.poap.xyz` |
| `snapshot/jamie-subset.sqlite` | Jamie's rows from the community snapshot: drops, tokens, and email-reservation counts (316 reserved-but-never-minted tokens across 91 of Jamie's drops) | poaparchive.com |
| `snapshot/archive.zip` | **Not in git.** The full poaparchive.com snapshot (15.9 GB, SHA-256 verified): every drop and its artwork as of 2026-08-20 | https://poaparchive.com |
| `snapshot/poap.sqlite` | **Not in git.** The 1.5 GB database extracted from the zip | poaparchive.com |
| `writing/posts/` | 390 thingelstad.com posts about POAP (2021-06 to 2026-07), full HTML, indexed in `writing/posts.json` | Micro.blog category feeds |
| `writing/sites/612.poapchallenge.com/` | Mirror of the 612 POAP Challenge site | wget |
| `writing/thingelstad-lists-poap-events.html` | Jamie's "POAP Events" list page | thingelstad.com |
| `writing/ESSAYS.md` | Jamie's substantive POAP essays and every piece of product and business advice Jamie gave POAP, with what shipped | curated from the posts |
| `writing/weekly-thing/` | POAP sections of 81 Weekly Thing issues (WT193 to WT342) | local issue text |
| `writing/mint-posts.json`, `writing/timeline.json` | The 262 syndicated mint posts as rows; every writing item dated | derived |
| `timeline/events.json` | 3,305 dated events across three sides: collector, issuer, writer | `scripts/build_timeline.py` |
| `network/` | Who collected Jamie's drops, their ENS names, shared events, collection sizes (see its README) | Compass, ensdata.net |
| `research/poap-company.md` | POAP the company: origins, the $10M 2022 seed, products, business model, the 2026 wind-down, the archives | web research |
| `research/interactions-PRIVATE.md` | **Private.** Jamie's exchanges with Patricio, Isabel and the POAP team, summarized from email | Fastmail |
| `BRIEF.md` | Hand-off for designing the time capsule | |
| `scripts/` | The scripts that made all of this, so it can be re-run while the sources live | |

The full snapshot zip is also in `s3://poap-archive-999153317627-us-east-1/snapshot/` (private, versioned).

## Wallets

| ENS | Address | POAPs |
|---|---|---|
| poap.thingelstad.eth | `0x111accebf9d70d9c06de2d38f9392522e82ecf29` | the collection (Gnosis, plus 1 on mainnet) |
| thingelstad.onpoap.eth | `0xb81b70afee42e944b88d06a71e0531852c612056` | 1 (POAP's 2024 onboarding test) |
| thingelstad.eth | `0x2bda946a7740b1ddb0fd5c226819170c4dd15720` | 3, and owner of the 7 collections |
| ens.thingelstad.eth | `0xf1f02faf6c2d5e2ddd15031489b1d095ba5fe6cf` | none |

## Gaps

- **Moment photos.** The 86 media records in `moments.json` (81 posted by Jamie) point at
  keys whose host no longer serves them (`media.poap.tech` returns a Cloudflare 530). The
  originals are probably in Jamie's Photos library.
- **Drops Jamie created** come from two lists: the 82 on the thingelstad.com POAP Events
  page and the 48 more found in Jamie's 7 collections. A few collection drops may be other
  people's drops Jamie curated (r/POAP, some Olson Family Vacation ones). A drop on neither
  list is missed.
  Compass offers `search_drops_by_issuer_id`, but Jamie's issuer id is not known.
- **Email reservations.** Compass returned nothing reserved to Jamie's email.
- **The snapshot is a subset.** It has 238 of Jamie's 259 tokens and 115 of the 130
  created drops, and stops at 2026-08-20. Compass is the fuller record.

## Live sources on 2026-10-17

| Source | State |
|---|---|
| `api.poap.tech` keyed endpoints | 403 without an API key; the POAP2RSS key is gone |
| `api.poap.tech/metadata/{drop}/{token}` | up, no key |
| `assets.poap.xyz` artwork | up |
| `public.compass.poap.tech/v1/graphql` | up, no key, 100 rows per page |
| `poap.gallery`, `collectors.poap.xyz` | redirect to the poap.xyz home page |
| Gnosis chain | the tokens themselves, permanent |

Re-running `scripts/compass_harvest.py` and `scripts/download_media.py` refreshes everything
while those sources last.
