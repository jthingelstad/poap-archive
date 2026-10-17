# Design: a POAP time capsule

A proposal for what to build from this archive, written 2026-10-17 against `BRIEF.md`.
Nothing here is decided for Jamie; the decisions Jamie owns are collected at the end.
Working prototypes of the two core pages are at `capsule/index.html` (the timeline,
`python3 -I scripts/build_capsule.py`) and `capsule/network.html` (the network,
`python3 -I scripts/build_network.py`). The site will be at **poap.thingelstad.xyz**.

## Summary

Build a static site with one spine and three views:

1. **The timeline** is the site. One stream, year by year, with two sides: what Jamie
   collected *from* the world on the left, what Jamie put *into* the world on the right,
   and Jamie's writing plus POAP's own milestones down the middle.
2. **Collector** and **issuer** are not two timelines. They are two overview pages that
   look at the same years from each side, and the two sides of every drop page.
3. **The network** is a page about the 639 people who collected Jamie's drops, drawn as
   a bipartite graph of drops and people, and shaped by a privacy choice Jamie has not
   made yet.

Three findings from the data changed the design:

- **The two sides overlap almost completely.** Jamie minted 129 of the 130 drops Jamie
  made. A mirrored timeline that puts every token on the left and every drop on the right
  shows the same artwork twice. So the left side is the 130 tokens from *other people's*
  drops and the right side is the 130 drops Jamie made, each with its fan-out of mints.
  That split is clean, and it is the real story: in and out.
- **Jamie was an on-ramp.** Of the 639 people, 227 hold exactly one POAP in total. Jamie's
  drop was the only one they ever minted. Another 205 hold five or fewer. The median
  collection size is 1. The network page should lead with that, not with a graph.
- **The sides have different rhythms.** Collecting is steady, about 50 tokens a year.
  Issuing is spiky: 57 drops in 2025, 40 of them the 612 POAP Challenge created on one day.
  The timeline needs grouping for campaigns and year chapters to carry the narrative.

## 1. Form: Astro, on the nnxyz pattern

Revised 2026-10-17 after reading `jthingelstad/nnxyz` and `jthingelstad/thingelstad.xyz`.
The earlier "Python generator" recommendation is withdrawn: it would mean a bespoke
templating, deploy, media and validation layer that nnxyz already has.

**Recommendation: a new repository, `jthingelstad/poap.thingelstad.xyz`, built with Astro
and TypeScript, with nnxyz's infrastructure and tooling copied over and renamed.** This
archive stays what it is: the capture and the Python data layer. The site consumes a slim
export from it.

Why nnxyz is the sibling, not the 11ty sites:

- Same shape. An archive of artwork that never changes, a gallery over it, Tinylytics with
  per-item kudos, a private versioned bucket for sources, a public write-once media
  bucket behind CloudFront, GitHub Actions deploying main through OIDC with a role that
  cannot touch media or IAM. Every one of those is a decision already made and tested.
- Reusable almost verbatim: `infra/storage.json`, `site.json`, `delivery.json`,
  `certificate.json` (14 occurrences of the project name to rename), `tools/deploy.mjs`,
  `media.mjs`, `delivery-plan.mjs`, `hydrate-collection.mjs`, `validate-site.py`,
  `validate-infra.mjs`, `write-revision.mjs`, `test-built-site.mjs`,
  `.github/workflows/ci.yml`, the Tinylytics gate in `Layout.astro`, `Kudos.astro`, and the
  ESLint, Prettier and Ruff configuration. About 1,200 lines of tooling that would
  otherwise be rewritten.
- Astro fits the two interactive pages. The timeline and network prototypes are plain
  HTML, CSS and a little script; they port into Astro components as they are, with the
  data typed from JSON at build time so a drift in the export fails the build instead of
  the page. 11ty would carry the same HTML but none of the typing or the tooling.
