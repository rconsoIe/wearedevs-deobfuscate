@echo off
echo Building WeAreDevs Deobfuscator...
echo.

pyinstaller --onefile --name deobfuscator --clean deobfuscator_console.py

echo.
echo Builded!
pause
