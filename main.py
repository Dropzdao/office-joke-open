#!/usr/bin/env python3
"""Office joke entry for the make.fun bounty.

Writes a single line of office comedy to /output/entry.txt.
Deterministic, stdlib-only, no network access.
"""

import os

ENTRY = (
    "I asked IT for a second monitor; they gave me a second manager "
    "instead \u2014 same glare, worse resolution."
)


def validate(entry: str) -> None:
    """Entry must be a single non-blank line of 1-200 characters."""
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
