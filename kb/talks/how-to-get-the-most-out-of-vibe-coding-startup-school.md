---
type: yc-video
title: "How To Get The Most Out Of Vibe Coding | Startup School"
video_id: BJjsfNO5JTo
slug: how-to-get-the-most-out-of-vibe-coding-startup-school
resource: https://www.youtube.com/watch?v=BJjsfNO5JTo
series: startup-school
speakers: [tom-blomfield]
topics: [building-product, mvp, ai-strategy]
transcript_source: auto-captions
upload_date: 2025-04-25
confidence: medium
created: 2026-07-05
updated: 2026-07-05
---
# How To Get The Most Out Of Vibe Coding | Startup School — Compiled Truth

YC partner Tom shares practical techniques, drawn from his own side projects and current YC founders, for getting better results out of AI coding tools like Cursor, Windsurf, and Claude Code.

**Key ideas (with timestamps):**
- Before writing code, work with the LLM to produce a plan in a markdown file, prune it, mark out-of-scope items, and implement it section by section rather than one-shotting the whole project [how-to-get-the-most-out-of-vibe-coding-startup-school @ 04:55](https://youtu.be/BJjsfNO5JTo?t=295)
- Use Git religiously — commit after each working step and don't hesitate to `git reset --hard` when the AI goes off on a "vision quest," since repeated re-prompting on broken code accumulates bad layers instead of fixing root causes [how-to-get-the-most-out-of-vibe-coding-startup-school @ 06:10](https://youtu.be/BJjsfNO5JTo?t=370)
- Write high-level end-to-end integration tests (not just low-level unit tests) so regressions from unrelated LLM changes get caught before moving to the next feature [how-to-get-the-most-out-of-vibe-coding-startup-school @ 07:09](https://youtu.be/BJjsfNO5JTo?t=429)
- Pasting a raw error message from server logs or the browser console straight into the LLM is often enough for it to identify and fix a bug without further explanation [how-to-get-the-most-out-of-vibe-coding-startup-school @ 08:56](https://youtu.be/BJjsfNO5JTo?t=536)
- For complex or unfamiliar functionality, first build a small clean reference implementation in an isolated project, then point the LLM at it to reimplement inside the larger codebase [how-to-get-the-most-out-of-vibe-coding-startup-school @ 12:06](https://youtu.be/BJjsfNO5JTo?t=726)
- Older, convention-heavy frameworks like Ruby on Rails perform better with AI coding tools than newer languages like Rust or Elixir because there is more consistent, high-quality training data online [how-to-get-the-most-out-of-vibe-coding-startup-school @ 13:16](https://youtu.be/BJjsfNO5JTo?t=796)
- Keep files small and modular, and favor service-based architecture with clear API boundaries, since huge monorepos with heavy interdependencies are hard for both humans and LLMs to reason about [how-to-get-the-most-out-of-vibe-coding-startup-school @ 12:29](https://youtu.be/BJjsfNO5JTo?t=749)
- Voice input tools (like YC company Aqua) can roughly double effective prompting speed compared to typing, since LLMs tolerate imperfect transcription [how-to-get-the-most-out-of-vibe-coding-startup-school @ 14:22](https://youtu.be/BJjsfNO5JTo?t=862)
- Different models excel at different tasks (e.g., Gemini for whole-codebase indexing and planning, Sonnet 3.7 for implementation) so switching models when one gets stuck is a useful debugging tactic [how-to-get-the-most-out-of-vibe-coding-startup-school @ 15:27](https://youtu.be/BJjsfNO5JTo?t=927)

**See also:** [[building-product]], [[mvp]], [[ai-strategy]]

---
## Timeline (append-only, reverse-chron, each entry dated + sourced)
- 2026-07-05 — ingested from transcript.
