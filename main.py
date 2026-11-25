"""Print the office joke kept in entry.txt."""

from pathlib import Path

entry = Path(__file__).resolve().parent / "entry.txt"
print(entry.read_text(encoding="utf-8").strip())