- Static output, `trailingSlash: 'always'`, sitemap, `llms.txt`, Open Graph, a light and
  dark switch: all conventions nnxyz already settled.

If Jamie still prefers 11ty, the data contract and URL scheme in sections 2 and 3 do not
change; only the templating layer does.

What is different from nnxyz, and how to handle it:

- **The source is a git repository, not a tarball.** `poap-archive` already commits the
  artwork. The site repo should not clone it at build. Instead `scripts/export_site_data.py`
  in this archive writes a JSON-only bundle (about 5 MB) that is committed into the site
  repo's `data/` with the archive commit SHA it came from. Media is published to the web
  bucket once, from this archive, with the same `media.mjs` flow.
- **Animated GIFs.** 30 drops have GIF artwork. Publish the original GIF as the archival
  key and a still WebP for grids; drop pages show the GIF.
- **People pages.** nnxyz has none. `/people/<address>/` is new, keyed by address (the
  stable identifier) and titled by ENS name.

## 2. Data contract

Freeze this before any page is built. The export is the only thing the site reads, and
the two prototypes are the spec for what it must contain.

| File | Rows | What |
|---|---|---|
| `drops.json` | 130 | id, name, series slug, event date, created date, city, virtual, description, artwork key, mint count, collector count, first and last mint, moments count, Jamie's own token id, Jamie's posts about it |
| `tokens.json` | 259 | token id, drop (id, name, artwork key, supply), minted date, wallet, chain, Jamie's mint post, own-drop flag |
| `people.json` | 639 | address, ENS name, total POAPs, drops held with first mint date, birthdays attended, 612 finish time |
| `mints.json` | 2,072 | person, drop, time: the edges |
| `events.json` | 3,305 | the timeline rows as today, plus the POAP company milestones with `side: world` |
| `writing.json` | 471 | essays, Weekly Thing issues, announcements, the 25-row advice table with "shipped" |
| `moments.json` | 266 | drop, author (address and ENS), date, text, media count; photos where Jamie supplies them |
| `series.json` | 13 | slug, label, color, drop ids, description |
| `layout.json` | 769 | node positions for the network, computed here with numpy so the site build needs no numpy |
| `media.json` | about 900 | every published key with SHA-256, width, height and MIME type |

Prose is content, not data: chapter titles and quotes, the closing essay, and the series
descriptions live as Markdown in the site repo's `content/`, so a word change never touches
code or the export.

## 3. URLs

Fixed now, because Tinylytics kudos, cross-links and the sitemap depend on them.

```
/                       Home: the six chapters, the numbers, the five essays
/timeline/              All years (the prototype)
/timeline/2023/         One year
/drops/<id>/            One drop Jamie made: both sides, collectors, moments, kudos
/tokens/<id>/           One token Jamie collected from someone else's drop
/people/<address>/      One person: ENS name as title, their path through Jamie's drops
/network/               The graph (the prototype)
/series/<slug>/         Birthdays, Weekly Thing, 612 Challenge, Family, SPS, Minnebar, ...
/collected/  /issued/   The two overview pages
/writing/  /writing/advice/  /poap/  /about/  /llms.txt  /sitemap-index.xml
```

Kudos buttons use `data-path` equal to the drop's canonical path, private counts, as nnxyz
does. The timeline's drop cards link to `/drops/<id>/`, which links to `/network/#drop-<id>`.

## 4. Information architecture

The URL scheme in section 3 is the map. What each page holds:

