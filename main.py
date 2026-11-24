#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — make.fun bounty entry.

Writes one line of office comedy to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I asked IT for a second monitor; they gave me a second manager "
    "instead — same glare, worse resolution."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
