@echo off
setlocal

cd /d "%~dp0"

echo [1/5] checking python...
python --version >nul 2>&1
if errorlevel 1 (
    echo python not found in PATH. install python and add it to PATH.
    pause
    exit /b 1
)

echo [2/5] installing build dependencies...
python -m pip install --upgrade pip >nul
python -m pip install -r build\requirements-build.txt
if errorlevel 1 (
    echo failed to install dependencies.
    pause
    exit /b 1
)

echo [3/5] generating installer banners...
python build\gen_banners.py
if errorlevel 1 (
    echo failed to generate banners.
    pause
    exit /b 1
)

echo [4/5] building exe with nuitka...
python build\build_nuitka.py
if errorlevel 1 (
    echo failed to build exe.
    pause
    exit /b 1
)

echo [5/5] building msi with wix...
where candle.exe >nul 2>&1
if errorlevel 1 (
    echo WiX not found in PATH.
    echo install: choco install wixtoolset -y
    echo or add C:\Program Files (x86)\WiX Toolset v3.14\bin to PATH.
    pause
    exit /b 1
)

candle.exe -out build\virtux.wixobj build\installer.wxs
if errorlevel 1 (
    echo candle.exe failed.
    pause
    exit /b 1
)

light.exe -out dist\virtux.msi build\virtux.wixobj
if errorlevel 1 (
    echo light.exe failed.
    pause
    exit /b 1
)

echo.
echo done: dist\virtux.msi
pause
