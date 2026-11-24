#!/usr/bin/env python3
"""Everyday Wonder entry — writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: no randomness, no network, stdlib only. The sentence is a
single everyday moment (an ice cube in a glass) turned at an unfamiliar
angle — a scale shift — so the surprise lands in one read.
"""

import os

SENTENCE = (
    "The last ice cube cracked like a glacier calving, "
    "and for a second my glass held the whole Arctic."
)


def main() -> None:
    # Self-check: the gate requires 1-200 UTF-8 chars and a single sentence.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "sentence must be exactly one sentence"
    )
    assert SENTENCE.strip() == SENTENCE, "no leading/trailing whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
