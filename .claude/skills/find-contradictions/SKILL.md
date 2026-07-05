---
name: find-contradictions
description: Surface places where YC talks or partners give conflicting advice on the same question, and record them as data with typed contradicts edges. Use when consolidating a topic, when the user asks where partners disagree, or as a periodic sweep of the knowledge base.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3 scripts/*), Bash(rg:*)
---

# Find contradictions (disagreement is data)

YC partners genuinely disagree (e.g. land-and-expand pilots vs. top-down urgency; raise-now vs.
stay-default-alive). That disagreement is **valuable signal** for the user — never flatten it.

## Steps

1. **Scan a topic** (or the whole `kb/topics/` set). For each recurring question, collect the
   distinct positions taken, each with its `[<slug> @ mm:ss]` citation.
2. **Identify true conflicts** — same question, incompatible advice. Distinguish from *nuance*
   (advice that differs because context/stage differs — capture that with `applies-at <stage>`).
3. **Record on the topic page** under `Open threads`: state both positions, cite both, and name
   who holds each.
4. **Emit a typed edge** so the graph carries it. Add to the relevant page body a linked line the
   graph builder can pick up, e.g.:
   `<!-- edge: contradicts | how-to-sell-to-enterprise @ 12:30 <-> lightcone-ep-42 @ 08:05 | topic: enterprise-sales -->`
5. **Never resolve a contradiction by fiat.** If YC hasn't converged, the KB shouldn't pretend to.
6. **Rebuild the graph** (`build_graph.py`) and validate.

## Quality bar

- Each contradiction cites BOTH sides.
- Genuine stage/context nuance is labeled as such, not mislabeled as a contradiction.
