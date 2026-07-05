#!/usr/bin/env python3
"""
search.py — offline, stdlib-only keyword retrieval over kb/. A deterministic complement to ripgrep
that ranks pages and shows [mm:ss] context. Used by the answer-from-kb skill / retriever subagent.

    python3 scripts/search.py index                        # what's in the KB, grouped by type
    python3 scripts/search.py search "how to price a B2B product"   # ranked pages + snippets
    python3 scripts/search.py read kb/topics/pricing.md    # print a page
"""
import sys, os, re
from collections import defaultdict
from kblib import iter_pages, parse_frontmatter

STOP = set("the a an and or of to in on for with is are be how do we i you it that this "
           "what when why can should our your their my his her they them as at by from".split())
TS_RE = re.compile(r'\[\d{1,2}:\d{2}(?::\d{2})?\]')


def tokens(q):
    return [w for w in re.findall(r'[a-z0-9]+', q.lower()) if w not in STOP and len(w) > 1]


def cmd_index():
    groups = defaultdict(list)
    for path, fm, _ in iter_pages():
        groups[fm.get("type", "untyped")].append((fm.get("title") or os.path.basename(path),
                                                   os.path.relpath(path)))
    if not any(groups.values()):
        print("KB is empty — no pages yet. Run acquisition + ingest (see README).")
        return 0
    for t in sorted(groups):
        print(f"\n== {t} ({len(groups[t])}) ==")
        for title, path in sorted(groups[t]):
            print(f"  {title}  —  {path}")
    return 0


def cmd_search(query):
    toks = tokens(query)
    if not toks:
        print("Empty query after stopword removal.")
        return 1
    scored = []
    for path, fm, body in iter_pages():
        hay = body.lower()
        score = sum(hay.count(t) for t in toks)
        # weight topic pages and title/tag hits
        title = (fm.get("title", "") + " " + " ".join(fm.get("tags", []) or [])).lower()
        score += 3 * sum(title.count(t) for t in toks)
        if fm.get("type") == "concept":
            score = int(score * 1.3)
        if score:
            scored.append((score, path, fm, body))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print(f"No matches for: {query}")
        return 0
    print(f"Query: {query}\nTokens: {' '.join(toks)}\nTop {min(8, len(scored))} of {len(scored)} matching pages:\n")
    for score, path, fm, body in scored[:8]:
        print(f"[{score:>4}] {os.path.relpath(path)}  ({fm.get('type','?')})")
        # show up to 2 matching lines, preferring lines that carry a [mm:ss] marker
        lines = [ln.strip() for ln in body.split('\n') if any(t in ln.lower() for t in toks)]
        lines.sort(key=lambda ln: (0 if TS_RE.search(ln) else 1, len(ln)))
        for ln in lines[:2]:
            print(f"        … {ln[:160]}")
        print()
    return 0


def cmd_read(path):
    if not os.path.exists(path):
        print(f"Not found: {path}")
        return 1
    with open(path, encoding='utf-8') as f:
        print(f.read())
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    cmd = argv[0]
    if cmd == "index":
        return cmd_index()
    if cmd == "search":
        return cmd_search(" ".join(argv[1:]))
    if cmd == "read":
        return cmd_read(argv[1]) if len(argv) > 1 else 1
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
