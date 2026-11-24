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
        "--disable-console",
        f"--windows-icon-from-ico={ROOT / 'assets' / 'icon.ico'}",
        "--windows-company-name=virtux",
        "--windows-product-name=virtux",
        "--windows-file-version=1.0.0.0",
        "--windows-product-version=1.0.0.0",
        "--windows-file-description=virtux soundpad",
        f"--include-data-dir={ROOT / 'base'}=base",
        f"--output-dir={ROOT / 'dist'}",
        "--output-filename=virtux.exe",
        "--nofollow-import-to=tkinter.test",
        "--nofollow-import-to=unittest",
        "--nofollow-import-to=pydoc",
        str(ROOT / "main.py"),
    ], check=True)

if __name__ == "__main__":
    build()
    print(f"done: dist/virtux.exe (v{VERSION})")
