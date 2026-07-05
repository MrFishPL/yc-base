---
description: Rules for the immutable raw transcript layer
paths:
  - "transcripts/raw/**"
---

# transcripts/raw/ is IMMUTABLE

This directory is **provenance**. It holds exactly what `yt-dlp` downloaded:

- `<date>_<video_id>.en.vtt` — YouTube captions (manual or auto).
- `<date>_<video_id>.info.json` — video metadata (title, upload_date, duration, chapters…).
- `audio/<video_id>.m4a` — audio, only when a video had no usable captions (git-ignored).

**Read these; never edit or delete them by hand.** Cleaning happens downstream in
`transcripts/clean/` via `scripts/clean_vtt.py`, and distillation happens in `kb/`. If a raw file
is wrong, re-fetch it with `yt-dlp`, don't hand-edit it — the whole point is a trustworthy,
reproducible source layer.
