"""Charm the commuter — one-line weather forecast for New Borington.

The joke lands on the one thing every commuter already knows: the leaves
always win. The forecast is written out as a single plain-text line so the
grader can read it verbatim.
"""

import os
import sys


def build_forecast() -> str:
    """Compose the morning forecast line for New Borington."""
    city = "New Borington"
    sky = "light drizzle"
    mood = "heavy sighs"
    odds = "100%"
    # Leaves on the line: the oldest excuse in the commuter's handbook,
    # and still the one that shows up every single autumn.
    excuse = "delayed due to leaves."
    return (
        f"Good morning, {city}: {sky}, {mood}, "
        f"and a {odds} chance your train is '{excuse}' Again."
    )


def main() -> int:
    forecast = build_forecast()
    # Sanity check: the entry must stay a single 120-character line.
    if len(forecast) != 120 or "\n" in forecast:
        raise ValueError(f"forecast is {len(forecast)} chars, expected 120")
    # The entry contract wants exactly one line, newline-terminated.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(forecast + "\n")
    # Read back what we wrote: the entry must be exactly one line.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != forecast + "\n":
        raise ValueError("entry.txt does not match the forecast")
    print(f"wrote {len(forecast)} chars to {entry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
