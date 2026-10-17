# Jamie's POAP Writing: Essays and Advice

This is a curated guide to Jamie Thingelstad's substantial writing about POAP, the
Proof of Attendance Protocol, from 2021 to 2026. It leaves out the routine mint and claim
posts, which are listed in `mint-posts.json`. Every quote is taken word for word from the
captured post HTML in `writing/posts/` or from the Weekly Thing issue files in
`writing/weekly-thing/`. The only edit is straightening curly quotes and apostrophes, and
all 89 quotes were checked against those files by script. "POAP KINGS" is a Clash Royale
clan and has nothing to do with the protocol, so it does not appear here.

Jamie's first POAP was the ENS 4th Anniversary Snapshot voter token, minted on
2021-06-07. The last protocol writing in the archive is the Flight Path build in March
2026. The archive holds no writing by Jamie about the protocol's 2026-07-31 wind-down.

## The five most important pieces

1. **[POAP Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html)** (2023-01-14).
   Jamie's main product memo to POAP: add integration hooks (RSS and webhooks), signed and
   location-based events, and wallet-free onboarding. POAP later shipped the onboarding and
   location ideas. RSS never came from POAP, so Jamie built it himself.
2. **[POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html)** (2023-01-16),
   published the same day as
   [Premium Features for POAP Issuers](https://www.thingelstad.com/2023/01/16/premium-features-for.html) and
   [POAP Extensions](https://www.thingelstad.com/2023/01/16/poap-extensions.html).
   This is a full pricing and packaging proposal: Collector at $3/mo, Pro at $20/mo, Studio at
   $500/event, Business, and a free Non-Profit tier. It also gives feature-by-feature feedback on
   POAP's issuer survey. Collections, one of the ideas, shipped a year later.
3. **[New POAP Onboarding Process](https://www.thingelstad.com/2024/01/14/new-poap-onboarding.html)** (2024-01-14).
   Published exactly one year after the wishlist. Jamie confirms that POAP shipped what he
   asked for: email reservations that prompt the holder to act, plus an embedded
   (Privy) wallet with an onpoap.eth name.
4. **[Vibe Coding POAP2RSS](https://www.thingelstad.com/2025/07/06/vibe-coding-poaprss.html)** (2025-07-06),
   which follows [POAP + RSS = Awesome?](https://www.thingelstad.com/2025/01/05/poap-rss-awesome.html) (2025-01-05).
   Jamie ran out of patience waiting for POAP to add RSS, specified the feature himself, and
   built poap2rss.com with AI coding tools. POAP2RSS went on to power the 612 Challenge and
   Airport Rally sites.
5. **[612 POAP Challenge: Collect them all!](https://www.thingelstad.com/2025/05/31/poap-challenge-collect-them-now.html)** (2025-05-31).
   Once location drops existed, Jamie turned them into a summer scavenger hunt around
   Minneapolis. That led to the
   [Airport POAP Rally Website](https://www.thingelstad.com/2025/12/26/airport-poap-rally-website.html) (2025-12-26)
   and the Flight Path globe ([WT342](https://weekly.thingelstad.com/archive/342/)).

---

## 1. Getting hooked (2021-2022)

### Poaps are a big deal (Weekly Thing 193 featured link)
- **Date:** 2021-09-04 - [WT193](https://weekly.thingelstad.com/archive/193/) (issue titled "POAPs, DAOs, NFTs")
- **Summary:** Jamie's first Weekly Thing piece on POAP. He features a NiftyTable analysis
  of record mint numbers and pitches POAP as the free, no-money way to bring people into
  crypto. He also likes POAP-weighted DAO voting.
- **Key quotes:**
  > "I think it is a very fun way to introduce people to some crypto / web3 technologies without having to spend any money."

### POAP NFT Treasure Hunt (Weekly Thing 194)
- **Date:** 2021-09-11 - [WT194](https://weekly.thingelstad.com/archive/194/)
- **Summary:** Jamie reacts to POAP's announced NFT treasure hunt. He suggests running
  multi-day hunts in cities and rewarding a full set with a bonus token. This is the seed of
  the 612 POAP Challenge four years later.
- **Key quotes:**
  > "It would be super cool to have POAP NFT treasure hunts in various cities. You have to find several POAP tokens over the course of some number of days. It would be great if you then got additional tokens when you collected all of them, like unlocking another NFT."

### Quantum Mirror at REM5VR
- **Date:** 2021-12-17 - [post](https://www.thingelstad.com/2021/12/17/quantum-mirror-at.html)
- **Summary:** A review of an immersive art exhibit that sold NFTs alongside its art.
  Jamie notes that the exhibit missed a chance to give visitors a POAP.
- **Key quotes:**
  > "This would have been a brilliant use for a POAP token. I was really wishing I could have gotten a Quantum Mirror @ REM5VR POAP token."

### POAP inc. raises $10M (Weekly Thing 208)
- **Date:** 2022-01-22 - [WT208](https://weekly.thingelstad.com/archive/208/)
- **Summary:** Jamie welcomes POAP becoming a company and raising money. He questions why it
  chose a closed, traditional raise over a DAO that people could buy into, and hopes it
  moves toward a model like ENS's.
- **Key quotes:**
  > "POAP is one of my very favorite crypto projects out there."
  >
  > "However, I scratch my head at why crypto projects like POAP take a traditional approach like this. POAP could have also formalized itself around a DAO. It could have allowed people to buy in and be part of it."

### Soulbound (Weekly Thing 209)
- **Date:** 2022-01-29 - [WT209](https://weekly.thingelstad.com/archive/209/)
- **Summary:** Jamie's commentary on Vitalik's essay about non-transferable NFTs. He
  sketches a check that the issuer is the only previous owner of a token, and is glad to
  see POAP highlighted.
- **Key quotes:**
  > "There are a lot of use cases that open up if you know that the NFT a user has was not purchased from someone else, but granted directly to them."

### My Introduction to the POAP Community
- **Date:** 2022-06-04 (first posted on the POAP Discourse on 2022-01-08) - [post](https://www.thingelstad.com/2022/06/04/my-introduction-to.html)
- **Summary:** Jamie's origin story: the ENS anniversary vote, his first issued drop for a
  book club, and his favorites (ConstitutionDAO, Weekly Thing #200, his 50th Birthday). It
  also tells the cautionary tale of the "Reading Things First 100" drop, which POAP farmers
  stripped.
- **Key quotes:**
  > "Photos stop time. Geo coordinates stop motion. POAPs are a time capsule of something of note."
  >
  > "I also love it as a way to introduce people to crypto as a totally non-economic activity."
  >
  > "I honestly wish I could 'burn' that whole event and destroy all those tokens because they are trash... the farmers destroyed what should have been a cool memory for us to celebrate with these 100 first subscribers..."

### Gift for Weekly Thing POAP Holders
- **Date:** 2022-05-29 - [post](https://www.thingelstad.com/2022/05/29/gift-for-weekly.html), reprinted in [WT222](https://weekly.thingelstad.com/archive/222/)
- **Summary:** Jamie downloaded the holder CSVs for two Weekly Thing drops and airdropped
  a Nifty Ink "HELLO" to every holder. It is an early case of using POAP as a list of a
  community's members.
- **Key quotes:**
  > "I should send one of these to everyone that has minted a Weekly Thing POAP token!"

### Magic Pines Summer of 2022 POAP
- **Date:** 2022-05-30 - [post](https://www.thingelstad.com/2022/05/30/magic-pines-summer.html)
- **Summary:** The first yearly in-person POAP for the family lake house, with art from a
  POAPathon contest and printed claim sheets for first-time collectors. It started a tradition
  that ran through 2025.
- **Key quotes:**
  > "I love finding ways to commemorate these fun times and I thought it would be fun to give people a POAP token each summer!"

### POAP x ENS x IYK swag at Devcon 6 (Weekly Thing 231)
- **Date:** 2022-10-29 - [WT231](https://weekly.thingelstad.com/archive/231/)
- **Summary:** Jamie admires a Devcon 6 event where 2,197 people collected 18,743 POAPs
  through NFC cards. He later adopted IYK discs and cards himself, for Pi Day 2023 and
  Minnebar 19.
- **Key quotes:**
  > "This should just be standard at any crypto events, or any events at all, going forward."

### State of Blockchain 2022 Event; Things 4 Good Fall Fundraiser Notes
- **Dates:** 2022-10-06 [post](https://www.thingelstad.com/2022/10/06/state-of-blockchain.html); 2022-11-27 [post](https://www.thingelstad.com/2022/11/27/101105.html)
- **Summary:** Lessons on distribution. A last-minute event POAP was "not thought out well
  enough". At the fundraiser, printed claim sheets worked much better, with 28 redemptions.
  The first "You've met me" POAP was given out at State of Blockchain.
- **Key quotes:**
  > "Printing out claim sheets with directions and the claim code was a much better way to distribute these."

### Mainnet Merge Lapse 12 "Thing"
- **Date:** 2022-11-14 - [post](https://www.thingelstad.com/2022/11/14/mainnet-merge-lapse.html)
- **Summary:** Jamie painted "Thing" on the POAP.art Merge canvas, defended his pixels
  overnight, and later minted the lapse NFT of that area.
- **Key quotes:**
  > "What a great way to remember such a historic event, and mark 'I was here!'"

### What in Ethereum ecosystem excites me; Crypto in Three Words
- **Dates:** 2022-12-11 [post](https://www.thingelstad.com/2022/12/11/what-in-ethereum.html) (also [WT237](https://weekly.thingelstad.com/archive/237/)); 2022-12-12 [post](https://www.thingelstad.com/2022/12/12/crypto-in-three.html)
- **Summary:** Jamie's broader crypto thesis puts POAP under Identity, his top category: a
  collection of POAPs shows who you are. "Common Digital Ownership" uses a cabin-visit POAP
  as its example of ownership.
- **Key quotes:**
  > "If you take a look at the POAPs that I have it gives you a clear sense of me, at least in some dimensions of my life."
  >
  > "It could be a POAP that proves you were at my cabin one summer."

### Find Unique Addresses for Multiple POAP Events
- **Date:** 2022-12-13 - [post](https://www.thingelstad.com/2022/12/13/find-unique-addresses.html)
- **Summary:** A shell recipe (cat, awk, sort, uniq) for deduplicating holders across drop
  CSV exports. The same day Jamie counted 27 events, 630 claims and 354 unique addresses
  ([post](https://www.thingelstad.com/2022/12/13/ive-created-poap.html)).
- **Key quotes:**
  > "How do you get a list of unique addresses that have claimed any set of POAPs?"

## 2. The January 2023 product series

Jamie's Weekly Thing introduced this run of posts in [WT238](https://weekly.thingelstad.com/archive/238/) (2023-01-21): "That is a lot of POAP."

### POAPathon Future Thoughts
- **Date:** 2023-01-03 - [post](https://www.thingelstad.com/2023/01/03/poapathon-future-thoughts.html)
- **Summary:** Feedback to POAPathon, the community design-contest group behind Jamie's
  favorite POAP art. He proposes a Gnosis-chain DAO with non-monetary governance tokens and
  on-chain contest escrow. He also asks for a POAP-only focus, a newsletter, more POAPs, and
  a closer tie to POAP itself.
- **Key quotes:**
  > "Governance tokens have no monetary value and should never be bought or sold."
  >
  > "Closer connection with POAP itself. POAPathon could be part of the POAP process. There seems to be no mention of POAPathon on the POAP website that I could easily find."

### POAP Wishlist
- **Date:** 2023-01-14 - [post](https://www.thingelstad.com/2023/01/14/poap-wishlist.html)
- **Summary:** Three areas for POAP to extend. (1) Integration hooks: an RSS feed of each
  event's claims for readers and IFTTT or Zapier, plus webhooks. (2) Event enhancements:
  events signed by the issuer's wallet, and location-bound "perpetual" POAPs for homes,
  summits and cafes. (3) Web2/3 onboarding: reminder emails for email reservations, and a
  non-custodial wallet POAP creates for you, Reddit-style.
- **Key quotes:**
  > "If every event offered an RSS feed of POAP claims, that could be used by event organizers to power a ton of automations when a token is claimed."
  >
  > "It would be great to be able to sign the event with your wallet! For example, my Birthday POAP would be more authentic if the event was signed by the thingelstad.eth wallet."
  >
  > "If you removed time limitations, this would be ideal for restaurants and cafes to have a perpetual POAP you can claim for visiting their location."
  >
  > "Better yet would be to have POAP provide a non-custodial wallet for users that don't have one."
  >
  > "I have personally introduced well over 100 people to crypto by giving out POAP tokens for various events."

### Premium Features for POAP Issuers
- **Date:** 2023-01-16 - [post](https://www.thingelstad.com/2023/01/16/premium-features-for.html)
- **Summary:** Jamie's written answers to a POAP issuer survey that had no comment fields.
  He weighs each candidate premium feature and adds three gaps: claim-code management,
  anti-farming tools, and image creation.
- **Key quotes:**
  > "One-way messaging to collectors of your POAPs would be great. For sure this would be a really big win. When I've explained to people how they can use POAPs at their events nearly everyone wants to use it to communicate and that isn't possible today."
  >
  > "I value privacy, and would want my drops to be the same way."
  >
  > "I do not like the idea of tracking anything relating to net worth value."

### POAP Extensions
- **Date:** 2023-01-16 - [post](https://www.thingelstad.com/2023/01/16/poap-extensions.html)
- **Summary:** Three feature ideas: POAPs with a back like a challenge coin, official
  POAP Collections that can unlock a completion POAP, and unique per-claim metadata (for
  example an escape-room team's time and clue count).
- **Key quotes:**
  > "POAPs are a bit like challenge coins, and physical coins have a front and a back."
  >
  > "You could even unlock a collection POAP when you have all the POAPs in that collection."
  >
  > "If an issuer could add one off metadata to a specific claim code it could unlock a ton of use cases."

### POAP as a Business
- **Date:** 2023-01-16 - [post](https://www.thingelstad.com/2023/01/16/poap-as-a.html)
- **Summary:** A revenue model with priced tiers for collectors and issuers, plus a free
  non-profit tier pitched as both reach and brand fit.
- **Key quotes:**
  > "POAP is more than just a fun crypto product, it is also a business."
  >
  > "Aligning with non-profits would reach a very solid set of organizations that could benefit from POAP, and be a wonderful brand alignment with POAP itself. Make it super cheap or free for non-profits to use advanced POAP Pro and Studio capabilities."

### POAP Family
- **Date:** 2023-01-31 - [post](https://www.thingelstad.com/2023/01/31/poap-family.html)
- **Summary:** Jamie praises POAP's new holder-overlap tool. Among holders of his 50th
  Birthday POAP he finds 7 Cryptog HODLERs, and 13 of the 34 who also hold his 51st.
- **Key quotes:**
  > "This kind of graph analysis of POAPs is an interesting extension and a way to build connection."

### Usability note (Weekly Thing 239)
- **Date:** 2023-01-29 - [WT239](https://weekly.thingelstad.com/archive/239/)
- **Summary:** In commentary on Pantera's outlook, Jamie argues that usability is crypto's
  biggest problem and uses his POAP onboarding experience as evidence.
- **Key quotes:**
  > "I have onboarded over a hundred people to crypto using POAPs for various events. It is getting easier, but it is still ridiculously complicated for even your average person to do this."

## 3. POAP in community and practice (2023-2024)

### Extending the Minnestar Community Supporter Program
- **Date:** 2023-02-11 - [post](https://www.thingelstad.com/2023/02/11/extending-the-minnestar.html)
- **Summary:** Advice to Minnestar: give supporters a yearly membership POAP with a local
  artist's art, and possibly gate a Minnestar DAO and supporter board seat on it.
- **Key quotes:**
  > "There should be a POAP for each year given to community supporters. Over the years, you collect each yearly POAP."

### Salsa (Weekly Thing 243)
- **Date:** 2023-02-26 - [WT243](https://weekly.thingelstad.com/archive/243/)
- **Key quotes:**
  > "One of the reasons I dig POAPs are all the things that could be built on them, and Salsa is an awesome example of that."

### Isolating Crypto Assets and Access; Transferring NFTs in Bulk
- **Date:** 2023-03-04 - [post](https://www.thingelstad.com/2023/03/04/isolating-crypto-assets.html), [post](https://www.thingelstad.com/2023/03/04/transferring-nfts-in.html)
- **Summary:** Why poap.thingelstad.eth exists. Jamie split his identity into wallets for
  each activity and moved 70+ POAPs in bulk with uNFT Wallet. He notes that transfers break
  the connections some POAP apps show, such as Salsa's.
- **Key quotes:**
  > "POAP.thingelstad.eth is an address I've made just for collecting POAP tokens. I currently hold 90 different POAP tokens in this address."

### Minnebar 17 POAPs; Creating Digital Community with POAPs; 612 Series Giveaway
- **Dates:** 2023-03-04 [Minnebar 17 POAPs](https://www.thingelstad.com/2023/03/04/minnebar-poaps.html), [session](https://www.thingelstad.com/2023/03/04/hosting-minnebar-creating.html); 2023-03-28 [giveaway](https://www.thingelstad.com/2023/03/28/minnebar-staynftympls-series.html)
- **Summary:** Minnebar 17 was the first Minnebar to give out POAPs, with attendee,
  presenter and organizer drops. It had a FAQ for newcomers, a session Jamie hosted on
  building community with POAP, and a raffle open to POAP holders of 32 612 Series NFTs.
  This Week in POAP featured the drops on
  [2023-04-25](https://www.thingelstad.com/2023/04/25/it-was-cool.html).
- **Key quotes:**
  > "It is like a digital version of a sticker or shirt."
  >
  > "POAPs are meant to collect and curate memories, not make money."
  >
  > "POAPs are an incredible asset to create digital communities, and there is a vibrant ecosystem built around them to enhance and add utility."

### Memory Dividends (Weekly Thing 250)
- **Date:** 2023-04-16 - [WT250](https://weekly.thingelstad.com/archive/250/)
- **Key quotes:**
  > "This post captures the thing I like the most about POAPs."

### Year in POAP mentions
- **Dates:** 2023-12-20 [post](https://www.thingelstad.com/2023/12/20/poap-just-published.html); 2024-12-20 [post](https://www.thingelstad.com/2024/12/20/the-year-in.html)
- **Summary:** POAP's annual Year in POAP highlighted Jamie's drops twice: 20 Years of
  Olson Family Vacations in 2023 and Thingelstad Ireland 2024 in 2024. This Week/Week in
  POAP also featured the Things 4 Good fundraiser
  ([2022-11-20](https://www.thingelstad.com/2022/11/20/i-love-that.html)), Minnebar 17
  (2023-04-25), his 52nd Birthday
  ([2024-01-09](https://www.thingelstad.com/2024/01/09/my-nd-birthday.html)) and the
  Weekly Thing Seven Year Anniversary
  ([2024-05-21](https://www.thingelstad.com/2024/05/21/awesome-to-see.html)).
- **Key quotes:**
  > "POAP is one of my favorite crypto projects! I've issued a bunch of them!" (2023)
  >
  > "There are so many cool things happening in the POAP world and this annual roundup is a great recap. I 💛 POAP!" (2024)

### Birthday POAPs
- **Date:** 2024-01-06 - [post](https://www.thingelstad.com/2024/01/06/birthday-poaps.html)
- **Summary:** Three years of birthday POAPs, each with POAPathon art, analyzed with POAP
  Family: 85 collectors in total, 12 holding all three, and unminted reservations left over.
  The tradition ran from the 50th to the 53rd birthday.
- **Key quotes:**
  > "I've made it a tradition since my 50th birthday to issue a POAP token for my birthday and share it as a gift from me to others to celebrate the day."

### New POAP Onboarding Process
- **Date:** 2024-01-14 - [post](https://www.thingelstad.com/2024/01/14/new-poap-onboarding.html), reprinted in [WT274](https://weekly.thingelstad.com/archive/274/)
- **Summary:** Jamie joined POAP's beta onboarding for his 52nd Birthday drop. Reserving
  with an email now sends actionable emails, "Create an account" makes a Privy embedded
  wallet with an onpoap.eth ENS name (thingelstad.onpoap.eth), and the key exports to Rainbow.
- **Key quotes:**
  > "I gave it a try myself and I was excited to see that they had addressed everything I had wished for in this process!"
  >
  > "With this new process, people will be able to claim and mint POAPs with nothing other than an email address! This is a big deal!"
  >
  > "I'm eager for this new onboarding process to be the default and I think I can get rid of my 'how to' page and simplify POAP distribution significantly."

### Interview with 612 Series creator Erik Halaas
- **Date:** 2024-01-15 - [post](https://www.thingelstad.com/2024/01/15/interview-with-series.html)
- **Summary:** A Q&A with the artist behind the 612 Series of Minneapolis landmark NFTs,
  which Jamie owns as a complete set. It sets up the 612 POAP Challenge, which reused those
  landmarks as location drops.
- **Key quotes:**
  > "How cool would it be in fifty years to see bronze plaques setup at the various landmarks highlighting these early NFTs that commemorate that spot."

### Connect the Drops with POAP Collections (Weekly Thing 276)
- **Date:** 2024-02-11 - [WT276](https://weekly.thingelstad.com/archive/276/)
- **Summary:** Jamie notes that POAP launched Collections, a year after he asked for them
  in POAP Extensions.
- **Key quotes:**
  > "On January 16th of last year I blogged about ways to extend POAP and highlighted my desire to have POAP Collections. A year later and POAP has launched exactly what I described!"

### ENS Continued Progress
- **Date:** 2024-09-24 - [post](https://www.thingelstad.com/2024/09/24/ens-continued-progress.html)
- **Summary:** Among ENS highlights, Jamie notes that the POAP Home app now gives collectors
  a free ENS subname.
- **Key quotes:**
  > "The latest release of the POAP Home app includes a feature allowing collectors to claim a free ENS subname."

## 4. Building on POAP (2025-2026)

### POAP Event Trends
- **Date:** 2025-01-02 - [post](https://www.thingelstad.com/2025/01/02/poap-event-trends.html)
- **Summary:** Using sequential drop IDs from his birthday drops, Jamie estimates drops
  created each year: 74,298 in 2022, 71,285 in 2023 and 16,826 in 2024. He reads the 2024
  drop as POAP consolidating its product.
- **Key quotes:**
  > "That is a big drop in 2024, however it is still 46 events a day."
  >
  > "I'm rooting for them to be massively successful. I think POAP could be one of the products that shows the path for blockchain adoption."

### POAP + RSS = Awesome?; Support the Web via Open RSS
- **Date:** 2025-01-05 - [post](https://www.thingelstad.com/2025/01/05/poap-rss-awesome.html), [post](https://www.thingelstad.com/2025/01/05/support-the-web-via-open.html)
- **Summary:** A spec for event and address RSS feeds built on the POAP API
  (`/event/{id}/poaps` and `/actions/scan/{address}`), offered to POAP or to Open RSS. A
  later update to the post links POAP2RSS.
- **Key quotes:**
  > "I'm a big fan of POAP, and I'm a big fan of RSS. Sadly, these two things don't know about each other, yet!"
  >
  > "As someone that issues POAPs a lot I would love to subscribe to the RSS feeds for each of my events and see via the feed when a new token is claimed."

### Minnebar 19 POAP planning
- **Dates:** 2025-04-06 [post](https://www.thingelstad.com/2025/04/06/poap-planing-for-minnebar.html); 2025-04-28 [post](https://www.thingelstad.com/2025/04/28/minnebar-poap.html)
- **Summary:** Jamie handled distribution with IYK NFC discs instead of claim codes,
  added a session POAP and a "You've met me" POAP, and pointed attendees to POAP Home and
  Memories for photos.
- **Key quotes:**
  > "This will be simpler and easier to distribute than what I did for Minnebar 17."

### 612 POAP Challenge: Collect them all!
- **Date:** 2025-05-31 - [post](https://www.thingelstad.com/2025/05/31/poap-challenge-collect-them-now.html) (site: 612.poapchallenge.com; captured in `writing/sites/` and `writing/thingelstad-projects-612-poap-challenge.html`)
- **Summary:** Location drops shipped. Jamie's first was the Magic Pines Peanuts Tree on
  [2025-05-25](https://www.thingelstad.com/2025/05/25/i-created-my-very-first.html). He paired
  them with the 612 Series landmarks to make a citywide summer game running to Labor Day.
  Follow-ups added achievement tokens, an Explorer award, a first winner and family
  completions.
- **Key quotes:**
  > "When I first found POAPs the capability to claim a POAP for a location was something I wanted right away, and now you can with location drops!"
  >
  > "I love that I was able to create an entire activity on the POAP platform."

### IndieWeb is Punk: Wear It!
- **Date:** 2025-06-21 - [post](https://www.thingelstad.com/2025/06/21/indieweb-is-punk-wear-it.html)
- **Summary:** A blog post that became a t-shirt and then a POAP, with a description
  written in the voice of Henry Rollins.
- **Key quotes:**
  > "This POAP? It's not just a collectible. It's a battle patch." (the ChatGPT-written drop description)

### Vibe Coding POAP2RSS
- **Date:** 2025-07-06 - [post](https://www.thingelstad.com/2025/07/06/vibe-coding-poaprss.html); launch [2025-07-04](https://www.thingelstad.com/2025/07/04/i-decided-to-declare-poaprss.html); submitted to the POAP Directory [2025-07-10](https://www.thingelstad.com/2025/07/10/i-submitted-poaprss-to-the.html)
- **Summary:** Jamie built POAP2RSS (an AWS Lambda with a DynamoDB cache, POAP API key plus
  OAuth) with Claude, o3 Deep Research and Codex. It provides RSS feeds for events and
  collector addresses and automates the 612 Challenge accounts. While researching, Deep
  Research found Jamie's own earlier posts asking POAP for RSS.
- **Key quotes:**
  > "Ever since I created my first POAP drop I've wished that I could see claims of POAPs in Feedbin."
  >
  > "It turns out over the years I've written about things that POAP could add including RSS feed support. Actually multiple times."

### Airport POAP Rally Website
- **Date:** 2025-12-26 - [post](https://www.thingelstad.com/2025/12/26/airport-poap-rally-website.html)
- **Summary:** POAP's own 2026 rally across 100 airports, larger than the 612 Challenge. Jamie
  built airport.poaprally.com on POAP2RSS and micro.blog, with Mastodon and Bluesky
  syndication. He also registered poapchallenge.com and poaprally.com for future challenges.
- **Key quotes:**
  > "Location-based POAPs at 100 airports throughout the world? I think this will be a super fun event to track throughout 2026."

### Patricio Worthalter talk (Weekly Thing 337)
- **Date:** 2026-01-18 - [WT337](https://weekly.thingelstad.com/archive/337/)
- **Key quotes:**
  > "I loved how he shared the impact of his 'You've Met Patricio' POAPs. It inspired me to get back to those and commit to doing them in an ongoing manner."

### Flight Path (Weekly Thing 342)
- **Date:** 2026-03-08 - [WT342](https://weekly.thingelstad.com/archive/342/) ("Flight Path" section); micro post [2026-02-25](https://www.thingelstad.com/2026/02/25/it-is-bonkers-to-me.html)
- **Summary:** Jamie built flightpath.poaprally.com, a rotating globe of Airport Rally claims
  with a leaderboard and per-collector paths, entirely from his phone in bed with ChatGPT and
  Claude Code. He calls the rally "exactly the kind of project that can bring people into
  POAPs".
- **Key quotes:**
  > "POAP is currently running a year-long Rally with POAPs at 100+ airports in the world — the POAP Airport Rally. **I absolutely love this!** It is exactly the kind of project that can bring people into POAPs and have fun."
  >
  > "Plus the POAP API isn't the easiest thing, so getting all the data."

---

## Jamie's advice to POAP (product and business)

Each suggestion below links to the post where Jamie made it. "Shipped?" reports only what
Jamie's own later writing says. "Not recorded" means the archive does not say either way.

| # | Suggestion | Date and source | Jamie's words | Shipped? (per Jamie's writing) |
|---|---|---|---|---|
| 1 | City treasure hunts in which collecting a full set unlocks a bonus token | 2021-09-11 [WT194](https://weekly.thingelstad.com/archive/194/) | "It would be super cool to have POAP NFT treasure hunts in various cities." | **Yes, by POAP and by Jamie.** Jamie ran it himself as the [612 POAP Challenge](https://www.thingelstad.com/2025/05/31/poap-challenge-collect-them-now.html) with achievement tokens (2025). POAP ran the [Airport POAP Rally 2026](https://www.thingelstad.com/2025/12/26/airport-poap-rally-website.html) as a Collection. |
| 2 | Organize as a DAO that people can buy into, instead of a closed VC raise | 2022-01-22 [WT208](https://weekly.thingelstad.com/archive/208/) | "POAP could have also formalized itself around a DAO. It could have allowed people to buy in and be part of it." | No. |
| 3 | A way to "burn" or invalidate a farmed event | 2022-06-04 [post](https://www.thingelstad.com/2022/06/04/my-introduction-to.html); 2023-01-16 [post](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "Anti-farming for issuers would be nice. I had one POAP event get completely farmed and I would like to be able to invalidate that event somehow." | Not recorded. His POAP Events list still marks Reading Things First 100 "**This event is invalid.**" |
| 4 | RSS feeds of claims for each event (and later each collector address) | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html); 2025-01-05 [POAP + RSS](https://www.thingelstad.com/2025/01/05/poap-rss-awesome.html) | "If every event offered an RSS feed of POAP claims, that could be used by event organizers to power a ton of automations when a token is claimed." | **No, so Jamie built it.** [POAP2RSS](https://www.thingelstad.com/2025/07/06/vibe-coding-poaprss.html) launched 2025-07-04 and was submitted to the POAP Directory 2025-07-10. |
| 5 | Webhooks on claim | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html) | "Webhooks would be a great middle option between the full POAP API, and something simple like RSS." | Not recorded. |
| 6 | Events signed by the issuer's wallet to prove authenticity | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html); 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "It would be great to be able to sign the event with your wallet!" | Not recorded. |
| 7 | Location-bound, timeless POAPs (home, summit, cafe) | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html) | "There is an opportunity to have POAPs for things that are bound to locations instead of times." | **Yes.** Location drops. Jamie's first was [2025-05-25](https://www.thingelstad.com/2025/05/25/i-created-my-very-first.html): "now you can with location drops!" ([2025-05-31](https://www.thingelstad.com/2025/05/31/poap-challenge-collect-them-now.html)). |
| 8 | Reminder emails and organizer visibility for email reservations | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html) | "POAP should send reminder emails to nudge those that have reserved to move forward with minting." | **Yes.** [New POAP Onboarding Process](https://www.thingelstad.com/2024/01/14/new-poap-onboarding.html) (2024-01-14): reservation emails now offer actions. |
| 9 | A non-custodial wallet POAP creates for new users, Reddit-style, with an optional ENS name | 2023-01-14 [Wishlist](https://www.thingelstad.com/2023/01/14/poap-wishlist.html) | "Better yet would be to have POAP provide a non-custodial wallet for users that don't have one." | **Yes.** Privy embedded wallet with an onpoap.eth name, exportable to Rainbow (2024-01-14): "they had addressed everything I had wished for". A free ENS subname in POAP Home followed ([2024-09-24](https://www.thingelstad.com/2024/09/24/ens-continued-progress.html)). |
| 10 | Priority support bundled with design help ("full service") | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "If bundled into a 'full service' experience I think there are companies that may pay for this." | Not recorded. |
| 11 | Event promotion that avoids "suggested user list" problems | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "POAP should avoid the problems that come from things like a 'suggested user list'." | Not recorded. |
| 12 | One-way notifications to collectors | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "One-way messaging to collectors of your POAPs would be great. For sure this would be a really big win." | Not recorded. |
| 13 | Post-claim URL setting | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html); [POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html) | "it would be sufficient for most use cases to be able to have a event setting for a URL for people to go to after claiming." | Not recorded. |
| 14 | Opt-in drop analytics with privacy; no net-worth tracking | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "these features need to all be at the wish of the issuer. I value privacy, and would want my drops to be the same way." | Not recorded. POAP Family's overlap graph is the analytics Jamie used and praised ([2023-01-31](https://www.thingelstad.com/2023/01/31/poap-family.html)). |
| 15 | Easier claim-code management and distribution | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html) | "When I talk with people about distributing POAPs managing the claim codes is always a burden." | **Partly**, per Jamie's practice. NFC IYK discs and POAP Cards made Minnebar 19 "simpler and easier to distribute" ([2025-04-06](https://www.thingelstad.com/2025/04/06/poap-planing-for-minnebar.html)). Email-only minting came with the 2024 onboarding. |
| 16 | Image and design services for drops | 2023-01-16 [Premium Features](https://www.thingelstad.com/2023/01/16/premium-features-for.html); POAPathon post | "Creating images for POAPs seems like an obvious capability." | Not recorded. Jamie kept using POAPathon, then DALL-E, GPT and Gemini to make art. |
| 17 | Two-sided POAPs (front and back) | 2023-01-16 [Extensions](https://www.thingelstad.com/2023/01/16/poap-extensions.html) | "Why not support two images for POAPs so they have a front and a back." | Not recorded. |
| 18 | Official POAP Collections, with a completion POAP | 2023-01-16 [Extensions](https://www.thingelstad.com/2023/01/16/poap-extensions.html) | "It would be cool if there was an official collection that these were part of and that was part of the event pages." | **Yes.** "A year later and POAP has launched exactly what I described!" ([WT276](https://weekly.thingelstad.com/archive/276/), 2024-02-11). The Airport Rally ran as a Collection. |
| 19 | Unique metadata for each claim (e.g. escape-room time and clues) | 2023-01-16 [Extensions](https://www.thingelstad.com/2023/01/16/poap-extensions.html) | "If an issuer could add one off metadata to a specific claim code it could unlock a ton of use cases." | Not recorded. |
| 20 | POAP Collector plan at $3/mo: on-chain analytics, notes on each POAP, nearby-drop alerts, delivery alerts, one mainnet migration credit a month | 2023-01-16 [POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html) | "As a POAP collector, I would want to pay a relatively small monthly fee to be able to get cool information about my collection and display it well." | Not recorded as a paid plan. A related free feature appears in his writing: Moments/Memories photos attached to drops ([2024-02-03](https://www.thingelstad.com/2024/02/03/i-wanted-to.html), [2025-04-28](https://www.thingelstad.com/2025/04/28/minnebar-poap.html)). |
| 21 | POAP Pro at $20/mo: issue by email, collections, analytics embed, external IDs, redirect, metadata per claim | 2023-01-16 [POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html) | "What if we just kept everything as is, but added a new POAP Pro level." | Not recorded as a plan. Collections and email-based minting shipped separately (rows 8, 9, 18). |
| 22 | POAP Studio at $500/event and POAP for Business at $100/mo or $1,000/yr | 2023-01-16 [POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html) | "I think you could then have a service to provide a 'full service' experience for the issuer." | Not recorded. |
| 23 | Free or cheap tier for non-profits | 2023-01-16 [POAP as a Business](https://www.thingelstad.com/2023/01/16/poap-as-a.html) | "Make it super cheap or free for non-profits to use advanced POAP Pro and Studio capabilities." | Not recorded. |
| 24 | Bring POAPathon into the POAP drop-creation flow | 2023-01-03 [POAPathon Future Thoughts](https://www.thingelstad.com/2023/01/03/poapathon-future-thoughts.html) | "Getting in this flow of requests would help make sure there are enough contests to have a thriving community." | Not recorded. |
| 25 | Make onboarding usable for "your average person" | 2023-01-29 [WT239](https://weekly.thingelstad.com/archive/239/) | "It is getting easier, but it is still ridiculously complicated for even your average person to do this." | **Largely yes**, per 2024-01-14: "POAP ease-of-use is much improved!" |

Advice Jamie gave to others about POAP, kept here for completeness:
- **POAPathon** (2023-01-03): form a Gnosis-chain DAO with non-monetary governance tokens,
  run contests on-chain with escrow, focus only on POAP art, start a newsletter, and give
  POAPs for submitting and winning.
- **Minnestar** (2023-02-11): issue yearly Community Supporter POAPs with local-artist art,
  and possibly gate a supporter board seat or DAO on them. Minnebar 17 gave its first POAPs
  in 2023, and Jamie ran them.
- **Events in general**: the Quantum Mirror exhibit (2021-12-17), Halloween candy POAPs
  ([2022-10-17](https://www.thingelstad.com/2022/10/17/idea-could-be.html)), Art Shanty
  Projects ([2023-02-04](https://www.thingelstad.com/2023/02/04/art-shanty-projects.html)),
  the EFF ("If only they did POAPs", [2025-07-03](https://www.thingelstad.com/2025/07/03/ive-supported-the-electronic-frontier.html)),
  and the Devcon NFC swag ("should just be standard at any crypto events, or any events at all").

### The pattern, in Jamie's own arc

- 2023-01: Jamie publishes a three-part wishlist plus a business plan.
- 2024-01: POAP ships onboarding ("they had addressed everything I had wished for").
- 2024-02: POAP ships Collections ("exactly what I described").
- 2025-05: Location drops arrive ("now you can with location drops!").
- 2025-07: RSS never arrives, so Jamie builds POAP2RSS.
- 2025-12: POAP's Airport Rally does at global scale what Jamie's 612 POAP Challenge did in
  Minneapolis.
