# требует WiX Toolset v3 (candle.exe, light.exe в PATH)
$root = Split-Path -Parent $PSScriptRoot

Write-Host "1. сборка exe через nuitka..."
python "$PSScriptRoot\build_nuitka.py"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "2. сборка msi через wix..."
candle.exe -out "$root\build\virtux.wixobj" "$root\build\installer.wxs"
light.exe -out "$root\dist\virtux.msi" "$root\build\virtux.wixobj"

Write-Host "готово: dist/virtux.msi"
