import os
from pathlib import Path

LINE = "Good morning, New Borington: light drizzle, heavy sighs, and a 100% chance your train is 'delayed due to leaves.' Again."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
