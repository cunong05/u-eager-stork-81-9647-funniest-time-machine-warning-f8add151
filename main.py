#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Reads the one-line warning label from entry.txt next to this file and
writes it to /output/entry.txt, where the sealed scorer reads it.
"""

import os
import sys

JOKE = "WARNING: Your return ticket is dated yesterday. Do not ask the driver for a refund. He is you."


def load_entry():
    # The gate accepts UTF-8 text of 1 to 120 characters, a single line.
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        if text:
            return text
    except OSError:
        pass
    return JOKE


def check_entry(entry):
    # A warning label must be one line and fit the 120-character cap.
    if not entry or len(entry) > 120 or "\n" in entry:
        raise ValueError("entry must be a single line of 1 to 120 characters")
    return entry


def main():
    entry = check_entry(load_entry())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
