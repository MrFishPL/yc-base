---
type: yc-video
title: "Recursion Is The Next Scaling Law In AI"
video_id: DGtUUMNYLcc
slug: recursion-is-the-next-scaling-law-in-ai
resource: https://www.youtube.com/watch?v=DGtUUMNYLcc
series: talks
speakers: []
topics: [ai-strategy, moats-and-competition]
transcript_source: auto-captions
upload_date: 2026-05-01
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Recursion Is The Next Scaling Law In AI — Compiled Truth

An episode of Decoded arguing that recursive computation (as shown by hierarchical reasoning models and tiny recursive models) can beat much larger transformer LLMs on hard combinatorial tasks, pointing to recursion as a complementary scaling axis to raw model size.

**Key ideas (with timestamps):**
- LLM transformers do a one-shot feedforward pass per input at train time, so unlike RNNs they avoid vanishing-gradient/backprop-through-time problems but give up latent, compressed reasoning in the time direction [recursion-is-the-next-scaling-law-in-ai @ 03:09](https://youtu.be/DGtUUMNYLcc?t=189)
- Incompressible problems like sorting, Sudoku, and mazes are theoretically impossible to solve in one shot if the model has fewer layers than the required sequential steps, because there's a proven lower bound on comparisons needed [recursion-is-the-next-scaling-law-in-ai @ 04:39](https://youtu.be/DGtUUMNYLcc?t=279)
- The Hierarchical Reasoning Model (HRM), a 27M-parameter model trained from scratch on only ~1,000 ARC-Prize tasks with no pretraining, hit ~70% on ARC-Prize 1 at a time when OpenAI's o3 scored zero [recursion-is-the-next-scaling-law-in-ai @ 09:43](https://youtu.be/DGtUUMNYLcc?t=583)
- HRM's key trick versus prior recursive nets (e.g. Neural Turing Machines) is to not backprop through all recursion steps — it uses a deep-equilibrium-style fixed-point iteration with a stop-grad, effectively building a "mini-batch" from different hidden-state positions instead of different inputs [recursion-is-the-next-scaling-law-in-ai @ 11:17](https://youtu.be/DGtUUMNYLcc?t=677)
- The follow-on Tiny Recursive Model (TRM) simplifies HRM by collapsing the separate low-/high-level networks into one shared network and shrinking it to 7M parameters, yet improves ARC-Prize 1 performance from 70% to 87% [recursion-is-the-next-scaling-law-in-ai @ 33:19](https://youtu.be/DGtUUMNYLcc?t=1999)
- The single most important factor found across both papers is the "outer refinement loop," a form of truncated backprop-through-time (T=1) that turns out to be sufficient, even though it seemed counterintuitive [recursion-is-the-next-scaling-law-in-ai @ 20:42](https://youtu.be/DGtUUMNYLcc?t=1242)
- These recursive models can discover strategies (like partially filling in a Sudoku board) without chain-of-thought supervision, whereas chain-of-thought and tool-use approaches are fundamentally bounded by existing human-generated training traces [recursion-is-the-next-scaling-law-in-ai @ 27:15](https://youtu.be/DGtUUMNYLcc?t=1635)
- TRMs and HRMs are narrow, task-specific models (a Sudoku-trained model can't do ARC-Prize), unlike general-purpose LLMs, so the interesting frontier is combining recursive reasoning inside a general model's learned embedding space rather than at the token level [recursion-is-the-next-scaling-law-in-ai @ 36:09](https://youtu.be/DGtUUMNYLcc?t=2169)

**See also:** [[ai-strategy]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
