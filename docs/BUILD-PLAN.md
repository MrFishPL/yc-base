# yc-base — Build Plan: A File-Over-App Claude Code Knowledge Base from the Y Combinator YouTube Channel

A promptable, git-native knowledge base where **markdown + YAML frontmatter in git is the system of record**, Claude Code retrieves with **agentic ripgrep over an index**, and every answer **cites `video-slug @ mm:ss`** with a deep-link back to the exact YouTube moment. You can `git init` and run Stage 1 today.

> Verified-facts note baked into this plan: a Claude Code Skill's `SKILL.md` frontmatter **requires BOTH `name` and `description`** (both mandatory — there is no "first paragraph of the body" fallback). All skill/command/subagent conventions below follow the current Claude Code docs.

---

## A) Recommended Architecture (one paragraph + rationale)

**Architecture in one paragraph:** Build `yc-base` as an **OKF-style bundle inside a Claude Code repo**: immutable source transcripts live in `transcripts/raw/` (never edited by the agent) and `transcripts/clean/` (LLM-normalized, one file per video with timestamps + speaker labels); pre-computed **synthesis** lives in `kb/` as two-layer markdown pages — per-video "talk" pages, cross-cutting `kb/topics/` concept pages, and `kb/entities/` people/company pages — each carrying a queryable YAML frontmatter block (`type` required, OKF-style) and a `resource:` YouTube URL that is the citation anchor. A hand-written-then-generated `kb/INDEX.md` map plus relative-markdown **wikilinks** turn the directory into a lightweight, greppable knowledge graph, and a derived `kb/graph.json` holds **typed** edges (something bare `[[wikilinks]]` cannot carry). Claude Code retrieves **agentically**: it reads `INDEX.md`, greps compiled pages with `ripgrep`, and only reads the handful of pages it needs — inside an isolated **retriever subagent** so raw transcript text never floods the main context — then a **synthesizer** writes a grounded, cited answer. Embeddings/vector DB are explicitly **deferred** and, if ever added, remain a *derived cache* rebuildable from the files.