| Page | Holds |
|---|---|
| `/` | The story in six chapters, the numbers, the five essays |
| `/timeline/`, `/timeline/<year>/` | The two-sided stream (prototype: `capsule/index.html`); the home page links each chapter to its year |
| `/collected/` | Collector view: 259 tokens, grid by year, firsts, rarities, places |
| `/tokens/<id>/` | One token from someone else's drop: art, the drop, when and where, Jamie's mint post |
| `/issued/` | Issuer view: 130 drops in a dozen series, mint totals and curves |
| `/drops/<id>/` | One drop Jamie made: art, description, mint curve, moments with authors, posts, collectors by name, kudos |
| `/people/<address>/` | One person: ENS name, total POAPs, their path through Jamie's drops |
| `/series/<slug>/` | Birthdays, Weekly Thing, 612 Challenge, Family, SPS, Minnebar, Things 4 Good, You've met Jamie, Community |
| `/network/` | The graph (prototype: `capsule/network.html`), the on-ramp, the regulars, the 612 finishers |
| `/writing/`, `/writing/advice/` | Jamie on POAP: the five essays, every post by year; "What I told POAP" beside what shipped |
| `/poap/` | POAP the company, 2019 to 2026, from `research/poap-company.md` |
| `/about/` | Wallets, sources, what is lost, how it was captured, colophon |

## 5. The timeline

The prototype in `capsule/index.html` is the proposed layout. What it does, and why:

- **Two sides, one time axis.** Rows are days. A day with a collected token on the left
  and an essay in the middle reads as one moment. Wide screens get three columns;
  phones get one stream with colored edges for side.
- **Drops sit at their event date, not their creation date.** Night of Crypto was created
  in July for an October event; TeamSPS Cyberweek 2022 was created in April 2023 for a
  November 2022 event. The event date is the human one. The mint span (first mint to last
  mint) is shown under each drop, and some are long: SPS TechJam 2021 was still being
  minted in February 2023; the 53rd Birthday ran from January to June.
- **The 2,087 mints by others are not cards.** They are the counts on each drop and the
  "mints by N people" line in each chapter header. On the drop page they become a mint
  curve.
- **Campaigns are grouped.** The 612 POAP Challenge is one expandable card per side: 40
  drops issued, 31 visits collected across the summer. The Airport Rally tokens in 2026
  stay as single cards because they are the last seven things Jamie collected, and they
  are the ending.
- **Writing is attached where it belongs.** The 262 syndicated mint posts become a "post"
  link on the token card they describe. The 40 drop announcements become links on their
  drop card. Essays, Weekly Thing issues and notes stay in the spine. The 2023 bulk move
  of 88 tokens into poap.thingelstad.eth is one spine note, not 88 transfer rows.
- **POAP's milestones are in the spine, in black.** The seed round, paid issuance, the
  Airport Rally, maintenance mode, the last drop, the wind-down, the final snapshot, and
  this capture. Jamie's story and POAP's story are read against each other.
- **Each year opens with its numbers and one of Jamie's sentences.** The six chapter
  titles and quotes in the prototype are a draft for Jamie to rewrite.

Things the prototype leaves for the real build:

- Per-year pages. The single page is 190 KB of HTML and lazy-loads 260 images; fine for a
  prototype, slow on a phone over cellular.
- A filter by series and by place (in person or virtual). The side toggles exist.
- Moments on collected drops (13) and moments by others on Jamie's drops (185 of 253).
- The 2026 ending needs an essay. See section 7.

## 6. Collector and issuer views

**Collector page.** The 259 tokens as a grid by year with the same thumbnails, then a few
reads that the data supports:

- Firsts and lasts: the ENS 4th Anniversary vote on 2021-06-07, the 200th POAP at the
  Minneapolis Institute of Art on 2025-08-17, the last at Seattle-Tacoma on 2026-07-06.
- Places: 93 virtual, 75 in Minneapolis, then New York, Berlin, Miami Beach, Warsaw,
  Toronto, Amsterdam, Barcelona, Nashville. A small map or just a list.
- Rarity from `network/drop_supply.json`: "one of 2,153" for the ENS vote, "one of 1" for
  the TeamSPS New Hire Coffee. A sortable table.
- Wallets: 255 tokens at poap.thingelstad.eth, 3 at thingelstad.eth, 1 at the onpoap.eth
  test wallet; 257 on Gnosis, 1 on mainnet, 1 on ApeChain.

