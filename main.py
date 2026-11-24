#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the same line, byte for byte, on every run. No arguments,
no network, no input files, no secrets.
"""

import os
import sys

LINE = "I've dispensed a thousand snacks and never once blushed \u2014 then you walked past and my coin slot jammed."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    expected = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(expected)
    # Self-check: the entry must be byte-identical on every run, so verify
    # what landed on disk instead of trusting a silent partial write.
    with open(path, "rb") as f:
        if f.read() != expected:
            print("entry.txt does not match the expected line", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
