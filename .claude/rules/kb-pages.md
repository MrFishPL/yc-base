---
description: Page schema and conventions for the knowledge base
paths:
  - "kb/**"
  - "transcripts/clean/**"
---

# kb/ page conventions

Every file under `kb/` and `transcripts/clean/` is Markdown with a **YAML frontmatter** block.
The only OKF-required field is `type`. Talks additionally require `resource` (the YouTube URL).

## Frontmatter schema

```yaml
---
type: yc-video          # REQUIRED. yc-video (talks) | concept (topics) | person | company | series
title: "How to Sell to Enterprise — Startup School"
video_id: dQw4w9WgXcQ   # talks only: the 11-char YouTube ID = stable key
slug: how-to-sell-to-enterprise
resource: https://www.youtube.com/watch?v=dQw4w9WgXcQ   # talks: REQUIRED (citation anchor)
series: startup-school  # startup-school | lightcone | how-to-start-a-startup | dalton-and-michael | talks
speakers: [michael-seibel]     # canonical entity slugs (talks)
aliases: []                    # alt titles / name variants — used for dedup
upload_date: 2023-11-14        # talks: from .info.json
duration_s: 2731
topics: [enterprise-sales, pricing]   # slugs of linked kb/topics/ pages
transcript_source: auto-captions      # auto-captions | manual-captions | whisper-large-v3
confidence: high        # high | medium | low  (drop for heavy-ASR videos)
created: 2026-07-05
updated: 2026-07-05
---
```

## Two-layer page format (topic & entity pages)

Above the `---` rule: **Compiled Truth** — the current synthesis, rewritten each update
(thesis → state fields → open threads → See also).
Below it: an **append-only, reverse-chronological Timeline** — each entry dated and *sourced*
with a citation. "Current state?" read top. "What happened / who said what?" read bottom.

```markdown
---
type: concept
title: Enterprise Sales
slug: enterprise-sales
tags: [sales, gtm]
updated: 2026-07-05
---
# Enterprise Sales — Compiled Truth

**Thesis:** …
**State:** maturity: strong · #talks: 14 · open-contradictions: 1
**Open threads:** pricing anchoring vs. land-and-expand (partners split).
**See also:** [[pricing]], [[do-things-that-dont-scale]], [[michael-seibel]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — "Find the champion, then arm them to sell internally"
  — [how-to-sell-to-enterprise @ 12:30](https://youtu.be/dQw4w9WgXcQ?t=750)
```

## Rules

- **Kebab-case filenames = identity.** Talks: `kb/talks/<slug>.md`. Never rename to break links.
- **Cite everything** as `[<slug> @ mm:ss]` → `https://youtu.be/<video_id>?t=<seconds>`.
  `mm:ss` → seconds: `minutes*60 + seconds`. Never invent a timestamp.
- **Link, don't duplicate.** Shared ideas are `[[wikilinks]]` to topic/entity pages.
- **Preserve `[mm:ss]` markers** already present in `transcripts/clean/`.
- After editing `kb/`, the derived caches are stale — rebuild with
  `python3 scripts/build_catalog.py` and `python3 scripts/build_graph.py`, and run
  `python3 scripts/validate.py`.
