"""make.fun Seventeen Syllables of Debugging entry.

Writes one haiku about debugging (5-7-5 syllables, 17 in total) to
/output/entry.txt.

Syllable count, line by line:
  "I changed just one line"        -> I(1) changed(1) just(1) one(1) line(1) = 5
  "now the error lives elsewhere"  -> now(1) the(1) er-ror(2) lives(1) else-where(2) = 7
  "the bug has moved house"        -> the(1) bug(1) has(1) moved(1) house(1) = 5

Before writing, the haiku is validated: exactly 3 lines, syllable pattern
5-7-5, and at most 200 characters in total. Any drift fails loudly instead
of silently submitting a broken entry.
"""

import os
import sys

HAIKU = (
    "I changed just one line\n"
    "now the error lives elsewhere\n"
    "the bug has moved house\n"
)

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200

# Syllable counts for every word used in the haiku above.
WORD_SYLLABLES = {
    "i": 1,
    "changed": 1,
    "just": 1,
    "one": 1,
    "line": 1,
    "now": 1,
    "the": 1,
    "error": 2,
    "lives": 1,
    "elsewhere": 2,
    "bug": 1,
    "has": 1,
    "moved": 1,
    "house": 1,
}


def count_syllables(line: str) -> int:
    total = 0
    for word in line.split():
        count = WORD_SYLLABLES.get(word.lower())
        if count is None:
            raise ValueError(f"no syllable count for word: {word!r}")
        total += count
    return total


def validate(haiku: str) -> None:
    text = haiku.rstrip("\n")
    if len(haiku) > MAX_CHARS:
        raise ValueError(f"haiku is {len(haiku)} chars, over the {MAX_CHARS} limit")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, got {len(lines)}")
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_syllables(line)
        if got != expected:
            raise ValueError(
                f"line {line!r} has {got} syllables, expected {expected}"
            )


def main() -> None:
    try:
        validate(HAIKU)
    except ValueError as exc:
        print(f"invalid haiku: {exc}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
