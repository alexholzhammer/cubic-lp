#!/usr/bin/env python3
"""Inline local assets as data URIs so index.html is a single self-contained file.
Edit src.html, then run: python3 build.py"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).parent
src = (root / "src.html").read_text()

ASSETS = {
    "{{HERO}}":   ("hero-landscape.jpg", "image/jpeg"),
    "{{HERO_V}}": ("hero-vertical.jpg",  "image/jpeg"),
    "{{LOGO}}":   ("Logo.svg",           "image/svg+xml"),
    "{{OUR_STORY}}": ("our-story.jpg", "image/jpeg"),
    "{{TILE_1}}": ("t1.jpg", "image/jpeg"),
    "{{TILE_2}}": ("t2.jpg", "image/jpeg"),
    "{{TILE_3}}": ("t3.jpg", "image/jpeg"),
    "{{TILE_4}}": ("t4.jpg", "image/jpeg"),
}

for token, (fname, mime) in ASSETS.items():
    if token not in src:
        continue
    fp = root / fname
    if not fp.exists():
        sys.exit(f"missing asset: {fname}")
    b64 = base64.b64encode(fp.read_bytes()).decode()
    src = src.replace(token, f"data:{mime};base64,{b64}")

leftover = re.findall(r"\{\{[A-Z0-9_]+\}\}", src)
if leftover:
    sys.exit(f"unresolved tokens: {set(leftover)}")

(root / "index.html").write_text(src)
print(f"built index.html — {(root / 'index.html').stat().st_size:,} bytes")
