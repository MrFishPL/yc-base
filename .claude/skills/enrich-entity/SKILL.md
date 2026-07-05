---
name: enrich-entity
description: Create or merge a person or company page in the knowledge base, deduping name variants via aliases. Use when a talk introduces a founder, YC partner, or company, or when the user asks to add/merge/clean up an entity. Prevents the "PG vs Paul Graham" split-brain.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3 scripts/*), Bash(rg:*)
---

# Enrich an entity (person or company)

**You** maintain one canonical page per entity — no external LLM API.

## Steps

1. **Search before creating.** Grep the name and likely variants across `kb/entities/` and the
   corpus (`rg -i 'paul graham|pg' kb/`). If a page exists, MERGE into it; do not make a second one.
2. **Home:** `kb/entities/people/<slug>.md` (`type: person`) or
   `kb/entities/companies/<slug>.md` (`type: company`). Slug = canonical name, kebab-case.
3. **Frontmatter:** `type`, `title` (canonical name), `slug`, `aliases: []` (every variant seen —
   "PG", "Paul", "@paulg"), `role` (partner/founder), `company`/`companies` links, dates.
4. **Body (two-layer):** Compiled Truth = who they are + their recurring themes/positions (each
   cited). Timeline = talks they gave / were mentioned in, dated + cited.
5. **Backlink.** Add `[[<slug>]]` references from the talks and topics that involve them.
6. **Dedup rule:** filename = identity. Two facts about the same field are recorded, not
   overwritten; conflicting attributions are surfaced, not silently merged.
7. **Log + rebuild** (`build_graph.py`, `validate.py`).

## Quality bar

- Exactly one page per real-world entity. All name variants live in `aliases:`.
- Every claim about the entity is cited to a talk moment.
