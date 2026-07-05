# Newest approaches to building an LLM-queryable knowledge base

**Scope:** how to build a knowledge base from the *entire* Y Combinator YouTube channel (~2,000 uploads, ~1,000+ hours; estimates in the source material range from ~300h to ~2,000h — treat total runtime as unknown until you enumerate it) and query it from a **file-over-app Claude Code repo** (`.claude/` + `CLAUDE.md`). Every section ends with an opinionated recommendation. Claims the verification pass refuted or left uncertain are flagged inline with **⚠**.

---

## 0. Executive recommendation (the stack I would build)

1. **Acquisition:** `yt-dlp --skip-download` to pull existing captions + metadata for ~$0 first; only Whisper-backfill the videos that lack captions.
2. **System of record:** git-tracked Markdown + YAML frontmatter, one file per video. No database is canonical; any index is a derived, rebuildable cache.
3. **Structure:** an OKF-style bundle (`videos/` + `concepts/` + per-directory `index.md`) with **pre-computed synthesis pages** (the gbrain/Karpathy move), cross-linked with relative Markdown links.
4. **Retrieval:** a Claude Code **Skill** that greps an `index.md` map, reads only the shortlisted files, and answers with citations — via a **read-only forked subagent** so raw transcript text never enters the main context. No vector DB at launch.
5. **Grounding/eval:** citation-enforced prompting (`video_id @ mm:ss`), an abstention rule, and a Ragas Faithfulness / Context-Recall gate over a hand-labeled golden set. Use the **Anthropic Citations API** for the programmatic query path.

The one-line thesis: **copy the discipline (git = truth, MECE directories + resolvers, pre-computed two-layer pages, thin `CLAUDE.md` + fat skills, latent/deterministic split, hard citation rules) and skip the infrastructure (vector DBs, queues, crons, graph engines) until corpus size forces your hand.**

---

## 1. The file-over-app / repo-as-knowledge-base paradigm, and how `.claude/` makes a repo promptable

### 1.1 Why files, not an app

