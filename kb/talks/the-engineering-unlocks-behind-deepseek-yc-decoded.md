---
type: yc-video
title: "The Engineering Unlocks Behind DeepSeek | YC Decoded"
video_id: 4Tmn-XP93m4
slug: the-engineering-unlocks-behind-deepseek-yc-decoded
resource: https://www.youtube.com/watch?v=4Tmn-XP93m4
series: talks
speakers: []
topics: [ai-strategy, moats-and-competition, building-product, startup-ideas]
transcript_source: auto-captions
upload_date: 2025-02-05
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# The Engineering Unlocks Behind DeepSeek | YC Decoded — Compiled Truth

This YC Decoded explainer breaks down the real engineering innovations behind DeepSeek's V3 and R1 models, arguing the hype cycle was overblown but the underlying efficiency gains are real and mean the cost of intelligence keeps falling for startups.

**Key ideas (with timestamps):**
- DeepSeek V3 is a base model comparable to GPT-4o/Claude 3.5 Sonnet/Gemini 1.5, while R1 is a reasoning model built on top of V3 that matches OpenAI o1 on certain benchmarks [the-engineering-unlocks-behind-deepseek-yc-decoded @ 00:48](https://youtu.be/4Tmn-XP93m4?t=48)
- DeepSeek trained V3 natively in fp8 (rather than 16/32-bit) with an fp8 accumulation fix that periodically merges into a higher-precision fp32 accumulator, enabling large memory savings without sacrificing quality [the-engineering-unlocks-behind-deepseek-yc-decoded @ 02:19](https://youtu.be/4Tmn-XP93m4?t=139)
- V3 uses a mixture-of-experts architecture with 671B total parameters but only 37B activated per token, versus Llama 3's dense 405B activated every forward pass, an 11x reduction in per-token compute [the-engineering-unlocks-behind-deepseek-yc-decoded @ 04:33](https://youtu.be/4Tmn-XP93m4?t=273)
- Multi-head latent attention (MLA), introduced in the V2 paper, compresses key/value matrices into a latent representation, cutting KV cache size by 93.3% and boosting max generation throughput 5.76x [the-engineering-unlocks-behind-deepseek-yc-decoded @ 05:31](https://youtu.be/4Tmn-XP93m4?t=331)
- R1 was trained with reinforcement learning using simple rule-based accuracy/formatting rewards (no human or AI-labeled reasoning examples), via a technique called Group Relative Policy Optimization (GRPO) published in February 2024 [the-engineering-unlocks-behind-deepseek-yc-decoded @ 08:15](https://youtu.be/4Tmn-XP93m4?t=495)
- Pure RL alone produced emergent reasoning skills including an "aha moment" where the model recognized its own mistakes and backtracked, but raw R1-Zero output mixed languages randomly until a cold-start fine-tuning phase was added [the-engineering-unlocks-behind-deepseek-yc-decoded @ 09:36](https://youtu.be/4Tmn-XP93m4?t=576)
- Just two weeks after R1's release, OpenAI shipped o3-mini, which outperforms both R1 and o1 on key benchmarks, illustrating how fast frontier progress is moving [the-engineering-unlocks-behind-deepseek-yc-decoded @ 10:31](https://youtu.be/4Tmn-XP93m4?t=631)
- The widely cited $5.5 million training cost figure covers only the final V3 training run, not R1's training, R&D, or hardware opex, which are presumably in the hundreds of millions [the-engineering-unlocks-behind-deepseek-yc-decoded @ 11:25](https://youtu.be/4Tmn-XP93m4?t=685)
- A UC Berkeley lab reproduced R1-Zero's key reasoning techniques on a smaller model for just $30, showing the approach is genuinely reproducible and there's still room for new players at the frontier [the-engineering-unlocks-behind-deepseek-yc-decoded @ 11:53](https://youtu.be/4Tmn-XP93m4?t=713)

**See also:** [[ai-strategy]], [[moats-and-competition]], [[building-product]], [[startup-ideas]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
