@echo off
REM Quick build script for Windows (using WSL2)

echo ========================================
echo VCU Trading Bot - Windows APK Builder
echo ========================================
echo.

REM Check if WSL is installed
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: WSL not installed!
    echo.
    echo To install WSL2:
    echo 1. Open PowerShell as Administrator
    echo 2. Run: wsl --install -d Ubuntu-22.04
    echo 3. Restart computer
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo WSL detected. Starting build in Ubuntu...
echo.

REM Navigate to project and build
wsl -e bash -c "cd /mnt/c/Users/Chaarvi\ D/Desktop/android/mobile_app && chmod +x build_apk.sh && ./build_apk.sh"

REM Check if APK was created
if exist "bin\*.apk" (
    echo.
    echo ========================================
    echo SUCCESS! APK built successfully!
    echo ========================================
    echo.
    echo APK Location: mobile_app\bin\
    echo.
    echo Next steps:
    echo 1. Transfer APK to your OnePlus 13R
    echo 2. Enable Unknown Sources in phone settings
    echo 3. Install APK
    echo 4. Open VCU Trading Bot app
    echo.
    pause
) else (
    echo.
    echo ========================================
    echo BUILD FAILED - Check errors above
    echo ========================================
    echo.
    echo Common fixes:
    echo 1. Run: wsl -e bash -c "cd /mnt/c/Users/Chaarvi\ D/Desktop/android/mobile_app && buildozer android clean"
    echo 2. Update buildozer: wsl -e bash -c "pip3 install --upgrade buildozer"
    echo 3. Check disk space: wsl -e bash -c "df -h"
    echo.
    pause
)

