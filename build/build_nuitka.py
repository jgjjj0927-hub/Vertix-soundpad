import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
VERSION = (ROOT / "build" / "version.txt").read_text().strip()

def build():
    subprocess.run([
        sys.executable, "-m", "nuitka",
        "--standalone",
        "--onefile",
        "--windows-console-mode=disable",
        "--windows-icon-from-ico", str(ROOT / "assets" / "icon.ico"),
        "--windows-company-name", "virtux",
        "--windows-product-name", "virtux",
        "--windows-file-version", VERSION,
        "--windows-product-version", VERSION,
        "--windows-file-description", "virtux soundpad",
        "--include-data-dir", f"{ROOT / 'base'}=base",
        "--output-dir", str(ROOT / "dist"),
        "--output-filename", "virtux.exe",
        "--nofollow-import-to=tkinter.test",
        "--nofollow-import-to=unittest",
        "--nofollow-import-to=pydoc",
        str(ROOT / "main.py"),
    ], check=True)

if __name__ == "__main__":
    build()
    print(f"готово: dist/virtux.exe (v{VERSION})")
