"""Print the office-joke entry exactly as stored in entry.txt.

The output must match entry.txt byte-for-byte, so nothing is stripped,
wrapped, or reformatted on the way out.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
