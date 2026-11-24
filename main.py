#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence (1-220 chars) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no time.
"""

import os

SENTENCE = (
    "The Emergency Square: a toilet-paper roll that saves one last square "
    "for the moment you discover you're out, sealed behind a tiny glass "
    "panel marked \"break in case of emergency.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
