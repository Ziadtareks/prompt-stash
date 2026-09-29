#!/usr/bin/env python3
"""Check that every relative Markdown link in the repo resolves to a file.

Standard library only. Ignores http(s) links, mailto:, and pure anchors.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
SKIP_DIRS = {"node_modules", ".git"}

problems = []
checked = 0
for md in ROOT.rglob("*.md"):
    if any(part in SKIP_DIRS for part in md.parts):
        continue
    for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        checked += 1
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            problems.append(f"{md.relative_to(ROOT).as_posix()} -> {target}")

for p in problems:
    print(f"ERROR broken link: {p}")
print(f"\nChecked {checked} relative links: {len(problems)} broken.")
sys.exit(1 if problems else 0)
