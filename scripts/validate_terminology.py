#!/usr/bin/env python3
"""Validate public taxonomy completeness and Markdown cross-links (stdlib only)."""
from __future__ import annotations
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
atlas = json.loads((root / "terminology/data/public-index.json").read_text(encoding="utf-8"))
entries = atlas["entries"]
chapters = atlas["chapters"]
assert len(entries) == 500, "Expected 500 entries"
assert len(chapters) == 25, "Expected 25 chapters"
assert len(set(x["id"] for x in entries)) == 500, "Duplicate entry IDs"
assert [x["id"] for x in entries] == [f"CP-{n:03d}" for n in range(1,501)], "Missing or reordered IDs"
assert len(set(x["title"].casefold() for x in entries)) == 500, "Duplicate term titles"
assert {x["type"] for x in entries} <= {"E","D","Q"}, "Unexpected type"
assert sum(x["public_definition"] is not None for x in entries) == 50, "Expected 50 public definitions"
for i, chapter in enumerate(chapters, 1):
    assert chapter["number"] == i
    es = [x for x in entries if x["chapter"] == i]
    assert len(es) == 20, f"Chapter {i} should contain 20 entries"
    assert (root / "terminology/chapters" / chapter["slug"]).exists()
    assert sum(x["public_definition"] is not None for x in es) == 2
for entry in entries:
    page = root / "terminology/entries" / f'{entry["id"]}.md'
    assert page.exists() == (entry["public_definition"] is not None), f'Entry file mismatch: {entry["id"]}'
# Validate relative Markdown links, excluding external URLs and anchors.
pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
checked = 0
for file in root.rglob("*.md"):
    content = file.read_text(encoding="utf-8")
    for link in pattern.findall(content):
        target = link.split("#", 1)[0].strip("<>")
        if not target or target.startswith(("https://", "http://", "mailto:")):
            continue
        assert (file.parent / target).exists(), f"Broken link in {file.relative_to(root)}: {target}"
        checked += 1
print(f"PASS: {len(entries)} terms, {len(chapters)} chapters, 50 preview definitions, {checked} internal links")
