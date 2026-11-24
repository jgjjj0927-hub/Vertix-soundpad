Usage: python.exe -m nuitka [--mode=compilation_mode] [--run] [options] main_module.py

    Note: For general plugin help (they often have their own
    command line options too), consider the output of
    '--help-plugins'.

__main__.py: error: The '--windows-icon-from-ico' option requires an argument with '--windows-icon-from-ico='.
Traceback (most recent call last):
  File "C:\Users\User\vertix\build\build_nuitka.py", line 30, in <module>
    build()
  File "C:\Users\User\vertix\build\build_nuitka.py", line 9, in build
    subprocess.run([
  File "C:\Users\User\AppData\Local\Programs\Python\Python311\Lib\subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python.exe', '-m', 'nuitka', '--standalone', '--onefile', '--windows-console-mode=disable', '--windows-icon-from-ico', 'C:\\Users\\User\\vertix\\assets\\icon.ico', '--windows-company-name', 'virtux', '--windows-product-name', 'virtux', '--windows-file-version', '1.0.0', '--windows-product-version', '1.0.0', '--windows-file-description', 'virtux soundpad', '--include-data-dir', 'C:\\Users\\User\\vertix\\base=base', '--output-dir', 'C:\\Users\\User\\vertix\\dist', '--output-filename', 'virtux.exe', '--nofollow-import-to=tkinter.test', '--nofollow-import-to=unittest', '--nofollow-import-to=pydoc', 'C:\\Users\\User\\vertix\\main.py']' returned non-zero exit status 2.
failed to build exe.
Для продолжения нажмите любую клавишу . .