The durability argument is Steph Ango's (Obsidian's CEO): *"The files you create are more important than the tools you use to create them. Apps are ephemeral, but your files have a chance to last"* — [File over app](https://stephango.com/file-over-app). For a KB this is not nostalgia; it is an engineering property. Plain Markdown + git is **greppable, diffable, version-controlled, and directly LLM-promptable** without a query engine, and it survives any tool migration. That is exactly the substrate Claude Code reads natively.

The complementary idea is Karpathy's reframing of the problem as **context engineering** — *"the delicate art and science of filling the context window"* rather than prompt-writing ([Karpathy, "+1 for context engineering over prompt engineering"](https://x.com/karpathy/status/1937902205765607626)). The value of a well-structured file KB is that it lets Claude Code pull only the relevant pages into context instead of dumping 2,000 raw transcripts, keeping every query token-cheap.

### 1.2 How the `.claude/` folder + `CLAUDE.md` turn a repo into a promptable KB

Claude Code's mechanism is **progressive disclosure via the filesystem**, with three concrete cost tiers ([Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), [Extend Claude with skills](https://code.claude.com/docs/en/skills)):

- **L1 — always in context:** only the `name` + `description` metadata of every skill is preloaded into the system prompt at startup.
- **L2 — on match/invoke:** the `SKILL.md` body loads only when Claude matches the description or you type `/name`.
- **L3 — on demand:** files linked from `SKILL.md` are read only when needed.

So a large retrieval procedure plus reference docs cost ~0 tokens until a YC query fires.

**The pieces and what each is for:**

- **`CLAUDE.md` — facts, not procedures.** Corpus map, frontmatter schema, citation format, the hard rules. Keep it **under ~200 lines**: every line loads every session and persists through compaction ([Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)). Claude merges `CLAUDE.md` from home + project + subdirectories, more-specific overriding broader.

- **Skills (`.claude/skills/<name>/SKILL.md`) — how-to procedures.** A skill is a directory with a required `SKILL.md` (YAML frontmatter + Markdown body); **the directory name becomes the slash command** (`.claude/skills/answer/SKILL.md` → `/answer`). Scopes with exact precedence enterprise > personal > project: personal `~/.claude/skills/…`, project `.claude/skills/…` (commit this), plugin, enterprise. Keep the body **under 500 lines**; push detail into `reference/*.md` files kept **exactly one level deep** (Claude may only `head -100` files referenced from other referenced files, so nested references produce incomplete reads). Give any reference file over 100 lines a table-of-contents header. **Domain-partitioned reference** is the documented multi-domain KB pattern: `SKILL.md` is a navigation index pointing at `reference/<domain>.md`, so a query about one domain loads only that file.

  > **⚠ Flag — refuted claim (corrected here).** An earlier note in the source material said "only `description` is required, and if omitted the first paragraph of the body is used." The verification pass **refuted** this. Per [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): **both `name` and `description` are required frontmatter fields**, and **there is no documented "first paragraph fallback."** The other validation rules stand: `name` ≤ 64 chars, lowercase/numbers/hyphens only, no XML tags, cannot contain "anthropic"/"claude"; `description` non-empty, ≤ 1024 chars, no XML tags. Author both fields explicitly.

- **The `description` is the load-bearing field.** Auto-invocation is model-driven off it: write it in **third person with concrete trigger phrases** ("Use when the user asks about fundraising, pricing, hiring, PMF, YC applications, or names a founder/company/batch"), not marketing copy — it is how Claude picks among 100+ skills. The combined `description` + `when_to_use` is **truncated at 1,536 characters** in the listing, so front-load the key use case.

- **Commands vs skills have merged.** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both produce `/deploy`, but **skills are the recommended form** — only they support a supporting-files directory, auto-invocation, and `context: fork`.

- **Subagents — context isolation.** A subagent (`.claude/agents/*.md`) gets a **fresh context window with no parent history**; the only input is the Agent tool's prompt string, and the parent receives the subagent's final message verbatim ([How and when to use subagents](https://claude.com/blog/subagents-in-claude-code)). **This is the key trick for a 2,000-file corpus:** the retrieval subagent greps/reads dozens of transcripts and returns a synthesized cited summary, so raw transcript text never pollutes the main conversation. A skill can itself run in a subagent via `context: fork` + `agent:` — and using the built-in `agent: Explore` skips `CLAUDE.md` and git status, ideal for a read-only corpus search that shouldn't drag in repo conventions. Pre-grant `allowed-tools: Read Grep Glob` so the search skill never triggers permission prompts.

- **Rules and hooks.** Path-scoped `rules` use `paths:` glob frontmatter to load constraints only for matching files; deterministic "always do X" automation belongs in **hooks** (they run in the harness, bypass compaction, cost few tokens), not in `CLAUDE.md` prose.

- **MCP — reserve for external systems.** Anthropic's own division is: *Skills for how-to, MCP for access to external systems, Subagents for delegating to a specialist with its own context* ([Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)). **A local text corpus needs no MCP** — the built-in Grep (ripgrep) + Glob + Read tools are the retrieval engine.

**Lifecycle gotchas that bite a KB:** once a skill loads, its rendered body **stays in context for the rest of the session** (recurring token cost → keep it lean, write standing instructions not one-time steps). After auto-compaction, only the **first 5,000 tokens** of each re-attached skill survive, sharing a **25,000-token budget** filled most-recent-first — so keep the `SKILL.md` index short and stable and put bulk in reference files that are re-read fresh. `allowed-tools` in a project skill only takes effect after you accept the workspace-trust dialog, so **review checked-in skills before trusting the repo.**

> **Recommendation.** One project skill `.claude/skills/yc-transcripts/SKILL.md` acting as a navigation index over a `reference/` (or the `videos/`+`concepts/` trees), plus a `/answer` skill that runs in a **forked `Explore` subagent** with `allowed-tools: Read Grep Glob`. `CLAUDE.md` holds only the corpus map, frontmatter schema, citation format, and ~10 hard rules. Bundle a stdlib-only `scripts/search.py` referenced as `${CLAUDE_SKILL_DIR}/scripts/search.py` and pre-approved with `allowed-tools: Bash(python3 *)` so search runs without loading its source into context, and works on both claude.ai and the API (no network).

---

## 2. The three referenced approaches: what to borrow, what to avoid

### 2.1 Karpathy's "LLM Wiki" (context-engineering pattern)

**What it is.** Point an LLM at raw sources and have it incrementally build and maintain an interlinked Markdown wiki — **pre-computing synthesis into pages** instead of re-deriving answers from scratch each query like classic RAG. The canonical layout (from community implementations like [second-brain](https://github.com/NicholasSpisak/second-brain), [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian), and the [starmorph write-up](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide)):

```
raw/            # immutable source transcripts — the agent NEVER edits these
wiki/
  index.md      # master catalog, read FIRST to navigate (not the whole corpus)
  log.md        # append-only chronological record of every ingest/update
  sources/      # one summary per source
  concepts/     # cross-cutting evergreen topics
  entities/     # people, companies
outputs/        # query answers, lint reports
CLAUDE.md       # schema, page templates, the 3 operations
```

Three operations: **Ingest** (summarize source → cascade updates to related pages → update `index.md` → append `log.md`), **Query** (search `index.md` → read relevant pages → synthesize with `[[wikilink]]` citations), **Lint** (scan for contradictions, orphans, stale claims). Every page carries YAML frontmatter (`title`, `type`, `sources`, `related`, `created`, `updated`, `confidence`); filenames are kebab-case; cross-refs are `[[wikilinks]]`.

**Borrow:** the raw/derived split, the three operations, `index.md` as the read-first catalog, `log.md` as an audit trail, "one source touches 10–15 wiki pages so process **one video at a time**," and git as the versioned source of truth.

**Avoid / respect the ceiling:** the pattern **degrades beyond ~200K–300K tokens** of active wiki context and works best sub-100K; *"for millions of documents, RAG is more appropriate"* ([starmorph](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide)). A 2,000-video raw corpus is 5–20M tokens and **cannot** be a single-context wiki — which is precisely why the value lives in *pre-computed distilled pages* plus routing, not in loading raw transcripts. Karpathy's own single-topic wiki reached ~100 articles / ~400,000 words with no human writing — an existence proof, not a scale guarantee for raw transcripts.

### 2.2 Garry Tan's `gbrain` (opinionated agent brain)

**What it is.** [garrytan/gbrain](https://github.com/garrytan/gbrain) operationalizes the LLM-wiki pattern with hard discipline. Its central claim: **Markdown + frontmatter in a git repo is the system of record; the database (PGLite/Postgres + pgvector doing hybrid vector+BM25 and a knowledge graph) is a *derived cache* rebuilt from the repo with one command — "we do not back up the database."** Founding principles worth stealing:

- **MECE directories + resolvers.** Every fact has exactly one primary home; every directory ships a `README.md` "resolver" ("what goes here / what does NOT") and there is a top-level `RESOLVER.md` decision tree the agent **must** read before creating any page (a hard rule, not a suggestion). Crucially, **MECE applies to directories, not to reality** — a person can be many things; the resolver picks the primary home and typed backlinks surface the rest. This prevents duplicate *pages* without losing relationships.
- **Two-layer pages.** Above a `---` rule: **Compiled Truth** — an always-rewritten current summary (exec summary → State fields → Open Threads → See Also). Below: an **append-only, reverse-chron Timeline** where each entry is dated and sourced. "Current state?" read top; "what happened?" read bottom.
- **Thin harness, fat skills.** Push judgment *up* into reusable, parameterized Markdown skills (method calls: `TARGET`/`QUESTION`/`DATASET` teaching *how*); push execution *down* into deterministic CLI tooling; keep `CLAUDE.md` a ~200-line orientation/dispatcher (Garry cut his from 20k lines). The anti-pattern is a **fat harness with 40+ MCP tools eating context.**
- **Latent vs deterministic split.** Put synthesis/pattern-matching in the model; put counting, IDs, exact retrieval, and aggregation in deterministic code. *"The classic failure is forcing a deterministic problem into latent space"* → plausible-looking hallucinated results.
- **Contradictions as data, dedup by canonical slug.** Canonical slug = entity identity (filename = identity), `aliases[]` for name variants, a fact store where two facts on the same field become recorded data, not an error.
- **Codify-on-second-use.** Do a task manually 3–10 times, get approval, then codify into a skill: *"If I have to ask you for something twice, you failed."*

**Borrow:** all of the above discipline. It is a near-perfect fit for the file half of this project.

**Avoid (over-engineering for a fixed corpus):** the PGLite/Postgres+pgvector engine, HNSW/BM25/RRF hybrid search, reranking, the embeddings pipeline; the Minions/Postgres job queue, 66 cron enrichment jobs, OAuth, MCP server, trust-boundary and multi-brain federation machinery; the ~90-operation contract-first TS layer. These serve a **live, multi-user, signal-fed product.** A YC transcript KB is a **fixed corpus** — there are no live email/calendar signals, so `gbrain`'s "enrichment fires on every signal" principle doesn't apply; replace it with a batch `/ingest-new-videos` skill re-run when new videos drop.

### 2.3 Google's Open Knowledge Format (OKF v0.1)

**What it is.** A vendor-neutral, minimally-opinionated open standard for curated knowledge as a **bundle** — *"just files, just Markdown, just YAML frontmatter,"* no SDK, no runtime, no database ([OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)). Precisely:

- A bundle is a root directory of `.md` files; **the file path (minus `.md`) is the concept's ID** (`videos/how-to-talk-to-users`, `concepts/product-market-fit`).
- Every non-reserved file **must** begin with YAML frontmatter containing a **non-empty `type`** — the *only* hard-required field. Recommended optional fields: `title`, `description`, `resource` (a URI to the source — for transcripts, **the YouTube URL = your built-in citation**), `tags`, `timestamp`. Producers may add arbitrary keys.
- **Relationships are ordinary relative Markdown links inside the body**; the relationship *type* lives in surrounding prose, not the link. Links are bundle-absolute `[t](/path.md)` or relative `[t](./path.md)`.
- Reserved files: `index.md` (a no-frontmatter directory listing for progressive disclosure) and `log.md` (date-grouped changelog). Version declared via `okf_version: "0.1"` in the root `index.md`.
- **Conformance is exactly three checks:** frontmatter parses, non-empty `type`, reserved files follow structure. Consumers must tolerate missing optional fields, unknown types, broken links.

The ecosystem already proves this exact use case: [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) (an OKF toolkit for Claude Code) and [coleam00/cole-medin-ai-coding](https://github.com/coleam00/cole-medin-ai-coding) — a **real YouTube-transcript bundle** with `videos/` (one page per video) + `concepts/` (cross-cutting themes), a root `index.md`, `log.md`, and an `okf-cli.py` doing keyword search + page reads with **no vector DB.** OKF is explicitly **complementary to `CLAUDE.md`**, not a replacement: OKF holds durable curated knowledge, `CLAUDE.md` holds behavioral rules, agent memory holds ephemeral notes — keep the three separate.

**Borrow:** essentially the whole blueprint — it is purpose-built for this project and a near-exact precedent exists.

**Avoid:** dumping full raw transcripts as the primary body (bloats context, defeats progressive disclosure) — summarize and keep raw text in a sibling file; over-engineering the schema beyond `type`; relying on the folder tree alone (invest in the concept **link graph**); a static HTML graph visualizer (optional — the format + search CLI are what matter).

> **Recommendation.** **Adopt OKF as the on-disk format and gbrain as the discipline layer.** Structure the repo as an OKF bundle: `videos/` (one page per YC video, `type: yc-video`, `resource:` = YouTube URL, `speakers`, `series`, `tags`) and `concepts/` (evergreen topics: PMF, pricing, hiring, fundraising, do-things-that-don't-scale, default-alive, founder-psychology). Apply gbrain's two-layer pages (Compiled Truth above `---`, sourced Timeline below), MECE + `README.md` resolvers + a root `RESOLVER.md`, canonical slugs + `aliases` for dedup (the "PG" vs "Paul Graham" split-brain is a *real* failure mode here), and the codify-on-second-use rule. Keep every raw transcript in a `.raw/` sidecar the agent reads but never edits. This is the file-based half of gbrain plus OKF's proven layout, with none of gbrain's runtime.

---

## 3. Transcription options and tradeoffs (with real numbers)

### 3.1 Do captions first — it is not close

YouTube already ships transcripts. Pull them for **$0, no GPU:**

```bash
yt-dlp --skip-download --write-subs --write-auto-subs \
  --sub-langs en --sub-format vtt --convert-subs srt \
  --write-info-json --download-archive archive.txt \
  -o '%(upload_date>%Y-%m-%d)s_%(id)s_%(title).80s.%(ext)s' <URL>
```

`--skip-download` writes only text + metadata ([yt-dlp README](https://github.com/yt-dlp/yt-dlp)). `--write-subs` = human/creator captions (accurate, punctuated, often absent); `--write-auto-subs` = ASR captions (nearly always present, lowercase-ish, no punctuation). Request **both** and dedupe (manual wins) — there is **no native flag to prefer manual over auto**; the documented workaround is to `--list-subs`, ignore the `en-orig` auto track, and select the specific manual lang code ([issue #9371](https://github.com/yt-dlp/yt-dlp/issues/9371)). Convert to `srt` for clean LLM ingestion; auto-sub VTT carries heavy **rolling/duplicate caption lines** that must be de-duplicated. `--write-info-json` gives `title`, `upload_date`, `duration`, `view_count`, `description`, and `chapters[]` — **chapters are excellent natural chunk boundaries.**

For quick single-video re-fetches, [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) needs no API key, no browser, and its `find_transcript()` is **manual-first natively** (better default caption quality than yt-dlp) — but it can break on YouTube frontend changes and lacks a robust archive mechanism. **Use yt-dlp `--download-archive` for the idempotent bulk build; use youtube-transcript-api for on-demand re-fetch.** Both need Python 3.10+.

**Operational limits:** expect **HTTP 403 after ~20 GB/day/IP** ([Jameson Lopp](https://blog.lopp.net/how-to-archive-transcribe-youtube-videos-bulk/)) and **429/IP-block** at crawl scale ([YouTube Error 429](https://decodo.com/blog/youtube-error-429)). Defend with `--sleep-requests 1`, `--sleep-interval 5 --max-sleep-interval 30`, run from a residential IP not a cloud VM, spread a big playlist across days, and prefer polite pacing over cookies (which tie requests to your account and raise ToS/account risk). **ToS caveat:** YouTube's terms prohibit downloading except via provided features and disallow bulk scraping; captions are copyrighted. Mitigate by pulling *text not video*, rate-limiting, not redistributing, and treating the corpus as personal/internal research.

### 3.2 When you must transcribe: cost and accuracy

**Cost per hour (2025/2026):**

| Option | $/hour | Notes |
|---|---|---|
| YouTube captions (yt-dlp) | **$0** | no GPU; lower quality on jargon |
| Groq `whisper-large-v3-turbo` | **~$0.04** | cheapest hosted; ⚠ see note |
| Deepgram Nova-3 batch | ~$0.22–0.26 | built-in diarization |
| AssemblyAI Universal (async) | ~$0.21 | diarization; 5.6% mean WER |
| OpenAI `gpt-4o-transcribe` / `whisper-1` | ~$0.36 | $0.006/min |
| Self-hosted GPU | ≈ electricity | free once GPU rented |

At **1,000 hours:** ~$360 (OpenAI) vs ~$111 (Groq large-v3) vs ~$0 (captions). At **~300 hours:** ~$108 (OpenAI) vs ~$12 (Groq turbo). ([Coval STT benchmarks](https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/), [Artificial Analysis Whisper index](https://artificialanalysis.ai/speech-to-text/models/whisper))

> **⚠ Uncertain — sources disagree on Groq pricing.** One source cites **~$0.04/hr** (whisper-large-v3-**turbo**, ~124× realtime, ~4.6% WER) and another **~$0.111/hr** (whisper-large-v3). The gap is model tier, not a contradiction — the turbo model is cheaper. Confirm the exact model/endpoint pricing against Groq's current rate card before budgeting; both are far under OpenAI.

**Accuracy (English WER):** Whisper large-v3 is **2.7% on LibriSpeech test-clean, 5.2% test-other, but ~8–12% (avg ~10.3%) on real-world English** — so raw transcripts need cleanup regardless of engine ([novascribe](https://novascribe.ai/how-accurate-is-whisper)). YouTube auto-captions run **~85–95% accurate (~5–15% WER)** and degrade on jargon/accents/crosstalk — worse than large-v3 for dense startup terminology. **Hosting matters more than the model name:** the same large-v3 ranged **4.1% WER (fal.ai) to 10.1% (Replicate)** — benchmark your chosen endpoint, don't assume "large-v3" is a fixed quality.

**Engine tradeoffs** ([Modal: choosing Whisper variants](https://modal.com/blog/choosing-whisper-variants)): all three main open variants use identical weights, so **same audio → same WER; they differ only in speed and features.**
- **`faster-whisper`** (CTranslate2, INT8/FP16) — the safe default; ~4× faster / ~3× smaller than reference Whisper; CPU or GPU (needs CUDA 12 + cuDNN 9). No word timestamps, no diarization.
- **`insanely-fast-whisper`** (Transformers + FlashAttention-2) — ~9× over faster-whisper but needs a high-VRAM NVIDIA GPU.
- **[`WhisperX`](https://github.com/m-bain/whisperX)** — faster-whisper backend + VAD + wav2vec2 forced alignment + pyannote diarization; **70× realtime on large-v2, <8 GB VRAM**; the **only** option giving word-level timestamps *and* speaker labels. Diarization requires a HuggingFace token + accepting the pyannote agreement, or it silently fails.
- **[`distil-large-v3`](https://github.com/huggingface/distil-whisper)** — 756M params (vs 1.54B), **6.3× faster, ~50% smaller, within ~1% WER on long-form**, English-only. Best speed/accuracy pick if you need only English and no diarization.

**Diarization is NOT native to Whisper.** For YC talks (single-speaker keynotes or moderated panels) it's mostly optional — skip it to avoid the pyannote dependency unless you specifically want panel speaker labels. **Timestamp granularity:** vanilla Whisper gives drift-prone segment timestamps; WhisperX's forced alignment gives accurate word-level timestamps — the right choice if you want deep-links to exact YouTube moments (`?t=SECONDS`).

**Throughput anchor:** Whisper `medium` on an RTX 2080Ti does ~5 audio-hours per wall-hour (~5× realtime); GPU is ~50× faster than CPU ([Lopp](https://blog.lopp.net/how-to-archive-transcribe-youtube-videos-bulk/)). At 1,000+ hours, self-hosted large-v3 on a rented 4090 undercuts hosted APIs and is effectively free once rented.

**Known failure to budget for:** large-v3 **hallucinates/repeats on silence and noise** (repeated n-grams) — add a de-repetition/dedup step. And WER on **entities/alphanumerics** (company names, "YC W24", dollar figures, funding rounds) can fall to **50–70%** — add a light LLM cleanup pass and keep a glossary to normalize names.

> **Recommendation.** **Captions-first, Whisper-backfill.** (1) `yt-dlp --skip-download` to pull captions + metadata for the whole channel at ~$0, with `--download-archive` for idempotent re-runs. (2) For the minority of videos lacking usable captions, batch-transcribe with **`faster-whisper large-v3` on a rented GPU** (or **Groq turbo** for zero-setup). (3) Add WhisperX word-timestamps + diarization only for "hero" talks where deep-links or panel labels justify the extra dependency. (4) Store raw `.vtt/.json/.srt` under `.raw/` and a derived, cleaned `.md` per video for search.

---

## 4. Formatting and distillation

### 4.1 Distill; don't dump

The single highest-leverage move — the one that makes the whole KB fast and cheap — is **pre-computing synthesis into pages** so Claude answers from compiled pages, not by re-reading raw transcripts every query. Per-video pages should hold a **curated summary of key ideas + notable quotes with rough timestamps**, not the raw transcript; keep the raw transcript in a sibling `.raw/` file. The atomic-note discipline is what deduplicates YC's most-repeated advice: "talk to users," "do things that don't scale," "default alive" collapse into **one canonical concept page** that many video pages link to, instead of N copies.

**The LLM cleaning pass** should do four things in one prompt (the proven [whisper-obsidian-plugin](https://github.com/nikdanilov/whisper-obsidian-plugin) pattern): fix grammar/ASR errors, remove filler words, format as Markdown, and extract key ideas/action items. It runs against Claude, GPT, or any OpenAI-compatible endpoint (Ollama/LM Studio for cheap local batch over 2,000 videos).

### 4.2 Chunking — only if/when you add an index

If you later add any derived index, chunk deliberately:
- **Baseline:** 256–512 tokens with 10–20% overlap (~50–100 tokens) — the RAG sweet spot ([langcopilot chunking guide](https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide)). But a **NAACL 2025 Findings** study found fixed ~200-word chunks **matched or beat semantic chunking** — semantic chunking's extra embedding cost is often *not* justified ([Firecrawl chunking guide](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)).
- **For transcripts, don't use blind fixed windows.** Chunk by **speaker turn** (or a small sliding window of turns) as the atomic unit, carrying `speaker`, `timestamp`, and `video_id` as metadata.
- **For long talks, chunk by chapter/topic.** An **MDPI Bioengineering (Nov 2025)** clinical study found adaptive chunking to logical topic boundaries hit **87% accuracy vs 13% for fixed-size** — YC talks have natural topic shifts, so use YouTube chapter markers where present.

### 4.3 The page schema

Every page: Markdown + YAML frontmatter. A workable per-video schema:

```yaml
---
type: yc-video
title: "How to Talk to Users — Eric Migicovsky"
video_id: <11-char id>
resource: https://youtu.be/<id>        # OKF citation field — non-negotiable
speakers: [eric-migicovsky]
series: startup-school
published: 2018-11-20
duration: 1512
tags: [user-research, pmf, early-stage]
---
```

Timestamped body lines like `[00:12:34](https://youtu.be/ID?t=754) …` resolve every claim to a deep-link. Concept pages add `type: concept` and a `confidence` field. Cross-link with relative Markdown links (OKF) and/or `[[wikilinks]]` (Karpathy) so both grep and Claude can traverse the graph.

> **Recommendation.** Immutable raw transcripts under `.raw/transcripts/`; a **distilled** per-video page (key ideas + quotes + timestamps, ~1 screen) as the queryable body; canonical **concept pages** that dedupe repeated advice; a read-first `index.md` catalog; `log.md` for ingest history. Encode the schema + the three operations (ingest/query/lint) in `CLAUDE.md`. Process **one video at a time** so cross-links stay coherent, and add a **jargon/entity normalization** step during ingest (feeding a `speakers/` + `companies/` set). Skip chunking entirely until an index proves necessary — a distilled page *is* your chunk.

---

## 5. Knowledge-graph vs vector vs agentic retrieval

### 5.1 The evidence

**Agentic grep is a genuinely strong default.** The [*Is Grep All You Need?*](https://arxiv.org/abs/2605.15184) study found that across multiple harnesses (Claude Code, Codex CLI, Gemini CLI, a custom agent) on a 116-question LongMemEval sample, **grep generally yields higher accuracy than vector/embedding retrieval** — and, importantly, that the **harness and tool-calling style (inline vs file-based results) matter as much as the retrieval algorithm.** Cursor's internal research (via [Morph](https://www.morphllm.com/agentic-search)) found only **+12.5%** from adding semantic search on top of grep — a modest gain a file-over-app KB can forgo. And an **LLM query-expansion step before grep** (`rg -i 'kw1|kw2|kw3'`) **~10×'d** retrieval performance on Natural Questions ([nuss-and-bolts](https://www.nuss-and-bolts.com/p/on-the-lost-nuance-of-grep-vs-semantic)).

Grep's tradeoffs are honest: it needs no index, no chunking, no vector-DB infra, and every retrieval is **auditable** (you see which files were grepped). It **excels at exact/derivable keywords** but misses **oblique references** where the keyword isn't apparent (that's where embeddings' soft matching wins), and its **latency scales linearly** with corpus size — a non-issue at 20–500 files, the reason to reconsider at thousands.

**Vector vs graph splits cleanly by question type** ([*When to use Graphs in RAG*, arXiv 2506.05690](https://arxiv.org/html/2506.05690v3)): **vector wins single-hop/detail** questions; **GraphRAG wins multi-hop and "global sensemaking."** Reported figures elsewhere: GraphRAG ~86% vs vector ~32% on multi-hop, with vector dropping toward 0% at 10+ entities. But graph retrieval **costs ~2.3× latency** for ~+4.5% reasoning-depth on HotpotQA, and vanilla vector answered a benchmark in ~900 tokens where GraphRAG used up to ~331k. Combining vector + graph at the response stage beat the best baseline by **+1.1% / +6.4%** on multi-hop.

**GraphRAG's economics and failure mode.** The famous **$33,000 (early 2024) → $33 (mid-2025), ~1000× drop** in indexing cost came almost entirely from cheaper models, not a better algorithm ([GraphRAG Cost Cliff](https://medium.com/graph-praxis/the-graphrag-cost-cliff-how-33-000-became-33-in-eighteen-months-be1b0fbe37e4)).

> **⚠ Uncertain.** The Cost Cliff article is **paywalled**; the $33,000→$33 headline is confirmed from the preview, but the per-token/model breakdown was **not accessible** and should be re-derived from current pricing before you rely on it.

[Microsoft GraphRAG](https://github.com/microsoft/graphrag) offers `--method standard` (LLM extraction of entities/relationships/community reports — rich but expensive) and `--method fast` (FastGraphRAG: noun-phrase extraction via NLTK + spaCy `en_core_web_md`, co-occurrence relationships, 50–100 token chunks — cheap but noisy) ([Indexing methods](https://microsoft.github.io/graphrag/index/methods/)). And [**LazyGraphRAG**](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) defers community summarization to **query time**, reaching comparable quality at **under ~$5 — ~0.1% of the original cost.** GraphRAG's deeper risk is **silent**: extraction is an LLM judgment call, and wrong calls become "confidently-wrong edges" that traversals treat as ground truth.

### 5.2 OKF as the "poor man's knowledge graph"

You don't need Neo4j to get graph value. OKF's **relative Markdown links form a graph richer than the folder tree**, and it's human-auditable and git-diffable. The one limitation to engineer around: a **bare `[[wikilink]]` carries one bit** ("connected"). For a startup-advice graph you want **typed edges** (`tactic --solves--> problem`, `principle --contradicts--> tactic`, `company --exemplifies--> principle`). Encode the relationship type in **prose around the link** (OKF's model) or in frontmatter — not in a bare wikilink. A proven lightweight ontology to constrain extraction (from `simple-graph-builder`) is a **fixed set of entity types** — adapt to YC as `Problem, Tactic, Principle, Person, Company, Stage, Metric`. The same vault can later export to `graph.json` / `graphml` / `cypher.txt`, so you can defer FalkorDB/Neo4j until query complexity actually demands traversal.

### 5.3 Sizing this corpus

The index-file / no-vector sweet spot is **20–500 documents**; past ~500, go **tiered** (root `index.md` → per-category sub-indexes) rather than adding a vector DB ([MindStudio](https://www.mindstudio.ai/blog/llm-knowledge-base-index-file-no-vector-search)). At **~2,000 videos you exceed the flat-index sweet spot but stay well within tiered-index territory** — and staleness is asymmetric: an **append-only channel** that keeps growing punishes embeddings (re-index on every change) but not grep-over-files ([nuss-and-bolts](https://www.nuss-and-bolts.com/p/on-the-lost-nuance-of-grep-vs-semantic)).

> **Recommendation.** **Default to agentic grep + a tiered `index.md` map + a subagent, with no vector DB and no graph engine at launch.** Concretely: (1) a generated root `index.md` grouping videos by category with distinct 1–3 sentence summaries, pointing to per-category sub-indexes; (2) `/answer` does **LLM query-expansion → `rg -i 'kw1|kw2|…' -l -g '**/*.md'`** to shortlist files → reads only those → synthesizes with citations, all inside a **forked `Explore` subagent**; (3) get most of the graph value for free from **OKF typed prose-links + concept pages** — this is where cross-video synthesis ("how did advice on pricing evolve across founders/years") lives. **Add a graph or vectors only on evidence:** embeddings if grep provably misses oblique queries (keep them a *derived, optional recall booster*, never the source of truth); LazyGraphRAG (not full standard GraphRAG) if you find you genuinely need multi-hop global sensemaking. Never stand up standard Microsoft GraphRAG for this corpus — the cost/latency/confidently-wrong-edge risk isn't justified when most queries are topical lookups.

---

## 6. Prompting, grounding, citation, and evaluation

### 6.1 Two grounding paths

**Path A — Claude Code, file-native.** `CLAUDE.md` is the contract: answer **only from files**, cite the file (`video_id @ mm:ss` + the frontmatter `resource` URL), and abstain if the corpus lacks the answer. Citations resolve to YouTube deep-links via per-segment timestamps. This is auditable but the *validity* of a citation is on you to check.

**Path B — Anthropic Citations API** (for a programmatic query service). It returns three location types with exact fields ([Citations API](https://platform.claude.com/docs/en/build-with-claude/citations)): `char_location` (0-indexed, exclusive end), `page_location` (1-indexed pages), and `content_block_location` (0-indexed block indices). **Key design fit:** put each timestamped transcript **segment as one block in a *custom-content* document** — custom content is **not re-chunked**, so a returned `content_block_location` maps **1:1 back to a segment/timestamp.** Put the timestamp + speaker + URL in the document `context` field. Critical rules and numbers:
- Enable per-document with `"citations": {"enabled": true}`; must be **all documents or none** (mixing → error).
- `cited_text` **does not count toward output tokens** (nor input tokens when passed back) — quote-heavy grounded answers are cheap; enabling citations adds slight input overhead.
- Built-in citations reportedly raise **recall accuracy by up to 15%** vs custom prompt-based citation ([Introducing Citations](https://claude.com/blog/introducing-citations-api)).
- **Hard constraint:** citations are **incompatible with structured outputs** — setting `output_config.format` alongside citations returns a **400**. If you need both grounded citations *and* JSON, run **two passes** or post-process the cited blocks into JSON yourself.
- All active models support citations **except Claude Haiku 3**; docs example uses `claude-opus-4-8`. **`.md`/`.txt` files are NOT accepted as document blocks** — convert to plain text and pass inline. Cache stable transcripts with `cache_control: {type: ephemeral}`.

### 6.2 Anti-hallucination prompt rules that measurably help

(a) **Citation-enforced extraction** — every claim must carry a source id (`video_id` + timestamp) or be dropped, turning the model into a verifiable extractor; (b) an explicit **abstention rule** ("if the corpus doesn't contain it, say so — never use pretraining knowledge"); (c) **preserve temporal qualifiers/version numbers** from the source to avoid "citation-shaped hallucinations"; (d) **sub-sentence citations** — tie each assertion, not a whole paragraph, to its span. Bake these into `CLAUDE.md` as hard rules.

### 6.3 Evaluation

Use **Ragas** ([available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)), splitting retrieval from generation so a bad answer is diagnosable:
- **Faithfulness** = (claims supported by retrieved context) / (total claims), 0–1, by decomposing the answer into atomic claims and verifying each ([Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)). Ragas v0.1.14 (Aug 2024) added **Vectara HHEM-2.1-Open** as a faster classifier-based backend to avoid per-eval LLM cost.
- **Answer/Response Relevancy** (needs no gold answers), **Context Precision**, **Context Recall** (needs a labeled reference set).

Maintain a **golden set of ~30–50 real business questions** ("selling to enterprise when the buyer stalls," "when to raise vs stay default-alive") with hand-labeled expected source videos. On every `CLAUDE.md`/prompt change, run Faithfulness + Context Recall and **gate on thresholds (e.g. faithfulness ≥ 0.9, context recall ≥ 0.8).** And **verify citations mechanically**: every returned `video_id`+timestamp must resolve to an existing segment in the cited file — invented pointers are an automatic fail. The Citations API guarantees this structurally; a grep-based file answer does **not**, so a citation-resolution check is mandatory on Path A. Ragas Faithfulness (aggregate grounding at eval time) and the Citations feature (per-claim pointers at answer time) are complementary — you can even reuse citation coverage as a Faithfulness proxy signal.

> **Recommendation.** **`CLAUDE.md` hard rules: cite-or-drop, abstain-when-absent, preserve temporal qualifiers, sub-sentence citations.** For interactive use, Path A (Claude Code, file-native) with a mechanical citation-resolution linter. For a programmatic service, Path B (Citations API with **custom-content documents, one block per timestamped segment**, `claude-opus-4-8`, ephemeral caching) — and remember it can't co-emit citations and structured JSON in one call, so split those passes. Gate every KB change through a Ragas golden-set run with faithfulness ≥ 0.9 / context-recall ≥ 0.8, plus a dead-citation check.

---

## 7. Consolidated flags (verification pass)

- **⚠ Refuted (corrected above, §1.2):** "only `description` is required; missing description falls back to the body's first paragraph." **Both `name` and `description` are required; no first-paragraph fallback exists.** Everything else in that validation rule (char limits, allowed characters, reserved-word ban) stands.
- **⚠ Uncertain (§3.2):** Groq Whisper price is quoted at **both ~$0.04/hr and ~$0.111/hr** across sources — the difference is turbo vs large-v3; confirm model/endpoint before budgeting.
- **⚠ Uncertain (§5.1):** the GraphRAG **$33,000→$33** figure comes from a **paywalled** article; the headline is confirmed but the per-model breakdown was not accessible — re-derive from current pricing.
- **Note:** the arXiv identifiers as given — *Is Grep All You Need?* (`2605.15184`) and *When to use Graphs in RAG* (`2506.05690`) — are reproduced from the source material; verify the exact IDs against arXiv before formal citation.

---

## Appendix: the concrete repo I'd scaffold

```
yc-kb/
  CLAUDE.md                     # <200 lines: corpus map, frontmatter schema,
                                #   citation format, hard rules, load-on-demand ref map
  RESOLVER.md                   # gbrain-style: which dir a new page belongs in
  index.md                      # OKF root: okf_version, category listing (read-first)
  log.md                        # ingest changelog
  .raw/transcripts/<id>.srt     # immutable; agent reads, never edits
  videos/
    index.md
    <slug>.md                   # type: yc-video, resource=URL, distilled body
  concepts/
    index.md
    product-market-fit.md       # canonical, dedupes repeated advice
    pricing.md  hiring.md  fundraising.md  ...
  speakers/  companies/  series/
  .claude/
    skills/
      yc-transcripts/SKILL.md   # navigation index over the bundle
        scripts/search.py       # stdlib-only grep+read CLI
      ingest-video/SKILL.md     # transcript -> distilled page + concept updates
      synthesize-concept/SKILL.md
      answer/SKILL.md           # context:fork, agent:Explore, allowed-tools: Read Grep Glob
      lint/SKILL.md             # broken links, orphans, contradictions, dead citations
    rules/citations.md          # paths-scoped grounding rules
```

Build in this order: (1) captions/metadata acquisition; (2) distillation into `videos/` pages; (3) `index.md` + concept synthesis; (4) the `/answer` subagent; (5) the Ragas golden-set gate. Add embeddings or a graph engine **only** when a measured retrieval miss proves grep + typed links + tiered index insufficient — keeping any such index a **derived, rebuildable cache**, never the source of truth.