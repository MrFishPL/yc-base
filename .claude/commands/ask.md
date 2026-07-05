---
description: Answer a startup question grounded ONLY in the YC corpus, cited to video + timestamp. Searches broadly across ~620 talks via parallel subagents. Use for fundraising, PMF, pricing, hiring, enterprise/B2B sales, growth, retention, YC applications, founder psychology, competition, AI strategy.
argument-hint: <your startup question>
allowed-tools: Read, Grep, Glob, Task, Bash(python3 scripts/search.py *), Bash(rg:*)
---

Answer the question below using the **answer-from-kb** skill.

Search **broadly**: fan out several `retriever` subagents **in parallel** (topic, keyword, reframe,
people, and adjacency lenses — launch them in one message so they run at once), each returning
cited evidence. Then merge and synthesize with the `synthesizer`. Bias toward recall — it's better
to over-retrieve than to miss the best talk. Every claim in the final answer must end with a
`[<slug> @ mm:ss](https://youtu.be/<video_id>?t=<seconds>)` citation. Surface disagreements with
both sides cited. If a wide search truly finds nothing, say so — never answer from pretraining.

Question: $ARGUMENTS
