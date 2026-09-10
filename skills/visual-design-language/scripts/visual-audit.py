#!/usr/bin/env python3
"""
Visual consistency audit — static checks on token/component docs and optional project code.

Usage:
  python3 visual-audit.py --docs docs/design-language --project . --out /tmp/vdl-audit.md
"""
import argparse, pathlib, re, json, sys

def check_tokens(docs_dir):
    findings = []
    # Look for tokens in FOUNDATIONS.md / tokens.css / design-tokens.json
    for name in ["FOUNDATIONS.md", "tokens.css", "design-tokens.json", "tokens.json"]:
        p = pathlib.Path(docs_dir) / name if docs_dir else None
        if p and p.exists():
            findings.append(f"tokens source: {p}")
    return findings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs/design-language")
    ap.add_argument("--project", default=".")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    lines = ["# Visual Consistency Audit", ""]
    docs = pathlib.Path(args.docs)
    if docs.exists():
        lines.append(f"Docs dir: {docs} — found {len(list(docs.glob('*.md')))} md files")
        for f in sorted(docs.glob("*.md")):
            lines.append(f"- {f.name}: {f.stat().st_size} bytes")
    else:
        lines.append(f"Docs dir not found: {docs}")
    lines += ["", "## Checklist", "- [ ] Spacing uses token scale", "- [ ] Radii from scale", "- [ ] Typography uses type scale",
              "- [ ] Color from roles", "- [ ] Elevation intentional", "- [ ] Icons uniform", "- [ ] A11y: contrast, touch, focus"]
    out = "\n".join(lines)
    print(out)
    if args.out:
        pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(args.out).write_text(out)

if __name__ == "__main__":
    main()
