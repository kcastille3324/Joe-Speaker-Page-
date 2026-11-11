#!/usr/bin/env python3
"""Build the Claude artifact copy of the page from index.html.

The artifact host wraps the page in its own <!doctype>/<html>/<head>/<body>
with charset and viewport tags, so this strips those wrappers, puts the
artifact's short title first, and keeps everything else identical.

Usage: python3 scripts/build-artifact.py [output_path]
"""
import pathlib
import re
import sys

ARTIFACT_TITLE = "Joe Bogdan, C2H Speaker"

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root.parent / "joe-bogdan-speaker.html"

head = src[src.index("<head>") + len("<head>"):src.index("</head>")]
body = src[src.index("<body>") + len("<body>"):src.rindex("</body>")]

head = re.sub(r'<meta charset="utf-8">\n', "", head)
head = re.sub(r'<meta name="viewport"[^>]*>\n', "", head)
head = re.sub(r"<title>.*?</title>\n", "", head, count=1)

out = (
    f"<title>{ARTIFACT_TITLE}</title>\n"
    '<meta name="claude:viewport-fit-sides" content="cover">\n'
    + head.strip() + "\n" + body.strip() + "\n"
)
out_path.write_text(out, encoding="utf-8")
print(f"wrote {out_path} ({len(out):,} chars)")