**Issuer page.** The 130 drops in about a dozen series, with totals: 2,216 tokens minted,
642 collectors, 316 email reservations never minted. Reads worth building:

- The mint curve for each drop (days since event vs cumulative mints), which shows the
  difference between a live event (Minnebar 17: 71 of its 81 mints in the days around the event) and a tradition
  (birthdays: a month-long tail of reservations).
- Series pages that are small stories: five birthdays and the 7 people who came to all
  of them; four Magic Pines summers; 12 Weekly Thing drops from issue 200 to the Reddit
  Revival; the 612 Challenge with its 9 finishers.
- The one Jamie wishes he could burn: Reading Things First 100, farmed. Show it, with the
  "This event is invalid" note from Jamie's own events page.
- The two drops Jamie never minted himself: the 612 Congratulations token and Lake Geneva
  Loop Legends.

Both pages share one component: the drop page. It shows both sides for a drop Jamie made
(the drop, and Jamie's own token of it) and one side for a drop Jamie only collected.

## 7. The network

The data says this is a story about reach, not a graph. What `network/` supports:

| Fact | Number |
|---|---|
| People who hold a token from one of Jamie's drops | 639 (zero address and Jamie's wallets removed) |
| With a primary ENS name | 105 |
| Collected exactly one of Jamie's drops | 428 |
| Collected five or more | 82 |
| Collected ten or more | 37 |
| At all five birthdays | 7 (and 7 more at four) |
| Hold exactly one POAP in total, so Jamie's was their only one | 227 |
| Hold five or fewer in total | 432 |
| Hold 100 or more in total | 76 |

The inner ring is family (three Thingelstad names at 85 to 89 drops each), then
quinnchrest.eth at 56, then ten people in the 30 to 48 range who are mostly SPS
colleagues without ENS names.

**Recommended view: a bipartite graph, drops and people.** The prototype in
`capsule/network.html` is this. Drops are the labeled, colored nodes (by series, sized by
mints); people are unlabeled gray dots sized by the log of their total collection; one
edge per mint. The layout is computed at build time with a force-directed pass and
written as static SVG, so the page is a picture before it is an app. The structure draws
itself: the 612 Challenge is a dense cluster at the center, the SPS drops form their own
cluster of colleagues, and the farmed Reading Things First 100 drop sits detached with
its halo of 96 one-drop wallets. Clicking a drop lights up its collectors and the other
drops they hold, with a link to that drop on the timeline; clicking a person shows their
path through Jamie's drops. No person-to-person edges. The page then tells the four
stories under the diagram:

1. **The on-ramp.** 227 people whose only POAP is one of Jamie's. A single bar.
2. **The regulars.** Birthday attendance across five years, Weekly Thing anniversaries,
   Magic Pines summers. A small matrix: people with five or more drops as rows, series
   as columns.
3. **The 612 finishers.** Nine people, with the order they finished in from mint times.
4. **We were both there.** Co-attendance at drops Jamie did not make. Filter
   `co_attendance.json` to drops outside `created_drops.json` and drop the bulk wallet
   (35,359 POAPs) and the zero address. The top shared outside events are the ENS DAO
   Delegator 2022 drop (40 people) and the Times Square redeemable NFT (65). Most of the
   rest are SPS drops made by colleagues, which is a story about TeamSPS.

Edges that do not matter: person-to-person edges. Nobody needs to see which two of
Jamie's collectors also share a drop with each other; that is the hairball.

## 8. Privacy: decided

**Jamie decided on 2026-10-17: option C.** It is all on the public blockchain. Show the
primary ENS name where one is set, else the shortened wallet address (`0x018a…3c47`), as
POAP itself did. The network prototype does this. The options that were on the table:

