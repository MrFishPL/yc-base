---
type: yc-video
title: "Making Music and Art Through Machine Learning - Doug Eck of Magenta"
video_id: yz-fHidp1M8
slug: making-music-and-art-through-machine-learning-doug-eck-of-ma
resource: https://www.youtube.com/watch?v=yz-fHidp1M8
series: talks
speakers: [doug-eck]
topics: [ai-strategy, building-product, talking-to-users, resilience]
transcript_source: auto-captions
upload_date: 2017-07-21
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Making Music and Art Through Machine Learning - Doug Eck of Magenta — Compiled Truth

Doug Eck, a Google research scientist leading Magenta, discusses building open-source machine-learning tools for music and art as a product-and-research problem: chasing quality over benchmarks, learning from what artists actually use, and betting on techniques (like LSTM and reinforcement learning) long before they pay off.

**Key ideas (with timestamps):**
- Eck frames Magenta's models like new artistic mediums whose current "weird, ugly, uncomfortable" failure modes (per a Brian Eno quote) will eventually become signature effects, the way tape distortion or 8-bit sound did [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 00:35](https://youtu.be/yz-fHidp1M8?t=35)
- Evaluating generative-art models is an unsolved, open problem for the team — Eck admits Magenta hasn't shipped a viral consumer app that could generate a feedback loop of human ratings to improve models, unlike his past work in music recommendation [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 04:48](https://youtu.be/yz-fHidp1M8?t=288)
- Direct user feedback from musicians (e.g., "why would I want to run a Python command to generate a thousand MIDI files?") pointed the team toward building more fluid, workflow-integrated tools (DAW plugins) instead of command-line outputs [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 07:17](https://youtu.be/yz-fHidp1M8?t=437)
- The most engaged users of NSynth turned out to be serious sound-design musicians, not casual users, because the model produced genuinely new harmonic textures rather than familiar synthesizer sounds [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 10:16](https://youtu.be/yz-fHidp1M8?t=616)
- LSTM was a near-dead research dead-end used by only three researchers worldwide in the early days at IDSIA; it only became broadly useful once faster machines and more memory let these data-hungry models finally scale — a "20-year overnight success" for one researcher (Alex Graves) who stuck with it [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 17:08](https://youtu.be/yz-fHidp1M8?t=1028)
- Reinforcement learning (deep Q-learning) can be layered onto a trained generative model to reward it for following arbitrary rules (e.g., 1800s counterpoint composition rules), making otherwise "pretty boring" LSTM-generated music noticeably catchier — a general technique for tilting any pretrained generative model toward a target aesthetic without hand-coding rules into it [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 33:14](https://youtu.be/yz-fHidp1M8?t=1994)
- Eck's team deliberately positions Magenta as a tool, not a replacement, because early internal and external discussion made clear that a "push button, get finished music" product would be uninteresting and lose the cathartic creative value that engages users [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 28:14](https://youtu.be/yz-fHidp1M8?t=1694)
- Negative public reactions (a researcher calling AI-generated folk songs "bad for humanity") don't worry Eck — he argues that art nobody dislikes is boring, and finding even a narrow, engaged audience is a sign of real creative value [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 26:42](https://youtu.be/yz-fHidp1M8?t=1602)
- The team's near-term "holy grail" is generating long-form, structurally coherent compositions (handling chord changes and larger musical arcs) rather than just convincing 10-20 second textures, which would let composers offload longer-timescale decisions to the model [making-music-and-art-through-machine-learning-doug-eck-of-ma @ 39:16](https://youtu.be/yz-fHidp1M8?t=2356)

**See also:** [[ai-strategy]], [[building-product]], [[talking-to-users]], [[resilience]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
</content>
