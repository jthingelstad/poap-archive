# POAP, the company: background research

Compiled 2026-10-17 for Jamie's POAP archive. Every claim carries a source. Where
sources disagree, the conflict is noted. **Unverified** means I could not confirm
it from a primary or reliable secondary source. Times are UTC unless marked.

## Summary

POAP (Proof of Attendance Protocol) began as a hackathon project at ETHDenver in
February 2019. Patricio Worthalter, an Argentine entrepreneur, came up with it. The
first drop was about 100 ERC-721 badges for hackathon attendees. Ethereum gas costs
pushed minting to the xDai sidechain (later Gnosis Chain) in late 2020. POAP Inc.
was incorporated around 2021 (sources say anywhere from August 2020 to late 2021),
with Isabel Gonzalez as COO and later co-founder and general manager. In January
2022 it announced a $10M seed round co-led by Archetype and Sapphire Sport. In
April 2023 it began charging commercial issuers, at roughly $1 per POAP. Through
2023 and 2024 it shipped POAP Drops, Collections, Moments, the POAP Home app,
email onboarding with embedded wallets, GPS minting, Airship and the Compass API.
Its agency arm, POAP Studio, served brands such as Coinbase, American Express,
Bayer and Porsche.

Growth stalled. On 2026-03-12 Gonzalez announced that POAP would enter
**maintenance mode on 2026-03-16**: no new issuers and no active development. On
**2026-08-03** she announced on X that POAP was **winding down**. She blamed
crypto's funding cycles and distribution dynamics. By then nearly 7.6 million
POAPs had been minted by about 46,000 issuers. The tokens stay on-chain. The
gallery, collectors site, help center, curation site and docs now redirect to
poap.xyz.

The archive at **poaparchive.com** has the most official standing of the archives.
Its domain was registered on 2026-06-30 with the registrant organization listed as
**POAP Inc**, and it offers a 15 GB SQLite plus WebP snapshot. Two community
archives sit beside it: **poap.in** (POAPin Archive, by "Kira" of Glory Lab, Tokyo)
and **POAP Saver** (Ben Meadows, IPFS).

**On the 2026-07-31 date:** I found no public statement that names July 31 as the
sunset date. The public record has two dates: maintenance mode on 2026-03-16 and
the wind-down announcement on 2026-08-03. Several things do point to a cutover
around the end of July:

- the archive domain was registered on 2026-06-30;
- the first archive snapshot was taken on 2026-07-02;
- POAPin started its archive repo, headlined "POAP is dead", on 2026-07-22;
- the newest drop in the official snapshot was created at **2026-07-31 09:39 UTC**.

Treat "sunset 2026-07-31" as Jamie's working date, backed by that evidence, but not
as a published date.

## Timeline

