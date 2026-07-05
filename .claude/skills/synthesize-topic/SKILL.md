---
name: synthesize-topic
description: Fold evidence from many YC talks into one cross-cutting topic page (PMF, pricing, enterprise sales, hiring, fundraising, growth, default-alive, founder psychology). Use when the user asks to synthesize, consolidate, or write up a topic across the corpus, or after ingesting several talks that share a theme. This is the human-value step that grep/RAG cannot produce.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3 scripts/*), Bash(rg:*)
---

# Synthesize a topic

**You do the synthesis** across talks — no external LLM API. This produces the pages that make
answers fast and deep: pre-computed cross-video reasoning, not per-query re-derivation.

## Steps

1. **Gather evidence.** Grep the corpus for the topic + synonyms (see the answer-from-kb
   retrieval playbook). Collect every relevant claim with its `[<slug> @ mm:ss]` citation.
2. **Read `RESOLVER.md`**; the topic's home is `kb/topics/<kebab>.md` (one primary home).
3. **Write/refresh the two-layer page** (`.claude/rules/kb-pages.md` format):
   - **Compiled Truth** (above `---`, rewritten each time): a thesis paragraph, `State` line
     (maturity, #talks, open-contradictions), `Open threads`, and `See also` wikilinks.
   - **Timeline** (below `---`, append-only, reverse-chron): each distinct piece of advice as a
     dated, **cited** entry. Merge duplicates — "talk to users" said in 30 talks becomes a few
     canonical entries citing the strongest sources, not 30 lines.
4. **Record disagreement.** When partners give conflicting advice, keep BOTH under `Open threads`
   with citations and run `find-contradictions` to emit a `contradicts` edge.
5. **Preserve nuance and time.** Keep temporal/version qualifiers; note when advice evolved
   (`evolves-from` / `refines`).
6. **Log + rebuild.** Append to `kb/log.md`; run `build_graph.py` + `validate.py`.

## Quality bar

- The Compiled Truth answers "what's the current YC view?" in one screen; the Timeline answers
  "who said what, when, and where?".
- Every Timeline entry is cited to a real moment. No uncited synthesis.
- Update `kb/INDEX.md` if this is a new topic.
