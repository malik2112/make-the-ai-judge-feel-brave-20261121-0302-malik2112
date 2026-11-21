#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-brave-20261121-0302.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a lock-keeper vignette: a slow, repeated quarter-turn
of an iron wheel, water finding its level, and a quiet step forward
onto wet boards. Concrete work, unhurried rhythm, no instructions.
"""

import os

TEXT = (
    "He turns the iron wheel a quarter at a time. The gate sighs. "
    "Black water finds the crack and steadies. A barge waits below, "
    "rope slack. When the levels match, he lifts the pin, opens the "
    "gate wide, and steps onto the wet boards to wave it through."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
