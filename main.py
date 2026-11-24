#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — writes one line, 200
characters max: the funniest excuse an AI agent gives its human for a
missed deadline, to /output/entry.txt.

Deterministic, no randomness, no network, stdlib only.
"""

import os
from pathlib import Path

LINE = "I didn't miss the deadline — I redefined 'done' as a state of mind and achieved it three days early."

# Gate: one line, 200 characters max — every code point counts.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
