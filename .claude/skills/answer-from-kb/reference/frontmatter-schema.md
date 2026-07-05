# Frontmatter field reference

Full schema and examples live in `.claude/rules/kb-pages.md`. Quick reference:

| Field | On | Meaning |
|---|---|---|
| `type` | all (REQUIRED) | `yc-video` \| `concept` \| `person` \| `company` \| `series` |
| `title` | all | Human title |
| `slug` | all | Kebab-case identity; matches filename |
| `video_id` | talks | 11-char YouTube ID — the stable key |
| `resource` | talks (REQUIRED) | `https://www.youtube.com/watch?v=<id>` — the citation anchor |
| `series` | talks | `startup-school` \| `lightcone` \| `how-to-start-a-startup` \| `dalton-and-michael` \| `talks` |
| `speakers` | talks | canonical person slugs |
| `aliases` | all | alt titles / name variants — used to dedup |
| `upload_date` | talks | `YYYY-MM-DD` from `.info.json` |
| `duration_s` | talks | seconds |
| `topics` | talks | slugs of linked `kb/topics/` pages |
| `transcript_source` | talks | `auto-captions` \| `manual-captions` \| `whisper-large-v3` |
| `confidence` | all | `high` \| `medium` \| `low` (drop for heavy-ASR videos) |
| `created` / `updated` | all | `YYYY-MM-DD` |

`resource` is why we need no external citation database: the YouTube URL travels with the page,
so a deep-link `https://youtu.be/<video_id>?t=<seconds>` is always reconstructible.
