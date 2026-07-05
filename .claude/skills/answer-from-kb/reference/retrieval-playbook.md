# Retrieval playbook

Grep beats vector search on this corpus **if** you expand the query first. The failure mode of
grep is the *oblique reference* (no shared keyword) — beat it by ORing synonyms and jargon.

## Recipe

1. **Route with the index.** `kb/INDEX.md` groups pages by series/topic. Shortlist candidate
   files before grepping — don't grep the whole tree blindly.
2. **Expand the question into an OR-pattern.** Include synonyms, acronyms, and the YC vernacular.
3. **List, then read.** `rg -i -l '<pattern>' kb/ -g '*.md'` to route; then `rg -i -C 3 '<pattern>'`
   on the shortlisted files for citable spans; `rg -i -c` per-file counts as a cheap relevance score.
4. **Hop the graph.** Follow `See also` / `[[wikilinks]]`; use `kb/graph.json` for typed edges.

## Query-expansion cheatsheet (extend as the corpus grows)

| User asks about | OR-pattern to grep |
|---|---|
| enterprise / B2B sales | `enterprise\|B2B\|sales\|procurement\|champion\|pilot\|POC\|stall\|urgency\|compelling event\|contract` |
| product-market fit | `product.?market fit\|PMF\|retention\|pull\|desperate\|must.?have\|cohort` |
| pricing | `pricing\|price\|charge\|willingness to pay\|discount\|anchor\|tier\|usage.?based` |
| fundraising | `raise\|fundrais\|valuation\|SAFE\|dilution\|term sheet\|angel\|Series A\|runway\|default alive` |
| hiring / team | `hire\|hiring\|recruit\|co.?founder\|equity\|first employee\|firing` |
| growth | `growth\|acquisition\|channel\|virality\|retention\|funnel\|CAC\|LTV` |
| talking to users | `talk to users\|customer interview\|user research\|feedback\|Mom Test` |
| doing things that don't scale | `do things that don.?t scale\|manual\|concierge\|hand.?recruit` |

## Ranked search helper (stdlib, offline)

```bash
python3 scripts/search.py search "how to price a B2B product"   # ranked files + [mm:ss] snippets
python3 scripts/search.py index                                  # what's in the KB, by type
python3 scripts/search.py read kb/topics/pricing.md              # print a page
```
