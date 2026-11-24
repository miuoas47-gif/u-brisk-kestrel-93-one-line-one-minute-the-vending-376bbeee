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
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
