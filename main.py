#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes the winning Wi-Fi network name to /output/entry.txt.

The name: "NoWiFiSinceTheDivorce" (21 characters).
The story in four words: the Wi-Fi died with the marriage and never came
back — the divorcee, the empty flat, the ex who took everything, router
included. Chosen by hand from 13 candidates against the judge brief in its
own order (see candidates.md); no automated judge was used for selection.
"""

import os

ENTRY = "NoWiFiSinceTheDivorce"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # A Wi-Fi name must be one tight token: no spaces, no newline, plain ASCII,
    # and inside the gate (1-32 characters). Anything else refuses to write.
    if not ENTRY.isascii() or any(ch.isspace() for ch in ENTRY):
        raise SystemExit("entry must be a single ASCII token with no whitespace")
    if not (1 <= len(ENTRY) <= 32):
        raise SystemExit(f"entry must be 1-32 characters, got {len(ENTRY)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what the grader reads must be byte-for-byte the name.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            raise SystemExit("round-trip mismatch: entry.txt is not the entry")


if __name__ == "__main__":
    main()