| Option | What shows | What it costs |
|---|---|---|
| A. Counts only | Rings, bars and matrices with no labels at all | The network page is a chart, not people. Family regulars are anonymous. |
| B. ENS names only | The 105 named people by name; the other 534 as unlabeled dots | Names are the one thing those people chose to make public. Still, 105 people did not opt into a tribute site. |
| C. ENS names plus truncated addresses | POAP's own convention (`0x018a…3c47`) for the unnamed | Every holder is identifiable with one lookup. Closest to what POAP itself showed. |
| D. Family and opt-in | Name the family and anyone Jamie asks; everyone else as counts | Most work. Most defensible. Fits a tribute. |

Related calls that follow from it:

- Moments written by others (185, of which 29 have text and 184 had photos): quote the
  text without the author, or not at all.
- Drop pages: show a collectors list, a count, or a mint curve only.
- Jamie's own four wallets are already in the README; the about page can list them.
- `research/interactions-PRIVATE.md` never appears, in any form. The POAP company page
  cites only the public sources in `research/poap-company.md`.

Moments written by others are quoted with their author's name (Jamie, 2026-10-17).

## 9. Voice

Jamie's writing is the narration, and most of it is already extracted:

- **Chapter quotes.** `writing/ESSAYS.md` has 89 verified quotes. The prototype uses six.
- **"What I told POAP."** The 25-row advice table, each row linked to the post, set
  against the company timeline. Seven shipped (treasure hunts, location drops, reminder
  emails, embedded wallets, collections, easier distribution, usable onboarding), one
  Jamie built himself (RSS), the rest never came. This page is the most original thing
  the site can say about POAP as a product, and it is already written.
- **The five essays** as the home page's reading list.
- **Mint commentary.** Nine of the 262 mint posts have more than the boilerplate line;
  those nine are good card captions (the 200th POAP, the first 612 winner, the recursive
  selfie at the Grain Belt sign).

What is missing: **Jamie has written nothing about the wind-down.** The archive's last
protocol writing is Flight Path in March 2026. The capsule ends on the last Airport Rally
token in July and POAP's announcement in August, and then needs Jamie's own last word.
A suggested shape, since it is Jamie's to write: what POAP got right, what Jamie asked for
and whether it mattered, what the 639 people mean, and what should replace it. Jamie's
2022 line is the thesis already: "POAPs are a time capsule of something of note."

## 10. Lost things and gaps

- **Moment photos.** 263 media records, none served. 79 were posted by Jamie (in 81 moments), with
  timestamps to the second. Export from Photos by date range and match on time; the
  capsule can then show Jamie's photos on the drop pages. The other 184 belong to other
  people and are gone unless they share them.
- **Drops Jamie may have missed.** 130 came from the POAP Events page and the seven
  collections. The snapshot has no issuer column, and Compass needs an issuer id Jamie
  does not have. A cheap check: search the full `poap.sqlite` for drops whose
  `drop_url` or description mentions thingelstad.com, Weekly Thing, Things 4 Good,
  Minnebar, Magic Pines or SPS, and compare with the 130.
- **Email reservations.** 316 reserved-but-never-minted tokens across 91 drops. That is
  the "invitations never accepted" number for the issuer page.
- **Writing after July 2026.** None about POAP. See section 7.
- **The 612 site and the Airport Rally site.** `writing/sites/612.poapchallenge.com/` is
  mirrored; flightpath.poaprally.com and airport.poaprally.com are not in the archive.
  If Jamie has the build output, add it alongside.
- **Jesus, Krampus and POAP KINGS.** Some collected drops are other people's "you've met
  me" tokens and Jamie's Clash Royale clan tokens. They are real tokens and stay, with
  the clan ones labeled so nobody reads "POAP KINGS" as a protocol group.

## 11. Hosting and permanence

