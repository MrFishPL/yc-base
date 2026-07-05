# yc-base

A **file-over-app knowledge base** built from the entire [Y Combinator YouTube
channel](https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg). Ask a startup question — *"How do we sell to
enterprise when the buyer keeps stalling?"* — and get an answer synthesized **only** from YC
talks, cited to the exact video and timestamp.

The repo **is** the knowledge base and the query engine. Git-tracked Markdown is the source of
truth; you query it by prompting [Claude Code](https://claude.com/claude-code) in this directory.
No database, no server, no vector store.

## Design in one line

> Copy the *discipline* (git = truth, one home per fact, pre-computed distilled pages, hard
> citation rules) and skip the *infrastructure* (vector DBs, queues, graph engines) until corpus
> size forces your hand.

Full rationale: [`docs/RESEARCH.md`](docs/RESEARCH.md) · Full plan: [`docs/BUILD-PLAN.md`](docs/BUILD-PLAN.md).

## Local-first, minimal external API

| Stage | Tool | Cost |
|---|---|---|
| Acquire captions + metadata | `yt-dlp --skip-download` (local) | $0 |
| Clean transcripts | `scripts/clean_vtt.py` (Python stdlib) | $0 |
| Transcribe caption-gaps | `faster-whisper` (local GPU/CPU) | $0 (compute only) |
| Distill / synthesize / answer | **Claude Code, in this session** | — |
| Build catalog / graph / search / validate | stdlib Python | $0 |

The only step that needs an external account is **speaker diarization** (pyannote, gated on a
HuggingFace login) — it is **off by default**. Ask before enabling it.

## Layout

```
CLAUDE.md              # the contract Claude loads every session
RESOLVER.md            # where each page belongs (read before creating pages)
transcripts/raw/       # immutable: yt-dlp captions (.vtt) + metadata (.info.json)
transcripts/clean/     # deterministically cleaned transcripts, [mm:ss] preserved
kb/                    # the distilled knowledge (talks, topics, entities, series) + INDEX.md
data/catalog.json      # derived index of every video (rebuildable)
kb/graph.json          # derived typed relationship graph (rebuildable)
scripts/               # stdlib Python + yt-dlp/whisper wrappers
docs/                  # the research report and build plan
.claude/               # commands, skills, subagents, rules, settings
```

## Quickstart

```bash
# 0. one-time: install the two local tools (free, local — not an API)
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt        # yt-dlp (+ faster-whisper, optional)

# 1. acquire captions + metadata — whole channel (idempotent/resumable; or pass a playlist URL)
scripts/acquire.sh

# 2. clean the raw captions into transcripts/clean/*.md
python3 scripts/clean_vtt.py transcripts/raw

# 3. build the derived catalog
python3 scripts/build_catalog.py

# 4. distill into kb/ — done by Claude, one video at a time:
#    open Claude Code here and run:  /ask  or the ingest-video skill
```

Then just ask: open Claude Code in this repo and type `/ask How do we price a B2B product with no comparables?`

## Status — corpus built

The full channel is ingested: **618 talk pages · 36 topic syntheses · 46 people · 8,499 citations**,
with `validate.py` green (0 errors, 0 dead citations, 0 broken links). Open Claude Code here and ask.

> **Transcripts are not committed.** The raw/cleaned YouTube captions (~690 MB) are excluded to
> avoid bulk redistribution and repo bloat — regenerate them any time with
> `scripts/acquire.sh && python3 scripts/clean_vtt.py transcripts/raw`. The distilled, cited
> `kb/` pages (short quotes that link back to each source video) are what ship.

## Disclaimer

This is an **independent, unofficial** project — **not affiliated with, endorsed by, or sponsored
by Y Combinator.** It contains short, transformative summaries and quotations of publicly available
YC talks for research and educational use, each linked back to the original video for attribution.
All talk content belongs to its original creators.

## License

[MIT](LICENSE) © 2026 Michal Karp — applies to the tooling and the distilled pages authored here,
not to the underlying YC talk content.