**Rationale, tied to the referenced approaches:**
- **File-over-app source of truth (Steph Ango; Karpathy LLM-wiki).** "Apps are ephemeral, files last." A git repo of markdown is diffable, portable across tools, human- and agent-readable from the *same* file, and directly promptable. We pre-compute synthesis into pages (Karpathy's LLM-wiki) instead of re-deriving answers via RAG on every query.
- **Borrow gbrain's *discipline*, drop its *infrastructure*.** From `garrytan/gbrain` we take: git = truth + any index is a *derived cache rebuildable with one command*; **MECE directories + resolvers** (one primary home per entity, `README.md` resolver per dir, root `RESOLVER.md` read before creating a page); **two-layer pages** (Compiled Truth above `---`, append-only sourced Timeline below); **thin CLAUDE.md (~200 lines) + fat skills**; the **latent vs deterministic split** (grep/counts/timestamps = code; synthesis/reconciliation = model); **dedup by canonical slug + `aliases`**; and **citation discipline as a hard rule**. We *drop* PGLite/pgvector, HNSW/BM25/RRF hybrid search, cron enrichment, job queues, OAuth/MCP, and multi-tenant topology — this is a *fixed batch corpus of talks*, not a live operational brain.
- **Entity graph informed by OKF.** OKF (Google, v0.1) is a near-exact blueprint: a bundle is *just files, just markdown, just YAML frontmatter*; the file **path is the concept's stable ID**; only `type` is required; `resource` is the canonical source link (our citation); `index.md`/`log.md` are reserved; relationships are relative markdown links. The `coleam00/cole-medin-ai-coding` repo (`videos/` + `concepts/` + `index.md` + `log.md` + `okf-cli.py`) is a proven precedent for *exactly this YouTube-transcript use case*. We adopt its split but add **typed edges** (`graph.json`) because a bare link carries only "these are connected," and startup advice needs `tactic --solves--> problem`, `partner --contradicts--> partner`.
- **Agentic retrieval first, embeddings later.** The "Is Grep All You Need?" harness study finds iterative ripgrep generally beats vector retrieval on accuracy; Cursor/Morph measured only ~+12.5% from adding semantic on top of grep. Grep needs no index to rebuild — ideal for an **append-only** channel. An index-file/no-vector approach is documented as best for **20–500 well-structured docs**; because the full channel exceeds that, we use a **tiered index** (root `INDEX.md` → per-series/per-topic sub-indexes) and reserve embeddings as an *optional recall booster* only if grep proves insufficient at full scale.

---

## B) Full Repo Directory Tree

```
yc-base/
├── CLAUDE.md                      # ~200-line dispatcher: system-of-record contract, page
│                                  #   format, citation rule, "read RESOLVER before creating",
│                                  #   "search compiled pages before answering", load-on-demand map
├── RESOLVER.md                    # root decision tree: given a fact, which dir is its ONE home?
├── README.md                      # human onboarding + "how to build" quickstart
├── .gitignore                     # ignores audio/*.m4a, __pycache__, .venv, *.info.json.tmp
│
├── .claude/
│   ├── settings.json              # permissions (pre-allow rg/python3/yt-dlp read paths), hooks
│   ├── rules/                     # path-scoped constraint files (paths: glob frontmatter)
│   │   ├── transcripts.md         # paths: transcripts/**  → "raw/ is immutable, never edit"
│   │   ├── kb-pages.md            # paths: kb/**           → two-layer page schema + frontmatter
│   │   └── scripts.md             # paths: scripts/**      → stdlib-only Python, no network on API
│   ├── commands/
│   │   └── ask.md                 # /ask — thin entrypoint that dispatches to the answer skill
│   ├── skills/
│   │   ├── answer-from-kb/
│   │   │   ├── SKILL.md           # fat retrieval+synthesis procedure (the "brain-first" answer flow)
│   │   │   └── reference/
│   │   │       ├── citation-format.md      # exact cite syntax + youtu.be?t= math
│   │   │       ├── retrieval-playbook.md   # query-expansion → rg patterns → read → cite
│   │   │       └── frontmatter-schema.md   # canonical YAML fields (mirrors rules/kb-pages.md)
│   │   ├── ingest-video/
│   │   │   └── SKILL.md           # one transcript → clean file + talk page + Timeline + concepts
│   │   ├── synthesize-topic/
│   │   │   └── SKILL.md           # diarize across N talks → one kb/topics/*.md with citations
│   │   ├── enrich-entity/
│   │   │   └── SKILL.md           # build/update kb/entities/<slug>.md, merge aliases, dedup
│   │   └── find-contradictions/
│   │       └── SKILL.md           # surface partners disagreeing on advice as DATA (edge type)
│   └── agents/
│       ├── retriever.md           # isolated-context subagent: greps/reads, returns cited snippets
│       └── synthesizer.md         # takes retriever output, writes grounded cited answer only
│
├── data/
│   └── catalog.json               # DERIVED: [{video_id, title, url, series, upload_date,
│                                  #   duration_s, speakers[], has_manual_subs, has_auto_subs,
│                                  #   transcript_source, clean_path}] — deterministic index
│
├── transcripts/
│   ├── archive.txt                # yt-dlp --download-archive ledger (idempotent incremental runs)
│   ├── raw/                       # IMMUTABLE provenance the agent reads but NEVER edits
│   │   ├── <upload_date>_<id>.en.vtt        # YouTube captions (auto or manual)
│   │   ├── <upload_date>_<id>.info.json     # full metadata (title, chapters[], duration, ...)
│   │   └── <upload_date>_<id>.whisper.json  # only for re-transcribed videos (word timestamps)
│   └── clean/                     # LLM-normalized, one file per video, timestamps + speakers kept
│       └── <upload_date>_<id>_<slug>.md
│
├── kb/                            # PRE-COMPUTED synthesis = what Claude answers FROM
│   ├── INDEX.md                   # tiered map: series → sub-index; read FIRST (progressive disclosure)
│   ├── log.md                     # append-only ISO-dated ingest/sync changelog (OKF reserved)
│   ├── talks/                     # one two-layer page per video (Compiled Truth + Timeline)
│   │   ├── README.md              # resolver: "what goes here / what does NOT"
│   │   └── <slug>.md
│   ├── topics/                    # cross-cutting evergreen concepts (fundraising, pmf, pricing…)
│   │   ├── README.md
│   │   ├── product-market-fit.md
│   │   ├── enterprise-sales.md
│   │   └── pricing.md
│   ├── entities/                  # one page per person/company; canonical slug = identity
│   │   ├── people/  (paul-graham.md, michael-seibel.md, …  aliases: ["PG"])
│   │   └── companies/ (airbnb.md, stripe.md, …)
│   ├── series/                    # per-series landing/index pages (Startup School, Lightcone…)
│   └── graph.json                 # DERIVED typed entity/relationship graph (rebuildable from pages)
│
└── scripts/                       # deterministic tooling (latent work stays in skills/agents)
    ├── acquire.py                 # wraps yt-dlp: enumerate channel/playlist, pull subs+metadata
    ├── build_catalog.py           # raw/*.info.json + *.vtt → data/catalog.json
    ├── clean_vtt.py               # dedup rolling captions, keep timestamps → transcripts/clean/*.md
    ├── transcribe.py              # faster-whisper/WhisperX fallback for missing/poor captions
    ├── search.py                  # stdlib grep-first retrieval CLI (index / search / read-page)
    ├── build_graph.py             # parse fenced blocks + wikilinks in kb/ → graph.json
    ├── validate.py               # OKF conformance + broken-wikilink + dead-citation lint
    └── videos.txt / playlists.txt # INPUT lists that make the pipeline scale (see Phase rollout)
```

**What each holds (annotations):**

| Path | Role |
|---|---|
| `CLAUDE.md` | Facts + contract only, ~200 lines: corpus map, frontmatter schema pointer, citation format, hard rules, load-on-demand reference table. Loads every session, so kept lean. |
| `RESOLVER.md` | Numbered decision tree: "a fact about a *person* → `kb/entities/people/`; a *reusable framework* → `kb/topics/`; a *single talk's thesis* → `kb/talks/`." Read before any page creation. |
| `.claude/rules/*.md` | Path-scoped constraints via `paths:` glob frontmatter — load only when editing matching files (e.g. the immutability rule only surfaces when touching `transcripts/**`). |
| `.claude/commands/ask.md` | Thin slash-command entrypoint (`/ask`). Merges with the skill system; kept minimal, delegates to the fat skill. |
| `.claude/skills/answer-from-kb/` | The fat retrieval+synthesis skill; `reference/` holds detail loaded on demand at ~0 token cost until read. |
| `.claude/agents/{retriever,synthesizer}.md` | Isolated-context subagents; retriever keeps raw transcript bytes out of the main window. |
| `data/catalog.json` | Deterministic, machine-built inventory of every video; the "which videos exist / mention X" lookup that must never be guessed. |
| `transcripts/raw/` | `.raw`-style immutable sidecar: captions + `.info.json` + optional Whisper JSON. Source-of-truth provenance. |
| `transcripts/clean/` | Normalized prose with `[mm:ss]` markers and speaker labels; the substrate for synthesis. |
| `kb/INDEX.md` | The navigation map the agent reads first (tiered because the corpus > 500 docs). |
| `kb/log.md` | Append-only audit trail of every sync/ingest run (OKF reserved file). |
| `kb/talks / topics / entities / series` | The four MECE homes; each with a `README.md` resolver. |
| `kb/graph.json` | Derived typed graph for multi-hop/"how did advice evolve" queries. |
| `scripts/` | All deterministic tooling; `videos.txt`/`playlists.txt` are the scaling inputs. |

---

## C) Pipeline — Stage by Stage (exact commands/tooling)

### C.1 Acquisition (`yt-dlp`)

**Install & pin** (YouTube extraction breaks often; updates are the fix; needs CPython ≥ 3.10):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -U "yt-dlp>=2025.1.1" faster-whisper
```

**Step 1 — enumerate the channel cheaply (IDs only), to build the input list:**
```bash
# --flat-playlist lists video IDs without touching media; cover all tabs
yt-dlp --flat-playlist --print "%(id)s	%(title)s	%(duration)s" \
  "https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg/videos"  > scripts/videos.txt
# add /streams and /shorts as separate passes if you want them
yt-dlp --flat-playlist --print id "https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg/streams" >> scripts/videos.txt
```

**Step 2 — pull captions + metadata only (no media), incremental & idempotent:**
```bash
yt-dlp \
  --download-archive transcripts/archive.txt \  # skip already-processed IDs on reruns
  --skip-download \                             # NO media stream — text + metadata only (ToS-lighter)
  --write-subs --write-auto-subs \              # request BOTH manual and auto; yt-dlp writes whichever exist
  --sub-langs "en.*" --sub-format vtt \         # native vtt is the reliable format
  --convert-subs srt \                          # clean SRT for LLM ingestion (strips positioning/styling)
  --write-info-json \                           # per-video metadata incl. chapters[] (chunk boundaries!)
  --sleep-requests 1 \                          # pace metadata requests
  --sleep-interval 5 --max-sleep-interval 30 \  # random per-video delay — 429 defense
  -o "transcripts/raw/%(upload_date>%Y-%m-%d)s_%(id)s.%(ext)s" \
  --batch-file scripts/videos.txt               # OR a channel/playlist URL directly
```
- `--write-subs` = human/creator captions (punctuation, higher accuracy, often absent). `--write-auto-subs` = YouTube ASR (nearly always present, no punctuation, word-timed). There is **no single "prefer manual then auto" flag** (yt-dlp issue #9371) — request both, then let `clean_vtt.py` dedupe with **manual winning**.
- `chapters[]` in `.info.json` (start/end/title) are **excellent natural chunk boundaries** — capture them.
- **Audio-only fallback, only when re-transcribing** (edge case — YC videos almost always have captions):
  ```bash
  yt-dlp -f bestaudio -x --audio-format m4a --download-archive transcripts/archive.txt \
    -o "transcripts/raw/audio/%(id)s.%(ext)s" "https://youtu.be/<ID>"
  ```

**Step 3 — build the deterministic catalog:**
```bash
python3 scripts/build_catalog.py   # raw/*.info.json + *.vtt → data/catalog.json
```

**ToS / rate-limit handling (design constraint, state it plainly):**
- YouTube's Terms disallow bulk/automated download except via provided features; captions are copyrighted. **Mitigation baked in:** pull *text* not video (`--skip-download`), rate-limit politely, treat the corpus as **personal/internal research**, do **not** redistribute raw video, and keep `resource:` URLs so all attribution points back to YouTube.
- Expect **HTTP 403** after ~20 GB/day/IP and **429** at crawl scale (IP-based). Mitigation: text-only stays far under 20 GB; the `--sleep-*` flags above; run from a **residential IP, not a cloud VM**; spread a full-channel backfill across days via `--download-archive`; on `"Sign in to confirm you're not a bot,"` add `--cookies-from-browser chrome` *sparingly* (ties requests to your account → account risk; prefer pacing first).

### C.2 Transcription (chosen default)

**Default = YouTube auto-captions where adequate; re-transcribe with `faster-whisper large-v3` (or `WhisperX` when speaker labels matter) where quality matters.** Captions cost **$0** and no GPU, so they are the bulk-backfill winner.

- **Coverage policy:** (1) manual captions if present; (2) else auto-captions; (3) re-transcribe with Whisper **only** for videos with *no captions* OR flagged low-quality (dense jargon, heavy accents, panel crosstalk, or entity/number-critical hero talks).
- **Whisper command (fallback, GPU or CPU):**
  ```bash
  # faster-whisper (CTranslate2; ~4x faster & ~3x smaller than reference Whisper; CPU or GPU)
  python3 scripts/transcribe.py --model large-v3 --language en \
      --compute_type int8 transcripts/raw/audio/<ID>.m4a
  # panels needing "who spoke when": WhisperX adds word-level timestamps + diarization
  #   whisperx <audio> --model large-v2 --diarize --highlight_words True --output_format json,srt
  #   (needs HF_TOKEN + accept pyannote speaker-diarization-community-1 agreement, or diarize silently fails)
  ```
  All Whisper variants share identical weights → same WER; they differ in **speed/features**. Use `distil-large-v3` (English-only, ~6x faster, within ~1% WER) for a cheap first draft, reserve full `large-v3`/WhisperX for hero content.

**Cost/time estimate for the chosen coverage** (channel planning anchor: **~2,000 videos ≈ ~1,000 hours**, *hedge: exact hours depend on shorts/streams mix*):

| Path | Coverage | Time | Cost |
|---|---|---|---|
| Auto/manual captions (default) | ~90–95% of videos have captions | Bounded by yt-dlp pacing: text-only backfill over ~2–4 evenings | **$0**, no GPU |
| Whisper fallback | the missing ~5–10% (~50–100 hrs) | faster-whisper large-v3 ≈ real-time–several×RT on a rented GPU (WhisperX large-v2 up to ~70× RT, <8 GB VRAM); medium ≈ 5 audio-hrs/wall-hr on an RTX 2080Ti | Self-host ≈ GPU rental only; hosted: **Groq ≈ $0.04/hr → ~$2–4** for 50–100 hrs; OpenAI $0.006/min → ~$18–36 |

*Net: the full-channel transcription bill is effectively $0 for captions plus a few dollars for the Whisper backfill.* Whisper WER on real-world English is ~8–12%, and it **hallucinates/repeats on silence** — so a cleaning pass (next stage) is mandatory, and entity/number tokens (company names, "YC W24", dollar figures) can degrade to 50–70% and need LLM normalization.

### C.3 Cleaning / Formatting

**`scripts/clean_vtt.py` (deterministic):** de-duplicate the "rolling" overlapping auto-caption lines, drop styling/positioning, merge word-timed cues into ~1-sentence segments, prefer the manual track when both exist, and emit `transcripts/clean/<date>_<id>_<slug>.md` **preserving `[mm:ss]` markers**. Whisper `.txt` timestamp prefixes can be stripped with `sed -r 's/^.+]....//g'` if you go that route.

**LLM distillation prompt (run per video, latent step — used by `/ingest-video`):**
```
SYSTEM: You are cleaning a YC talk transcript. Do NOT summarize or drop content here — this
is the CLEAN transcript layer, not the synthesis layer.
TASK, in one pass:
1) Fix ASR errors and restore punctuation/casing. Correct startup proper nouns and numbers
   using this glossary: {YC batch codes, known founders/partners, portfolio companies}.