- **Domain.** Decided: `poap.thingelstad.xyz`. DNS for `thingelstad.xyz` is Namecheap
  BasicDNS with DNSSEC (see `thingelstad.xyz/DNS.md`); the site needs one CNAME `poap` to
  the CloudFront hostname and one ACM validation CNAME, kept for renewal. Jamie makes DNS
  changes.
- **Stacks**, following nnxyz: `poap-storage` (private archive bucket, public-through-
  CloudFront web bucket, both versioned and encrypted), `poap-certificate` (us-east-1),
  `poap-site` (distribution, cache policy, access log, 5xx alarm to the family topic),
  `poap-delivery` (the OIDC role for `jthingelstad/poap.thingelstad.xyz`, main only,
  denied `PutObject` on media prefixes). Tags as in `infra/deployment.json`.
- **Media prefixes.** `art/` (originals, GIF where animated), `raster/` (WebP at 160, 320,
  640, 1200), `records/` (per-drop JSON downloads). Published once with `If-None-Match: *`,
  immutable cache headers, recorded in `media.json`.
- **Tinylytics.** Registered 2026-10-17: site 3838, "POAP Capsule",
  `https://poap.thingelstad.xyz`. The embed, supplied by Jamie, is a public browser
  identifier, not a credential:

  ```html
  <script src="https://tinylytics.app/embed/nQYJ5URe6Y3umkYW7HQN.js" defer></script>
  ```

  Load it as nnxyz does: one script in the shared layout, only when
  `PUBLIC_TINYLYTICS_ENABLED=true` and the page is on the production hostname, so local
  review, CloudFront preview URLs and browser tests send nothing. Kudos per drop with
  `?kudos=custom`, `class="tinylytics_kudos"` and `data-path` set to `/drops/<id>/`, private
  counts. Copy this into the site repo as `design/tinylytics.md`.
- **Permanence.** Submit to the Wayback Machine at launch. The archive bucket keeps the
  export bundle by SHA-256 as nnxyz keeps its collection. The built site is also a folder
  that works from `file://` because every page is static.

## 12. Plan, in the order that avoids rework

Each step is finished before the next starts, and nothing later changes what an earlier
step produced.

| Step | Work | Where | Needs from Jamie |
|---|---|---|---|
| 0 | Remaining decisions below | | Chapter text, closing essay, photo export |
| 1 | `scripts/export_site_data.py` and the contract in section 2; the network layout moves into it | poap-archive | Nothing |
| 2 | Bootstrap the site repo from the nnxyz skeleton: infra renamed, tools copied, CI, an empty Layout. Deploy it so DNS, certificate and the delivery role are done first; they have external waits | new repo | DNS records, one reviewed change set |
| 3 | Publish media once from this archive; commit `media.json` | both | Nothing |
| 4 | Pages: Layout and the drop page first (the hinge), then timeline per year, network, people, tokens, series, collected and issued, writing and advice, POAP, about | site repo | Review at the drop page and again at the timeline |
| 5 | Content: chapters, series descriptions, the closing essay | site repo | The essay |
| 6 | Launch: Tinylytics on, Wayback, README in both repos | | Nothing |

The prototypes in `capsule/` are the spec for steps 1 and 4 and are retired once the site
pages exist.

## Decisions Jamie owns

```
Time capsule decisions:
	- Privacy: C, ENS name or shortened address @done
	- Domain: poap.thingelstad.xyz @done
	- Moments by others: quote with the author's name @done
	- Form: Astro in a new repo jthingelstad/poap.thingelstad.xyz, on the nnxyz pattern (recommended; 11ty keeps the same contract and URLs)
	- Tinylytics: site 3838, embed nQYJ5URe6Y3umkYW7HQN @done
	- Chapter titles and quotes: keep or rewrite the six drafts in build_capsule.py
	- Export moment photos from Photos for the 81 you posted (timestamps in compass/moments.json)
	- Write the closing essay on the wind-down
	- Confirm whether 2026-07-31 should appear as "the sunset" or as "the last drop"
```
