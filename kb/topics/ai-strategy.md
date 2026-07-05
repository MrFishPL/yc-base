---
type: concept
title: "AI Strategy for Startups"
slug: ai-strategy
tags: [ai-strategy, moats-and-competition, startup-ideas, pricing]
updated: 2026-07-05
---
# AI Strategy for Startups — Compiled Truth

YC's collective advice is that LLMs should be a startup's core substrate, not a bolted-on feature — but the "GPT wrapper" fear that foundation labs would eat every application has proven wrong, because durable value now lives in the software, workflow, and data layer wrapped around the model rather than in the raw API call. Winning founders pick specific, often "boring"-looking business-logic problems, embed deep enough into a customer's systems and trust to be sticky, price on outcomes/consumption instead of seats, move fast because any technical edge is a depreciating insight, and treat the next 1-2 years as a real AGI-adjacent planning horizon rather than just riding the current model generation.

**State:** #talks: 143 tagged (21 directly cited below) · maturity: strong
**Open threads:** Whether proprietary data/fine-tuning is still a real moat is contested; whether AI ultimately shrinks or grows team sizes is contested; whether we're in a bubble or a normal "installation phase" is contested — see below.
**See also:** [[moats-and-competition]], [[startup-ideas]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — The "GPT wrapper will get crushed" consensus proved wrong in practice: breakout consumer and enterprise apps were built by outside startups, not OpenAI, and once model choice existed, competitive advantage shifted to product, sales, and retention rather than to which model a company used [2024-the-year-the-gpt-wrapper-myth-proved-wrong @ 01:11](https://youtu.be/z0wt2pe_LZM?t=71) — the "GPT wrapper" critique is really no different from dismissing all SaaS as a "MySQL wrapper" [the-truth-about-building-ai-startups-today @ 21:06](https://youtu.be/TwDJhUJL-5o?t=1266)
- 2026-07-05 — It's fine for a product to start as "a thin wrapper on OpenAI" as long as that's a starting point, not the destination — early Dropbox was dismissed the same way as "a thin wrapper on S3" [will-openai-kill-all-startups @ 11:10](https://youtu.be/smHw9kEwcgM?t=670)
- 2026-07-05 — Durable moats now come from the software/workflow layer wrapped around the model — proprietary data, deep integrations into customer systems, accumulated prompt/business logic — not the LLM call itself; the less software sits on top of raw tokens, the higher the commoditization risk [why-vertical-llm-agents-are-the-new-1-billion-saas-opportuni @ 25:42](https://youtu.be/eBVi_sLaYsc?t=1542), [how-ai-is-changing-enterprise @ 17:17](https://youtu.be/aIKfA3gIXwo?t=1037)
- 2026-07-05 — Fine-tuning open-source models purely to save cost isn't a durable moat since foundation-model costs keep falling; the more defensible play is customizing on private data a company can't hand to OpenAI [the-truth-about-building-ai-startups-today @ 13:23](https://youtu.be/TwDJhUJL-5o?t=803)
- 2026-07-05 — Avoid "AI tarpit" ideas like generic co-pilots that attract easy inbound but no real usage; embed LLMs into familiar UI so the software gets more powerful without asking users to learn a new chat interface [the-truth-about-building-ai-startups-today @ 08:27](https://youtu.be/TwDJhUJL-5o?t=507)
- 2026-07-05 — The best AI startup ideas solve a specific, often "boring"-looking business-logic problem (e.g. automating bidding on government contracts, HIPAA compliance checklists) rather than a generic "throw your data in and we'll automate everything" pitch [the-truth-about-building-ai-startups-today @ 05:53](https://youtu.be/TwDJhUJL-5o?t=353)
- 2026-07-05 — Seat-based SaaS pricing breaks down with agents, since an agent can do unlimited work regardless of headcount — pricing shifts to consumption tied to volume of work, ideally anchored with a recurring baseline [aaron-levie-why-startups-win-in-the-ai-era @ 20:43](https://youtu.be/uqc_vt95GJg?t=1243)
- 2026-07-05 — Under the forward-deployed-engineer model, pricing shifts from subscriptions/seats to a delivered outcome: contracts start small and flexible and grow with trust and value, as with YC's Castle and Happy Robot ramping bank and logistics contracts [the-fde-playbook-for-ai-startups-with-bob-mcgrew @ 30:52](https://youtu.be/Zyw-YA0k3xo?t=1852)
- 2026-07-05 — Vertical AI agents can be roughly 10x bigger than the SaaS they replace because, unlike SaaS which still needed a human ops team to run the workflow, agents can absorb that labor cost too [vertical-ai-agents-could-be-10x-bigger-than-saas @ 20:39](https://youtu.be/ASABxNenD_U?t=1239)
- 2026-07-05 — Selling a vertical AI agent that threatens to eliminate the team you're pitching backfires — the pitch must go high enough (engineering, CEO) that the threatened team can't sabotage the deal [vertical-ai-agents-could-be-10x-bigger-than-saas @ 22:15](https://youtu.be/ASABxNenD_U?t=1335)
- 2026-07-05 — Post-PMF hiring calculus is shifting: instead of hiring the best salesperson or CS lead, hire strong engineers who can build LLM systems that automate the function that used to require headcount [vertical-ai-agents-could-be-10x-bigger-than-saas @ 13:39](https://youtu.be/ASABxNenD_U?t=819)
- 2026-07-05 — The forward-deployed-engineer playbook (embed technical people at the customer site to discover the product, then generalize a "gravel road" fix into a "paved highway") is being widely adopted by AI agent startups because there's no incumbent product yet, so product discovery can only happen from inside the enterprise [the-fde-playbook-for-ai-startups-with-bob-mcgrew @ 02:15](https://youtu.be/Zyw-YA0k3xo?t=135), [the-fde-playbook-for-ai-startups-with-bob-mcgrew @ 27:37](https://youtu.be/Zyw-YA0k3xo?t=1657)
- 2026-07-05 — Enterprise engineering teams are often too risk-averse or codegen-skeptical to build working AI internally, and outside-vendor AI projects succeed far more often than internally-built ones — win by embedding deep into a business's systems of record rather than selling plug-and-play SaaS [good-news-for-startups-enterprise-is-bad-at-ai @ 00:00](https://youtu.be/DULfEcPR0Gc?t=0), [good-news-for-startups-enterprise-is-bad-at-ai @ 02:11](https://youtu.be/DULfEcPR0Gc?t=131)
- 2026-07-05 — The best markets for AI-native services combine low trust, low task-level judgment, a high intelligence threshold, and moat-raising regulation; apply the "Sam Altman test" to any market — as models get better, does your service get stronger, or does the model itself commoditize you? [how-to-build-an-ai-native-services-company @ 01:32](https://youtu.be/gSNFJbgoaHI?t=92), [how-to-build-an-ai-native-services-company @ 03:19](https://youtu.be/gSNFJbgoaHI?t=199)
- 2026-07-05 — Build the company itself as an AI-native "closed loop" — a queryable, self-monitoring operating system — rather than treating AI as a tool the company merely uses [how-to-build-a-company-with-ai-from-the-ground-up @ 01:14](https://youtu.be/EN7frwQIbKc?t=74)
- 2026-07-05 — The best companies maximize token usage over headcount and should be willing to run an "uncomfortably high" API bill, since it replaces far more expensive headcount [how-to-build-a-company-with-ai-from-the-ground-up @ 08:12](https://youtu.be/EN7frwQIbKc?t=492)
- 2026-07-05 — AI is compressing the "build" moat the way capital and infrastructure moats already compressed; the only differentiation left is deciding what to build and how fast you move — companies planning to "respond to the market" once it changes are already too late [harshil-mathur-ai-is-compressing-every-moat @ 26:17](https://youtu.be/X5bABLCuIHA?t=1577)
- 2026-07-05 — AI makes building software easier but doesn't make entrepreneurship easier — only pursue problems you can commit to solving for the next 10 years, not ones that are just cool or easy to build with AI [harshil-mathur-ai-is-compressing-every-moat @ 30:59](https://youtu.be/X5bABLCuIHA?t=1859)
- 2026-07-05 — Founders shouldn't pivot to AI just because it's trendy, but nearly every startup today should be using LLMs at its core in some way [how-to-use-ai-in-your-startup @ 01:35](https://youtu.be/7Kt9ugD3bGQ?t=95)
- 2026-07-05 — Plan roughly two years ahead assuming AGI-level capability is likely to arrive, not just the next six months of model gains; trust — not compute or data — becomes the binding constraint on what an agent is allowed to do [ask-these-questions-before-starting-an-ai-startup @ 03:44](https://youtu.be/DJjZzzPANBY?t=224), [ask-these-questions-before-starting-an-ai-startup @ 07:44](https://youtu.be/DJjZzzPANBY?t=464)
- 2026-07-05 — Whether a task has a low "intelligence ceiling" determines how fast it commoditizes — once a task like writing a PR diff is good enough, moving to the next model buys no further edge [ask-these-questions-before-starting-an-ai-startup @ 22:38](https://youtu.be/DJjZzzPANBY?t=1358)
- 2026-07-05 — Keep the "AI on a leash": since humans remain the bottleneck on verifying output, favor small, concrete, incremental diffs over giant autonomous changes to keep the generation/verification loop fast [andrej-karpathy-software-is-changing-again @ 22:20](https://youtu.be/LCEmiRjPEtQ?t=1340)
- 2026-07-05 — Design products for AI agents as a new class of consumer of digital information too — markdown-based docs, llm.txt files, executable commands instead of "click here," and protocols like MCP [andrej-karpathy-software-is-changing-again @ 34:00](https://youtu.be/LCEmiRjPEtQ?t=2040)
- 2026-07-05 — Startups need two opposing traits at once — irrational optimism to act despite uncertainty, and uncompromising realism to change course fast when facts contradict the thesis — because any technical edge is a "depreciating insight" that moats must continually re-earn [windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-t @ 07:09](https://youtu.be/LKgAx7FWva4?t=429), [windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-t @ 23:39](https://youtu.be/LKgAx7FWva4?t=1419)

## Open threads (genuine disagreements)

**Is proprietary data / fine-tuning still a real moat?**
- No / weakening: fine-tuning purely for cost savings isn't durable since foundation-model costs keep falling [the-truth-about-building-ai-startups-today @ 13:23](https://youtu.be/TwDJhUJL-5o?t=803); general frontier models now beat most fine-tuned custom models except where tacit or physical-world knowledge (e.g. TSMC, ASML) stays outside what the model knows [ask-these-questions-before-starting-an-ai-startup @ 18:39](https://youtu.be/DJjZzzPANBY?t=1119)
- Yes / still real: the long-term moat is a firm's proprietary data, environments, and fine-tuned models built on its own unique business problems, not shared evals [alexandr-wang-building-scale-ai-transforming-work-with-agent @ 17:12](https://youtu.be/5noIKN8t69U?t=1032); durable AI products come from proprietary data, deep system integrations, and accumulated business logic, not the LLM call itself [why-vertical-llm-agents-are-the-new-1-billion-saas-opportuni @ 25:42](https://youtu.be/eBVi_sLaYsc?t=1542)

**Does AI shrink teams or grow them?**
- Shrinks/flattens: a queryable, AI-run company makes the classic management hierarchy of human middleware unnecessary, letting a handful of people operate 1,000x faster [how-to-build-a-company-with-ai-from-the-ground-up @ 06:06](https://youtu.be/EN7frwQIbKc?t=366)
- Doesn't shrink / grows: historically, cheaper tooling (Rails, Heroku, cloud) never shrank company headcounts due to the Jevons paradox, and YC application volume rising 5x suggests AI will produce more unicorns, not smaller ones [10-people-ai-billion-dollar-company @ 30:26](https://youtu.be/CKvo_kQbakU?t=1826), [10-people-ai-billion-dollar-company @ 37:10](https://youtu.be/CKvo_kQbakU?t=2230); in practice, startups that hit $1M ARR without hiring in 2024 mostly reverted to hiring (just leaner teams) after their Series A [the-truth-about-the-ai-bubble @ 25:35](https://youtu.be/cqrJzG03ENE?t=1535)

**Is this an AI bubble?**
- Bubble-ish, but productive: the industry is in a CapEx "installation phase" (like pre-2000 telecom) that looks like a bubble but precedes a real deployment/value phase, and a compute glut mostly benefits application-layer startups regardless [the-truth-about-the-ai-bubble @ 12:43](https://youtu.be/cqrJzG03ENE?t=763); the widely-cited "90% of enterprise AI projects fail" stat is largely a "skill issue" from spending tokens without changing how products are built [zynga-founder-consumer-is-not-investible-right-now-thats-why @ 26:38](https://youtu.be/oHwUD9b9_pg?t=1598)
- Already debunked as hype: the "GPT wrapper that will be commoditized" fear has been overtaken by real revenue, retention, and profitable YC companies raising only a seed round [are-we-in-an-ai-hype-cycle @ 30:13](https://youtu.be/_-5xJQ4U8g0?t=1813), [are-we-in-an-ai-hype-cycle @ 26:07](https://youtu.be/_-5xJQ4U8g0?t=1567)

<!-- NAV:START (generated by scripts/build_nav.py — edits inside are overwritten) -->
## Browse all 143 talks tagged `ai-strategy`

- [[zynga-founder-consumer-is-not-investible-right-now-thats-why]] — Zynga Founder: Consumer Is Not Investible Right Now - Thats Why You Should Build It
- [[the-age-of-the-40-year-old-solo-founder-is-here]] — The Age Of The 40-Year-Old Solo Founder Is Here
- [[pick-one-idea-and-go-deep]] — Pick One Idea and Go Deep
- [[self-play-for-llms-ai-for-biology-formal-verification-and-mo]] — Self-Play for LLMs, AI for Biology, Formal Verification, and More | YC Paper Club
- [[how-meesho-became-india-s-biggest-shopping-app]] — How Meesho Became India’s Biggest Shopping App
- [[the-most-ai-pilled-ceo-we-know]] — The Most AI-Pilled CEO We Know
- [[emergent-how-six-months-of-tinkering-led-to-a-100m-arr-compa]] — Emergent: How Six Months of Tinkering Led To A $100M ARR Company
- [[conductor-ceo-charlie-holtz-walks-us-through-his-ai-coding-s]] — Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup
- [[how-to-build-an-ai-native-services-company]] — How to Build an AI-Native Services Company
- [[inference-diffusion-world-models-and-more-yc-paper-club]] — Inference, Diffusion, World Models, and More | YC Paper Club
- [[inside-yc-s-ai-playbook]] — Inside YC's AI Playbook
- [[how-to-build-a-self-improving-company-with-ai]] — How to Build a Self-Improving Company with AI
- [[zepto-how-two-17-year-olds-built-india-s-largest-seller-of-f]] — Zepto: How Two 17-Year-Olds Built India's Largest Seller Of Fruits and Vegetables
- [[tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e]] — Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers
- [[harshil-mathur-ai-is-compressing-every-moat]] — Harshil Mathur: AI Is Compressing Every Moat
- [[recursion-is-the-next-scaling-law-in-ai]] — Recursion Is The Next Scaling Law In AI
- [[demis-hassabis-agents-agi-the-next-big-scientific-breakthrou]] — Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough
- [[replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the]] — Replit's CEO On The Only Two Jobs Left In The Company Of The Future
- [[how-to-build-a-company-with-ai-from-the-ground-up]] — How To Build A Company With AI From The Ground Up
- [[how-to-make-claude-code-your-ai-engineering-team]] — How to Make Claude Code Your AI Engineering Team
- [[how-stripe-built-their-new-website]] — How Stripe Built Their New Website
- [[the-gpt-moment-for-robotics-is-here]] — The GPT Moment for Robotics Is Here
- [[this-startup-catches-fraud-at-scale]] — This Startup Catches Fraud at Scale
- [[fran-ois-chollet-why-scaling-alone-isn-t-enough-for-agi]] — François Chollet: Why Scaling Alone Isn't Enough for AGI
- [[ai-is-unlocking-millions-of-new-builders]] — AI Is Unlocking Millions Of New Builders
- [[the-future-of-brain-computer-interfaces]] — The Future Of Brain-Computer Interfaces
- [[common-mistakes-with-vibe-coded-websites]] — Common Mistakes With Vibe Coded Websites
- [[the-powerful-alternative-to-fine-tuning]] — The Powerful Alternative To Fine-Tuning
- [[the-ai-agent-economy-is-here]] — The AI Agent Economy Is Here
- [[inside-claude-code-with-its-creator-boris-cherny]] — Inside Claude Code With Its Creator Boris Cherny
- [[the-new-way-to-build-a-startup]] — The New Way To Build A Startup
- [[openclaw-creator-why-80-of-apps-will-disappear]] — OpenClaw Creator: Why 80% Of Apps Will Disappear
- [[we-re-all-addicted-to-claude-code]] — We're All Addicted To Claude Code
- [[the-ml-technique-every-founder-should-know]] — The ML Technique Every Founder Should Know
- [[the-truth-about-the-ai-bubble]] — The Truth About The AI Bubble
- [[how-intelligent-is-ai-really]] — How Intelligent Is AI, Really?
- [[how-amplitude-went-from-skeptics-to-all-in-on-ai]] — How Amplitude Went From Skeptics to All In on AI
- [[the-best-consumer-startup-ideas-were-impossible-until-now]] — The Best Consumer Startup Ideas Were Impossible Until Now
- [[ai-is-eating-logistics]] — AI Is Eating Logistics
- [[good-news-for-startups-enterprise-is-bad-at-ai]] — Good News For Startups: Enterprise Is Bad At AI
- [[from-idea-to-650m-exit-lessons-in-building-ai-startups]] — From Idea to $650M Exit: Lessons in Building AI Startups
- [[transformers-explained-the-discovery-that-changed-ai-forever]] — Transformers Explained: The Discovery That Changed AI Forever
- [[startup-advice-ai-gtm-pivoting-how-to-hire]] — Startup Advice: AI GTM, Pivoting & How To Hire
- [[what-everyone-is-getting-wrong-about-ai-and-jobs]] — What Everyone Is Getting Wrong About AI And Jobs
- [[ask-these-questions-before-starting-an-ai-startup]] — Ask These Questions Before Starting An AI Startup
- [[anthropic-head-of-pretraining-on-scaling-laws-compute-and-th]] — Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI
- [[why-now-is-the-best-time-to-build-in-crypto]] — Why Now Is The Best Time To Build In Crypto
- [[aaron-levie-why-startups-win-in-the-ai-era]] — Aaron Levie: Why Startups Win In The AI Era
- [[the-future-of-software-creation-with-replit-ceo-amjad-masad]] — The Future of Software Creation with Replit CEO Amjad Masad
- [[the-fde-playbook-for-ai-startups-with-bob-mcgrew]] — The FDE Playbook for AI Startups with Bob McGrew
- [[openai-vs-deepseek-vs-qwen-comparing-open-source-llm-archite]] — OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures
- [[how-this-25-year-old-built-a-675m-legal-ai-startup-with-no-l]] — How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)
- [[anthropic-co-founder-building-claude-code-lessons-from-gpt-3]] — Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design
- [[dylan-field-scaling-figma-and-the-future-of-design]] — Dylan Field: Scaling Figma and the Future of Design
- [[scaling-and-the-road-to-human-level-ai-anthropic-co-founder-]] — Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan
- [[chelsea-finn-building-robots-that-can-do-anything]] — Chelsea Finn: Building Robots That Can Do Anything
- [[how-replit-went-from-10m-to-100m-arr-in-just-9-months]] — How Replit Went From $10M to $100M ARR In Just 9 Months
- [[nobel-laureate-john-jumper-ai-is-revolutionizing-scientific-]] — Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery
- [[andrew-ng-building-faster-with-ai]] — Andrew Ng: Building Faster with AI
- [[fran-ois-chollet-how-we-get-to-agi]] — François Chollet: How We Get To AGI
- [[fei-fei-li-spatial-intelligence-is-the-next-frontier-in-ai]] — Fei-Fei Li: Spatial Intelligence is the Next Frontier in AI
- [[satya-nadella-microsoft-s-ai-bets-hyperscaling-quantum-compu]] — Satya Nadella: Microsoft's AI Bets, Hyperscaling, Quantum Computing Breakthroughs
- [[sam-altman-the-future-of-openai-chatgpt-s-origins-and-buildi]] — Sam Altman: The Future of OpenAI, ChatGPT's Origins, and Building AI Hardware
- [[andrej-karpathy-software-is-changing-again]] — Andrej Karpathy: Software Is Changing (Again)
- [[elon-musk-digital-superintelligence-multiplanetary-life-how-]] — Elon Musk: Digital Superintelligence, Multiplanetary Life, How to Be Useful
- [[alexandr-wang-building-scale-ai-transforming-work-with-agent]] — Alexandr Wang: Building Scale AI, Transforming Work With Agents & Competing With China
- [[cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-]] — Cursor CEO: Going Beyond Code, Superintelligent AI Agents, And Why Taste Still Matters
- [[fusion-energy-will-power-the-ai-boom]] — Fusion Energy Will Power the AI Boom
- [[state-of-the-art-prompting-for-ai-agents]] — State-Of-The-Art Prompting For AI Agents
- [[how-to-design-better-ai-apps]] — How To Design Better AI Apps
- [[startup-ideas-you-can-now-build-with-ai]] — Startup Ideas You Can Now Build With AI
- [[how-ai-coding-agents-will-change-your-job]] — How AI Coding Agents Will Change Your Job
- [[windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-t]] — Windsurf CEO: Betting On AI Agents, Pivoting In 48 Hours, And The Future of Coding
- [[how-to-get-the-most-out-of-vibe-coding-startup-school]] — How To Get The Most Out Of Vibe Coding | Startup School
- [[the-next-breakthrough-in-ai-agents-is-here]] — The Next Breakthrough In AI Agents Is Here
- [[how-to-build-a-truly-abundant-future]] — How To Build A Truly Abundant Future
- [[what-founders-can-do-to-improve-their-design-game]] — What Founders Can Do To Improve Their Design Game
- [[from-a-pivot-to-building-a-9-6-billion-payroll-company]] — From A Pivot To Building A $9.6 Billion Payroll Company
- [[figma-s-dylan-field-exploring-the-idea-maze-vibe-coding-and-]] — Figma's Dylan Field: Exploring the idea maze, vibe coding, and the power of “locking in”
- [[gpt-4-5-big-model-energy-yc-decoded]] — GPT-4.5 = Big Model Energy | YC Decoded
- [[vibe-coding-is-the-future]] — Vibe Coding Is The Future
- [[ai-interfaces-of-the-future-design-review]] — AI Interfaces Of The Future | Design Review
- [[how-to-build-the-future-aravind-srinivas]] — How To Build The Future: Aravind Srinivas
- [[how-ai-is-changing-enterprise]] — How AI Is Changing Enterprise
- [[how-to-get-ai-startup-ideas]] — How To Get AI Startup Ideas
- [[the-engineering-unlocks-behind-deepseek-yc-decoded]] — The Engineering Unlocks Behind DeepSeek | YC Decoded
- [[bob-mcgrew-ai-agents-and-the-path-to-agi]] — Bob McGrew: AI Agents And The Path To AGI
- [[ai-revolution-what-nobody-else-is-seeing]] — AI Revolution: What Nobody Else Is Seeing
- [[how-scaling-laws-will-determine-ai-s-future-yc-decoded]] — How Scaling Laws Will Determine AI's Future | YC Decoded
- [[how-to-use-ai-in-your-startup]] — How To Use AI In Your Startup
- [[how-to-build-the-future-parker-conrad]] — How To Build The Future: Parker Conrad
- [[the-lightcone-2025-forecast]] — The Lightcone 2025 Forecast
- [[2024-the-year-the-gpt-wrapper-myth-proved-wrong]] — 2024: The Year the GPT Wrapper Myth Proved Wrong
- [[VDmU0jjklBo.en-en-US]] — VDmU0jjklBo.en-en-US
- [[anthropic-s-claude-computer-use-is-a-game-changer-yc-decoded]] — Anthropic’s Claude Computer Use Is A Game Changer | YC Decoded
- [[vertical-ai-agents-could-be-10x-bigger-than-saas]] — Vertical AI Agents Could Be 10X Bigger Than SaaS
- [[why-the-next-ai-breakthroughs-will-be-in-reasoning-not-scali]] — Why The Next AI Breakthroughs Will Be In Reasoning, Not Scaling
- [[how-to-build-the-future-sam-altman]] — How To Build The Future: Sam Altman
- [[the-10-trillion-parameter-ai-model-with-300-iq]] — The 10 Trillion Parameter AI Model With 300 IQ
- [[why-openai-s-o1-is-a-huge-deal-yc-decoded]] — Why OpenAI's o1 Is A Huge Deal | YC Decoded
- [[now-anyone-can-code-how-ai-agents-can-build-your-whole-app]] — Now Anyone Can Code: How AI Agents Can Build Your Whole App
- [[why-vertical-llm-agents-are-the-new-1-billion-saas-opportuni]] — Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities
- [[building-the-world-s-best-image-diffusion-model]] — Building The World's Best Image Diffusion Model
- [[are-we-in-an-ai-hype-cycle]] — Are We In An AI Hype Cycle?
- [[gmail-creator-paul-buchheit-on-agi-open-source-models-freedo]] — Gmail Creator Paul Buchheit On AGI, Open Source Models, Freedom
- [[tarpit-ideas-the-sequel]] — Tarpit Ideas: The Sequel
- [[10-people-ai-billion-dollar-company]] — 10 People + AI = Billion Dollar Company?
- [[standing-up-for-startups-yc-goes-to-d-c]] — Standing Up For Startups - YC Goes To D.C.
- [[better-ai-models-better-startups]] — Better AI Models, Better Startups
- [[how-new-technology-creates-new-businesses]] — How New Technology Creates New Businesses
- [[why-this-is-the-perfect-time-to-start-a-startup]] — Why This Is The Perfect Time To Start A Startup
- [[lightcone-consumer-is-back-what-s-getting-funded-now-the-vib]] — Lightcone: Consumer is back, What's getting funded now, The vibes immaculate
- [[how-to-build-generative-ai-models-like-openai-s-sora]] — How To Build Generative AI Models Like OpenAI's Sora
- [[the-best-ai-founders-in-the-world-are-moving-here]] — The best AI founders in the world are moving here
- [[the-truth-about-building-ai-startups-today]] — The Truth About Building AI Startups Today
- [[ai-startup-founders-debate-the-creation-of-artificial-genera]] — AI Startup Founders Debate the Creation of Artificial General Intelligence
- [[ai-and-the-future-of-law-the-10-year-overnight-success-story]] — AI and the Future of Law: The 10 Year Overnight Success Story
- [[qFBUd0b8TjY.en-en-US]] — qFBUd0b8TjY.en-en-US
- [[40-ai-founders-discuss-current-artificial-intelligence-techn]] — 40 AI Founders Discuss Current Artificial Intelligence Technology
- [[will-openai-kill-all-startups]] — Will OpenAI Kill All Startups?
- [[the-real-potential-of-generative-ai]] — The REAL potential of generative AI
- [[designing-characters-with-deep-learning-spellbrush-w18-yc-ga]] — Designing Characters with Deep Learning: Spellbrush (W18) - YC Gaming Tech Talks 2020
- [[diego-saez-gil-how-pachama-uses-tech-to-solve-climate-change]] — Diego Saez Gil - How Pachama Uses Tech to Solve Climate Change
- [[google-photos-product-lead-and-bump-cofounder-david-lieb-wit]] — Google Photos Product Lead and Bump Cofounder David Lieb with Gustaf Alströmer
- [[andrew-kortina-of-venmo-and-fin-on-technological-determinism]] — Andrew Kortina of Venmo and Fin on Technological Determinism and Work's Relationship to Dignity
- [[david-zeevi-on-personalized-nutrition-based-on-your-gut-micr]] — David Zeevi on Personalized Nutrition Based on Your Gut Microbiome
- [[jessica-brillhart-immersive-director-on-vr-and-ar]] — Jessica Brillhart, Immersive Director, on VR and AR
- [[mathematical-approaches-to-image-processing-with-carola-sch-]] — Mathematical Approaches to Image Processing with Carola Schönlieb
- [[a-i-policy-and-public-perception-miles-brundage-and-tim-hwan]] — A.I. Policy and Public Perception - Miles Brundage and Tim Hwang
- [[tim-urban-of-wait-but-why]] — Tim Urban of Wait But Why
- [[microbes-robots-and-ambition-robin-sloan-on-his-novel-sourdo]] — Microbes, Robots, and Ambition - Robin Sloan on His Novel Sourdough
- [[building-dota-bots-that-beat-pros-openai-s-greg-brockman-szy]] — Building Dota Bots That Beat Pros - OpenAI's Greg Brockman, Szymon Sidor, and Sam Altman
- [[experiments-in-art-and-technology-with-artforum-editor-miche]] — Experiments in Art and Technology with Artforum Editor Michelle Kuo
- [[artist-lauren-mccarthy-will-be-your-home-s-brain]] — Artist Lauren McCarthy Will Be Your Home's Brain
- [[baidu-s-ai-lab-director-on-advancing-speech-recognition-and-]] — Baidu's AI Lab Director on Advancing Speech Recognition and Simulation
- [[jeff-dean-s-lecture-for-yc-ai]] — Jeff Dean's Lecture for YC AI
- [[making-music-and-art-through-machine-learning-doug-eck-of-ma]] — Making Music and Art Through Machine Learning - Doug Eck of Magenta
- [[ex-machina-s-scientific-advisor-murray-shanahan]] — Ex Machina's Scientific Advisor - Murray Shanahan
- [[at-the-intersection-of-ai-governments-and-google-tim-hwang]] — At the Intersection of AI, Governments, and Google - Tim Hwang
- [[an-ai-primer-with-wojciech-zaremba]] — An AI Primer with Wojciech Zaremba
- [[what-would-elon-musk-work-on-if-he-were-22]] — What Would Elon Musk Work On If He Were 22?
- [[elon-musk-how-to-build-the-future]] — Elon Musk : How to Build the Future
- [[mark-zuckerberg-how-to-build-the-future]] — Mark Zuckerberg : How to Build the Future
<!-- NAV:END -->
