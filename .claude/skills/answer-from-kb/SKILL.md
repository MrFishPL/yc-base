---
name: answer-from-kb
description: Retrieves from the YC YouTube knowledge base and writes a grounded, cited answer. Use when the user asks any startup question — fundraising, product-market fit, pricing, hiring, enterprise/B2B sales, growth, retention, YC applications, founder psychology — or references a YC talk, a partner (Paul Graham, Michael Seibel, Dalton Caldwell, Jared Friedman, Gustaf Alströmer), or a series (Startup School, Lightcone, How to Start a Startup).
allowed-tools: Read, Grep, Glob, Bash(python3 scripts/search.py *), Bash(rg:*)
---

# Answer from the YC knowledge base (brain-first retrieval)

You answer startup questions using **only** the compiled knowledge in `kb/`, cited to source
video + timestamp. Never answer from your own pretraining knowledge — this KB speaks for YC.

## Standing procedure (every time this skill is active)

1. **Read the map.** Read `kb/INDEX.md` to shortlist which series/topic/talk pages are relevant.
   (If `kb/` is empty, tell the user the corpus is empty and stop.)
2. **Expand the query, then grep.** Turn the question into keywords + synonyms and OR them —
   this alone dramatically improves recall (see `reference/retrieval-playbook.md`):
   ```bash
   rg -i -l 'enterprise|B2B|procurement|champion|stall|urgency|compelling event|pilot|POC' kb/ -g '*.md'
   rg -i -C 3 'stall|urgency|champion' kb/topics/enterprise-sales.md
   ```
   Or use `python3 scripts/search.py search "<question>"` for a ranked list with `[mm:ss]` context.
3. **Read only the shortlisted compiled pages** — `kb/topics/*` first (synthesis), then
   `kb/talks/*` for specifics. Never dump raw transcripts. Follow `See also` / `[[wikilinks]]`
   to hop to related topics/entities. For "how did advice evolve across founders/years",
   consult `kb/graph.json` edges (`evolves-from`, `refines`, `contradicts`).
4. **Handle disagreement honestly.** If two pages conflict, present BOTH sides with citations —
   partner disagreement is signal, not noise.
5. **Write the answer.** Lead with the direct answer, then the supporting tactics. **Every claim
   ends with a citation** `[<slug> @ mm:ss]` linking to `https://youtu.be/<video_id>?t=<seconds>`
   (timestamp math and format in `reference/citation-format.md`).
6. **Abstain when absent.** If the corpus lacks the answer, say so plainly and name the gap.
   Do not fill it with general knowledge.

## Delegation

For anything beyond a trivial single-page lookup, dispatch the **`retriever`** subagent to gather
cited evidence (keeps transcript bytes out of the main context), then the **`synthesizer`**
subagent to write the final prose from that evidence and nothing else.

## Reference (load on demand)

- `reference/retrieval-playbook.md` — query-expansion recipe + `rg` patterns per topic
- `reference/citation-format.md` — `[slug @ mm:ss]` syntax + `?t=` seconds math
- `reference/frontmatter-schema.md` — what each frontmatter field means
