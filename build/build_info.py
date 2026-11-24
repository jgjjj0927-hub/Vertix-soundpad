import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
VERSION = (ROOT / "build" / "version.txt").read_text().strip()

# Nuitka читает это через --windows-version-info
if __name__ == "__main__":
    print(VERSION)
