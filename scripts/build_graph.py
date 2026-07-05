#!/usr/bin/env python3
"""
build_graph.py — build kb/graph.json (a DERIVED, rebuildable typed-edge graph) from the kb/ pages.

The Markdown pages + [[wikilinks]] are canonical; this is a cache for multi-hop queries
("how did advice evolve", "who disagrees with whom"). Stdlib only, offline.
    python3 scripts/build_graph.py
"""
import os, json
from kblib import iter_pages, wikilinks, edge_comments

OUT = "kb/graph.json"


def node_id(ntype, slug):
    return f"{ntype or 'page'}:{slug}"


def main():
    nodes, edges = {}, []
    slug_to_id = {}

    # First pass: nodes
    for path, fm, body in iter_pages():
        slug = fm.get("slug") or os.path.splitext(os.path.basename(path))[0]
        ntype = fm.get("type", "page")
        nid = node_id(ntype, slug)
        nodes[nid] = {
            "id": nid, "type": ntype, "label": fm.get("title", slug),
            "slug": slug, "page": os.path.relpath(path),
        }
        if fm.get("resource"):
            nodes[nid]["resource"] = fm["resource"]
        if fm.get("aliases"):
            nodes[nid]["aliases"] = fm["aliases"]
        slug_to_id[slug] = nid

    # Second pass: edges
    for path, fm, body in iter_pages():
        slug = fm.get("slug") or os.path.splitext(os.path.basename(path))[0]
        ntype = fm.get("type", "page")
        src = node_id(ntype, slug)

        # frontmatter-typed edges
        for sp in fm.get("speakers", []) or []:
            edges.append({"from": src, "type": "authored-by", "to": node_id("person", sp)})
        if fm.get("series"):
            edges.append({"from": src, "type": "part-of", "to": node_id("series", fm["series"])})
        for tp in fm.get("topics", []) or []:
            edges.append({"from": src, "type": "about", "to": node_id("topic", tp)})

        # body wikilinks -> links-to (resolve slug to a real node id when possible)
        for target_slug in set(wikilinks(body)):
            to_id = slug_to_id.get(target_slug, f"slug:{target_slug}")
            edges.append({"from": src, "type": "links-to", "to": to_id})

        # explicit typed edge comments
        for raw in edge_comments(body):
            edges.append({"from": src, "type": "typed", "raw": raw})

    # de-dup edges
    seen, uniq = set(), []
    for e in edges:
        key = (e.get("from"), e.get("type"), e.get("to"), e.get("raw"))
        if key in seen:
            continue
        seen.add(key)
        uniq.append(e)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump({"version": "0.1", "generated_from": "kb/**",
                   "nodes": list(nodes.values()), "edges": uniq},
                  f, ensure_ascii=False, indent=2)
    print(f"Wrote {OUT}: {len(nodes)} nodes, {len(uniq)} edges.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
