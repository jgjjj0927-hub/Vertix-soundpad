import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

def build():
    subprocess.run([
        sys.executable, "-m", "nuitka",
        "--standalone",
        "--onefile",
        "--windows-console-mode=disable",
        "--windows-icon-from-ico", str(ROOT / "assets" / "icon.ico"),
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
    print("готово: dist/virtux.exe")
