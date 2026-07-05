#!/usr/bin/env python3
"""
build_index.py — regenerate kb/INDEX.md (the read-first navigation map) from the kb/ pages.
Deterministic, stdlib only, offline. A tiered map: topics (with talk counts) + people + per-series
talk counts — NOT a full 600-line listing (browse talks via search/grep).

    python3 scripts/build_index.py
"""
import glob, re, os
from collections import Counter
from kblib import iter_pages, parse_frontmatter

OUT = "kb/INDEX.md"


def main():
    topics, people, talks = [], [], []
    topic_counts = Counter()
    series_counts = Counter()

    for path, fm, body in iter_pages():
        t = fm.get("type")
        slug = fm.get("slug") or os.path.splitext(os.path.basename(path))[0]
        title = fm.get("title", slug)
        if t == "concept":
            topics.append((slug, title))
        elif t == "person":
            people.append((slug, title))
        elif t == "yc-video":
            talks.append((slug, title, fm.get("series", "talks")))
            series_counts[fm.get("series", "talks")] += 1
            for tp in fm.get("topics", []) or []:
                topic_counts[tp] += 1

    lines = [
        "# yc-base — INDEX (read me first)",
        "",
        "The read-first navigation map of the knowledge base. Topics and people are the synthesis",
        "layer; browse individual talks with `python3 scripts/search.py search \"<query>\"` or ripgrep.",
        "",
        f"> **{len(talks)} talks · {len(topics)} topics · {len(people)} people.** "
        "Ask a question with `/ask` (routes here, greps compiled pages, answers with video+timestamp citations).",
        "",
        "## Topics (cross-cutting synthesis)",
        "",
    ]
    for slug, title in sorted(topics, key=lambda x: -topic_counts.get(x[0], 0)):
        n = topic_counts.get(slug, 0)
        lines.append(f"- [[{slug}]] — {title}  ({n} talks)")

    lines += ["", "## People", ""]
    for slug, title in sorted(people, key=lambda x: x[1].lower()):
        lines.append(f"- [[{slug}]] — {title}")

    lines += ["", "## Talks by series", ""]
    for series, n in series_counts.most_common():
        lines.append(f"- **{series}** — {n} talks")

    lines += ["", "## How to query", "",
              "Open Claude Code in this repo and run `/ask <your question>`. The answer-from-kb skill",
              "routes through this index, greps the compiled pages, and answers **grounded only in the",
              "corpus, cited to video + timestamp**.", ""]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {OUT}: {len(talks)} talks, {len(topics)} topics, {len(people)} people.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
