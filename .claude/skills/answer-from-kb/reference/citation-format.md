# Citation format

Every factual claim in an answer must carry a citation that resolves to the exact YouTube moment.

## Syntax

```
[<slug> @ mm:ss](https://youtu.be/<video_id>?t=<seconds>)
```

- `<slug>` — the talk page slug (from `kb/talks/<slug>.md` frontmatter `slug`).
- `<video_id>` — the 11-char YouTube ID (frontmatter `video_id`).
- `mm:ss` — the timestamp marker copied verbatim from the cleaned transcript / talk page.
  **Never invent it.** Use the nearest real `[mm:ss]` marker.
- `<seconds>` — `mm:ss` converted to total seconds.

## Timestamp → seconds

```
seconds = minutes * 60 + seconds
          # 12:30  -> 12*60 + 30  = 750
          # 1:04:15 (h:mm:ss) -> 1*3600 + 4*60 + 15 = 3855
```

## Examples

```
The stall usually means no urgency — manufacture a compelling event
[how-to-sell-to-enterprise @ 12:30](https://youtu.be/dQw4w9WgXcQ?t=750).

Do things that don't scale early [do-things-that-dont-scale-pg @ 03:12](https://youtu.be/XXXXXXXXXXX?t=192).
```

## Rules

- One citation per assertion, tied to the sentence it supports — not one citation for a whole paragraph.
- If a claim draws on two talks, cite both.
- If you cannot find a real timestamp for a claim, you cannot make the claim — retrieve more or drop it.
- When presenting a contradiction, cite **each** side.
