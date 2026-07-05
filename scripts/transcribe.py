#!/usr/bin/env python3
"""
transcribe.py — LOCAL transcription fallback for the ~5-10% of videos that lack usable captions.

Runs faster-whisper on THIS machine (CPU or GPU). No hosted API, no cost beyond local compute.
Model weights download once from the public HuggingFace Hub — no login required.

    # 1) get audio for a gap video (audio is git-ignored, transient):
    yt-dlp -f bestaudio -x --audio-format m4a -o "transcripts/raw/audio/%(id)s.%(ext)s" "https://youtu.be/<ID>"
    # 2) transcribe locally -> transcripts/clean/<id>.md with [mm:ss] markers:
    python3 scripts/transcribe.py transcripts/raw/audio/<ID>.m4a --video-id <ID>

Options: --model large-v3 (default) | distil-large-v3 (faster, English-only) | medium | small
         --compute-type int8 (default, CPU-friendly) | float16 (GPU)

NOTE: speaker diarization (who-spoke-when) needs a HuggingFace login + a gated pyannote model.
It is intentionally NOT implemented here. If you want it, STOP and ask the user to log in first.
"""
import sys, os, re, argparse, datetime

CLEAN_DIR = "transcripts/clean"


def fmt_ts(sec):
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def slugify(text, fallback):
    s = re.sub(r'[^a-z0-9]+', '-', (text or '').lower()).strip('-')
    return s[:60] or fallback


def main():
    ap = argparse.ArgumentParser(description="Local faster-whisper transcription (no API, no HF login).")
    ap.add_argument("audio")
    ap.add_argument("--video-id", default=None, help="YouTube ID (for citation URL + filename)")
    ap.add_argument("--title", default="", help="optional talk title")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--compute-type", default="int8")
    ap.add_argument("--language", default="en")
    ap.add_argument("--diarize", action="store_true", help="(blocked) needs a HuggingFace login")
    args = ap.parse_args()

    if args.diarize:
        print("Diarization needs a HuggingFace account + accepting the gated pyannote model.\n"
              "This script does NOT do that. Stop and ask the user to log in first, then we can add it.")
        return 2

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper is not installed. It is LOCAL and free (no API):\n"
              "    pip install faster-whisper\n"
              "(Model weights download once from the public HuggingFace Hub — no login needed.)")
        return 127

    if not os.path.exists(args.audio):
        print(f"Audio not found: {args.audio}")
        return 1

    vid = args.video_id or os.path.splitext(os.path.basename(args.audio))[0]
    print(f"Loading faster-whisper model '{args.model}' (compute={args.compute_type})… "
          f"first run downloads weights locally.")
    model = WhisperModel(args.model, device="auto", compute_type=args.compute_type)
    segments, info = model.transcribe(args.audio, language=args.language, vad_filter=True)
    print(f"Transcribing (detected language={info.language}, p={info.language_probability:.2f})…")

    os.makedirs(CLEAN_DIR, exist_ok=True)
    slug = slugify(args.title, vid)
    out_path = os.path.join(CLEAN_DIR, f"{vid}_{slug}.md")
    today = datetime.date.today().isoformat()
    lines = [
        "---", "type: transcript", f"video_id: {vid}",
        f'title: "{args.title}"' if args.title else f"title: {vid}",
        f"slug: {slug}", f"resource: https://www.youtube.com/watch?v={vid}",
        f"transcript_source: whisper-{args.model}", f"generated: {today}",
        "confidence: medium", "---", f"# Transcript — {args.title or vid}", "",
    ]
    count = 0
    for seg in segments:
        text = seg.text.strip()
        if text:
            lines.append(f"[{fmt_ts(seg.start)}] {text}")
            lines.append("")
            count += 1
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines).rstrip() + '\n')
    print(f"Wrote {out_path} ({count} segments). Whisper can repeat on silence — review "
          f"<!-- SUSPECT --> spans during ingest.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
