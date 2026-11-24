@echo off
setlocal

cd /d "%~dp0"

echo [1/4] проверка python...
python --version >nul 2>&1
if errorlevel 1 (
    echo python не найден в PATH. установи python и добавь в PATH.
    pause
    exit /b 1
)

echo [2/4] установка зависимостей...
python -m pip install --upgrade pip >nul
python -m pip install -r build\requirements-build.txt
if errorlevel 1 (
    echo ошибка установки зависимостей.
    pause
    exit /b 1
)

echo [3/4] генерация баннеров...
python build\gen_banners.py
if errorlevel 1 (
    echo ошибка генерации баннеров.
    pause
    exit /b 1
)

echo [4/4] сборка exe через nuitka...
python build\build_nuitka.py
if errorlevel 1 (
    echo ошибка сборки exe.
    pause
    exit /b 1
)

echo [5/5] сборка msi через wix...
where candle.exe >nul 2>&1
if errorlevel 1 (
    echo WiX не найден в PATH.
    echo установи: choco install wixtoolset -y
    echo или добавь C:\Program Files (x86)\WiX Toolset v3.14\bin в PATH.
    pause
    exit /b 1
)

candle.exe -out build\virtux.wixobj build\installer.wxs
if errorlevel 1 (
    echo ошибка candle.exe.
    pause
    exit /b 1
)

light.exe -out dist\virtux.msi build\virtux.wixobj
if errorlevel 1 (
    echo ошибка light.exe.
    pause
    exit /b 1
)

echo.
echo готово: dist\virtux.msi
pause
