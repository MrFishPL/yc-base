#!/usr/bin/env python3
"""
kblib.py — tiny shared helpers for the yc-base scripts. Stdlib only, offline.

Parses the simple YAML frontmatter subset we actually use (scalars, quoted strings, and inline
[a, b] lists) without requiring PyYAML.
"""
import os, re, glob

KB_DIR = "kb"
SKIP_NAMES = {"README.md", "INDEX.md", "log.md", "RESOLVER.md"}


def parse_frontmatter(text):
    """Return (frontmatter_dict, body_str). Empty dict if no frontmatter."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.S)
    if not m:
        return {}, text
    block, body = m.group(1), m.group(2)
    fm = {}
    for line in block.split('\n'):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        mm = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if val.startswith('[') and val.endswith(']'):
            items = [x.strip().strip('"\'') for x in val[1:-1].split(',')]
            fm[key] = [x for x in items if x]
        elif val == '':
            fm[key] = ''
        else:
            fm[key] = val.strip('"\'')
    return fm, body


def iter_pages(kb_dir=KB_DIR):
    """Yield (path, frontmatter, body) for every content page under kb/ (skips READMEs/INDEX/log)."""
    for path in sorted(glob.glob(os.path.join(kb_dir, "**", "*.md"), recursive=True)):
        if os.path.basename(path) in SKIP_NAMES:
            continue
        try:
            with open(path, encoding='utf-8') as f:
                text = f.read()
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        yield path, fm, body


def wikilinks(body):
    return re.findall(r'\[\[([a-z0-9][a-z0-9-]*)\]\]', body)


def edge_comments(body):
    """Parse explicit typed edges: <!-- edge: <type> | <a> <-> <b> | topic: <t> -->"""
    out = []
    for m in re.finditer(r'<!--\s*edge:\s*(.*?)\s*-->', body, re.S):
        out.append(m.group(1))
    return out
