#!/usr/bin/env python3
"""
remaining.py — print watch URLs for worklist IDs that don't yet have a transcripts/raw/*_<id>.info.json.

Makes captions-only acquisition idempotent/resumable: yt-dlp's --download-archive does NOT record
runs made with --skip-download, so we track completion by the presence of each video's .info.json.
Stdlib only, offline.

    python3 scripts/remaining.py [worklist.txt]   # default: scripts/worklist.txt
"""
import sys, os, glob

RAW = "transcripts/raw"


def existing_ids():
    # filename is <YYYY-MM-DD>_<id>.info.json; the id is everything after the FIRST underscore
    # (video IDs can themselves contain '_' or '-', e.g. oHwUD9b9_pg), so never split on the last one.
    ids = set()
    for f in glob.glob(os.path.join(RAW, "*.info.json")):
        base = os.path.basename(f)[:-len(".info.json")]   # e.g. 2026-06-27_Ju8LVdvuxGM
        ids.add(base.split("_", 1)[1] if "_" in base else base)
    return ids


def main(argv):
    wl = argv[0] if argv else "scripts/worklist.txt"
    if not os.path.exists(wl):
        sys.stderr.write(f"worklist not found: {wl}\n")
        return 1
    done = existing_ids()
    ids = [l.strip().split("/")[-1].split("=")[-1] for l in open(wl) if l.strip()]
    remaining = [i for i in ids if i not in done]
    for vid in remaining:
        print(f"https://www.youtube.com/watch?v={vid}")
    sys.stderr.write(f"{len(remaining)} remaining of {len(ids)} ({len(done)} already fetched)\n")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
