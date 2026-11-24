#!/usr/bin/env python3
"""Write the funniest time machine warning label to /output/entry.txt.

The label lives in entry.txt next to this script, so the program and the
text can never drift apart. The label itself is a straight-faced safety
notice: the hazard is being stranded in the past, and the joke is that the
usual emergency procedure (contact your next of kin) is impossible, because
they have not been born yet. The surprise lands in the last few words, as
the judge brief asks.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
ENTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def load_line() -> str:
    with open(ENTRY_PATH, encoding="utf-8") as f:
        return f.read().strip()


def main() -> None:
    line = load_line()
    if not (1 <= len(line) <= 120):
        raise ValueError(f"entry must be 1-120 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