2) Remove filler ("um", "you know", false starts) WITHOUT changing meaning.
3) Label speakers when inferable (moderator vs guest); keep "Speaker 1/2" if uncertain.
4) Preserve a [mm:ss] timestamp at the start of every paragraph/turn — never invent times;
   copy the nearest real cue time.
5) Flag any segment you suspect is a silence-hallucination with <!-- SUSPECT --> and keep the
   raw text; do not delete it.
OUTPUT: markdown body only (frontmatter is added by the pipeline).
```

**Chunking strategy:** chunk by **speaker turn** (atomic unit) and by **chapter/topic boundary** (use `.info.json` `chapters[]` where present); adaptive/topic-aligned chunking beats fixed windows on long narrative talks. When a fixed target is needed, use **256–512 tokens with 10–20% overlap** (the RAG sweet spot). Carry `speaker`, `[mm:ss]`, and `video_id` on every chunk for retrieval-time filtering and citation.

**Exact YAML frontmatter schema** (identical for `transcripts/clean/*` and `kb/talks/*`; `type` required per OKF):
```yaml
---
type: yc-video            # REQUIRED (OKF). talks use yc-video; topics use concept; entities use person|company
title: "How to Sell to Enterprise — Startup School"
video_id: dQw4w9WgXcQ     # 11-char YouTube ID = stable key
slug: how-to-sell-to-enterprise
resource: https://www.youtube.com/watch?v=dQw4w9WgXcQ   # citation anchor (non-negotiable)
series: Startup School     # Startup School | Lightcone | How to Start a Startup | Dalton & Michael | Talks
speakers: [michael-seibel] # canonical entity slugs
aliases: []                # alt titles/name variants for dedup
upload_date: 2023-11-14
duration_s: 2731
topics: [enterprise-sales, pricing, sales]   # links to kb/topics/*
transcript_source: auto-captions             # auto-captions | manual-captions | whisper-large-v3
confidence: high           # high | medium | low  (drop to medium/low for heavy-ASR videos)
created: 2026-07-05
updated: 2026-07-05
---
```

**Filename conventions:** `transcripts/clean/<upload_date>_<video_id>_<slug>.md` (sortable, collision-free, stable even if the title changes — the 11-char ID is the key). `kb/talks/<slug>.md`, `kb/topics/<kebab-concept>.md`, `kb/entities/people/<kebab-name>.md`. Kebab-case everywhere; **filename = identity**.

**Timestamp + speaker preservation:** every paragraph begins `[mm:ss]`; the clean file keeps speaker labels; citations resolve to `https://youtu.be/<id>?t=<seconds>` (deep-link math in `reference/citation-format.md`).

### C.4 Knowledge Extraction (file-based graph informed by OKF)

**How pages are produced (latent work, deterministic scaffolding):**
- `/ingest-video` (one video at a time — *not* batch, because a single source touches 10–15 pages and coherence matters): read `transcripts/clean/<file>` → write/update the **two-layer** `kb/talks/<slug>.md` → create/update linked `kb/topics/*` and `kb/entities/*` → add wikilinks → append to `kb/log.md` → update `kb/INDEX.md`.
- `/synthesize-topic <topic>`: **diarize across N talks** into one `kb/topics/<topic>.md` — the human-value step no grep/RAG produces. Each claim carries a `[slug @ mm:ss]` citation.
- `/enrich-entity <slug>`: merge name variants via `aliases:` (kills the "PG" vs "Paul Graham" split-brain), keep one page per entity.
- `/find-contradictions`: when two talks answer the same question differently, **record both as data** with sources and emit a `contradicts` edge — partner disagreement is *valuable*, not noise.

**Two-layer page format (gbrain-adapted):**
```markdown
---
type: concept
title: Enterprise Sales
slug: enterprise-sales
resource: null
tags: [sales, fundraising-adjacent, gtm]
updated: 2026-07-05
---
# Enterprise Sales  — Compiled Truth (current synthesis)

**Thesis:** YC's recurring advice on selling to large orgs...
**State fields:** maturity: strong-coverage · #talks: 14 · open-contradictions: 1
**Open threads:** pricing anchoring vs. land-and-expand (partners split).
**See also:** [[pricing]], [[do-things-that-dont-scale]], [[michael-seibel]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — "Find the champion, then arm them to sell internally"
  — [how-to-sell-to-enterprise @ 12:30](https://youtu.be/dQw4w9WgXcQ?t=750)
- 2026-07-05 — "A stalling buyer usually = no urgency; manufacture a compelling event"
  — [lightcone-ep-42 @ 08:05](https://youtu.be/XXXX?t=485)
```

**Graph schema (typed — for the startup-advice domain):**

*Node types:* `person` (founder/partner), `company` (case study), `talk` (video), `topic` (framework/concept), `stage` (idea/MVP/PMF/growth/scale), `metric` (retention/CAC/burn), `problem`, `tactic`, `principle`, `series`.

*Edge types (typed, directional):* `mentions`, `advises`, `exemplifies` (company → principle), `solves` (tactic → problem), `contradicts` (talk/partner ↔ talk/partner), `refines`/`evolves-from` (advice-over-time), `applies-at` (tactic → stage), `measured-by` (goal → metric), `authored-by` (talk → person), `part-of` (talk → series).

**Concrete `kb/graph.json` entry (derived, rebuildable via `scripts/build_graph.py`):**
```json
{
  "version": "0.1",
  "generated_from": "kb/**",
  "nodes": [
    {"id": "topic:enterprise-sales", "type": "topic", "label": "Enterprise Sales", "page": "kb/topics/enterprise-sales.md"},
    {"id": "problem:buyer-stalling", "type": "problem", "label": "Buyer keeps stalling / no urgency"},
    {"id": "tactic:manufacture-compelling-event", "type": "tactic", "label": "Manufacture a compelling event"},
    {"id": "person:michael-seibel", "type": "person", "label": "Michael Seibel", "aliases": ["Michael"], "page": "kb/entities/people/michael-seibel.md"},
    {"id": "talk:how-to-sell-to-enterprise", "type": "talk", "label": "How to Sell to Enterprise", "resource": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
  ],
  "edges": [
    {"from": "tactic:manufacture-compelling-event", "type": "solves", "to": "problem:buyer-stalling",
     "source": "how-to-sell-to-enterprise @ 12:30",
     "url": "https://youtu.be/dQw4w9WgXcQ?t=750", "confidence": "high"},
    {"from": "talk:how-to-sell-to-enterprise", "type": "authored-by", "to": "person:michael-seibel"},
    {"from": "talk:how-to-sell-to-enterprise", "type": "part-of", "to": "series:startup-school"}
  ]
}
```
Keep it **file-based**: `graph.json` is a *derived cache*; the markdown pages + wikilinks are canonical. Export to `graphml`/`cypher` later only if real traversal is needed — do not stand up Neo4j until query complexity demands it.

### C.5 Indexing / Retrieval (how Claude Code actually retrieves)

**Default = agentic ripgrep + a tiered INDEX + wikilinks (no vector DB):**
1. **Read the map first.** Agent reads `kb/INDEX.md` (tiered: root → per-series/per-topic sub-index, because the corpus exceeds the ~500-doc flat-index ceiling) to shortlist candidate pages — a deterministic navigation layer replacing a vector router.
2. **Query-expand, then grep.** Expand the user's question into synonyms/keywords and OR them in one pattern (this alone ~10×'d retrieval quality on Natural Questions):
   ```bash
   rg -i -l 'enterprise|B2B|procurement|champion|stall|urgency|compelling event|pilot' kb/ -g '*.md'
   rg -i -C 3 --json 'stall|urgency|champion' kb/topics/enterprise-sales.md   # spans for exact-line citation
   ```
   Flags: `-i` case-insensitive, `-l` list files to route, `-C 3` context for citing surrounding passage, `-c` per-file counts as a cheap relevance score, `--json` structured spans.
3. **Read only the shortlisted compiled pages** (never dump raw transcripts). Follow `[[wikilinks]]`/`See also` to hop to related topics/entities. For multi-hop "how did advice evolve across founders/years," consult `graph.json` edges.
4. **`scripts/search.py`** wraps this as three stdlib ops — `index`, ranked keyword `search`, `read-page` — mirroring OKF's `okf-cli.py`, pre-approved via `allowed-tools: Bash(python3 *)` so no permission prompts.

**When to add embeddings:** only if, at full-channel scale, grep+index misses *oblique* references (no shared keyword). Then add a **derived, optional** vector index (rebuildable from files) as a *hybrid recall booster* — never the source of truth. GraphRAG-style indexing is now cheap (~$33 for a corpus vs a 2024 $33k outlier) but is only worth it for genuine multi-hop/global-sensemaking questions; most YC queries are topical lookups where grep wins on cost, transparency, and freshness.

**How answers cite source video + timestamp:** every claim carries `[<slug> @ mm:ss]` rendered as a live deep-link `https://youtu.be/<video_id>?t=<seconds>`, pulled from the cited page's `resource:` + the paragraph's `[mm:ss]`. For a programmatic path, the same clean segments feed the **Anthropic Citations API** as *custom-content* documents (one block per segment, `citations:{enabled:true}` on all or none), so a returned `content_block_location` maps 1:1 back to a segment/timestamp — structurally guaranteed, no invented pointers. (Note: Citations **cannot** be combined with structured outputs in the same request — run grounded-answer and JSON passes separately.)

### C.6 Prompting Layer

**`CLAUDE.md` skeleton (~200 lines; facts + contract only):**
```markdown
# yc-base — CLAUDE.md
## North Star
A promptable knowledge base of the entire YC YouTube channel. Answer startup questions
grounded ONLY in the corpus, always cited to video + timestamp.

## System-of-record contract
- Git-tracked markdown + YAML frontmatter is TRUTH. data/catalog.json, kb/graph.json, and any
  future embeddings are DERIVED caches, rebuildable with `python3 scripts/build_*.py`. Never treat them as canonical.
- transcripts/raw/** is IMMUTABLE. Read it; never edit it.

## Corpus map (load on demand)
| Need | Read |
|---|---|
| navigate | kb/INDEX.md (read FIRST) |
| which videos exist / mention X | data/catalog.json |
| a talk's thesis | kb/talks/<slug>.md |
| cross-cutting synthesis | kb/topics/<topic>.md |
| a person/company | kb/entities/** |
| typed relationships | kb/graph.json |
| retrieval + citation how-to | .claude/skills/answer-from-kb/ |

## Hard rules
1. Read RESOLVER.md before CREATING any page; one primary home per fact; one file per entity.
2. SEARCH compiled kb/ pages BEFORE answering. Prefer topic pages for synthesis.
3. CITE every claim as `[slug @ mm:ss]` → youtu.be/<id>?t=<sec>. Never invent quotes or timestamps.
4. If the corpus does not contain the answer, SAY SO. Never fall back to pretraining knowledge.
5. Preserve temporal qualifiers (YC batch, year) — advice can be stale.
6. Contradictions are DATA: record both sides with sources; do not silently pick one.
7. Dedup by canonical slug + aliases (PG == Paul Graham). Codify any repeated manual task into a skill.

## Frontmatter schema → see .claude/rules/kb-pages.md (path-scoped)
```

**ONE example slash command — `.claude/commands/ask.md` (`/ask`):**
```markdown
---
description: Answer a startup question grounded ONLY in the YC corpus, with video+timestamp citations. Use for questions about fundraising, PMF, pricing, hiring, enterprise sales, growth, YC application, founder psychology.
argument-hint: <your startup question>
allowed-tools: Read, Grep, Glob, Bash(python3 scripts/search.py *)
---
Answer the question below using the `answer-from-kb` skill. Delegate corpus search to the
`retriever` subagent so raw transcripts stay out of this context, then have `synthesizer`
write the final cited answer.

Question: $ARGUMENTS
```

**ONE example skill — `.claude/skills/answer-from-kb/SKILL.md`** (fat procedure; body < 500 lines; both `name` and `description` are **required**):
```markdown
---
name: answer-from-kb
description: Retrieves from the YC YouTube knowledge base and writes a grounded, cited answer. Use when the user asks any startup question — fundraising, product-market fit, pricing, hiring, enterprise/B2B sales, growth, retention, YC application, founder psychology — or references a YC talk, partner (Paul Graham, Michael Seibel, Dalton Caldwell), or series (Startup School, Lightcone).
allowed-tools: Read, Grep, Glob, Bash(python3 scripts/search.py *)
---
# Answer from the YC knowledge base (brain-first retrieval)

Standing procedure (apply every time this skill is active):
1. Read `kb/INDEX.md` to shortlist series/topic pages.
2. Expand the question into keywords/synonyms; grep compiled pages:
   `rg -i -l '<kw1|kw2|kw3>' kb/ -g '*.md'` then `rg -i -C 3 '<kws>' <shortlisted files>`.
3. Read ONLY the shortlisted `kb/topics/*` and `kb/talks/*` pages. Follow See-also wikilinks.
4. If two pages give conflicting advice, present BOTH with citations (see find-contradictions).
5. Write the answer. Every claim ends with `[slug @ mm:ss]` linking to youtu.be/<id>?t=<sec>.
   Timestamp→seconds and citation rules: see reference/citation-format.md.
6. If the corpus lacks the answer, say so and name the gap — never use pretraining knowledge.

Reference (load on demand):
- reference/retrieval-playbook.md   — query expansion + rg recipes
- reference/citation-format.md      — [slug @ mm:ss] syntax + ?t= math
- reference/frontmatter-schema.md   — field meanings
```

**ONE example subagent — `.claude/agents/retriever.md`** (isolated context; keeps transcript bytes out of the main window):
```markdown
---
name: retriever
description: Read-only corpus searcher. Greps kb/ and returns cited snippets only.
tools: Read, Grep, Glob, Bash
model: sonnet
---
You search the yc-base knowledge base and RETURN EVIDENCE, never a final answer.
Given a question: read kb/INDEX.md, expand keywords, `rg -i -C 3` the shortlisted pages,
and return a compact list of {claim, quote, slug, timestamp, youtu.be?t= url, page-path}.
Include contradictory evidence if present. Do NOT include raw transcript dumps. Do NOT
answer the user's question — only the synthesizer does that.
```
*(companion `synthesizer.md`: takes the retriever's evidence list and writes the grounded, cited prose answer, adding nothing not present in the evidence.)*

**Trace — "How do we sell to enterprise customers when the buyer keeps stalling?"**
1. User runs `/ask How do we sell to enterprise customers when the buyer keeps stalling?` → `ask.md` invokes `answer-from-kb` and dispatches the **retriever** subagent (fresh context; only the question string crosses in).
2. Retriever reads `kb/INDEX.md`, expands the query → `enterprise|B2B|champion|stall|urgency|compelling event|procurement|pilot|POC`.
3. `rg -i -l` routes to `kb/topics/enterprise-sales.md`, `kb/topics/pricing.md`, `kb/talks/how-to-sell-to-enterprise.md`, and (via wikilink) `kb/topics/do-things-that-dont-scale.md`.
4. `rg -i -C 3` on those pages surfaces the Compiled-Truth thesis + Timeline entries; retriever returns evidence: *"Manufacture a compelling event / deadline to break stalls"* `[how-to-sell-to-enterprise @ 12:30]`, *"A stall usually means no internal champion — find and arm one"* `[lightcone-ep-42 @ 08:05]`, plus a **noted contradiction** (one partner favors land-and-expand small pilots; another favors top-down urgency).
5. `graph.json` edge `tactic:manufacture-compelling-event --solves--> problem:buyer-stalling` confirms the mapping; retriever returns the evidence list — **no raw transcript enters the main context**.
6. **Synthesizer** writes: a stalling enterprise buyer almost always signals *no urgency and no internal champion*; (a) identify and arm a champion to sell internally `[how-to-sell-to-enterprise @ 12:30](https://youtu.be/dQw4w9WgXcQ?t=750)`; (b) manufacture a compelling event/deadline `[lightcone-ep-42 @ 08:05](https://youtu.be/XXXX?t=485)`; and notes the partner split on pilot-led vs urgency-led approaches as **data, with both citations**. Every claim carries a live deep-link; if a facet were uncovered, it would say so rather than inventing.

---

## D) Phased Rollout (pipeline takes a video/playlist list as input → scales)

The whole pipeline is driven by `scripts/videos.txt` / `scripts/playlists.txt`, so scaling = appending IDs and rerunning (`--download-archive` skips done work). Process **one video at a time** through ingest for graph coherence.

**Phase 0 — Scaffold (day 1).** `git init`; create the tree in §B; write `CLAUDE.md`, `RESOLVER.md`, the four `README.md` resolvers, `.claude/rules/*`, the `/ask` command, `answer-from-kb` skill, `retriever`/`synthesizer` agents, and `settings.json` (pre-allow `rg`, `python3 scripts/*`, read paths). *Milestone: `/ask` returns "corpus empty" cleanly.*

**Phase 1 — MVP on a curated high-signal subset.** Seed `playlists.txt` with **Startup School**, **Lightcone**, **How to Start a Startup** (Sam Altman's Stanford series), **Dalton & Michael**, and **key founder talks/office hours**. Run Acquisition → clean → ingest → synthesize the top ~10 `kb/topics/` (PMF, pricing, enterprise sales, hiring, fundraising, do-things-that-don't-scale, default-alive, growth, YC application, founder psychology). *Milestones:* (1) captions pulled for the subset (~150–300 videos); (2) `data/catalog.json` built; (3) 10 topic pages + entity pages for core partners/companies; (4) `validate.py` green (every file has non-empty `type`; every video has `resource`; no broken wikilinks; no dead citations); (5) golden-set eval passes (below).

**Phase 2 — Full channel.** Append the full `videos.txt` (all tabs), run the incremental backfill over several days (respecting the 20 GB/day + 429 limits), then batch `/ingest-video` (still one at a time) and re-run `/synthesize-topic` to fold new evidence into existing pages. Add `kb/series/` landing pages and tier `kb/INDEX.md` per series. *Milestones:* whole channel in `archive.txt`; `INDEX.md` tiered; `graph.json` rebuilt; contradiction sweep run.

**Phase 3 — Keep-fresh + optional scale-outs.** A `/ingest-new-videos` batch skill (replacing gbrain's cron-enrichment idea — there are no live signals, only new uploads) reruns yt-dlp with `--download-archive` on a cadence you choose and PRs the new pages for human review before merge. *Only if* grep proves insufficient at full scale: add a derived embeddings index (hybrid recall) and/or `graph.json → cypher` export for true multi-hop traversal — both remain rebuildable caches.

---

## E) Cost & Time Estimates + Risks/Gotchas (each with a mitigation)

**Cost & time (planning anchor ~2,000 videos / ~1,000 hrs; hedge on exact hours):**

| Item | Time | Cost |
|---|---|---|
| Acquisition (text-only, captions + metadata) | ~2–4 evenings, paced under 20 GB/day/IP | **$0** |
| Transcription — captions default | included above | **$0**, no GPU |
| Transcription — Whisper backfill (~5–10% of videos, ~50–100 hrs) | real-time–70× RT depending on variant/GPU | **~$0** self-host GPU rental; **~$2–4 Groq** / **~$18–36 OpenAI** |
| LLM distillation + ingest + synthesis | dominated by wall-clock of batch LLM calls | modest per-token; scales with corpus, one-time |
| Optional GraphRAG-style full index (only if added) | one-time batch | **~$33** at current model prices (vs 2024 $33k outlier) |
| Retrieval at query time | seconds | grep = ~$0; Citations `cited_text` is free on output |

*Bottom line: a full-channel build is dollars, not thousands — the value is the one-time synthesis labor, not compute.*

**Risks / gotchas + mitigations:**

- **ToS / legal gray area.** YouTube Terms disallow bulk download; captions are copyrighted. *Mitigation:* pull **text not video** (`--skip-download`), rate-limit, keep `resource:` URLs for attribution, treat as personal/internal research, never redistribute raw media.
- **Rate limits / IP bans (403 after ~20 GB/day, 429 at scale).** *Mitigation:* text-only stays under the cap; `--sleep-requests/--sleep-interval`; residential IP; spread backfill across days via `--download-archive`; cookies only as a last resort (account risk).
- **ASR errors & Whisper silence-hallucination.** ~8–12% real-world WER; entity/number tokens can hit 50–70% error; large-v3 repeats on silence. *Mitigation:* captions-first; LLM cleaning pass with a **startup-proper-noun glossary**; `<!-- SUSPECT -->` flags on silence segments; de-repetition dedup; `confidence:` frontmatter drops to `medium/low` for heavy-ASR videos.
- **Dedup of repeated advice ("talk to users" said 200×).** *Mitigation:* MECE + resolvers → one canonical `kb/topics/` page many talks *cite*, not N copies; `aliases:` merges person/company split-brains; the two-layer Timeline accumulates sources under one Compiled Truth.
- **Staleness (advice tied to a market/era, e.g. 2013 fundraising norms).** *Mitigation:* preserve temporal qualifiers (`upload_date`, YC batch) verbatim; CLAUDE.md rule 5; Timeline is dated + reverse-chron so "current" reads top; `evolves-from` edges trace how advice changed.
- **Hallucination / invented citations.** *Mitigation:* hard rules — search-before-answer, cite-or-drop, **explicit abstention** ("if not in corpus, say so; never use pretraining knowledge"); retriever/synthesizer split keeps answers to retrieved evidence; programmatic path uses the **Citations API** (custom-content blocks → structurally valid pointers); `validate.py` fails on any citation whose timestamp doesn't resolve to a real segment.
- **Split-brain / MECE drift as the graph grows.** *Mitigation:* `RESOLVER.md` read before any page creation; one primary home per fact; `validate.py` flags orphan pages and broken wikilinks in CI/pre-commit.
- **Derived-cache desync (`catalog.json`, `graph.json`, embeddings).** *Mitigation:* they are *never canonical* — one `scripts/build_*.py` command rebuilds them from the markdown; "we do not back up the cache," we rebuild it.
- **Context bloat at full scale (corpus ≫ 500 docs, ≫ 100–300k tokens).** *Mitigation:* progressive disclosure — tiered `INDEX.md`, thin `CLAUDE.md` (< 200 lines), fat skills that load on demand, retriever subagent isolation, and grep-then-read (never dump). Add embeddings only if grep genuinely misses oblique references.

**Evaluation gate (run on every prompt/CLAUDE.md/skill change):** maintain a golden set of ~30–50 real questions (incl. "selling to enterprise when the buyer stalls") with hand-labeled expected source videos; score with **Ragas Faithfulness** (supported-claims/total-claims) and **Context Recall**, gate at e.g. faithfulness ≥ 0.9, recall ≥ 0.8; **mechanically verify every returned timestamp resolves to a real segment** in the cited file (invented pointer = automatic fail).