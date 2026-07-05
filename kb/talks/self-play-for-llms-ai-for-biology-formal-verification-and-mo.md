---
type: yc-video
title: "Self-Play for LLMs, AI for Biology, Formal Verification, and More | YC Paper Club"
video_id: 3rWSvrFahIY
slug: self-play-for-llms-ai-for-biology-formal-verification-and-mo
resource: https://www.youtube.com/watch?v=3rWSvrFahIY
series: talks
speakers: []
topics: [ai-strategy, building-product, company-culture, management]
transcript_source: auto-captions
upload_date: 2026-06-12
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Self-Play for LLMs, AI for Biology, Formal Verification, and More — Compiled Truth

A YC Paper Club roundtable covering frontier AI research (protein language model scaling, LLM self-play, streaming RAG for voice, formal verification with Lean) and closing with a practical talk on running agentic coding teams like a real-time-strategy game.

**Key ideas (with timestamps):**
- The opening framing questions whether training only on human-generated data can ever be escaped via test-time compute or recursive self-improvement, since the full solution space is vastly larger than what's sampled from human demonstrations — motivating interest in self-play as an alternative [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 01:07](https://youtu.be/3rWSvrFahIY?t=67).
- A new protein language model (ESM Cambrian) trained purely on masked amino-acid prediction shows the same clean log-linear scaling law as LLMs, unlike its predecessor ESM2 which plateaued — the fix was scaling training data from 50 million to 2.8 billion sequences, not architecture [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 13:36](https://youtu.be/3rWSvrFahIY?t=816).
- That same model's structure predictor, using only a single input sequence with no hand-built multiple-sequence-alignment features, lands within a few points of AlphaFold3 on general proteins and edges it out on antibody design, suggesting handcrafted domain features matter most exactly where training data is scarce [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 18:44](https://youtu.be/3rWSvrFahIY?t=1124).
- A vanilla LLM self-play setup plateauses because rewarding the "conjecturer" model purely for producing problems the solver can't solve incentivizes messy, artificially overcomplicated problems rather than genuinely useful ones [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 33:36](https://youtu.be/3rWSvrFahIY?t=2016).
- A fix called self-guided self-play grounds generated problems in a set of real unsolved target problems and adds a third "guide" role to score relevance, letting a 7B model match the pass rate of a roughly 670B model on formal math proofs while using 8x more compute [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 36:35](https://youtu.be/3rWSvrFahIY?t=2195).
- Streaming RAG for voice agents runs retrieval on partial spoken queries instead of waiting for the question to finish, because even a few seconds of added latency breaks the feel of a natural conversation [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 40:36](https://youtu.be/3rWSvrFahIY?t=2436).
- The formal-verification language Lean is presented as central to an emerging "verified intelligence" trend spanning theorem proving (from GPT-f to recent Erdos-problem solutions), program verification, and even neural-network correctness proofs [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 54:36](https://youtu.be/3rWSvrFahIY?t=3276).
- Channel AI's engineering lead frames agentic coding as a real-time-strategy game: run many parallel Claude/Codex agents on separate git worktrees, default to spawning many "workers" (macro) rather than micromanaging any single agent, and never let agent capacity sit idle [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 1:00:12](https://youtu.be/3rWSvrFahIY?t=3612).
- The team maintains a shared, LLM-friendly knowledge base of linked markdown docs (cheaper for agents to parse than source code) that gets continuously updated with corrections, and broadly adopting these practices across the team grew PRs per engineer per month by another 60% [self-play-for-llms-ai-for-biology-formal-verification-and-mo @ 1:15:13](https://youtu.be/3rWSvrFahIY?t=4513).

**See also:** [[ai-strategy]], [[building-product]], [[company-culture]], [[management]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
