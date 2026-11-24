#!/usr/bin/env python3
"""Time machine warning label: one line, at most 120 characters.

Writes exactly one warning line to /output/entry.txt.
Standard library only.
"""

import os

LINE = "WARNING: If stranded in the past, do not panic. Your next of kin has not been born yet."
OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 120


def main() -> None:
    # Loud length gate: the entry must be exactly one non-blank line,
    # 1-120 chars (this line is 87). Fail loudly instead of writing bad output.
    # The source line must already be clean: no surrounding whitespace to hide
    # a length miscount, and no embedded newline to smuggle in a second line.
    if LINE != LINE.strip():
        raise SystemExit("ERROR: warning line has leading/trailing whitespace")
    line = LINE
    if not line:
        raise SystemExit("ERROR: warning line is blank")
    if len(line) > MAX_LENGTH:
        raise SystemExit(
            f"ERROR: warning line is {len(line)} chars, exceeds {MAX_LENGTH}-char limit"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("ERROR: warning line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
