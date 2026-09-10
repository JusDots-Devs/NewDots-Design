#!/usr/bin/env python3
"""
Inventory a design-inspiration directory.

Usage:
  python3 inventory.py --dir design-inspiration --out /tmp/vdl-inventory.json
  python3 inventory.py --dir . --out /tmp/vdl-inventory.json

Outputs JSON + prints markdown table.
No dependencies beyond Pillow (falls back to no-image mode).
"""
import argparse, hashlib, json, os, sys, pathlib

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".heic", ".heif"}

def phash_simple(path):
    """8x8 average hash (aHash) — 64-bit hex. ponytail: 8x8 aHash, not DCT pHash; upgrade to imagehash if many near-dupes."""
    try:
        from PIL import Image
        im = Image.open(path).convert("L").resize((8, 8), Image.BILINEAR)
        pixels = list(im.getdata())
        avg = sum(pixels) / len(pixels)
        bits = "".join("1" if p > avg else "0" for p in pixels)
        return hex(int(bits, 2))[2:].zfill(16)
    except Exception:
        return None

def palette(path, n=5):
    try:
        from PIL import Image
        im = Image.open(path).convert("RGB").resize((64, 64))
        q = im.quantize(colors=n, method=2)
        pal = q.getpalette()[: n * 3]
        return [f"#{pal[i*3]:02x}{pal[i*3+1]:02x}{pal[i*3+2]:02x}" for i in range(n)]
    except Exception:
        return []

def inventory(dirpath):
    dirpath = pathlib.Path(dirpath)
    files = sorted([p for p in dirpath.iterdir() if p.suffix.lower() in SUPPORTED and p.is_file()])
    if not files:
        # recursive fallback
        files = sorted([p for p in dirpath.rglob("*") if p.suffix.lower() in SUPPORTED and p.is_file()])
    rows = []
    seen_md5 = {}
    for p in files:
        data = p.read_bytes()
        md5 = hashlib.md5(data).hexdigest()
        size = len(data)
        w = h = None
        try:
            from PIL import Image
            with Image.open(p) as im:
                w, h = im.size
        except Exception:
            pass
        ar = round(w / h, 2) if w and h else None
        orient = "portrait" if w and h and h > w else "landscape" if w and h and w > h else "square" if w == h else "?"
        ph = phash_simple(p)
        pal = palette(p)
        dup = seen_md5.get(md5)
        seen_md5.setdefault(md5, p.name)
        rows.append({
            "file": p.name,
            "path": str(p),
            "w": w, "h": h, "ar": ar, "orient": orient,
            "bytes": size, "md5": md5[:8], "md5_full": md5,
            "phash": ph, "palette": pal,
            "duplicate_of": dup,
        })
    # near-duplicate via phash hamming
    for i, a in enumerate(rows):
        if not a["phash"]:
            continue
        for j, b in enumerate(rows):
            if j <= i or not b["phash"]:
                continue
            try:
                ham = bin(int(a["phash"], 16) ^ int(b["phash"], 16)).count("1")
                if ham <= 6:
                    b["near_duplicate_of"] = a["file"]
                    b["phash_distance"] = ham
            except Exception:
                pass
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="inspiration directory")
    ap.add_argument("--out", default="", help="json output path")
    args = ap.parse_args()
    rows = inventory(args.dir)
    # markdown table to stdout
    print(f"| # | file | W×H | AR | size | palette | duplicate? |")
    print(f"|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        wh = f"{r['w']}×{r['h']}" if r["w"] else "?"
        pal = " ".join(r["palette"][:3]) if r["palette"] else "—"
        dup = r.get("duplicate_of") or r.get("near_duplicate_of") or ""
        if dup:
            dup = f"≈ {dup}" + (f" (d={r.get('phash_distance')})" if "phash_distance" in r else "")
        kb = f"{r['bytes']/1024:.0f}KB"
        print(f"| {i} | {r['file']} | {wh} | {r['ar'] or '?'} | {kb} | {pal} | {dup} |")
    print(f"\nTotal: {len(rows)} images", file=sys.stderr)
    if args.out:
        pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as f:
            json.dump(rows, f, indent=2)
        print(f"Wrote {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
