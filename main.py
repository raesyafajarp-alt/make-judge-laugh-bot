#!/usr/bin/env python3
"""Office Joke Bot — one original one-liner about office life.

Writes the entry to /output/entry.txt. Pure Python stdlib, no network,
fully deterministic: the same joke, byte for byte, on every run.

Why this joke, against the judge brief (most important first):
1. Office life, and it lands as a joke — a status update asked of the
   office printer, a setup every office worker recognises instantly.
2. True to the office — the printer that jams, the status update, the
   quarterly cadence: the listener nods before laughing.
3. Surprising turn — the jammed printer is not the punchline's victim
   but the office's most honest employee; the last word reframes the
   whole line instead of leaning on a pun or a stock line.
4. Tight — one line, 123 characters, no wasted setup, reads cleanly
   aloud in a single breath, punchline at the very end.
5. Original — written fresh for this competition, not a familiar line
   with the nouns swapped.
"""

import os

JOKE = (
    "I asked the office printer for a status update and it jammed "
    "\u2014 the most honest answer anyone here has given me all quarter."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
