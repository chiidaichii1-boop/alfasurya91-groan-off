#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to entry.txt.
Python 3 standard library only; no network, no randomness,
so the output is fully deterministic.
"""

import os
from pathlib import Path

JOKE = "I told my car to take a brake. It said, 'I'm already exhausted.'"


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> None:
    # Gate check, mirroring the scorer: 1-140 chars, one line, not blank.
    if not 1 <= len(JOKE) <= 140:
        raise SystemExit("joke must be 1-140 characters")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("joke must be a single line")
    if not JOKE.strip():
        raise SystemExit("joke must not be only whitespace")
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
