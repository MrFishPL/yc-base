---
name: ingest-video
description: Turn ONE cleaned YC transcript into a distilled talk page plus updated topic and entity pages. Use when ingesting a new video into the knowledge base, processing transcripts/clean files, or when the user says "ingest", "add this video", or "distill this talk". Process one video at a time.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3 scripts/*), Bash(rg:*)
---

# Ingest one video

**You do the distillation** — read the cleaned transcript and write the pages yourself. Do not
call any external LLM API. Process **one video at a time**: a single talk touches ~10–15 pages and
coherence matters.

## Steps

1. **Pick the input.** A file in `transcripts/clean/<date>_<id>_<slug>.md` (produced by
   `scripts/clean_vtt.py`). Read its companion `transcripts/raw/<date>_<id>.info.json` for
   metadata (title, upload_date, duration, channel, chapters).
2. **Read `RESOLVER.md`** before creating any page.
3. **Write the talk page** `kb/talks/<slug>.md`:
   - Frontmatter per `.claude/rules/kb-pages.md` (`type: yc-video`, `resource`, `video_id`,
     `series`, `speakers`, `topics`, `transcript_source`, `confidence`, dates).
   - Body = a **distilled** page (NOT the raw transcript): the talk's thesis, then 5–12 key
     ideas / notable quotes, **each with a `[mm:ss]` marker** copied from the clean transcript.
   - `See also` links to the topic and entity pages it relates to.
4. **Update topic pages.** For each idea, find or create the canonical `kb/topics/<topic>.md`
   (use `synthesize-topic` conventions: two-layer page). **Append a dated, sourced Timeline
   entry** citing this talk — do not duplicate the idea onto the talk page and the topic page;
   the topic page is the home, the talk page cites it.
5. **Update entity pages.** Ensure `kb/entities/people/<speaker>.md` exists (use `enrich-entity`);
   add this talk to their page. Same for notable companies mentioned as case studies.
6. **Normalize names/numbers.** Fix ASR errors in proper nouns (founders, companies, "YC W24",
   dollar figures) using known aliases; add variants to the relevant `aliases:` lists.
7. **Record provenance.** Append a line to `kb/log.md`: date, video slug, pages touched.
8. **Rebuild + validate.** `python3 scripts/build_catalog.py && python3 scripts/build_graph.py &&
   python3 scripts/validate.py`. Fix anything validate.py flags (broken wikilinks, missing
   `type`/`resource`, dead citations).

## Quality bar

- Every claim on a page cites a real `[mm:ss]`. No invented timestamps or quotes.
- Repeated YC advice collapses into ONE concept page many talks cite — never N copies.
- Preserve temporal qualifiers (year, YC batch); advice can be stale.
- Flag anything the transcript marked `<!-- SUSPECT -->` (silence-hallucination) and don't rely on it.
