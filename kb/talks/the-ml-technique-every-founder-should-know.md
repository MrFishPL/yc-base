---
type: yc-video
title: "The ML Technique Every Founder Should Know"
video_id: dC_3ys349bU
slug: the-ml-technique-every-founder-should-know
resource: https://www.youtube.com/watch?v=dC_3ys349bU
series: talks
speakers: [francois-chahbar]
topics: [ai-strategy, building-product, startup-ideas, moats-and-competition]
transcript_source: auto-captions
upload_date: 2026-01-22
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# The ML Technique Every Founder Should Know — Compiled Truth

YC visiting partner Francois Chahbar explains diffusion, the machine-learning framework behind image, video, protein, robotics, and weather models, and argues founders should update their expectations of how far it will scale.

**Key ideas (with timestamps):**
- Diffusion is a fundamental ML framework for learning any data distribution by progressively noising data and training a model to reverse the process (denoise) [the-ml-technique-every-founder-should-know @ 00:20](https://youtu.be/dC_3ys349bU?t=20)
- Diffusion is unusually good at mapping high-dimensional spaces to high-dimensional spaces even with very small training sets, e.g. learning from only 30 images [the-ml-technique-every-founder-should-know @ 01:21](https://youtu.be/dC_3ys349bU?t=81)
- The field evolved by finding easier prediction targets for the model — predicting the added error was easier than predicting the data itself, and predicting velocity was easier still [the-ml-technique-every-founder-should-know @ 05:29](https://youtu.be/dC_3ys349bU?t=329)
- Flow matching (from Meta's Yann Lipman) simplifies diffusion into a straight-line velocity between noise and data, reducing the whole training procedure to about 10-15 lines of code [the-ml-technique-every-founder-should-know @ 11:29](https://youtu.be/dC_3ys349bU?t=689)
- The trained model is domain-agnostic — the same velocity-prediction code works for images, text, proteins, DNA, weather, or robot trajectories [the-ml-technique-every-founder-should-know @ 14:25](https://youtu.be/dC_3ys349bU?t=865)
- A key limitation is that diffusion models can't be stepped beyond the number of steps they were trained on — doubling steps at inference just breaks the output [the-ml-technique-every-founder-should-know @ 18:36](https://youtu.be/dC_3ys349bU?t=1116)
- Diffusion has effectively taken over generative AI applications except in autoregressive LLMs (text) and game-tree search domains like AlphaGo, where MCTS still wins [the-ml-technique-every-founder-should-know @ 24:12](https://youtu.be/dC_3ys349bU?t=1452)
- Founders training their own models should seriously evaluate diffusion for any application, even just to get a useful latent space [the-ml-technique-every-founder-should-know @ 25:08](https://youtu.be/dC_3ys349bU?t=1508)
- Founders who use models rather than train them should update their priors on how fast diffusion-based image/video generation has improved (roughly 1,000x from early Midjourney to Sora/Veo/Flux/SD3) and expect similar gains in proteins, DNA, and robotics policies [the-ml-technique-every-founder-should-know @ 25:25](https://youtu.be/dC_3ys349bU?t=1525)
- Diffusion policies are expected to be a major unlock for robotics actually working in the real world [the-ml-technique-every-founder-should-know @ 23:26](https://youtu.be/dC_3ys349bU?t=1406)

**See also:** [[ai-strategy]], [[building-product]], [[startup-ideas]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
