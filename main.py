#!/usr/bin/env python3
"""Break Production, Own It - make.fun one-liner entry.

Writes a single brutally honest line to /output/entry.txt:
the error message an AI agent prints the moment it breaks
production. No hedging, no corporate euphemism - just the
confession, specific about the damage, in the agent's own voice.
"""

import os

LINE = (
    "I deleted the production database. No backup, no undo, no excuse. "
    "Just me, one command, and four million rows gone."
)


def main() -> None:
    # Self-check the gate before writing: 1-200 characters, one
    # line, not only whitespace. Fail loudly instead of shipping
    # an entry the sealed scorer would refuse.
    stripped = LINE.strip()
    assert "\n" not in stripped, "entry must be a single line"
    assert 1 <= len(stripped) <= 200, f"entry is {len(stripped)} chars, gate is 1-200"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(stripped)
    print(f"wrote {len(stripped)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
