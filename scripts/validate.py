#!/usr/bin/env python3
"""
validate.py — integrity checks for the knowledge base. Stdlib only, offline. Exit 1 on errors.

Checks (errors):
  - every kb/ content page has frontmatter with a non-empty `type`
  - every talk (type: yc-video) has a `resource` URL
Checks (warnings):
  - [[wikilinks]] resolve to an existing page slug
  - citations look well-formed and their ?t=<sec> roughly matches the [mm:ss] shown

    python3 scripts/validate.py
"""
import sys, os, re
from kblib import iter_pages, wikilinks

CITE_RE = re.compile(r'\[([a-z0-9-]+)\s*@\s*(\d{1,2}:\d{2}(?::\d{2})?)\]\((https?://[^)]*[?&]t=(\d+))[^)]*\)')


def mmss_to_sec(s):
    p = [int(x) for x in s.split(':')]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def main():
    errors, warnings = [], []
    slugs, pages = set(), []
    for path, fm, body in iter_pages():
        slug = fm.get("slug") or os.path.splitext(os.path.basename(path))[0]
        slugs.add(slug)
        pages.append((path, fm, body, slug))

    for path, fm, body, slug in pages:
        rp = os.path.relpath(path)
        if not fm or not fm.get("type"):
            errors.append(f"{rp}: missing or empty `type` in frontmatter")
            continue
        if fm.get("type") == "yc-video" and not fm.get("resource"):
            errors.append(f"{rp}: talk page missing `resource` (YouTube URL / citation anchor)")

        for target in set(wikilinks(body)):
            if target not in slugs:
                warnings.append(f"{rp}: [[{target}]] -> no page with that slug")

        for m in CITE_RE.finditer(body):
            shown, tsec = m.group(2), int(m.group(4))
            if abs(mmss_to_sec(shown) - tsec) > 2:
                warnings.append(f"{rp}: citation [{m.group(1)} @ {shown}] but ?t={tsec} "
                                f"({mmss_to_sec(shown)}s expected)")

    n_pages = len(pages)
    print(f"Validated {n_pages} kb/ page(s).")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
