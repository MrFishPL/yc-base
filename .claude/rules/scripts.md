---
description: Constraints for pipeline scripts
paths:
  - "scripts/**"
---

# scripts/ constraints

- **`*.py` are stdlib-only and offline** by design (caption cleaning, catalog, graph, search,
  validate). No third-party imports, no network calls, no hosted-LLM/API calls. Keeping them
  dependency-free means they run anywhere and cost nothing. If you're tempted to add a dependency,
  first ask whether Claude can do that step in-session instead.
- **The two exceptions that DO use third-party tools** are local, free, and explicitly external
  tools (not APIs): `acquire.sh` (yt-dlp) and `transcribe.py` (faster-whisper). Both run locally.
- **`transcribe.py` must never require a HuggingFace login.** Plain `faster-whisper` on public
  models is fine. Speaker **diarization** (pyannote) is gated on an HF account — do NOT enable it;
  stop and ask the user first.
- Distillation, synthesis, and answering are **Claude's job in-session**, not a script.
