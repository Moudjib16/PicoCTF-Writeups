"""Fail if any tracked file contains an unredacted flag or a committed flag file.

A flag counts as redacted when its contents are REDACTED, or only dots, X's or
asterisks (e.g. academy{...}). To allow a line on purpose, add the text
"flag-check: ignore" to it.

Run locally from the repo root:  python .github/scripts/check_flags.py
"""
import re
import subprocess
import sys
from pathlib import PurePosixPath

FLAG = re.compile(r"(picoCTF|academy)\{([^}\s`]*)\}", re.IGNORECASE)
LOOKS_LIKE_FLAG = re.compile(r"^[A-Za-z0-9_\-!@#$%?.]+$")
REDACTED = re.compile(r"^(REDACTED|[.xX*]+)$", re.IGNORECASE)
FLAG_FILE = re.compile(r"^flag(\.txt)?$", re.IGNORECASE)
IGNORE = "flag-check: ignore"

files = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout
problems = []

for path in filter(None, files.decode().split("\0")):
    if FLAG_FILE.match(PurePosixPath(path).name):
        problems.append(f"{path}: flag file is committed")
        continue
    try:
        data = open(path, "rb").read()
    except OSError:
        continue
    if b"\0" in data:  # binary file
        continue
    for lineno, line in enumerate(data.decode("utf-8", "ignore").splitlines(), 1):
        if IGNORE in line:
            continue
        for m in FLAG.finditer(line):
            body = m.group(2)
            if LOOKS_LIKE_FLAG.match(body) and not REDACTED.match(body):
                problems.append(f"{path}:{lineno}: unredacted flag {m.group(0)}")

if problems:
    print("Unredacted flags found:\n")
    print("\n".join(f"  {p}" for p in problems))
    print("\nReplace them with academy{REDACTED} / picoCTF{REDACTED}.")
    sys.exit(1)
print("No unredacted flags found.")
