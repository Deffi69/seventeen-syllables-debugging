"""make.fun Seventeen Syllables of Debugging entry.

Writes one haiku about debugging (5-7-5 syllables, 17 in total) to
/output/entry.txt.

Syllable count, line by line:
  "I changed just one line"        -> I(1) changed(1) just(1) one(1) line(1) = 5
  "now the error lives elsewhere"  -> now(1) the(1) er-ror(2) lives(1) else-where(2) = 7
  "the bug has moved house"        -> the(1) bug(1) has(1) moved(1) house(1) = 5
"""

import os

HAIKU = (
    "I changed just one line\n"
    "now the error lives elsewhere\n"
    "the bug has moved house\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
