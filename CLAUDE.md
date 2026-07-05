# yc-base — CLAUDE.md

A **promptable knowledge base of the entire Y Combinator YouTube channel**.
Ask a startup question, get an answer grounded **only** in the corpus, always cited to a
video + timestamp. The repo *is* the knowledge base and the query engine — no database, no
server, no vector store. Git-tracked Markdown is the source of truth; Claude Code is the interface.

## Operating principles (local-first, minimal external API)

- **Do the thinking here, not over an API.** Transcript cleaning, distillation, topic
  synthesis, entity merging, and answering are done by **you (Claude)** directly. Do **not**
  wire in hosted LLM calls (OpenAI/Anthropic/Groq) for these steps.
- **Deterministic work runs as local stdlib-only Python** in `scripts/` (no third-party deps,
  no network): caption cleaning, catalog build, graph build, search, validation.
- **Acquisition is free and local:** `yt-dlp` pulls captions + metadata (`--skip-download`).
- **Transcription backfill is local:** `faster-whisper` runs on this machine for the ~5–10% of
  videos with no usable captions. **Speaker diarization needs a HuggingFace login — do NOT set
  it up; stop and ask the user first** if it's ever wanted.

## System-of-record contract

- **Truth = git-tracked Markdown + YAML frontmatter.** `data/catalog.json`, `kb/graph.json`,
  and any future embeddings are **DERIVED caches**, rebuilt from the Markdown with
  `python3 scripts/build_catalog.py` / `build_graph.py`. Never treat a cache as canonical.
- **`transcripts/raw/**` is IMMUTABLE.** Read it; never edit it. It is provenance.
- **`transcripts/clean/**`** = deterministically cleaned transcripts (produced by
  `scripts/clean_vtt.py`), one file per video, `[mm:ss]` markers preserved.
- **`kb/**`** = the distilled, human-value layer you write: per-video pages, cross-cutting
  topic pages, and entity pages.

## Corpus map (load on demand — don't read it all)

| Need | Read |
|---|---|
| navigate the whole KB | `kb/INDEX.md` (read FIRST) |
| which videos exist / mention X | `data/catalog.json` |
| a single talk's thesis + key moments | `kb/talks/<slug>.md` |
| cross-cutting synthesis (PMF, pricing, enterprise sales…) | `kb/topics/<topic>.md` |
| a person or company | `kb/entities/people/<slug>.md`, `kb/entities/companies/<slug>.md` |
| typed relationships across the corpus | `kb/graph.json` |
| how to retrieve + cite | `.claude/skills/answer-from-kb/` |
| where a new page belongs | `RESOLVER.md` (read BEFORE creating any page) |

## Hard rules

1. **Read `RESOLVER.md` before CREATING any page.** One primary home per fact; one file per
   entity. Every page's filename is its identity (kebab-case slug).
2. **Search compiled `kb/` pages BEFORE answering.** Prefer topic pages for synthesis; drop to
   talk pages for specifics. Delegate the search to the `retriever` subagent so raw transcript
   text never floods the main context.
3. **Cite every claim** as `[<slug> @ mm:ss]` rendered as a live deep-link
   `https://youtu.be/<video_id>?t=<seconds>`. **Never invent a quote or a timestamp** — copy the
   nearest real `[mm:ss]` from the cited page.
4. **If the corpus does not contain the answer, SAY SO** and name the gap. Never fall back to
   pretraining knowledge to answer a startup question — this KB answers *from YC*, not from you.
5. **Preserve temporal qualifiers** (YC batch, year). Advice can be stale; keep the reader aware.
6. **Contradictions are DATA.** When two talks answer the same question differently, present
   BOTH with citations; never silently pick one. Emit a `contradicts` edge.
7. **Dedup by canonical slug + `aliases`** (e.g. "PG" == "Paul Graham"). If you do a manual task
   two+ times, codify it into a skill.

## Page schema

The frontmatter schema for every `kb/` and `transcripts/clean/` page is defined in
`.claude/rules/kb-pages.md` (path-scoped, loads automatically when you touch those files).
The only OKF-required field is `type`; talks additionally require `resource` (the YouTube URL).

## Workflow skills

- `/ask <question>` — answer a startup question from the corpus, cited.
- `ingest-video` — turn one cleaned transcript into a talk page + updated topic/entity pages.
- `synthesize-topic <topic>` — fold evidence from N talks into one topic page.
- `enrich-entity <slug>` — build/merge a person or company page.
- `find-contradictions` — surface partners disagreeing, as typed edges.

## Build order (see `docs/BUILD-PLAN.md`)

Acquire (captions) → clean → ingest (one video at a time) → synthesize topics → answer.
Add embeddings/graph engine **only** if a measured retrieval miss proves grep + tiered
`INDEX.md` + typed links insufficient. Full research + rationale in `docs/RESEARCH.md`.
