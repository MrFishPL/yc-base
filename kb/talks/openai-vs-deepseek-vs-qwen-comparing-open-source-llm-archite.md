---
type: yc-video
title: "OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures"
video_id: raTbhtKZTZA
slug: openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite
resource: https://www.youtube.com/watch?v=raTbhtKZTZA
series: talks
speakers: []
topics: [ai-strategy, moats-and-competition]
transcript_source: auto-captions
upload_date: 2025-08-29
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures — Compiled Truth

A technical walkthrough comparing the architectures, training pipelines, and context-extension strategies of three flagship open-weight LLM releases (GPT OSS, Qwen 3, DeepSeek V3), arguing that headline benchmark scores matter less than the specific engineering choices behind them.

**Key ideas (with timestamps):**
- GPT OSS is a mixture-of-experts model (120B and 20B variants) that activates only the top four experts per token for efficient inference [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 00:27](https://youtu.be/raTbhtKZTZA?t=27)
- GPT OSS achieves its 131,000-token context window by applying YaRN scaling natively during pre-training rather than as a later fine-tune, so the model is "born with" long-context ability [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 01:27](https://youtu.be/raTbhtKZTZA?t=87)
- Qwen 3's mixture-of-experts base models match dense-model performance while activating only about a fifth as many parameters [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 08:40](https://youtu.be/raTbhtKZTZA?t=520)
- Qwen 3 replaced the QKV bias used in earlier Qwen models with QK norm, dynamically rescaling query/key vectors to keep attention scores stable at scale [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 04:03](https://youtu.be/raTbhtKZTZA?t=243)
- Qwen 3's reasoning RL stage needed only about 4,000 query-verifier pairs to meaningfully strengthen complex problem solving [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 05:44](https://youtu.be/raTbhtKZTZA?t=344)
- DeepSeek V3 uses multi-head latent attention (MLA), compressing keys/values into a smaller latent space, which the earlier V2 paper found delivers greater memory savings and better modeling performance than grouped-query attention in long-context models [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 08:03](https://youtu.be/raTbhtKZTZA?t=483)
- DeepSeek V3.1 extends the original V3 checkpoint with a two-phase long-context training approach and a hybrid thinking mode that toggles between reasoning-heavy and lightweight inference [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 07:22](https://youtu.be/raTbhtKZTZA?t=442)
- The three labs extend context length via very different paths: GPT OSS bakes YaRN in during pre-training, DeepSeek fine-tunes in stages (32K then 128K), and Qwen fine-tunes to 32K and only applies YaRN scaling at inference time [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 09:34](https://youtu.be/raTbhtKZTZA?t=574)
- Because most frontier labs report empirical findings without first-principles justification, and dataset engineering details remain opaque, the specific dataset work is likely a major part of each lab's competitive moat [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 11:32](https://youtu.be/raTbhtKZTZA?t=692)
- The core takeaway is to focus on the specific methods labs use to hit their results rather than on topline benchmark or context-length numbers alone [openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite @ 11:46](https://youtu.be/raTbhtKZTZA?t=706)

**See also:** [[ai-strategy]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
</content>
