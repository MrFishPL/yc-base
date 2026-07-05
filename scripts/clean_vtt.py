#!/usr/bin/env python3
"""
clean_vtt.py — turn raw YouTube caption files (.vtt / .srt) into clean Markdown with [mm:ss] markers.

Handles YouTube auto-caption "rolling window" duplication (where each cue repeats the tail of the
previous cue and adds a few new words) via suffix/prefix overlap merging — so the output reads once,
in order, with a timestamp at the start of each paragraph.

Stdlib only. No network, no API. Usage:
    python3 scripts/clean_vtt.py transcripts/raw            # clean every .vtt/.srt in a dir (recursive)
    python3 scripts/clean_vtt.py transcripts/raw/2023-11-14_ID.en.vtt
    python3 scripts/clean_vtt.py transcripts/raw --force    # overwrite existing clean files
"""
import sys, os, re, json, html, glob, datetime

CLEAN_DIR = "transcripts/clean"
WORDS_PER_PARA = 60          # soft paragraph size
GAP_SECONDS = 6.0            # start a new paragraph if this long a silence precedes a segment

TIME_RE = re.compile(r'(\d{1,2}:\d{2}:\d{2}[.,]\d{3}|\d{1,2}:\d{2}[.,]\d{3})\s*-->\s*'
                     r'(\d{1,2}:\d{2}:\d{2}[.,]\d{3}|\d{1,2}:\d{2}[.,]\d{3})')
TAG_RE = re.compile(r'<[^>]+>')


def to_seconds(ts):
    ts = ts.replace(',', '.')
    parts = ts.split(':')
    parts = [float(p) for p in parts]
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0.0, parts[0], parts[1]
    else:
        h, m, s = 0.0, 0.0, parts[0]
    return h * 3600 + m * 60 + s


