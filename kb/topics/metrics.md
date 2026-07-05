---
type: concept
title: "Metrics"
slug: metrics
tags: [metrics, retention, growth, product-market-fit, default-alive]
updated: 2026-07-05
---
# Metrics — Compiled Truth

YC's collective advice on metrics is aggressively minimalist: pick a single primary "north star" metric you'd bet the company on — almost always revenue (MRR/ARR), or a repeat-usage action that proves the product's core recurring value — pair it with three to five secondary metrics, define every one precisely in writing, and never quietly redefine a metric to make a bad number look better. Vanity numbers (registered users, downloads, pageviews, GMV, headcount, press, surveys) feel good but don't correlate with survival; what does is cohort retention curves that flatten instead of decaying to zero, growth rate expressed as a proper compounded rate (CMGR/WoW, never a naive average), net dollar retention, positive unit economics (LTV > CAC with a short payback), and the three-number financial trio of bank balance/burn/runway that determines default-alive status. Instrument event analytics and cohort dashboards from day one — or as soon after launch as possible — rather than bolting them on reactively once something looks wrong.

**State:** #talks: 119 (tagged) · maturity: strong
**Open threads:** (1) NPS/surveys as a PMF proxy — some talks treat NPS >50 as a trustworthy signal of fit, while Gustaf Alstromer calls NPS, surveys, registered users, and conversion rate all "weak proxies" versus actual repeat-usage retention data. (2) MAU as a north star — the Facebook-era playbook (and several YC talks) still endorse monthly active users as a legitimate primary metric, while Suhail Doshi argues MAU is becoming as weak a vanity metric as registered users once were and pushes DAU instead. (3) ARR-only optimization — many talks glorify ARR milestones as the primary proof point, but Replit explicitly avoids ARR-only tracking because "it's very easy in AI to increase ARR while users are not happy," pairing revenue with explicit retention/product goals. (4) Single-metric optimization can backfire — Twitter/X shows that handing a team one number (engagement/dwell time) can make them chase it while quietly eroding taste, quality, or the value users actually want.
**See also:** [[retention]], [[growth]], [[product-market-fit]], [[default-alive]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — Pick exactly one primary "North Star" metric you'd bet the whole company on, commit to it for at least six months, and pair it with only three to five secondary metrics — no sprawling dashboards [suhail-doshi-how-to-measure-your-product @ 34:35](https://youtu.be/MABmQhOlmJA?t=2075), [adora-cheung-how-to-set-kpis-and-goals @ 01:37](https://youtu.be/lL6GdUHIBsM?t=97)
- 2026-07-05 — Revenue, especially MRR, is the best primary metric because it's a lagging indicator that proves people truly value what you built — better than leading-indicator traps like email signups [adora-cheung-how-to-set-kpis-and-goals @ 02:35](https://youtu.be/lL6GdUHIBsM?t=155), [b2b-startup-metrics-startup-school @ 06:03](https://youtu.be/_mKeVGSqQac?t=363)
- 2026-07-05 — Tracking too many metrics causes decision paralysis rather than clarity (Doshi once had 25 sub-metrics on paper); real progress is anything that moves the primary KPI, everything else is "fake progress" [suhail-doshi-how-to-measure-your-product @ 06:12](https://youtu.be/MABmQhOlmJA?t=372), [adora-cheung-how-to-prioritize-your-time @ 02:19](https://youtu.be/XcCmMOWuAF4?t=139)
- 2026-07-05 — Fake metrics — registered users instead of paying/active users, website hits, downloads without registrations — let founders avoid measuring whether anything is actually working [the-secrets-to-setting-smarter-goals @ 03:25](https://youtu.be/rE2XaBGHN2I?t=205)
- 2026-07-05 — Write down and centralize metric definitions across teams (sales vs. marketing often disagree on "qualified lead"), and never quietly redefine a metric just to make a bad number look better [b2b-startup-metrics-startup-school @ 03:44](https://youtu.be/_mKeVGSqQac?t=224), [b2b-startup-metrics-startup-school @ 04:24](https://youtu.be/_mKeVGSqQac?t=264)
- 2026-07-05 — Measure retention by cohort — track a signup cohort's usage over subsequent weeks rather than mixing the whole user base together [ilya-volodarsky-analytics-for-startups @ 02:40](https://youtu.be/LLerCc7MOQo?t=160), [how-to-keep-your-users-startup-school @ 02:31](https://youtu.be/VNxBZ7ka5J0?t=151)
- 2026-07-05 — The only thing that matters in a retention curve is whether it flattens out, not the height it flattens at — a curve trending to zero means you haven't built something people want [how-to-keep-your-users-startup-school @ 11:53](https://youtu.be/VNxBZ7ka5J0?t=713), [growth-with-alex-schultz-how-to-start-a-startup-2014-lecture @ 02:40](https://youtu.be/vJqlG5ytLDs?t=160)
- 2026-07-05 — To measure product-market fit, pick the one metric that represents the product's core value (bookings for Airbnb, payroll runs for Gusto) and track repeat usage of it as a cohort retention curve [gustaf-alstromer-how-to-get-users-and-grow @ 13:11](https://youtu.be/T9ikpoF2GH0?t=791)
- 2026-07-05 — Don't push growth tactics or paid acquisition before retention flattens — layering acquisition on a leaky product produces a "grow like crazy then crash" (shark-fin) pattern [gustaf-alstromer-how-to-get-users-and-grow @ 06:55](https://youtu.be/T9ikpoF2GH0?t=415), [suhail-doshi-how-to-measure-your-product @ 23:21](https://youtu.be/MABmQhOlmJA?t=1401)
- 2026-07-05 — NPS, surveys, registered users, visitors, and conversion rate are all weak proxies for product-market fit compared to actual repeat usage [gustaf-alstr-mer-growth-for-startups @ 14:31](https://youtu.be/6lY9CYIY4pQ?t=871)
- 2026-07-05 — A healthy consumer NPS is +50 or higher, measured consistently, as a signal of real word-of-mouth potential [consumer-startup-metrics-startup-school @ 17:06](https://youtu.be/fdD4y4Civp4?t=1026), [david-rusenko-how-to-find-product-market-fit @ 29:16](https://youtu.be/0LNQxT9LvM0?t=1756)
- 2026-07-05 — Monthly active users is becoming as weak a vanity metric as total registered users once was; daily active users is a harsher, more honest signal that correlated with reduced churn [suhail-doshi-how-to-measure-your-product @ 26:33](https://youtu.be/MABmQhOlmJA?t=1593)
- 2026-07-05 — Net dollar retention above 100% (125-150% is strong for early B2B SaaS) means existing cohorts are growing via upsell/price increases and drives exponential growth on its own; below 100% (especially in enterprise) signals customers don't love the product [b2b-startup-metrics-startup-school @ 14:30](https://youtu.be/_mKeVGSqQac?t=870), [b2b-startup-metrics-startup-school @ 15:57](https://youtu.be/_mKeVGSqQac?t=957)
- 2026-07-05 — A good consumer growth-rate benchmark is 15% month-over-month (5x/year); 10% is okay; 5% or lower is unlikely to reach breakout success [consumer-startup-metrics-startup-school @ 00:54](https://youtu.be/fdD4y4Civp4?t=54)
- 2026-07-05 — Looking at recent YC demo-day startups, healthy early growth clusters around 5-10% week-over-week (roughly 20-50% month-over-month) [adora-cheung-how-to-set-kpis-and-goals @ 15:35](https://youtu.be/lL6GdUHIBsM?t=935)
- 2026-07-05 — Growth rate should be expressed as a compounded number (CMGR) rather than a naive average — a 6x revenue increase over six months is a ~35% compounded monthly rate, not the 100% a simple average implies [tim-brady-how-do-you-calculate-burn-rate-runway-and-growth-r @ 03:00](https://youtu.be/aDM8CNnCOwk?t=180), [tim-brady-how-do-you-calculate-burn-rate-runway-and-growth-r @ 03:46](https://youtu.be/aDM8CNnCOwk?t=226)
- 2026-07-05 — Every founder should know three numbers straight from the bank statement — balance, money in, money out — since burn, runway, growth rate, and default-alive status all derive from them, checked at least weekly [kirsty-nathoo-managing-startup-finances @ 01:29](https://youtu.be/LBC16jhiwak?t=89), [kirsty-nathoo-managing-startup-finances @ 07:31](https://youtu.be/LBC16jhiwak?t=451)
- 2026-07-05 — Revenue, net burn rate, and runway should be the three numbers at the very top of every investor update [b2b-startup-metrics-startup-school @ 07:43](https://youtu.be/_mKeVGSqQac?t=463)
- 2026-07-05 — Default alive means your current growth rate reaches profitability before the bank account hits zero with no further fundraising — distinct from being profitable today, and it gives founders enormous margin for error [save-your-startup-during-an-economic-downturn @ 01:28](https://youtu.be/0OVSTWozvfY?t=88)
- 2026-07-05 — Employee count is a vanity metric; revenue-per-employee is the better efficiency measure, and hiring too fast to chase headcount is dangerous [kirsty-nathoo-managing-startup-finances @ 14:30](https://youtu.be/LBC16jhiwak?t=870)
- 2026-07-05 — Customer acquisition cost must be tracked per channel and measured against an active, monetized, retaining user — not a raw signup — since a cheap channel can still deliver deeply unprofitable customers; only spend on paid acquisition where LTV clears CAC with a short (~3 month) payback period [consumer-startup-metrics-startup-school @ 07:22](https://youtu.be/fdD4y4Civp4?t=442), [building-product-talking-to-users-and-growing-with-adora-che @ 44:24](https://youtu.be/1e4izfOsijE?t=2664)
- 2026-07-05 — Unit economics (revenue per customer minus variable cost) must be positive before scaling acquisition; scaling negative unit economics (as Monzo did early on, or as blitz-scaling did in the zero-interest-rate era) burns capital fast [consumer-startup-metrics-startup-school @ 10:57](https://youtu.be/fdD4y4Civp4?t=657), [b2b-startup-metrics-startup-school @ 21:55](https://youtu.be/_mKeVGSqQac?t=1315)
- 2026-07-05 — Small differences in retention compound enormously: a seemingly modest 7% monthly revenue churn compounds to ~58% annual loss, and 95% vs 90% monthly retention produces a huge year-end gap in customer count [suhail-doshi-how-to-measure-your-product @ 28:52](https://youtu.be/MABmQhOlmJA?t=1732), [startup-business-models-and-pricing-startup-school @ 12:16](https://youtu.be/oWZbWzAyHAE?t=736)
- 2026-07-05 — Gross margin has become newly critical for AI companies specifically because model API costs are a real, non-hidden cost of goods sold, even when temporarily masked by free credits [b2b-startup-metrics-startup-school @ 17:56](https://youtu.be/_mKeVGSqQac?t=1076)
- 2026-07-05 — Use a "mission to metrics" framework: map mission (purpose) to strategy (how you make money) to metrics (how you quantify success or failure), and communicate the whole chain to the team; at least one metric should track efficiency (output/revenue per person), not just absolute output [reshma-shetty-founder-of-ginkgo-bioworks-at-the-female-found @ 12:47](https://youtu.be/OSZidU6R_mU?t=767), [reshma-shetty-founder-of-ginkgo-bioworks-at-the-female-found @ 15:17](https://youtu.be/OSZidU6R_mU?t=917)
- 2026-07-05 — Get baseline event analytics (Amplitude/Mixpanel/Segment/Heap) running from day one — Google Analytics alone can't answer onboarding, conversion, or retention questions — and put metrics on a visible shared dashboard to build a data-driven, self-accountable culture [yc-sus-gustaf-alstr-mer-and-eric-migicovsky-discuss-growth-t @ 08:33](https://youtu.be/oog7n_1fR-o?t=513), [ilya-volodarsky-analytics-for-startups @ 08:52](https://youtu.be/LLerCc7MOQo?t=532)
- 2026-07-05 — Run a disciplined product cycle around one top-line KPI (usually revenue or a usage metric like DAU): brainstorm, sort ideas by effort, then spec before building [michael-seibel-building-product @ 35:59](https://youtu.be/C27RVio2rOs?t=2159)
- 2026-07-05 — Beware ARR-only tracking: it's easy, especially in AI, to grow ARR while users are unhappy, so pair revenue with explicit retention and product-quality goals [how-replit-went-from-10m-to-100m-arr-in-just-9-months @ 24:40](https://youtu.be/kOyIjt6FUrw?t=1480)
- 2026-07-05 — Handing a team a single optimization number like dwell time or engagement causes them to chase it while neglecting harder-to-measure things like taste, quality, or real value delivered [twitter-vs-x-product-lessons-for-startup-founders @ 03:33](https://youtu.be/EW9TUqOgjmQ?t=213)
- 2026-07-05 — Not knowing what your main KPI is, or what number you're chasing when you wake up, is itself a signal you probably need to pivot [startup-experts-reveal-their-favorite-pivot-stories @ 18:52](https://youtu.be/DmehFuCMtvc?t=1132)

<!-- NAV:START (generated by scripts/build_nav.py — edits inside are overwritten) -->
## Browse all 119 talks tagged `metrics`

- [[the-most-ai-pilled-ceo-we-know]] — The Most AI-Pilled CEO We Know
- [[how-to-build-an-ai-native-services-company]] — How to Build an AI-Native Services Company
- [[how-to-build-a-self-improving-company-with-ai]] — How to Build a Self-Improving Company with AI
- [[tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-e]] — Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers
- [[the-truth-about-the-ai-bubble]] — The Truth About The AI Bubble
- [[how-intelligent-is-ai-really]] — How Intelligent Is AI, Really?
- [[anthropic-head-of-pretraining-on-scaling-laws-compute-and-th]] — Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI
- [[the-sales-playbook-for-founders-startup-school]] — The Sales Playbook For Founders | Startup School
- [[scaling-and-the-road-to-human-level-ai-anthropic-co-founder-]] — Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan
- [[how-replit-went-from-10m-to-100m-arr-in-just-9-months]] — How Replit Went From $10M to $100M ARR In Just 9 Months
- [[nobel-laureate-john-jumper-ai-is-revolutionizing-scientific-]] — Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery
- [[cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-]] — Cursor CEO: Going Beyond Code, Superintelligent AI Agents, And Why Taste Still Matters
- [[state-of-the-art-prompting-for-ai-agents]] — State-Of-The-Art Prompting For AI Agents
- [[gpt-4-5-big-model-energy-yc-decoded]] — GPT-4.5 = Big Model Energy | YC Decoded
- [[how-to-build-the-future-aravind-srinivas]] — How To Build The Future: Aravind Srinivas
- [[ai-revolution-what-nobody-else-is-seeing]] — AI Revolution: What Nobody Else Is Seeing
- [[2024-the-year-the-gpt-wrapper-myth-proved-wrong]] — 2024: The Year the GPT Wrapper Myth Proved Wrong
- [[twitter-vs-x-product-lessons-for-startup-founders]] — Twitter vs. X: Product Lessons For Startup Founders
- [[why-the-next-ai-breakthroughs-will-be-in-reasoning-not-scali]] — Why The Next AI Breakthroughs Will Be In Reasoning, Not Scaling
- [[the-10-trillion-parameter-ai-model-with-300-iq]] — The 10 Trillion Parameter AI Model With 300 IQ
- [[starting-a-company-the-key-terms-you-should-know-startup-sch]] — Starting A Company? The Key Terms You Should Know | Startup School
- [[why-design-matters-lessons-from-stripe-lyft-and-airbnb]] — Why Design Matters: Lessons from Stripe, Lyft and Airbnb
- [[why-vertical-llm-agents-are-the-new-1-billion-saas-opportuni]] — Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities
- [[how-to-convert-customers-with-cold-emails-startup-school]] — How To Convert Customers With Cold Emails | Startup School
- [[how-to-keep-your-users-startup-school]] — How To Keep Your Users | Startup School
- [[are-we-in-an-ai-hype-cycle]] — Are We In An AI Hype Cycle?
- [[how-to-price-for-b2b-startup-school]] — How To Price For B2B | Startup School
- [[what-is-zirp-and-how-did-it-poison-startups]] — What Is ZIRP And How Did It Poison Startups?
- [[lightcone-consumer-is-back-what-s-getting-funded-now-the-vib]] — Lightcone: Consumer is back, What's getting funded now, The vibes immaculate
- [[inside-the-hard-tech-startups-turning-sci-fi-into-reality]] — Inside The Hard Tech Startups Turning Sci-Fi Into Reality
- [[consumer-startup-metrics-startup-school]] — Consumer Startup Metrics | Startup School
- [[b2b-startup-metrics-startup-school]] — B2B Startup Metrics | Startup School
- [[tJTxDqjO4vg.en-en-US]] — tJTxDqjO4vg.en-en-US
- [[should-you-quit-your-job-at-a-unicorn]] — Should You Quit Your Job At A Unicorn?
- [[startup-experts-reveal-their-top-productivity-advice]] — Startup Experts Reveal Their Top Productivity Advice
- [[startup-experts-share-their-investor-horror-stories]] — Startup Experts Share Their Investor Horror Stories
- [[startup-experts-reveal-their-favorite-pivot-stories]] — Startup Experts Reveal Their Favorite Pivot Stories
- [[tips-for-technical-startup-founders-startup-school]] — Tips For Technical Startup Founders | Startup School
- [[how-startup-fundraising-works-startup-school]] — How Startup Fundraising Works | Startup School
- [[the-real-potential-of-generative-ai]] — The REAL potential of generative AI
- [[the-secrets-to-setting-smarter-goals]] — The Secrets To Setting Smarter Goals
- [[how-to-get-your-first-customers-startup-school]] — How to Get Your First Customers | Startup School
- [[startup-business-models-and-pricing-startup-school]] — Startup Business Models and Pricing | Startup School
- [[save-your-startup-during-an-economic-downturn]] — Save Your Startup During an Economic Downturn
- [[investors-said-no-now-what]] — Investors Said No, Now What?
- [[how-future-billionaires-get-sh-t-done]] — How Future Billionaires Get Sh*t Done
- [[yc-founders-made-these-fundraising-mistakes]] — YC Founders Made These Fundraising Mistakes
- [[weave-s-application-video-for-yc-w14]] — Weave's Application Video for YC W14
- [[tim-brady-how-do-you-calculate-burn-rate-runway-and-growth-r]] — Tim Brady - How do you calculate burn rate, runway and growth rate?
- [[2021-yc-top-companies-on-their-startup-journey]] — 2021 YC Top Companies on Their Startup Journey
- [[doordash-at-yc-summer-2013-demo-day]] — DoorDash at YC Summer 2013 Demo Day
- [[doordash-s-application-video-for-yc-s13]] — DoorDash's Application Video for YC S13
- [[mmos-in-the-instagram-era-highrise-s18-yc-gaming-tech-talks-]] — MMOs in the Instagram Era: Highrise (S18) - YC Gaming Tech Talks 2020
- [[yc-sus-eric-migicovsky-dalton-caldwell-discuss-pivoting-pitc]] — YC SUS: Eric Migicovsky & Dalton Caldwell discuss pivoting & pitching
- [[yc-sus-eric-migicovsky-hosts-founder-office-hours]] — YC SUS: Eric Migicovsky hosts founder office hours
- [[yc-sus-gustaf-alstr-mer-and-eric-migicovsky-discuss-growth-t]] — YC SUS: Gustaf Alströmer and Eric Migicovsky discuss growth tactics
- [[how-much-should-you-spend-after-fundraising-gustaf-alstr-mer]] — How Much Should You Spend After Fundraising? - Gustaf Alströmer
- [[carolynn-levy-modern-startup-funding]] — Carolynn Levy - Modern Startup Funding
- [[adora-cheung-how-to-prioritize-your-time]] — Adora Cheung - How to Prioritize Your Time
- [[kevin-hale-how-to-improve-conversion-rates]] — Kevin Hale - How to Improve Conversion Rates
- [[dalton-caldwell-all-about-pivoting]] — Dalton Caldwell - All About Pivoting
- [[kirsty-nathoo-managing-startup-finances]] — Kirsty Nathoo - Managing Startup Finances
- [[the-biggest-mistakes-first-time-founders-make-michael-seibel]] — The Biggest Mistakes First-Time Founders Make - Michael Seibel
- [[gustaf-alstr-mer-growth-for-startups]] — Gustaf Alströmer - Growth for Startups
- [[adora-cheung-how-to-set-kpis-and-goals]] — Adora Cheung - How to Set KPIs and Goals
- [[ilya-volodarsky-analytics-for-startups]] — Ilya Volodarsky - Analytics for Startups
- [[eric-migicovsky-how-to-talk-to-users]] — Eric Migicovsky - How to Talk to Users
- [[michael-seibel-how-do-you-decide-what-to-build-next]] — Michael Seibel: How do you decide what to build next?
- [[paul-buchheit-what-traits-do-startups-need-to-succeed]] — Paul Buchheit: What traits do startups need to succeed?
- [[updates-for-startup-school-2019-and-office-hours-with-kevin-]] — Updates for Startup School 2019 and Office Hours with Kevin Hale
- [[advice-on-organizing-and-running-growth-teams-from-dan-hocke]] — Advice on Organizing and Running Growth Teams from Dan Hockenmaier and Gustaf Alströmer
- [[analyzing-billions-of-transactions-to-understand-consumer-be]] — Analyzing Billions of Transactions to Understand Consumer Behavior - Michael Babineau and Kevin Hale
- [[google-photos-product-lead-and-bump-cofounder-david-lieb-wit]] — Google Photos Product Lead and Bump Cofounder David Lieb with Gustaf Alströmer
- [[ryan-hoover-on-product-hunt-s-acquisition-and-lessons-learne]] — Ryan Hoover on Product Hunt's Acquisition and Lessons Learned About Launches with Dalton Caldwell
- [[what-shutting-down-your-startup-feels-like-avni-patel-thomps]] — What Shutting Down Your Startup Feels Like - Avni Patel Thompson of Poppy with Kat Manalac
- [[cindy-mi-and-qi-lu-share-advice-for-entrepreneurs-building-g]] — Cindy Mi and Qi Lu Share Advice for Entrepreneurs Building Global Companies
- [[users-you-don-t-want-by-michael-seibel]] — Users You Don't Want by Michael Seibel
- [[why-does-your-company-deserve-more-money-by-michael-seibel]] — Why Does Your Company Deserve More Money? by Michael Seibel
- [[brian-donohue-on-operating-instapaper-through-an-acquisition]] — Brian Donohue on Operating Instapaper Through an Acquisition
- [[fundraising-fundamentals-by-geoff-ralston]] — Fundraising Fundamentals By Geoff Ralston
- [[seo-advice-from-surveymonkey-director-of-seo-and-growth-eli-]] — SEO Advice from SurveyMonkey Director of SEO and Growth, Eli Schwartz
- [[a-conversation-with-aileen-lee-moderated-by-geoff-ralston]] — A Conversation with Aileen Lee - Moderated by Geoff Ralston
- [[female-founders-conference-mountain-view]] — Female Founders Conference - Mountain View
- [[gustaf-alstromer-how-to-get-users-and-grow]] — Gustaf Alstromer - How to Get Users and Grow
- [[suhail-doshi-how-to-measure-your-product]] — Suhail Doshi - How to Measure Your Product
- [[david-rusenko-how-to-find-product-market-fit]] — David Rusenko - How To Find Product Market Fit
- [[michael-seibel-building-product]] — Michael Seibel - Building Product
- [[david-zeevi-on-personalized-nutrition-based-on-your-gut-micr]] — David Zeevi on Personalized Nutrition Based on Your Gut Microbiome
- [[reshma-shetty-founder-of-ginkgo-bioworks-at-the-female-found]] — Reshma Shetty, Founder of Ginkgo Bioworks at the Female Founders Conference
- [[3d-home-printing-for-the-developing-world-alexandria-lafci-a]] — 3D Home Printing for the Developing World – Alexandria Lafci and Brett Hagler of New Story Charity
- [[breaking-down-hackerrank-s-survey-of-40-000-developers-with-]] — Breaking Down HackerRank's Survey of 40,000 Developers with Vivek Ravisankar
- [[sam-altman-startup-investor-school-day-1]] — Sam Altman - Startup Investor School Day 1
- [[startup-investor-school-day-2-live-stream]] — Startup Investor School Day 2 Live Stream
- [[building-dota-bots-that-beat-pros-openai-s-greg-brockman-szy]] — Building Dota Bots That Beat Pros - OpenAI's Greg Brockman, Szymon Sidor, and Sam Altman
- [[content-marketing-tips-from-experts-at-first-round-capital-a]] — Content Marketing Tips from Experts at First Round Capital and Andreessen Horowitz
- [[founders-of-science-exchange-goldbely-and-the-flex-company-d]] — Founders of Science Exchange, Goldbely, and The Flex Company Discuss Fundraising
- [[jeff-dean-s-lecture-for-yc-ai]] — Jeff Dean's Lecture for YC AI
- [[morgan-debaun-on-reaching-20m-millennials-with-kat-manalac-a]] — Morgan DeBaun on Reaching 20M Millennials - With Kat Manalac at the Female Founders Conference
- [[scaling-growth-gustaf-alstromer-yc-partner-formerly-airbnb-e]] — Scaling Growth | Gustaf Alstromer, YC Partner (formerly Airbnb) & Ed Baker (formerly Uber)
- [[the-technical-advisor-for-silicon-valley-on-hbo-ed-mcmanus]] — The Technical Advisor for Silicon Valley on HBO: Ed McManus
- [[later-stage-advice-with-sam-altman-how-to-start-a-startup-20]] — Later Stage Advice with Sam Altman (How to Start a Startup 2014: Lecture 20)
- [[how-to-operate-with-keith-rabois-how-to-start-a-startup-2014]] — How to Operate with Keith Rabois (How to Start a Startup 2014: Lecture 14)
- [[growth-with-alex-schultz-how-to-start-a-startup-2014-lecture]] — Growth with Alex Schultz (How to Start a Startup 2014: Lecture 6)
- [[building-product-talking-to-users-and-growing-with-adora-che]] — Building Product, Talking to Users, and Growing with Adora Cheung (How to Start a Startup 2014: 4)
- [[team-and-execution-with-sam-altman-how-to-start-a-startup-20]] — Team and Execution with Sam Altman (How to Start a Startup 2014: Lecture 2)
- [[pitch-practice-with-paul-buchheit-and-sam-altman-at-startup-]] — Pitch Practice with Paul Buchheit and Sam Altman at Startup School SV 2016
- [[reham-fagiri-and-kalam-dennis-at-startup-school-sv-2016]] — Reham Fagiri and Kalam Dennis at Startup School SV 2016
- [[jessica-livingston-how-to-build-the-future]] — Jessica Livingston : How to Build the Future
- [[fundraising-panel-at-female-founders-conference-2016]] — Fundraising Panel at Female Founders Conference 2016
- [[adora-cheung-speaks-at-female-founders-conference-2015]] — Adora Cheung Speaks at Female Founders Conference 2015
- [[ruchi-sanghvi-speaks-at-female-founders-conference-2015]] — Ruchi Sanghvi Speaks at Female Founders Conference 2015
- [[chase-adam-at-startup-school-ny-2014]] — Chase Adam at Startup School NY 2014
- [[jessica-mah-at-female-founders-conference-2014]] — Jessica Mah at Female Founders Conference 2014
- [[kathryn-minshew-at-female-founders-conference-2014]] — Kathryn Minshew at Female Founders Conference 2014
- [[chase-adam-at-startup-school-2013]] — Chase Adam at Startup School 2013
- [[office-hours-at-startup-school-2013-with-paul-graham-and-sam]] — Office Hours at Startup School 2013 with Paul Graham and Sam Altman
- [[dan-siroker-at-startup-school-2013]] — Dan Siroker at Startup School 2013
- [[david-rusenko-at-startup-school-2012]] — David Rusenko at Startup School 2012
- [[travis-kalanick-at-startup-school-2012]] — Travis Kalanick at Startup School 2012
<!-- NAV:END -->
