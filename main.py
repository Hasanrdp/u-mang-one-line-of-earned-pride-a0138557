#!/usr/bin/env python3
"""One Line of Earned Pride entry: one quiet, earned moment of pride.

The program writes a single original line (143 characters, well inside
the 1-240 character gate) to /output/entry.txt and nothing else. It is
fully deterministic: the same bytes on every run, no network, no
randomness, no input read.

The line: a shoemaker who has spent forty years resoling other people's
shoes finally finishes a pair for himself, laces them up, and walks to
the market in them. The pride is earned inside the line by the long
effort itself, and it lands on the last words.
"""

import os

LINE = "Forty years of resoling other people's shoes, and this morning he finished a pair for himself, laced them up, and walked to the market in them."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("line must not be blank")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
