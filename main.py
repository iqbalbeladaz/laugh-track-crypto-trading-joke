"""laugh-track-crypto-trading-joke: one line about crypto trading life.

The joke turns on the trader's most honest habit: obsessive chart-checking.
The setup promises reform ("finally stopped checking every five minutes"),
the turn admits the reform lasted one minute ("now I check it every four"),
and the punchline reframes the failure as a system: that single minute of
not looking *is* the entire risk management plan. It is true to trading
life (the chart, the compulsion, the self-deception dressed up as strategy),
tight (150 of 200 characters), and ends on its strongest beat.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "I finally stopped checking the chart every five minutes. Now I check it every four \u2014 that one minute of not looking is my entire risk management plan."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    if any(ord(ch) < 0x20 for ch in ENTRY):
        raise ValueError("entry must not contain control characters")
    if "  " in ENTRY:
        raise ValueError("entry must not contain double spaces")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
