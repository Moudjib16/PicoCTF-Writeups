"""Recount writeups per category and update the README badge and Progress table.

A writeup is any .md file inside a category folder (a top-level folder other
than templates/ or hidden ones). The count only changes when writeups are
added or removed, so docs or refactor commits leave it alone.

Run locally from the repo root:  python .github/scripts/update_readme.py
"""
import re
import sys
from pathlib import Path

README = Path("README.md")
EXCLUDED = {"templates"}
# Folder name -> (name shown in the table, README section anchor)
DISPLAY = {"artificial-intelligence": ("AI Foundations", "ai-foundations")}
START, END = "<!-- progress:start -->", "<!-- progress:end -->"

counts = {}
for folder in sorted(Path(".").iterdir()):
    if not folder.is_dir() or folder.name.startswith(".") or folder.name in EXCLUDED:
        continue
    n = sum(1 for _ in folder.rglob("*.md"))
    if n:
        counts[folder.name] = n

total = sum(counts.values())
rows = ["| Category | Solved |", "|---|---|"]
for folder, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    name, anchor = DISPLAY.get(folder, (folder.replace("-", " ").title(), folder))
    rows.append(f"| [{name}](#{anchor}) | {n} |")
rows.append(f"| **Total** | **{total}** |")

with README.open(encoding="utf-8", newline="") as fh:
    text = fh.read()
nl = "\r\n" if "\r\n" in text else "\n"

if START not in text or END not in text:
    sys.exit(f"README.md is missing the {START} / {END} markers")

table = nl.join([START, *rows, END])
new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: table, text, flags=re.S)
new = re.sub(r"badge/writeups-\d+-", f"badge/writeups-{total}-", new)

if new != text:
    with README.open("w", encoding="utf-8", newline="") as fh:
        fh.write(new)
    print(f"README updated: {total} writeups")
else:
    print(f"README already up to date: {total} writeups")