def fmt_ts(sec):
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def parse_cues(text):
    """Return list of (start_seconds, cleaned_text) for each caption cue."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    cues = []
    for block in re.split(r'\n\n+', text):
        start, textlines = None, []
        for ln in block.split('\n'):
            m = TIME_RE.search(ln)
            if m:
                start = to_seconds(m.group(1))
            elif start is not None:
                textlines.append(ln)
        if start is None:
            continue
        raw = ' '.join(textlines)
        raw = TAG_RE.sub('', raw)          # strip inline <timestamp> and <c> tags
        raw = html.unescape(raw)
        raw = re.sub(r'\s+', ' ', raw).strip()
        if raw:
            cues.append((start, raw))
    return cues


def merge_cues(cues):
    """Merge overlapping caption windows into ordered segments [(start, new_text), ...]."""
    out_words = []       # original-case words emitted so far
    out_lc = []          # lowercased mirror, for overlap comparison
    segments = []
    for start, text in cues:
        toks = text.split()
        toks_lc = [t.lower() for t in toks]
        # largest k where the tail of what we've emitted equals the head of this cue
        maxk = min(len(out_lc), len(toks_lc))
        k = 0
        for kk in range(maxk, 0, -1):
            if out_lc[-kk:] == toks_lc[:kk]:
                k = kk
                break
        new = toks[k:]
        if new:
            segments.append((start, ' '.join(new)))
            out_words.extend(new)
            out_lc.extend(toks_lc[k:])
    return segments


def paragraphs(segments):
    """Group segments into paragraphs prefixed with [mm:ss]."""
    paras, cur, cur_start, cur_words, last_start = [], [], None, 0, None
    for start, text in segments:
        gap = (last_start is not None and start - last_start > GAP_SECONDS)
        if cur and (cur_words >= WORDS_PER_PARA or gap):
            paras.append((cur_start, ' '.join(cur)))
            cur, cur_words = [], 0
        if not cur:
            cur_start = start
        cur.append(text)
        cur_words += len(text.split())
        last_start = start
    if cur:
        paras.append((cur_start, ' '.join(cur)))
    return paras


def parse_prefix(vtt_path):
    """From transcripts/raw/<date>_<id>.<lang>.vtt derive (prefix, date, video_id)."""
    name = os.path.basename(vtt_path)
    name = re.sub(r'\.(vtt|srt)$', '', name)
    name = re.sub(r'\.[A-Za-z]{2}(-[A-Za-z0-9]+)?$', '', name)   # strip .en / .en-orig / .en-US
    date, vid = "", name
    if '_' in name:
        head, tail = name.split('_', 1)
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', head):
            date, vid = head, tail
        else:
            vid = name.split('_')[-1]
    return name, date, vid


def slugify(text, fallback):
    s = re.sub(r'[^a-z0-9]+', '-', (text or '').lower()).strip('-')
    return (s[:60] or fallback)


def sibling_info(vtt_path, prefix_name):
    d = os.path.dirname(vtt_path)
    cand = os.path.join(d, prefix_name + '.info.json')
    if os.path.exists(cand):
        try:
            with open(cand, encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    return None


def detect_source(vtt_path):
    """Distinguish manual from auto captions. YouTube auto tracks come as '<lang>-orig'; a plain
    '.en.vtt' is manual only if it differs from the auto '.en-orig.vtt' sibling (else it's auto)."""
    name = os.path.basename(vtt_path)
    if 'orig' in name:
        return 'auto-captions'
    base = re.sub(r'\.[A-Za-z]{2}(-[A-Za-z0-9]+)?\.(vtt|srt)$', '', vtt_path)
    for orig in (base + '.en-orig.vtt', base + '.en-orig.srt'):
        if os.path.exists(orig):
            try:
                a = open(vtt_path, encoding='utf-8', errors='replace').read()
                b = open(orig, encoding='utf-8', errors='replace').read()
                return 'manual-captions' if a != b else 'auto-captions'
            except Exception:
                return 'auto-captions'
    return 'auto-captions'   # no auto sibling to compare — assume auto unless proven otherwise


def choose_preferred(files):
    """Group caption files by (date, video_id); keep one per video, preferring the manual 'en' track."""
    def rank(fp):
        name = os.path.basename(fp)
        if re.search(r'\.en\.(vtt|srt)$', name):
            return 0                       # plain en — prefer (manual when available)
        if 'orig' in name:
            return 2                       # auto original — least preferred
        return 1                           # other en-XX variants
    groups = {}
    for fp in files:
        _, date, vid = parse_prefix(fp)
        groups.setdefault((date, vid), []).append(fp)
    return [sorted(g, key=rank)[0] for g in groups.values()]


def clean_one(vtt_path, force=False):
    prefix_name, date, vid = parse_prefix(vtt_path)
    info = sibling_info(vtt_path, prefix_name)
    title = (info or {}).get('title', '')
    if info and info.get('id'):
        vid = info['id']
    if info and info.get('upload_date') and not date:
        ud = str(info['upload_date'])
        date = f"{ud[:4]}-{ud[4:6]}-{ud[6:8]}" if len(ud) == 8 else ud
    slug = slugify(title, vid)
    src = detect_source(vtt_path)

    with open(vtt_path, encoding='utf-8', errors='replace') as f:
        raw = f.read()
    paras = paragraphs(merge_cues(parse_cues(raw)))
    if not paras:
        print(f"  ! no cues parsed: {vtt_path}")
        return None

    os.makedirs(CLEAN_DIR, exist_ok=True)
    out_name = f"{date + '_' if date else ''}{vid}_{slug}.md"
    out_path = os.path.join(CLEAN_DIR, out_name)
    if os.path.exists(out_path) and not force:
        print(f"  = exists (skip): {out_path}")
        return out_path

    today = datetime.date.today().isoformat()
    lines = [
        "---",
        "type: transcript",
        f"video_id: {vid}",
        f'title: "{title.replace(chr(34), "")}"' if title else f"title: {vid}",
        f"slug: {slug}",
        f"resource: https://www.youtube.com/watch?v={vid}",
        f"upload_date: {date}" if date else "upload_date:",
        f"transcript_source: {src}",
        f"source_file: {os.path.basename(vtt_path)}",
        f"generated: {today}",
        "---",
        f"# Transcript — {title or vid}",
        "",
    ]
    for start, text in paras:
        lines.append(f"[{fmt_ts(start)}] {text}")
        lines.append("")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines).rstrip() + '\n')
    print(f"  + wrote {out_path}  ({len(paras)} paragraphs)")
    return out_path


def main(argv):
    force = '--force' in argv
    args = [a for a in argv if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 1
    target = args[0]
    if os.path.isdir(target):
        allfiles = sorted(glob.glob(os.path.join(target, '**', '*.vtt'), recursive=True) +
                          glob.glob(os.path.join(target, '**', '*.srt'), recursive=True))
        files = sorted(choose_preferred(allfiles))    # one caption file per video (prefer manual)
    else:
        files = [target]
    if not files:
        print(f"No .vtt/.srt files under {target}")
        return 0
    print(f"Cleaning {len(files)} caption file(s) -> {CLEAN_DIR}/")
    for fp in files:
        clean_one(fp, force=force)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
