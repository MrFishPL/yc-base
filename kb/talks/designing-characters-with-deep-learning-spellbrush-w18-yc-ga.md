---
type: yc-video
title: "Designing Characters with Deep Learning: Spellbrush (W18) - YC Gaming Tech Talks 2020"
video_id: 4a0nj4o2O9k
slug: designing-characters-with-deep-learning-spellbrush-w18-yc-ga
resource: https://www.youtube.com/watch?v=4a0nj4o2O9k
series: talks
speakers: [corey]
topics: [ai-strategy, building-product, moats-and-competition, hiring]
transcript_source: auto-captions
upload_date: 2020-12-07
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Designing Characters with Deep Learning: Spellbrush (W18) - YC Gaming Tech Talks 2020 — Compiled Truth

Spellbrush CEO Corey explains how the company uses generative adversarial networks (GANs) to generate anime-style character art in seconds, dramatically cutting the cost and time of game art production.

**Key ideas (with timestamps):**
- Art production is one of the most expensive parts of game development, often 50-70% of total production budget on AAA titles, motivating Spellbrush to apply AI to the asset pipeline. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 00:21](https://youtu.be/4a0nj4o2O9k?t=21)
- Spellbrush's AI can generate a character illustration on par with a professional artist in under two seconds, versus the two to fifteen hours a human illustrator would need. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 01:04](https://youtu.be/4a0nj4o2O9k?t=64)
- The tool can generate hundreds of characters in the same time it takes to generate just one, making content creation at scale possible. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 01:52](https://youtu.be/4a0nj4o2O9k?t=112)
- Their approach uses a GAN with a generator network that learns to draw art and a discriminator network that learns to distinguish real art from generated art, trained adversarially over millions of iterations. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 02:30](https://youtu.be/4a0nj4o2O9k?t=150)
- Feeding random noise (the latent space) into the generator lets them control outputs, generating the same character in different expressions, colors, or illustration styles. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 04:06](https://youtu.be/4a0nj4o2O9k?t=246)
- The training dataset, crawled from publicly available anime images (~10 million images), is skewed roughly 6-to-1 female-to-male and under 3% dark-skinned characters, so the team corrected the generation distribution to better represent real-world demographics. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 05:29](https://youtu.be/4a0nj4o2O9k?t=329)
- Because cloud GPU training is expensive (roughly $10-24/hour on AWS, with models taking 7-10 days and costing $3,000-4,000 each to train), Spellbrush built its own in-office supercomputer cluster with Titan RTX GPUs, bringing running cost down to about $0.60/hour. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 07:39](https://youtu.be/4a0nj4o2O9k?t=459)
- The company is a small five-person team building the world's first AI-illustrated game and is hiring a sixth person across 2D animation, motion design, real-time VFX, and AI research. [designing-characters-with-deep-learning-spellbrush-w18-yc-ga @ 09:02](https://youtu.be/4a0nj4o2O9k?t=542)

**See also:** [[ai-strategy]], [[building-product]], [[moats-and-competition]], [[hiring]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
