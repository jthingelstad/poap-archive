# Network

Who collected Jamie's drops, captured 2026-10-17 from POAP Compass and ensdata.net by
`scripts/network_harvest.py`.

| File | What |
|---|---|
| `drop_supply.json` | Tokens per drop per chain, for every drop Jamie made or collected (rarity) |
| `co_attendance.json` | Tokens held by people in Jamie's network from drops Jamie also collected: "we were both there" edges |
| `collector_sizes.json` | Each person's total POAPs per chain |
| `ens.json` | Reverse ENS record (primary name, avatar, url, social) per address; null name means none set |

"People" means every address that holds a token from one of Jamie's 130 drops, minus
Jamie's four wallets: 632 addresses, 105 of them with a primary ENS name.

Shape on 2026-10-17:
- 82 people collected 5 or more of Jamie's drops, 37 collected 10 or more.
- Top collectors of Jamie's drops are family (tyler, mazie and tammy.thingelstad.eth, 86 to
  89 each), then quinnchrest.eth (56) and halaas.eth (41).

Outliers to handle before drawing anything:
- `0x0000000000000000000000000000000000000000` is the zero address: burned tokens, not a
  person.
- `0xc50630478e6020f656bf730cb9bb74c7b916c37c` is a plain wallet holding 35,359 POAPs from
  9,705 drops (per the snapshot). A bulk collector; it shares 42 events with Jamie and
  dominates `co_attendance.json` row counts.

Privacy: addresses and ENS names are public on-chain, but naming people on a public
tribute site is Jamie's call. See BRIEF.md.
