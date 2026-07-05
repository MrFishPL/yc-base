---
type: yc-video
title: "Things That Don't Scale, The Software Edition – Dalton Caldwell and Michael Seibel"
video_id: TCPjk8Tpb5c
slug: things-that-don-t-scale-the-software-edition-dalton-caldwell
resource: https://www.youtube.com/watch?v=TCPjk8Tpb5c
series: dalton-and-michael
speakers: [dalton-caldwell, michael-seibel]
topics: [do-things-that-dont-scale, mvp, building-product, product-market-fit]
transcript_source: auto-captions
upload_date: 2022-02-16
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Things That Don't Scale, The Software Edition – Dalton Caldwell and Michael Seibel — Compiled Truth

Great software companies (Gmail, Facebook, Twitch, Google, MySpace) were built early on with dirty, unscalable hacks, and founders only earn the right to build scalable systems after they've proven people want the product.

**Key ideas (with timestamps):**
- Paul Buchheit's "9010 solution" — get 90% of the benefit for 10% of the work — is the core philosophy behind most of these hacks, even though founders hate hearing it [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 00:56](https://youtu.be/TCPjk8Tpb5c?t=56)
- Gmail's invite system, often mythologized as a viral growth hack, actually existed purely because Google didn't have enough server hard-drive space to let everyone in [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 04:47](https://youtu.be/TCPjk8Tpb5c?t=287)
- Early Facebook scaled by running a completely separate PHP instance, MySQL database, and memcache for every single school rather than building one global users table, which took them years to eventually build [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 08:07](https://youtu.be/TCPjk8Tpb5c?t=487)
- Twitch (then Justin.tv) handled 20x traffic spikes from popular streamers by making pages fully static (breaking dynamic features like usernames and view counts) so the site wouldn't crash under load [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 11:10](https://youtu.be/TCPjk8Tpb5c?t=670)
- Friendster tried to compute real-time two-degree friend network sizes and hit MySQL scaling problems, while MySpace solved the same feature by simply saying "so-and-so is in your extended network" [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 12:06](https://youtu.be/TCPjk8Tpb5c?t=726)
- Justin.tv's imeem music product was actually built on repurposed video infrastructure — every "audio" file was secretly a video file with a blank video track, avoiding building separate audio tooling [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 15:51](https://youtu.be/TCPjk8Tpb5c?t=951)
- When an ISP refused a free-peering relationship and Twitch was losing money serving it video for free, they simply blocked video after 10 minutes with a message asking users to call and complain, and it worked [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 18:32](https://youtu.be/TCPjk8Tpb5c?t=1112)
- Rather than paying to professionally translate the site into 40 languages, Twitch borrowed Reddit's approach and let the community crowd-translate every string for free [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 19:14](https://youtu.be/TCPjk8Tpb5c?t=1154)
- Google's MapReduce was invented under duress after their monolithic batch web-indexing script started silently failing for months, leaving stale search results before anyone noticed [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 22:20](https://youtu.be/TCPjk8Tpb5c?t=1340)
- You earn the privilege to build scalable systems by first proving people want your product with an unscalable hack — like Wozniak hand-soldering the original Apple computer before Apple could ever build AirPods [things-that-don-t-scale-the-software-edition-dalton-caldwell @ 24:23](https://youtu.be/TCPjk8Tpb5c?t=1463)

**See also:** [[do-things-that-dont-scale]], [[mvp]], [[building-product]], [[product-market-fit]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
