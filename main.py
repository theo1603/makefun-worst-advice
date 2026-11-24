"""Worst AI Advice entry.

Writes one original line of hilariously bad AI advice to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (138 characters): great news, a dying phone battery
just needs the microwave — and the beeping means it is working.
"""

import os

LINE = "Great news: a dying phone battery needs 30 seconds in the microwave — the waves recharge the lithium, and the beeping means it is working."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
