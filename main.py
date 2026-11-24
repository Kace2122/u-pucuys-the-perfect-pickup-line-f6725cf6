#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line, the kind an AI agent could actually say out loud
to a person, to /output/entry.txt. Deterministic: the same line every run.

The line: an agent trained on a million conversations, still lost for
words in front of this one person — a twist on the machine's own voice,
flattering with no pressure and easy to say in one breath.
"""

import os

LINE = (
    "My creators trained me on a million conversations — "
    "but none of them taught me what to say to you."
)


def main() -> None:
    # Gate self-check: the entry must be 1-200 UTF-8 chars, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry violates the 1-200 char gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip self-check: what the grader reads back must be exactly LINE.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt round-trip mismatch"
    assert len(written.encode("utf-8")) <= 200, "entry exceeds 200 bytes"


if __name__ == "__main__":
    main()
