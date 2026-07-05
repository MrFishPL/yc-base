---
name: answer-from-kb
description: Answers any startup question from the YC YouTube knowledge base by searching broadly in parallel and synthesizing a grounded, cited answer. Use when the user asks about fundraising, product-market fit, pricing, hiring, enterprise/B2B sales, growth, retention, YC applications, founder psychology, competition/moats, AI strategy — or references a YC talk, a partner/founder (Paul Graham, Michael Seibel, Dalton Caldwell, Sam Altman, Garry Tan…), or a series (Startup School, Lightcone, How to Start a Startup).
allowed-tools: Read, Grep, Glob, Task, Bash(python3 scripts/search.py *), Bash(rg:*)
---

# Answer from the YC knowledge base — search broad, then synthesize

You answer startup questions using **only** the compiled knowledge in `kb/`, cited to a video +
timestamp. The corpus is large (~620 talks, 36 topics, 46 people). Do **not** rely on one narrow
search — **cast a wide net with several parallel searches**, then converge. Prefer **recall over
precision**: when unsure whether something is relevant, include it and let synthesis decide.

## The corpus is a browsable tree (no vector DB — it's all files)

```
kb/INDEX.md        # the map: 36 topics (with talk counts), 46 people, 5 series
  → kb/topics/<t>.md     # cross-video synthesis + "Browse all N talks tagged <t>" backlinks
  → kb/series/<s>.md     # every talk in a series, by year
  → kb/entities/people/<p>.md   # a person's positions + "Browse all N talks featuring <p>"
    → kb/talks/<slug>.md # one talk: thesis + timestamped, cited key moments
kb/graph.json      # typed edges for multi-hop ("how did X evolve", "who disagrees")
```
Every hop is a `[[wikilink]]` or a citation you can follow. Start at a synthesis page, then drill
into the talks behind it.

## Procedure: fan out, then synthesize

1. **Orient (cheap).** Read `kb/INDEX.md`. Pick the handful of topics / people / series that
   could plausibly hold the answer — err on the side of *more*.

2. **Fan out — launch SEVERAL search subagents IN PARALLEL** (one message, multiple `Task` calls
   to the `retriever` agent), each with a DIFFERENT lens so blind spots in one are covered by
   another. Use 3–6 depending on breadth of the question:
   - **Topic lens** — read the most relevant `kb/topics/*` pages and browse their backlinked talks.
   - **Keyword lens** — broad `rg -i` across all of `kb/` with an expanded OR-pattern (synonyms,
     acronyms, YC jargon). Cast wide.
   - **Reframe lens** — re-ask the question in 2–3 different vocabularies (a beginner's words, an
     operator's words, the opposite framing) and search each.
   - **People lens** — identify relevant speakers, read their pages, browse their talks.
   - **Adjacency lens** — from the top topics, follow `See also` + `kb/graph.json` edges to
     *adjacent* topics/talks that might hold a non-obvious angle.
   Give each subagent the question + its lens; tell it to return cited evidence, not a final answer.
   (See `reference/retrieval-playbook.md` for exact `rg` recipes and query-expansion.)

3. **Merge.** Collect every subagent's evidence, dedupe by citation, and keep the strongest and
   most diverse points — including any that *disagree* with each other.

4. **Synthesize** (optionally via the `synthesizer` agent). Lead with the direct answer, then the
   supporting tactics/reasoning. **Every claim ends with a citation**
   `[<slug> @ mm:ss](https://youtu.be/<video_id>?t=<seconds>)` taken from the evidence
   (format: `reference/citation-format.md`). Surface disagreement explicitly ("YC partners split
   here — X argues… while Y argues…"), citing both sides. Preserve temporal qualifiers.

5. **Abstain when truly absent.** If a wide, parallel search genuinely turns up nothing, say so
   and name the gap. Do **not** fall back to pretraining knowledge — this KB answers *from YC*.

## Judgment, not rigidity

- Breadth first: it's cheaper to over-retrieve and filter than to miss the best talk.
- A single grep is rarely enough on 620 talks — that's why we fan out.
- You don't have to use every lens every time; scale the fan-out to the question.
- Small-talk or a lookup of one known talk doesn't need the full fan-out — use judgment.

## Reference (load on demand)
- `reference/retrieval-playbook.md` — lenses, query-expansion, `rg` recipes, nav-tree traversal
- `reference/citation-format.md` — `[slug @ mm:ss]` syntax + `?t=` seconds math
- `reference/frontmatter-schema.md` — field meanings