| Date | Event | Source |
|---|---|---|
| Late 2018 | Worthalter conceives POAP (unverified, single wiki source) | [IQ.wiki: Patricio Worthalter](https://iq.wiki/wiki/patricio-worthalter) |
| 2019-02 (ETHDenver, drop starts 2019-02-15) | First POAPs: about 100 ERC-721 badges claimed at the ETHDenver hackathon. It is drop #14 in the official snapshot, which holds 89 tokens. One retrospective says a prototype was on mainnet within 72 hours and "several hundred" collected it (unverified) | [The Block, 2026-08-03](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years); [crypto.news, 2026-08-04](https://crypto.news/poap-shuts-down-despite-coinbase-and-amex-adoption/); [LikeCoin Substack, 2026-08-10](https://likecoin.substack.com/p/poap); local `snapshot/poap.sqlite` |
| 2019-05-28 | Earliest `created_at` in the official snapshot. Drops 1 to 13 are retroactive badges for earlier events (DappCon 2018, DevCon1 to 4, #DeFi Summit) | local `snapshot/poap.sqlite` |
| 2020 (DeFi Summer) | Gas spikes. Worthalter reportedly spent an estimated $2M to $3M on fees and infrastructure (unverified) | [LikeCoin Substack](https://likecoin.substack.com/p/poap) |
| 2020-10 | Minting contract moves to the xDai sidechain, now Gnosis Chain | [IQ.wiki: POAP](https://iq.wiki/wiki/poap); [BlockEden, 2026-04-23](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/) |
| 2020-08 or 2021 | POAP Inc. incorporated. Sources conflict: Aug 2020 (IQ.wiki person page), 2021 (IQ.wiki POAP page, CryptoBriefing, Unchained), "late 2021" (LikeCoin) | [IQ.wiki](https://iq.wiki/wiki/patricio-worthalter); [CryptoBriefing](https://cryptobriefing.com/poap-shuts-down-five-years/) |
| 2021-10 | "POAP farmers" and DDoS-style attacks overwhelm the app and force POAP to scale back operations | [Decrypt, 2022-01-19](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise) |
| 2021-11-30 | Worthalter interviewed by Adam Levy, including his roughly $10M CryptoPunk bid framed as an experiment (via IQ.wiki, not checked against the recording) | [IQ.wiki](https://iq.wiki/wiki/patricio-worthalter) |
| 2021 | POAP Studio agency starts. Its 2023 recap says Studio "celebrated two years in business" | [poap.news 2023 in review](https://www.poap.news/2023-in-review/) |
| 2021-12-08 / 2022-01-19 | $10M seed round. CB Insights dates it 2021-12-08. It was announced 2022-01-19, co-led by Archetype and Sapphire Sport | [Decrypt](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise); [CB Insights](https://www.cbinsights.com/company/poap/financials) |
| 2022-08-07 | Glory Lab's POAPin (third-party explorer, later poap.in) repo created | [GitHub glorylab/POAPin](https://github.com/glorylab/POAPin) |
| 2022-09-15 | The Merge. EthStaker's donation POAP (6,000+ bought, proceeds to Protocol Guild) | [The Block, 2022-09-15](https://www.theblock.co/post/170564/i-attended-the-merge-and-all-i-got-was-this-lousy-poap) |
| 2023-01 | POAP surveys issuers about premium features. Jamie blogs "POAP as a Business" and "Premium Features for POAP Issuers" (2023-01-16) | local `writing/posts/2023-01-16-poap-as-a.html`, `...premium-features-for.html` |
| 2023-04-04 | POAP announces paid commercial issuance from 2023-04-17. It will "likely converge" around $1 per POAP, existing commercial users get about $0.25 for a time, and personal use stays free | [Decrypt, 2023-04-04](https://decrypt.co/125462/paid-poap-proof-of-attendance-ethereum-nft) |
| 2023 | POAP Drops (new issuer interface), POAP Family, POAP Checkout, Commercial Use Policy, artist attribution beta | [poap.news 2023 in review](https://www.poap.news/2023-in-review/) |
| 2023-12 / 2024-01 | New email onboarding beta: email reservations trigger follow-up email and "Create an account" makes a Privy embedded wallet. Jamie tested it on 2024-01-14 and made `thingelstad.onpoap.eth` | local `writing/posts/2024-01-14-new-poap-onboarding.html` |
| 2024 | POAP Home mobile app, Dispenser, GPS minting (first POAP Rally in Tokyo), Airship (POAPs for onchain tips), Moments, minting on Base, Arbitrum and ApeChain | [Year in POAP 2024](https://www.poap.news/year-in-poap-looking-back-on-2024/) |
| 2025 | Jamie counts drops by sequential ID: about 74,298 created in 2022, 71,285 in 2023 and 16,826 in 2024 | local `writing/posts/2025-01-02-poap-event-trends.html` |
| 2026-01-01 | POAP Airport Rally 2026 begins: GPS-minted POAPs at 100+ airports, with a Boarding Pass POAP via Airship | [Airship boarding pass page](https://airship.poap.xyz/poap-airport-rally-2026-boarding-pass) |
| 2026-01 | More than 7.2M POAPs from more than 41,000 issuers | [BlockEden](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/) |
| 2026-03-12 19:47 | Isabel Gonzalez (@izonline) posts the X article "Looking forward to POAP's next chapter" | [X post](https://x.com/izonline/status/2032181803155333626) (read via fxtwitter); [Bored Ape Gazette, Mar 12](https://www.theboredapegazette.com/post/oh-the-places-you-poap-ed-poap-announces-its-going-into-maintenance-mode-as-the-gets-ready-for-its) |
| 2026-03-16 | Maintenance mode. New issuers lose the issuer interfaces. Existing issuers, collector tools, APIs and integrations keep working at reduced resources | same; [TechFlow, 2026-03-14](https://www.techflowpost.com/en-US/newsletter/116752) |
| 2026-06-30 | `poaparchive.com` registered at Gandi. Registrant org: **POAP Inc**, New York | WHOIS lookup, 2026-10-17 |
| 2026-07-02 14:28 | First poaparchive.com snapshot (73,876 drops, 6,218,154 tokens), as POAPin recorded it | [POAPin source inventory](https://github.com/glorylab/poapin-archive/blob/main/docs/source-inventory.md) |
| 2026-07-22 | Kira of Glory Lab creates `glorylab/poapin-archive` ("POAP is dead. Long live POAP!"). Collections snapshot 07-22, Moments 07-23, holdings 07-28 | [GitHub glorylab/poapin-archive](https://github.com/glorylab/poapin-archive) |
| 2026-07-24 | Jamie winds down POAP2RSS, flightpath.poaprally.com and poap-agent-api-docs | Jamie's project memory |
| 2026-07-31 09:39 | Last drop in the official snapshot is created (#229257, "Plages Electroniques 2026"). Drop creation each month had fallen from 400 in Feb 2026 to 99 in July | local `snapshot/poap.sqlite` |
| 2026-07-31 | **Jamie's working sunset date. No public announcement names it (unverified).** (A Worthalter X post that day is unrelated ENS art.) | [Worthalter X post](https://x.com/worthalter/status/2083144703659192366) |
| 2026-08-03 13:43 | Gonzalez announces on X: "After 5+ years, we're winding down POAP." About 934k views | [X post](https://x.com/izonline/status/2084273977938080092); [The Block](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years) |
| 2026-08-03 to 08-04 | Coverage: The Block, CryptoBriefing, crypto.news, Unchained, Times of Blockchain, Molly White's *Web3 is Going Just Great*. Site, collector pages and docs still up on 08-04, with no final service date | [crypto.news](https://crypto.news/poap-shuts-down-despite-coinbase-and-amex-adoption/); [Web3 is Going Just Great](https://web3isgoinggreat.com/single/proof-of-attendance-protocol-shuts-down) |
| 2026-08-04 | Ben Meadows creates POAP Saver (`mdws-org/poap-saver`) | [GitHub mdws-org/poap-saver](https://github.com/mdws-org/poap-saver) |
| 2026-08-06 | POAPin publishes the `archive-data-2026-08-06` supplement release (Collections and Moments media) | [GitHub glorylab/poapin-archive](https://github.com/glorylab/poapin-archive) |
| 2026-08-10 | LikeCoin retrospective "Farewell to POAP's Geek Ethos" | [LikeCoin Substack](https://likecoin.substack.com/p/poap) |
| 2026-08-20 13:42 | Current poaparchive.com snapshot (73,990 drops, same 6,218,154 tokens). Jamie's copy matches the published SHA-256 `aed7ec75...aa3d0` | local `snapshot/poap.sqlite` `snapshot_metadata`; [poaparchive.com](https://poaparchive.com/) |
| 2026-10-17 | poap.gallery, collectors, collections, curation, help and documentation all 301 to poap.xyz. blog.poap.xyz goes to poap.news. home.poap.xyz still offers POAP Home. `media.poap.tech` returns 530 | HTTP checks, 2026-10-17 |

## Origins

- **ETHDenver 2019.** Verified. POAP's own website, as cited by The Block, traces
  the concept to "about 100 ERC-721 badges claimed at an ETHDenver hackathon in
  2019." A more formal project launched in 2021
  ([The Block](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years)).
  ETH Daily calls it "launched at Ethereum Denver 2019"
  ([ETH Daily, 2026-08-03](https://ethdaily.io/eth-daily-news-august-3-2026)).
  The official snapshot has drop #14 "ETHDenver 2019" starting 2019-02-15 with 89
  surviving tokens. Drops 1 to 13 are retroactive badges for earlier Ethereum
  events, from DevCon1 in 2015 to DappCon 2018.
- **Founders.** Worthalter is the founder. His X bio reads "Founder of Proof of
  Attendance Protocol (@poapxyz)" ([fxtwitter read of @worthalter](https://x.com/worthalter/status/2083144703659192366)).
  **Isabel Gonzalez** (X: `@izonline`, formerly `@izgnzlz`, based in New York)
  describes herself as "co-founder and general manager @poapxyz | minting memories
  since 2021" ([X post](https://x.com/izonline/status/2032181803155333626)).
  Decrypt called her COO in January 2022
  ([Decrypt](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise)).
  Her "since 2021" bio suggests she joined at incorporation, not at ETHDenver.
  IQ.wiki also lists Lucas Verra (CTO) and Mariano Rodriguez as co-founders and
  Agustin Lavarello as technical lead (unverified)
  ([IQ.wiki: POAP](https://iq.wiki/wiki/poap)). I found nothing about Gonzalez's
  career before POAP.
- **POAP Inc.** The incorporation date is unsettled: August 2020 (IQ.wiki person
  page), 2021 (IQ.wiki POAP page, CryptoBriefing, Unchained), late 2021 (LikeCoin).
  WHOIS for poaparchive.com puts POAP Inc in New York State. The poap.xyz footer
  still reads "© 2026 POAP Inc", and the About page says the contracts are
  "currently governed by POAP Inc." ([poap.xyz/about-the-protocol](https://poap.xyz/about-the-protocol)).
- **Move to xDai / Gnosis Chain.** This was October 2020 by IQ.wiki's account
  ([IQ.wiki](https://iq.wiki/wiki/poap)), and "late 2020" by LikeCoin's. In the
  final snapshot, 6,096,425 of 6,218,154 tokens (98%) are on `xdai`. 36,520 are on
  Ethereum mainnet. The rest are spread over Base, Arbitrum, Unichain, Celo,
  Mantle, ApeChain, Polygon, Linea and Chiliz
  ([POAPin source inventory](https://github.com/glorylab/poapin-archive/blob/main/docs/source-inventory.md)).
- **Mainnet migration fee.** POAP's help center said collectors could migrate a
  POAP from Gnosis to Ethereum mainnet from its page on POAP Scan, paying the gas
  in ETH themselves. It was a network move inside the same wallet, not a transfer
  (help article 9673605937549, seen in search results; the help center now
  redirects to poap.xyz). I found **no evidence of a separate fee charged by POAP**
  beyond gas, so that part is unverified. Jamie's 2023 wishlist proposed "credit
  for 1 mainnet migration a month" as a paid collector perk, which suggests the gas
  cost was a real barrier.

## Funding

- **Seed, $10M.** Announced 2022-01-19 and **co-led by Archetype and Sapphire
  Sport**. Other participants were Collab Currency, 1kx, Libertus Capital, Red Beard
  Ventures, 6th Man Ventures, Delphi Digital, A Capital, Sound Ventures, Advancit
  Capital and The Chernin Group. More than 2 million POAPs had been minted at that
  point. Gonzalez: "We intend for this raise to be the first along the road to our
  building a better POAP"
  ([Decrypt, Jason Nelson](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise)).
  The Defiant also covered it ([The Defiant](https://thedefiant.io/news/nfts-and-web3/poap-nfts-events-fundraise)).
- **Your guess was right:** about $10M, early 2022, led by Archetype (as co-lead).
- **Conflicts.** CB Insights dates the round to 2021-12-08 as "Seed VC - II"
  ([CB Insights](https://www.cbinsights.com/company/poap/financials)). IQ.wiki
  names Delphi Digital as co-lead in place of Sapphire Sport and adds Fabric
  Ventures. I trust Decrypt's contemporaneous list.
- **Valuation.** Not reported anywhere I found.
- **Later rounds.** None found. Both CryptoBriefing and LikeCoin say the $10M
  bought time but not profitability, and that refusing to launch a token cut off
  the usual crypto funding route
  ([CryptoBriefing](https://cryptobriefing.com/poap-shuts-down-five-years/);
  [LikeCoin](https://likecoin.substack.com/p/poap)).
- **Worthalter's personal wealth.** On-chain trackers report large ETH holdings
  and sales: 2,000 ETH sold in September 2025 with about 41k ETH left, and 4,000
  ETH moved in October 2026. These are third-party wallet-attribution reports
  (unverified) ([IQ.wiki](https://iq.wiki/wiki/patricio-worthalter);
  [blockchain.news](https://blockchain.news/flashnews/patricio-worthalter-transfers-another-4000-eth)).
  The point for the archive: POAP's money problem was the company's, not its
  founder's.

## Product timeline

- **poap.gallery / collectors / app.** poap.gallery (drops) and
  collectors.poap.xyz (wallets; app.poap.xyz redirected there) were the public
  browsers that Jamie's posts linked from 2021 to 2026. I could not find launch
  dates. As of 2026-10-17 both 301 to poap.xyz.
- **POAP Home** (iOS and Android). The official mobile app, launched in 2024, with
  Dispenser and Moments notifications
  ([Year in POAP 2024](https://www.poap.news/year-in-poap-looking-back-on-2024/);
  [App Store](https://apps.apple.com/us/app/poap-home/id6478871538)).
  home.poap.xyz still serves the download page.
- **Collections.** Announced on the blog in "Connect the Drops with POAP
  Collections" (the post is gone; blog.poap.xyz now redirects to poap.news). Anyone
  with a wallet could make a titled collection of drops. The launch date is
  unverified. The Airport Rally 2026 ran as a Collection. POAPin preserved 2,016
  collections with 35,954 items.
- **Moments.** Photos, video, audio, links and notes attached to a POAP or drop,
  grouped into "Capsules." Highlighted in 2024
  ([Year in POAP 2024](https://www.poap.news/year-in-poap-looking-back-on-2024/);
  [help article](https://help.poap.xyz/hc/en-us/articles/27197060755725-How-to-Create-Edit-and-Share-Moments)).
  Moment media lived on `media.poap.tech`, which now returns a Cloudflare 530.
  POAPin captured 30,548 media objects in July 2026.
- **Compass.** A GraphQL indexer API (public endpoint
  `public.compass.poap.tech/v1/graphql`). The SDK's `PoapCompass` provider used it
  ([npm @poap-xyz/poaps](https://npmjs.com/package/%40poap-xyz%2Fpoaps)). From
  March 2022 POAP used Goldsky for indexing
  ([IQ.wiki](https://iq.wiki/wiki/patricio-worthalter);
  [Goldsky case study](https://goldsky.com/case-studies/poap-goldsky)). The launch
  date is unverified. On 2026-10-17 it still answers without a key at 100 rows a
  page, and Jamie's harvest used it.
- **Email reservations and onboarding.** Claim codes could always be reserved to
  an email without minting. A beta in late 2023 and early 2024 added follow-up
  emails and a "Create an account" flow that made a Privy embedded wallet with an
  `*.onpoap.eth` name. Jamie tested it on 2024-01-14 (local post). The official
  snapshot records 495,531 email reservations, of which 184,643 were minted and
  **310,888 never were** (`email_reservation_stats`, local).
- **POAP Studio.** The brand and agency arm, running "two years in business" by
  the end of 2023. Its clients included Bayer, Sibos/SWIFT, Sofar Sounds, Skoda,
  Porsche, Shell and Ubisoft. It also tested POAP Passport and Lu.ma distribution
  ([2023 review](https://www.poap.news/2023-in-review/);
  [2024 review](https://www.poap.news/year-in-poap-looking-back-on-2024/)).
- **Drops, curation and the issuer interface.** In 2023 a new "POAP Drops" issuer
  interface let issuers choose a distribution method at setup. A Curation Body
  reviewed every drop by hand, within 24 to 72 hours, with an appeals process.
  Drops could be rejected for low-effort art, vague descriptions, too many mint
  links or farmable distribution
  ([curation guidelines](https://curation.poap.xyz/guidelines/policy-and-process),
  now redirected). The review was a response to the 2021 farming crisis. Founder
  quote on farming: "spamming requests for codes, secret words, or direct links to
  claim POAPs for events you did not attend"
  ([Decrypt](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise)).
- **Other 2023 and 2024 products.** POAP Family (shared collectors), POAP
  Checkout (selling POAPs), POAP Station and Kiosk, POAP Scan, GPS minting, Airship
  (POAPs for onchain tips), and multi-chain minting
  ([2023](https://www.poap.news/2023-in-review/),
  [2024](https://www.poap.news/year-in-poap-looking-back-on-2024/)).
- **Partnerships.** Coinbase, American Express (U.S. Open golf and tennis, ACL
  Fest), Warner Music Group, Bayer, Adidas, Porsche, TIME, Starbucks, Mastercard,
  Google Cloud, JP Morgan Chase. Devcon got an 8,000+ collectible activation, and
  ETHDenver 2023 minted 26,000+
  ([Unchained](https://unchainedcrypto.com/poap-winds-down-after-five-years-and-nearly-7-6-million-onchain-badges/);
  [2023 review](https://www.poap.news/2023-in-review/)).
- **Stats over time.**

  | Date | Tokens minted | Issuers | Source |
  |---|---|---|---|
  | Jan 2022 | 2M+ | n/a | [Decrypt](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise) |
  | Apr 2023 | 6.5M+ | n/a | [Decrypt](https://decrypt.co/125462/paid-poap-proof-of-attendance-ethereum-nft) |
  | mid-2023 | 6.7M+ | 37,000+ | search-result summary (unverified) |
  | Jan 2026 | 7.2M+ | 41,000+ | [BlockEden](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/) |
  | Aug 2026 | ~7.6M | 46,210+ | [The Block](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years), citing poap.xyz |
  | Snapshot 2026-08-20 | 6,218,154 token rows held by 1,236,466 addresses; 73,990 public drops (drop IDs reach 229,257) | n/a | local snapshot |

  The poap.xyz homepage HTML shows "1,000,000 POAPs minted / 10,000 Issuers." That
  looks like a static placeholder for a JS counter, not a real figure.
- **Issuance trend** (drops created per year in the official snapshot):
  2019 74; 2020 477; 2021 11,811; **2022 27,172 (peak)**; 2023 17,542; 2024 8,209;
  2025 6,994; 2026 1,711 (to 07-31). Tokens minted per year: **2021 2.95M (peak)**;
  2022 2.03M; 2023 616k; 2024 296k; 2025 244k. The snapshot's token table stops at
  2026-04-14, so 2026 token counts are incomplete.

## Patricio Worthalter

- **Background.** An Argentine (Buenos Aires) serial entrepreneur. He co-founded
  Dift (CTO, 2013 to 2017), founded Millares (2015), and led OrderApp, a
  restaurant POS, at Millienium S.A. (2015 to 2018). He came into crypto around
  2017 ([IQ.wiki](https://iq.wiki/wiki/patricio-worthalter);
  [LinkedIn](https://www.linkedin.com/in/worthalter/)). Details come from a wiki
  built on LinkedIn and Crunchbase, so treat them as lightly verified.
- **Roles.** Founder of POAP and, by some accounts, CEO of POAP Inc. Gonzalez was
  the public face of the company's operations and its end. He was a hands-on
  evangelist, handing out personal POAPs in Miami, Denver, London and elsewhere
  ([LinkedIn posts](https://www.linkedin.com/posts/worthalter_im-in-miami-for-the-week-find-me-to-get-activity-6871520823832834048-tRjo);
  [Ben Edgington on X](https://x.com/benjaminion_xyz/status/1768364491710882142)).
  He is also an angel investor (Taiko, Salsa, Evertas, Laylo, tokenproof, per
  IQ.wiki).
- **Talks and interviews.** Two Adam Levy interviews (2021-11-30); Pragma Lisbon
  2023; the podcast "#28 Patricio Worthalter, let's POAP"
  ([YouTube](https://www.youtube.com/watch?v=olYVI19_dmE)). I found no long-form
  writing by him.
- **On POAP's purpose.** The brand line "POAPs are bookmarks for your life" is his
  framing ([poap.xyz](https://poap.xyz/)). IQ.wiki quotes him: "I believe in a
  future where humans will have a new way to express their identity based on their
  experiences in life" (no primary source found, so unverified). The site's mission
  line: "We mint POAPs so people can own their stories."
- **At the end.** I found no wind-down statement from Worthalter. IQ.wiki
  attributes the 2026-08-03 announcement to him, but that is wrong: it was
  Gonzalez's post.

## Business model struggles and changes

- **Free at the start.** Minting was free and POAP paid the gas, which became
  ruinous in the 2020 DeFi Summer and led to the xDai move.
- **The 2021 farming crisis.** Bots and farmers overwhelmed claims in October 2021
  ([Decrypt](https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise)).
  POAP's answer was manual curation, which cost money and slowed issuers down.
- **Premium survey (January 2023).** POAP surveyed issuers about paid features.
  Jamie's posts that month sketched a $3/mo collector tier, a $20/mo Pro tier, and
  Studio at $500 per event (local posts).
- **Commercial pricing (April 2023).** Commercial issuers were charged per POAP
  from 2023-04-17, at about $1 each. Personal use stayed free, and art projects
  could be subsidized case by case. Gonzalez: "We like people creating true
  precious digital collectibles more than we care that they pay"
  ([Decrypt](https://decrypt.co/125462/paid-poap-proof-of-attendance-ethereum-nft)).
  Drawing the line between personal and commercial was the weak point
  ([BlockEden](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/)).
- **Enterprise via Studio.** Brand deals brought one-off, not recurring, revenue
  ([LikeCoin](https://likecoin.substack.com/p/poap)).
- **No token.** POAP never launched a token. Commentators read that as a
  principled choice that also cut off funding
  ([CryptoBriefing](https://cryptobriefing.com/poap-shuts-down-five-years/)).
- **Competition and design limits.** POAPs were transferable ERC-721s, so they
  were weak as credentials. Galxe, Gitcoin Passport, EAS and ENS each took a slice
  of the use cases ([BlockEden](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/)).
- **Layoffs.** I found no reporting of layoffs at any point, so this is
  unverified. Maintenance mode's "resources will be reduced" is the closest
  statement. Coverage notes there was no staffing update at shutdown
  ([Times of Blockchain](https://www.timesofblockchain.com/news/poap-is-shutting-down-after-five-years/)).

## The wind-down

- **Step 1, maintenance mode** (announced 2026-03-12, effective 2026-03-16).
  Gonzalez's X article "Looking forward to POAP's next chapter" said the platform
  had found a niche but "did not grow much beyond it," and that "digital
  collectibles are still an emerging medium." New issuers lost the issuer
  interfaces. Existing issuers, collector interfaces, APIs and integrations kept
  working, and "some operations may run more slowly." The team would work on "a
  standard for open collectibles" with a canonical implementation, and might
  later connect the old platform to it
  ([X article](https://x.com/izonline/status/2032181803155333626);
  [Bored Ape Gazette](https://www.theboredapegazette.com/post/oh-the-places-you-poap-ed-poap-announces-its-going-into-maintenance-mode-as-the-gets-ready-for-its);
  [TechFlow](https://www.techflowpost.com/en-US/newsletter/116752);
  [The Defiant](https://thedefiant.io/news/nfts-and-web3/poap-moves-to-maintenance-mode-as-founders-eye-next-generation-of-digital-collectibles)).
- **Step 2, archive preparation** (late June and July 2026, inferred).
  poaparchive.com was registered 2026-06-30 by POAP Inc, and its first snapshot
  is dated 2026-07-02. The last drop was created 2026-07-31 09:39 UTC. **I found
  no public notice giving 2026-07-31 as the end date** (unverified). It may have
  reached issuers or API-key holders privately.
- **Step 3, wind-down announcement** (2026-08-03, 13:43 UTC, X note by
  @izonline). It opens "After 5+ years, we're winding down POAP." It lists
  millions of collectibles, Coinbase, Amex, WMG, Bayer, an 8,000+ collectible
  Devcon activation and the Airport Rally. The stated reason: "crypto's funding
  cycles and distribution dynamics made it hard to build a sustainable company"
  without "cannibalizing the ethos that made POAP mean something," plus a fragile,
  fast-changing tech stack. Lessons: "Customer communities are the most
  undervalued asset a company can have"; connection is the core; "Longevity and
  brand equity are the only moats left." She said next steps were unannounced and
  that she is focused on go-to-market in the age of AI
  ([X post](https://x.com/izonline/status/2084273977938080092);
  [The Block](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years);
  [Unchained](https://unchainedcrypto.com/poap-winds-down-after-five-years-and-nearly-7-6-million-onchain-badges/);
  [crypto.news](https://crypto.news/poap-shuts-down-despite-coinbase-and-amex-adoption/)).
  There was no final service date, no migration plan and no successor
  ([Times of Blockchain](https://www.timesofblockchain.com/news/poap-is-shutting-down-after-five-years/)).
  The "open collectibles standard" has not surfaced since.
- **What happened to the services** (HTTP checks on 2026-10-17, plus Jamie's
  archive README):
  - **Tokens:** permanent on Gnosis and the other chains.
  - **Redirect to poap.xyz:** poap.gallery, collectors.poap.xyz,
    collections.poap.xyz, curation.poap.xyz, help.poap.xyz,
    documentation.poap.tech.
  - **Blog:** blog.poap.xyz redirects to poap.news. Its newest post is "Product
    updates - June 25", with nothing about the shutdown.
  - **API:** api.poap.tech keyed endpoints return 403. `api.poap.tech/metadata`
    still answers without a key.
  - **Assets and media:** assets.poap.xyz artwork is still up. media.poap.tech
    (Moments media) returns 530.
  - **Compass:** the GraphQL endpoint is still up without a key.
  - **Still online:** home.poap.xyz (POAP Home download) and the poap.xyz marketing
    site.
- **Archives.**
  - **poaparchive.com.** Run by POAP Inc, judging by the WHOIS registrant org
    "POAP Inc" (Gandi, New York, registered 2026-06-30, Cloudflare DNS). The page
    itself names no operator. It offers `archive.zip` (SQLite plus WebP artwork,
    about 15 GB) and `archive.zim` (Kiwix), with SHA-256 checksums. Tables:
    `drops`, `tokens`, `email_reservation_stats`, `snapshot_metadata`. No license
    is stated. It links to POAP.in "BY KIRA" for browsing
    ([poaparchive.com](https://poaparchive.com/)). There have been at least two
    versions: the 2026-07-02 snapshot, with SHA `046850de...` (per POAPin), and the
    2026-08-20 snapshot, with SHA `aed7ec75...`, which is the one Jamie holds. It
    has no Moments, no Collections and no private drops.
  - **poap.in (POAPin Archive).** Built by **Kira** ([email removed]) of Glory
    Lab, Tokyo. GitHub user RockerFlower, "Founder of @glorylab", is probably the
    same person (unverified). POAPin was a long-running Gitcoin-funded third-party
    POAP explorer and app, started in 2022. It now serves the official 2026-07-02
    snapshot on Cloudflare Workers, plus its own captures: Collections
    (2026-07-22), Moments (2026-07-23, 30,548 media objects) and Compass holdings
    (2026-07-28). It looks up addresses and ENS names and builds a downloadable
    personal-site ZIP. The code is MIT, and it says it is "not endorsed by or
    affiliated with POAP"
    ([GitHub glorylab/poapin-archive](https://github.com/glorylab/poapin-archive)).
  - **POAP Saver** (Ben Meadows, repo created 2026-08-04). It claims all
    **197,577** POAP events are saved, verified and published to IPFS, with roots
    for metadata (145 MB), thumbnails (4.4 GB) and artwork (194 GB), and a public
    registry. It has a browser rescuer and a CLI, and falls back to a community
    mirror, IPFS and S3
    ([poap-saver](https://thebenmeadows.srht.site/projects/poap-saver/);
    [GitHub](https://github.com/mdws-org/poap-saver)). It says "POAP shut down in
    August 2026." The 197,577 figure, almost triple the official archive's 73,990
    public drops, suggests it includes private drops (unverified).
  - **Other.** `artlu99/all-the-poaps-ever-and-forever` on GitHub builds on the
    08-20 snapshot ([GitHub](https://github.com/artlu99/all-the-poaps-ever-and-forever)).
    Goldsky's demo feed (`feed.poap.demo.goldsky.com`) still indexed POAP accounts
    when I searched.

## Reception and retrospectives

- **The Block** (Daniel Kuhn, 2026-08-03) placed it among other 2026 crypto
  shutdowns (Leap Wallet, Zapper, BitMEX)
  ([link](https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years)).
- **CryptoBriefing** (2026-08-03): "raising questions about utility NFT
  viability." Its argument: no token meant no revenue model
  ([link](https://cryptobriefing.com/poap-shuts-down-five-years/)).
- **Molly White, *Web3 is Going Just Great*** (2026-08-03). POAPs were sold as
  proof of NFT utility, but their tradability undercut "proof of attendance." She
  quotes the site's promise that POAP makes memories "last forever"
  ([link](https://web3isgoinggreat.com/single/proof-of-attendance-protocol-shuts-down)).
- **crypto.news, Unchained, Times of Blockchain** (2026-08-04) all stressed that
  no end date or data plan had been published
  ([crypto.news](https://crypto.news/poap-shuts-down-despite-coinbase-and-amex-adoption/);
  [Unchained](https://unchainedcrypto.com/poap-winds-down-after-five-years-and-nearly-7-6-million-onchain-badges/);
  [Times of Blockchain](https://www.timesofblockchain.com/news/poap-is-shutting-down-after-five-years/)).
- **BlockEden** (2026-04-23, after maintenance mode), "POAP Goes Dark." Its
  analysis: a soulbound-less design, the commercial-classification problem, and
  rivals taking over the niches
  ([link](https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/)).
- **LikeCoin, kin ko** (2026-08-10), "Farewell to POAP's Geek Ethos." A "tragic"
  case of Web3 idealism meeting economics. It traces the path from sybil farming
  to manual review costs, the commercial pivot and backlash, and the 2026 bear
  market as "the final straw" ([link](https://likecoin.substack.com/p/poap)).
- **Community response.** Gonzalez's post drew 742 replies and 422 quotes on
  about 934k views (fxtwitter read). The archivists' own framing: "POAP is dead.
  Long live POAP!" (POAPin) and "a community's memories should not disappear when
  a website does."

## Sources

Primary (POAP and founders)

- Isabel Gonzalez, "Looking forward to POAP's next chapter," X, 2026-03-12: https://x.com/izonline/status/2032181803155333626
- Isabel Gonzalez, wind-down post, X, 2026-08-03: https://x.com/izonline/status/2084273977938080092
- Patricio Worthalter, X, 2026-07-31 (unrelated ENS art; used only to rule out a sunset post): https://x.com/worthalter/status/2083144703659192366
- poap.xyz home and About the protocol: https://poap.xyz/ , https://poap.xyz/about-the-protocol
- POAP News 2023 in review: https://www.poap.news/2023-in-review/
- POAP News Year in POAP 2024: https://www.poap.news/year-in-poap-looking-back-on-2024/
- POAP News index: https://www.poap.news/
- POAP Airship, Airport Rally 2026 boarding pass: https://airship.poap.xyz/poap-airport-rally-2026-boarding-pass
- POAP curation guidelines (now redirected): https://curation.poap.xyz/guidelines/policy-and-process
- POAP Moments help article (now redirected): https://help.poap.xyz/hc/en-us/articles/27197060755725-How-to-Create-Edit-and-Share-Moments
- POAP Home, App Store: https://apps.apple.com/us/app/poap-home/id6478871538
- poaparchive.com: https://poaparchive.com/ (WHOIS checked 2026-10-17)

Archives

- POAPin Archive (Kira, Glory Lab): https://github.com/glorylab/poapin-archive and https://poap.in
- POAPin source inventory: https://github.com/glorylab/poapin-archive/blob/main/docs/source-inventory.md
- POAPin app repo: https://github.com/glorylab/POAPin
- POAP Saver (Ben Meadows): https://thebenmeadows.srht.site/projects/poap-saver/ and https://github.com/mdws-org/poap-saver
- all-the-poaps-ever-and-forever: https://github.com/artlu99/all-the-poaps-ever-and-forever

News and analysis

- Decrypt, POAP raises $10M (2022-01-19): https://decrypt.co/90689/ethereum-nft-badge-app-poap-10m-seed-raise
- The Defiant, POAP raises $10M: https://thedefiant.io/news/nfts-and-web3/poap-nfts-events-fundraise
- CB Insights, POAP financials: https://www.cbinsights.com/company/poap/financials
- Decrypt, paid POAPs (2023-04-04): https://decrypt.co/125462/paid-poap-proof-of-attendance-ethereum-nft
- The Block, The Merge POAP (2022-09-15): https://www.theblock.co/post/170564/i-attended-the-merge-and-all-i-got-was-this-lousy-poap
- The Bored Ape Gazette, maintenance mode (Mar 12): https://www.theboredapegazette.com/post/oh-the-places-you-poap-ed-poap-announces-its-going-into-maintenance-mode-as-the-gets-ready-for-its
- TechFlow, maintenance mode (2026-03-14): https://www.techflowpost.com/en-US/newsletter/116752
- The Defiant, maintenance mode: https://thedefiant.io/news/nfts-and-web3/poap-moves-to-maintenance-mode-as-founders-eye-next-generation-of-digital-collectibles
- BlockEden, "POAP Goes Dark" (2026-04-23): https://blockeden.xyz/blog/2026/04/23/poap-maintenance-mode-web3-identity-primitive-sunset-proof-of-attendance/
- The Block, POAP shutting down (2026-08-03): https://www.theblock.co/post/410482/proof-of-attendance-protocol-is-shutting-down-after-5-years
- CryptoBriefing (2026-08-03): https://cryptobriefing.com/poap-shuts-down-five-years/
- Web3 is Going Just Great (2026-08-03): https://web3isgoinggreat.com/single/proof-of-attendance-protocol-shuts-down
- ETH Daily (2026-08-03): https://ethdaily.io/eth-daily-news-august-3-2026
- crypto.news (2026-08-04): https://crypto.news/poap-shuts-down-despite-coinbase-and-amex-adoption/
- Unchained (2026-08-04): https://unchainedcrypto.com/poap-winds-down-after-five-years-and-nearly-7-6-million-onchain-badges/
- Times of Blockchain (2026-08-04): https://www.timesofblockchain.com/news/poap-is-shutting-down-after-five-years/
- LikeCoin Substack, kin ko (2026-08-10): https://likecoin.substack.com/p/poap

Profiles (secondary, lower confidence)

- IQ.wiki, POAP: https://iq.wiki/wiki/poap
- IQ.wiki, Patricio Worthalter: https://iq.wiki/wiki/patricio-worthalter
- Patricio Worthalter, LinkedIn: https://www.linkedin.com/in/worthalter/
- Goldsky case study: https://goldsky.com/case-studies/poap-goldsky
- blockchain.news, Worthalter ETH transfer: https://blockchain.news/flashnews/patricio-worthalter-transfers-another-4000-eth
- Podcast "#28 Patricio Worthalter, let's POAP": https://www.youtube.com/watch?v=olYVI19_dmE

Local (in this archive)

- `snapshot/poap.sqlite`: official poaparchive.com snapshot of 2026-08-20 (drop and token counts, last drop date, email reservations)
- `writing/posts/`: Jamie's posts, especially 2023-01-16 (business and premium features), 2024-01-14 (email onboarding), 2025-01-02 (event trends)
