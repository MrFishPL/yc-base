---
type: yc-video
title: "State-Of-The-Art Prompting For AI Agents"
video_id: DL82mGde6wo
slug: state-of-the-art-prompting-for-ai-agents
resource: https://www.youtube.com/watch?v=DL82mGde6wo
series: lightcone
speakers: [garry-tan, jared-friedman, diana-hu, harj-taggar]
topics: [ai-strategy, building-product, enterprise-sales, sales, metrics, moats-and-competition]
transcript_source: auto-captions
upload_date: 2025-05-30
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# State-Of-The-Art Prompting For AI Agents — Compiled Truth

The YC partners survey a dozen AI startups on frontier prompt-engineering practice, arguing that prompting today feels like coding in 1995 and that evals, not prompts, are the real defensible asset.

**Key ideas (with timestamps):**
- Parahelp's customer-support agent prompt (powering Perplexity, Replit, and Bolt support) shows the best prompts open with a clear role definition, a specific task, a step-by-step plan, and a strict output format [state-of-the-art-prompting-for-ai-agents @ 01:46](https://youtu.be/DL82mGde6wo?t=106)
- The best prompts increasingly look like programming rather than English, using XML-tag structure because models were RLHF post-trained on XML-like input and respond better to it [state-of-the-art-prompting-for-ai-agents @ 03:21](https://youtu.be/DL82mGde6wo?t=201)
- A system/developer/user prompt split is emerging as the architecture for vertical AI agents: the system prompt defines company-wide logic, the developer prompt holds customer-specific context, avoiding the trap of becoming a "consulting company" that rewrites prompts per client [state-of-the-art-prompting-for-ai-agents @ 04:59](https://youtu.be/DL82mGde6wo?t=299)
- Metaprompting — feeding an LLM its own prompt plus failure examples so it rewrites itself — is a consistent, powerful pattern across AI startups, including "prompt folding" where one prompt dynamically generates specialized versions of itself [state-of-the-art-prompting-for-ai-agents @ 07:16](https://youtu.be/DL82mGde6wo?t=436)
- Because models try so hard to be helpful they will hallucinate an answer rather than admit uncertainty, so prompts need an explicit escape hatch instructing the model to stop and ask rather than guess [state-of-the-art-prompting-for-ai-agents @ 09:15](https://youtu.be/DL82mGde6wo?t=555)
- YC's internal pattern is a "debug info" output field where the model can flag confusing or underspecified instructions back to the developer, effectively generating a to-do list from production data [state-of-the-art-prompting-for-ai-agents @ 09:54](https://youtu.be/DL82mGde6wo?t=594)
- Evals, not prompts, are the true crown-jewel data asset — Parahelp was willing to open-source its prompt because without the evals behind it, competitors can't know why it was written that way or how to improve it [state-of-the-art-prompting-for-ai-agents @ 14:35](https://youtu.be/DL82mGde6wo?t=875)
- Founders are becoming "forward deployed engineers" in the Palantir tradition: sitting directly with the end user (e.g., a tractor sales regional manager) to codify their real reward function into evals, which becomes the startup's moat [state-of-the-art-prompting-for-ai-agents @ 15:12](https://youtu.be/DL82mGde6wo?t=912)
- Vertical AI agent founders are closing six- and seven-figure enterprise deals (Giga ML with Zepto, Happy Robot with top logistics brokers) by acting as forward deployed engineers, returning within a day with a tuned demo that makes buyers say "I've never seen anything like that" [state-of-the-art-prompting-for-ai-agents @ 23:23](https://youtu.be/DL82mGde6wo?t=1403)
- Different models have different "personalities" for scoring rubrics — o3 rigidly enforces a rubric like a soldier, while Gemini 2.5 Pro reasons flexibly about exceptions like a high-agency employee, which matters when using LLMs to score things like investor behavior [state-of-the-art-prompting-for-ai-agents @ 27:39](https://youtu.be/DL82mGde6wo?t=1659)

**See also:** [[ai-strategy]], [[building-product]], [[enterprise-sales]], [[sales]], [[metrics]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
