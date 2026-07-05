# RESOLVER — where does a page belong?

Read this **before creating any page.** MECE applies to *directories*, not to reality: a person
can be many things, but each fact/entity gets exactly **one primary home**. Everything else is a
typed backlink (`[[slug]]`) from that home. This prevents duplicate pages without losing relationships.

## Decision tree

```
Is it a single YouTube video?                      → kb/talks/<slug>.md            (type: yc-video)
Is it a cross-cutting idea / framework / question? → kb/topics/<kebab>.md          (type: concept)
Is it a person (founder, partner, guest)?          → kb/entities/people/<slug>.md  (type: person)
Is it a company / product (case study)?            → kb/entities/companies/<slug>.md (type: company)
Is it a show / playlist / series?                  → kb/series/<slug>.md           (type: series)
Is it the raw downloaded transcript?               → transcripts/raw/   (IMMUTABLE — never create/edit by hand)
Is it a deterministically cleaned transcript?      → transcripts/clean/ (written by scripts/clean_vtt.py)
```

## Rules of the road

- **Filename = identity.** Kebab-case, stable. For talks, the slug derives from the title but the
  `video_id` (11-char YouTube ID) in frontmatter is the true key — the title can change, the ID can't.
- **One entity, one page.** Before creating `kb/entities/people/michael-seibel.md`, grep for the
  name and known aliases. If a page exists, add the new name to its `aliases:` list instead of
  making a second page. Same for companies ("Airbnb" vs "AirBed & Breakfast").
- **Repeated advice → one concept page, many citations.** "Talk to users", "do things that don't
  scale", "default alive" each live in ONE `kb/topics/` page that many talk pages *cite* — never
  copy the advice into every talk page.
- **A talk page links up to topics/entities; it doesn't restate them.** The talk page holds that
  talk's thesis + timestamped key moments; shared ideas are `[[wikilinks]]` to the topic pages.
- **When unsure between two topics,** pick the most specific existing one; if none fits, create the
  topic page and note it in `kb/log.md`. Don't fan a fact across three topics — pick the primary
  home and backlink the rest.

## Per-directory resolvers

Each `kb/` subdirectory has its own `README.md` restating "what goes here / what does NOT." When
they conflict with this file, this root RESOLVER wins.
