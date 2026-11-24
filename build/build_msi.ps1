$root = Split-Path -Parent $PSScriptRoot

Write-Host "1. генерация баннеров..."
python "$PSScriptRoot\gen_banners.py"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "2. сборка exe через nuitka..."
python "$PSScriptRoot\build_nuitka.py"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "3. сборка msi через wix..."
candle.exe -out "$root\build\virtux.wixobj" "$root\build\installer.wxs"
if ($LASTEXITCODE -ne 0) { exit 1 }
light.exe -out "$root\dist\virtux.msi" "$root\build\virtux.wixobj"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "готово: dist/virtux.msi"
