"""One-line entry for make.fun's "Make the Judge Smile" bounty.

The entry is a single warm line about a small good thing that happened
today: a stray cat paying rent in leaves. Warmth comes first (the cat
bringing a gift), the surprise is the rent framing, and the one concrete
detail is the single leaf on the doormat — a small, specific image rather
than a vague happy mood. The line is written to entry.txt under
$MAKEFUN_OUTPUT_DIR (or /output) and verified byte-for-byte against the
TEXT constant.
"""

import os
import sys

TEXT = "The stray cat outside my door left one leaf on my doormat this morning — her rent for the bowl of milk I left yesterday."


def main() -> int:
    if not TEXT or not TEXT.strip():
        print("entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"entry is {len(TEXT)} characters, over the 200 limit", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
