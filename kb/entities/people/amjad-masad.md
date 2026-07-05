---
type: person
title: "Amjad Masad"
slug: amjad-masad
aliases: []
role: founder
updated: 2026-07-05
---
# Amjad Masad — Compiled Truth

Founder and CEO of Replit, who steered the company from a near-failure through an all-in bet on AI coding agents to $100M ARR. His recurring throughline is that software creation is undergoing an expert-to-everyone transition like mainframes-to-PCs: the hard problem isn't the model writing code but building the "habitat" (sandboxed infra, transactional file systems, testing, deployment, payments) that lets agents work reliably and autonomously, and that this shift collapses application-software value while turning non-engineers — product managers, designers, domain experts — into builders. He is skeptical of scaling context windows or raw model hype as substitutes for custom orchestration/retrieval and rigorous internal evals, and argues company structure should flatten toward small, generalist, agent-augmented teams rather than traditional management hierarchies.

**Talks:** 4 in the corpus.
**See also:** [[ai-strategy]], [[building-product]], [[moats-and-competition]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — Masad frames the company of the future as made of builders and salespeople: sales becomes evangelism/education (one of the more defensible jobs since people trust humans), while nearly everyone acts as a generalist founder finding problems and deputizing agents to solve them [replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the @ 35:04](https://youtu.be/kMYeTRqzAfc?t=2104)
- 2026-07-05 — Masad believes the industry is headed to a "post-prompting world" where users give agents high-level goals rather than detailed prompts, and expects a future version could be told to "build me a SaaS company and try to market it" [replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the @ 28:14](https://youtu.be/kMYeTRqzAfc?t=1694)
- 2026-07-05 — Replit's ambition is that anyone who can read and write can go from an idea to a deployed, scalable app without touching any technical details, having solved the dev environment, deployment, and now the coding itself via natural language [replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the @ 00:49](https://youtu.be/kMYeTRqzAfc?t=49)
- 2026-07-05 — A physical therapist with no coding background built a sophisticated body-tracking health app on Replit after spending hundreds of thousands of dollars offshoring development unsuccessfully, illustrating that domain experts can now build their own products [replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the @ 06:45](https://youtu.be/kMYeTRqzAfc?t=405)
- 2026-07-05 — Enterprise clients like Whoop report the number of ideas they can try has grown by an order of magnitude (from ~5 tried out of 100 to ~50) because non-engineers can now build software themselves [replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the @ 09:19](https://youtu.be/kMYeTRqzAfc?t=559)
- 2026-07-05 — Software engineering is shifting from something only trained experts do to something anyone can do, mirroring the arc from mainframes to PCs [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 01:57](https://youtu.be/lWmDiDGsLK4?t=117)
- 2026-07-05 — The hard part of agentic coding isn't the model writing code, it's building the sandboxed, scalable "habitat" infrastructure (VMs, package managers, deployments, databases) the agent operates in [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 04:33](https://youtu.be/lWmDiDGsLK4?t=273)
- 2026-07-05 — Prediction: application software value will trend toward zero over the coming years as anyone can generate any software with one prompt, disrupting the vertical SaaS market [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 16:01](https://youtu.be/lWmDiDGsLK4?t=961)
- 2026-07-05 — To survive the collapse in application-software value, Replit itself must evolve from "makes applications" to "solves problems with software," becoming a universal problem solver [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 39:13](https://youtu.be/lWmDiDGsLK4?t=2353)
- 2026-07-05 — As transaction costs fall to zero, hiring full-time employees becomes less necessary; getting a developer (human or agent) could become as frictionless as hailing an Uber [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 24:28](https://youtu.be/lWmDiDGsLK4?t=1468)
- 2026-07-05 — The best way to start an "agent company" is to build in a domain you personally have deep expertise in, since domain knowledge is the key advantage in a crowded agent-startup market [the-future-of-software-creation-with-replit-ceo-amjad-masad @ 37:12](https://youtu.be/lWmDiDGsLK4?t=2232)
- 2026-07-05 — Replit nearly failed before pivoting fully to its AI agent; the company laid off roughly half its staff and "burned the boats" on making Replit Agent work [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 02:57](https://youtu.be/kOyIjt6FUrw?t=177)
- 2026-07-05 — Claude 3.5's release was the turning point that let the agent stay coherent for 5-10 minutes instead of the 2-3 minutes GPT-4o managed, and without it Replit likely would have failed [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 03:30](https://youtu.be/kOyIjt6FUrw?t=210)
- 2026-07-05 — Replit built a fully transactional, snapshot-based file system and database so agents can roll back mistakes and sample multiple branches, then pick the best one much like Anthropic's SWE-bench "with sampling" scores jump from ~70% to ~80% [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 06:23](https://youtu.be/kOyIjt6FUrw?t=383)
- 2026-07-05 — Security is the biggest blocker to letting non-engineers ship straight to production, so Replit builds in vetted auth, database, and payments components rather than letting LLMs write their own [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 12:51](https://youtu.be/kOyIjt6FUrw?t=771)
- 2026-07-05 — Replit deliberately avoids ARR-only goals, tracking product and retention goals instead, because it is "very easy in AI to increase ARR while users are not happy" [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 24:40](https://youtu.be/kOyIjt6FUrw?t=1480)
- 2026-07-05 — Masad frames Replit's real moat as two years of hard-to-replicate infrastructure work (a transactional, snapshot-based distributed file system and NixOS-based package caching), comparing it to Netflix's non-obvious content-production moat [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 30:24](https://youtu.be/kOyIjt6FUrw?t=1824)
- 2026-07-05 — Replit hides the underlying model choice from users because heavy internal eval work shows raw hype (e.g. users wanting "Gemini") doesn't match actual task performance [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 28:01](https://youtu.be/kOyIjt6FUrw?t=1681)
- 2026-07-05 — His advice to founders is to build "on the edge of what's possible" so that model improvements make an already-built product suddenly valuable [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 34:44](https://youtu.be/kOyIjt6FUrw?t=2084)
- 2026-07-05 — After raising a large round, Replit tried to "grow up" by hiring executives and building management layers, which Amjad found made the company miserable and unproductive; reversing to a small, flat structure with no roadmap made the team far more productive [now-anyone-can-code-how-ai-agents-can-build-your-whole-app @ 26:18](https://youtu.be/jbIQfoldLag?t=1578)
- 2026-07-05 — The system is a multi-agent orchestration (using different models per task, e.g. Claude Sonnet 3.5 for coding) rather than one model doing everything, because plain RAG hits a ceiling on large codebases and requires a custom retrieval/indexing system to find the right places to edit [now-anyone-can-code-how-ai-agents-can-build-your-whole-app @ 04:27](https://youtu.be/jbIQfoldLag?t=267)
- 2026-07-05 — Large context windows alone are risky and don't substitute for good context/memory management, since models bias toward whatever is placed at the end of the context [now-anyone-can-code-how-ai-agents-can-build-your-whole-app @ 14:33](https://youtu.be/jbIQfoldLag?t=873)
- 2026-07-05 — Amjad believes "functional AGI" (automating economically useful tasks) is reachable via brute-force, carefully-orchestrated multi-agent systems per domain, but true AGI would additionally require efficient learning in novel environments, which LLMs don't have [now-anyone-can-code-how-ai-agents-can-build-your-whole-app @ 17:18](https://youtu.be/jbIQfoldLag?t=1038)
- 2026-07-05 — No-code tools tend to hit hard ceilings once users push past simple use cases, whereas an AI coding agent lets users start with prompts and gradually read/edit real code, becoming programmers over time [now-anyone-can-code-how-ai-agents-can-build-your-whole-app @ 21:27](https://youtu.be/jbIQfoldLag?t=1287)

<!-- NAV:START (generated by scripts/build_nav.py — edits inside are overwritten) -->
## Browse all 4 talks featuring Amjad Masad

- [[replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the]] — Replit's CEO On The Only Two Jobs Left In The Company Of The Future
- [[the-future-of-software-creation-with-replit-ceo-amjad-masad]] — The Future of Software Creation with Replit CEO Amjad Masad
- [[how-replit-went-from-10m-to-100m-arr-in-just-9-months]] — How Replit Went From $10M to $100M ARR In Just 9 Months
- [[now-anyone-can-code-how-ai-agents-can-build-your-whole-app]] — Now Anyone Can Code: How AI Agents Can Build Your Whole App
<!-- NAV:END -->
