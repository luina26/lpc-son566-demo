@echo off
rem Build standalone executable using PyInstaller

set SCRIPT_NAME=your_script.py
set DIST_DIR=dist

rem Check if PyInstaller is installed
pip show pyinstaller >nul 2>nul
if errorlevel 1 (
    echo PyInstaller is not installed. Please install it using the command "pip install pyinstaller".
    exit /b 1
)

rem Create the executable
pyinstaller --onefile --distpath %DIST_DIR% %SCRIPT_NAME%
echo Build completed!