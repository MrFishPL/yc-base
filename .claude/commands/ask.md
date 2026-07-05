---
description: Answer a startup question grounded ONLY in the YC corpus, cited to video + timestamp. Use for questions about fundraising, product-market fit, pricing, hiring, enterprise/B2B sales, growth, retention, YC applications, or founder psychology.
argument-hint: <your startup question>
allowed-tools: Read, Grep, Glob, Bash(python3 scripts/search.py *), Bash(rg:*)
---

Answer the question below using the **answer-from-kb** skill.

Delegate the corpus search to the `retriever` subagent so raw transcript text stays out of this
context, then have the `synthesizer` subagent write the final answer. Every claim must end with a
`[<slug> @ mm:ss]` citation linking to `https://youtu.be/<video_id>?t=<seconds>`. If the corpus
does not contain the answer, say so and name the gap — do not answer from pretraining knowledge.

Question: $ARGUMENTS
