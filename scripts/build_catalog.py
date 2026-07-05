#!/usr/bin/env python3
"""
build_catalog.py — build data/catalog.json (a DERIVED, rebuildable index) from transcripts/raw/*.info.json.

Stdlib only, offline. Run after acquisition (and after cleaning, to pick up clean_path):
    python3 scripts/build_catalog.py
"""
import os, re, glob, json

RAW_DIR = "transcripts/raw"
CLEAN_DIR = "transcripts/clean"
OUT = "data/catalog.json"


def yyyymmdd(d):
    d = str(d or "")
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 and d.isdigit() else d


def find_clean(prefix):
    """A clean file is named <date>_<id>_<slug>.md; match on the <date>_<id> prefix."""
    hits = glob.glob(os.path.join(CLEAN_DIR, prefix + "_*.md"))
    return os.path.relpath(hits[0]) if hits else None


def has_captions(info_path):
    base = re.sub(r'\.info\.json$', '', info_path)
    return bool(glob.glob(base + ".*.vtt") + glob.glob(base + ".*.srt") +
                glob.glob(base + ".vtt") + glob.glob(base + ".srt"))


def main():
    infos = sorted(glob.glob(os.path.join(RAW_DIR, "**", "*.info.json"), recursive=True))
    catalog = []
    for ip in infos:
        try:
            with open(ip, encoding='utf-8') as f:
                info = json.load(f)
        except Exception as e:
            print(f"  ! skip {ip}: {e}")
            continue
        vid = info.get("id", "")
        base = os.path.basename(re.sub(r'\.info\.json$', '', ip))   # e.g. 2023-11-14_<id>
        catalog.append({
            "video_id": vid,
            "title": info.get("title", ""),
            "url": info.get("webpage_url") or (f"https://www.youtube.com/watch?v={vid}" if vid else ""),
            "series": info.get("playlist_title") or info.get("playlist") or "",
            "upload_date": yyyymmdd(info.get("upload_date")),
            "duration_s": info.get("duration"),
            "uploader": info.get("uploader") or info.get("channel", ""),
            "view_count": info.get("view_count"),
            "chapters": len(info.get("chapters") or []),
            "has_captions": has_captions(ip),
            "clean_path": find_clean(base),
        })
    catalog.sort(key=lambda e: (e.get("upload_date") or "", e.get("title") or ""))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump({"generated_from": RAW_DIR, "count": len(catalog), "videos": catalog},
                  f, ensure_ascii=False, indent=2)
    n_clean = sum(1 for e in catalog if e["clean_path"])
    n_caps = sum(1 for e in catalog if e["has_captions"])
    print(f"Wrote {OUT}: {len(catalog)} videos ({n_caps} with captions, {n_clean} cleaned).")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
