"""Real-Life Patch Notes — writes the entry line to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "v1.4.7: fixed a bug where the brain replayed an embarrassing moment from 2009 at 3 a.m. for no reason."


def main():
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError("entry must be 1-160 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
