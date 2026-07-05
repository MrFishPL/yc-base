#!/usr/bin/env bash
#
# acquire.sh — pull YouTube captions + metadata (NO video/audio) with yt-dlp.
# Free, local, and RESUMABLE. No API.
#
# Resumability note: yt-dlp's --download-archive does NOT record runs made with --skip-download,
# so we track completion by each video's .info.json in transcripts/raw/ (via scripts/remaining.py).
# Re-running only fetches videos you don't already have.
#
# Usage:
#   scripts/acquire.sh                         # whole channel: enumerate /videos + /streams, then fetch
#   scripts/acquire.sh scripts/worklist.txt    # fetch a specific list of IDs/URLs (recommended for big runs)
#   scripts/acquire.sh "<playlist-or-video-URL>"
#
set -euo pipefail

YTDLP="yt-dlp"
[ -x ".venv/bin/yt-dlp" ] && YTDLP=".venv/bin/yt-dlp"
if ! command -v "$YTDLP" >/dev/null 2>&1 && [ ! -x "$YTDLP" ]; then
  echo "yt-dlp not found. Install (local, free):  pip install -r scripts/requirements.txt" >&2
  exit 127
fi
mkdir -p transcripts/raw scripts

ARG="${1:-CHANNEL}"
WORKLIST="scripts/worklist.txt"

# 1) Resolve the arg to a worklist file of IDs/URLs.
if [ "$ARG" = "CHANNEL" ]; then
  echo "Enumerating the Y Combinator channel /videos + /streams (IDs only, no media)…"
  "$YTDLP" --flat-playlist --print "%(id)s" "https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg/videos"  >  scripts/videos.txt
  "$YTDLP" --flat-playlist --print "%(id)s" "https://www.youtube.com/channel/UCcefcZRL2oaA_uBNeo5UOWg/streams" >  scripts/streams.txt || true
  cat scripts/videos.txt scripts/streams.txt | awk 'NF && !seen[$0]++' > "$WORKLIST"
elif [ -f "$ARG" ]; then
  WORKLIST="$ARG"
else
  # a channel/playlist/video URL: enumerate it
  echo "Enumerating $ARG …"
  "$YTDLP" --flat-playlist --print "%(id)s" "$ARG" | awk 'NF && !seen[$0]++' > "$WORKLIST"
fi
echo "Worklist: $(grep -c . "$WORKLIST") videos ($WORKLIST)"

# 2) Filter to the not-yet-fetched remainder (resumable).
python3 scripts/remaining.py "$WORKLIST" > scripts/remaining.txt 2> scripts/remaining.info
cat scripts/remaining.info
if [ ! -s scripts/remaining.txt ]; then
  echo "Nothing to fetch — every video already has metadata. Done."
  exit 0
fi

# 3) Fetch captions + metadata only, paced (429 defense), never aborting on one bad video.
echo "Fetching captions + metadata into transcripts/raw/ …"
"$YTDLP" \
  --skip-download \
  --write-subs --write-auto-subs \
  --sub-langs "en.*" --sub-format vtt \
  --write-info-json \
  --no-overwrites \
  --sleep-requests 1 --sleep-interval 3 --max-sleep-interval 12 \
  --ignore-errors --no-abort-on-error \
  -o "transcripts/raw/%(upload_date>%Y-%m-%d)s_%(id)s.%(ext)s" \
  --batch-file scripts/remaining.txt

echo
echo "Done (re-run this script to pick up any that failed — it's resumable). Next:"
echo "  python3 scripts/clean_vtt.py transcripts/raw   # clean captions -> transcripts/clean/"
echo "  python3 scripts/build_catalog.py               # rebuild data/catalog.json"
echo "  then ingest with the ingest-video skill."
