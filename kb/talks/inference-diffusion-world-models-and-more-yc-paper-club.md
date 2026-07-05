---
type: yc-video
title: "Inference, Diffusion, World Models, and More | YC Paper Club"
video_id: wE1ZgJdt4uM
slug: inference-diffusion-world-models-and-more-yc-paper-club
resource: https://www.youtube.com/watch?v=wE1ZgJdt4uM
series: talks
speakers: []
topics: [ai-strategy, moats-and-competition]
transcript_source: auto-captions
upload_date: 2026-05-28
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Inference, Diffusion, World Models, and More | YC Paper Club — Compiled Truth

The inaugural YC Paper Club brought together researchers and founders in Palo Alto to present five recent papers spanning inference speedups, diffusion-based robotic control, world models, and the theory of generalization and data-constrained pre-training.

**Key ideas (with timestamps):**
- Inference is shifting from being seen as a cost/convenience lever to being a capability itself, since for methods whose performance scales with thinking time, tokens-per-second effectively caps peak intelligence [inference-diffusion-world-models-and-more-yc-paper-club @ 05:57](https://youtu.be/wE1ZgJdt4uM?t=357)
- "Speculative speculative decoding" (SSD) parallelizes the normally sequential draft-then-verify loop by having the draft model anticipate likely verification outcomes and start drafting the next round before verification finishes, hiding drafting latency almost entirely [inference-diffusion-world-models-and-more-yc-paper-club @ 12:18](https://youtu.be/wE1ZgJdt4uM?t=738)
- SSD can correctly predict verification outcomes roughly 80-90% of the time, enough to deliver large speedups in both latency and throughput compared to standard speculative decoding [inference-diffusion-world-models-and-more-yc-paper-club @ 14:13](https://youtu.be/wE1ZgJdt4uM?t=853)
- Diffusion Model Predictive Control (DMPC) uses diffusion models for both multi-step action proposals and multi-step dynamics models, reducing compounding errors and letting a simple sampling-based planner outperform prior approaches [inference-diffusion-world-models-and-more-yc-paper-club @ 20:26](https://youtu.be/wE1ZgJdt4uM?t=1226)
- Because DMPC factorizes the action proposal from the dynamics model, it can adapt to novel dynamics (e.g., a robot walker with a broken ankle) simply by re-adapting the dynamics model on new play data, recovering most lost performance [inference-diffusion-world-models-and-more-yc-paper-club @ 28:14](https://youtu.be/wE1ZgJdt4uM?t=1694)
- Lay World Model (a JEPA-style world model out of Yann LeCun's group) avoids representation collapse using a new SIG (sketching, isotropic, Gaussian) regularizer instead of the ad hoc tricks other world models rely on, and runs about 50x faster than competitors using under 24GB VRAM and only 15M parameters [inference-diffusion-world-models-and-more-yc-paper-club @ 41:38](https://youtu.be/wE1ZgJdt4uM?t=2498)
- World-model-based agents can quantify their own prediction error (e.g., detecting a spike in model error when an object's color or position is perturbed unexpectedly), giving them a form of native uncertainty estimation that model-free approaches lack [inference-diffusion-world-models-and-more-yc-paper-club @ 42:09](https://youtu.be/wE1ZgJdt4uM?t=2529)
- Andrew Gordon Wilson's PAC-Bayes-based work argues that "mysteries" of deep learning like overparameterization and benign overfitting are actually explainable by classical generalization theory once compression and inductive bias are measured correctly [inference-diffusion-world-models-and-more-yc-paper-club @ 44:51](https://youtu.be/wE1ZgJdt4uM?t=2691)
- When pre-training is data-constrained but compute-unconstrained, classical techniques (aggressive regularization, ensembling, and their combination) produce clean power-law scaling with measurably lower loss asymptotes than standard recipes, yielding a roughly 5x data-efficiency win [inference-diffusion-world-models-and-more-yc-paper-club @ 1:01:08](https://youtu.be/wE1ZgJdt4uM?t=3668)
- An 8-member ensemble can be distilled into a single dense 300M-parameter model while retaining about 83% of the loss improvement, showing data efficiency gains don't require large inference-time compute [inference-diffusion-world-models-and-more-yc-paper-club @ 1:02:40](https://youtu.be/wE1ZgJdt4uM?t=3760)

**See also:** [[ai-strategy]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
