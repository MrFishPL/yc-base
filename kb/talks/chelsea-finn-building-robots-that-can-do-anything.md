---
type: yc-video
title: "Chelsea Finn: Building Robots That Can Do Anything"
video_id: a8-QsBHoH94
slug: chelsea-finn-building-robots-that-can-do-anything
resource: https://www.youtube.com/watch?v=a8-QsBHoH94
series: talks
speakers: [chelsea-finn]
topics: [ai-strategy, startup-ideas, moats-and-competition, hiring]
transcript_source: auto-captions
upload_date: 2025-07-22
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# Chelsea Finn: Building Robots That Can Do Anything — Compiled Truth

Physical Intelligence co-founder Chelsea Finn argues that general-purpose foundation models for robots, not narrow per-application robotics companies, are the path to bringing intelligence into the physical world, and walks through the pre-training/post-training recipe that got a robot to reliably fold laundry.

**Key ideas (with timestamps):**
- Solving a single robotics application from scratch (hardware, software, movement primitives, edge cases) is so costly that most robotics companies fail to bring robots into daily life, motivating a general-purpose "any robot, any task, any environment" foundation model instead [chelsea-finn-building-robots-that-can-do-anything @ 00:43](https://youtu.be/a8-QsBHoH94?t=43)
- Large-scale data alone (industrial automation logs, YouTube videos, simulation) is necessary but not sufficient because each source lacks either diversity, embodiment match, or realism [chelsea-finn-building-robots-that-can-do-anything @ 02:04](https://youtu.be/a8-QsBHoH94?t=124)
- The breakthrough for the laundry-folding robot came from pre-training on all robot data then fine-tuning on a small, curated, high-quality demonstration set, rather than training on all data uniformly [chelsea-finn-building-robots-that-can-do-anything @ 09:15](https://youtu.be/a8-QsBHoH94?t=555)
- Swapping in a 3B-parameter pre-trained vision-language model (PaliGemma) with a flow-matching diffusion action head, trained on the full robot dataset and fine-tuned with the same curated recipe, improved speed and consistency further [chelsea-finn-building-robots-that-can-do-anything @ 11:06](https://youtu.be/a8-QsBHoH94?t=666)
- The same pre-training/post-training recipe transferred with no laundry-specific tuning to unrelated tasks like cleaning tables, grinding coffee, folding a cardboard box, and lighting a candle, and even to a different company's robot never seen in person [chelsea-finn-building-robots-that-can-do-anything @ 15:29](https://youtu.be/a8-QsBHoH94?t=929)
- To generalize to unseen homes, the team collected mobile-manipulation data from 100+ rooms that made up only 2.4% of the pre-training mix, yet excluding the rest of the (non-mobile) data dropped performance from over 80% to under 60% in novel homes [chelsea-finn-building-robots-that-can-do-anything @ 22:35](https://youtu.be/a8-QsBHoH94?t=1355)
- Naive models often ignored language instructions; predicting tokenized actions and stopping gradients into the randomly-initialized diffusion head preserved the VLM's language-following ability, raising instruction-follow rate from 20% to 80% [chelsea-finn-building-robots-that-can-do-anything @ 20:44](https://youtu.be/a8-QsBHoH94?t=1244)
- Robots were tested successfully in three never-before-seen Airbnb kitchens and bedrooms on tasks like closing cabinets, putting away dishes, cleaning spills, and tidying beds [chelsea-finn-building-robots-that-can-do-anything @ 21:23](https://youtu.be/a8-QsBHoH94?t=1283)
- To handle open-ended prompts (e.g. "make me a vegan sandwich, no pickles"), the team used vision-language models to generate synthetic hypothetical human prompts for existing robot data, training a high-level policy to decompose requests into low-level commands [chelsea-finn-building-robots-that-can-do-anything @ 26:51](https://youtu.be/a8-QsBHoH94?t=1611)
- Existing frontier foundation models performed substantially worse than Physical Intelligence's purpose-trained high-level planner because they struggle with visual understanding grounded in physical/robotics scenarios [chelsea-finn-building-robots-that-can-do-anything @ 29:28](https://youtu.be/a8-QsBHoH94?t=1768)

**See also:** [[ai-strategy]], [[startup-ideas]], [[moats-and-competition]], [[hiring]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
