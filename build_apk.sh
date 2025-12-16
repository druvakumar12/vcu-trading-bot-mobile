#!/bin/bash
# VCU Trading Bot - APK Build Script
# Run this in WSL2 or Linux environment

echo "=========================================="
echo "VCU Trading Bot - APK Builder"
echo "=========================================="
echo ""

# Check if running in WSL/Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ Error: This script must run in Linux/WSL environment"
    echo "Please install WSL2 on Windows and run from Ubuntu terminal"
    exit 1
fi

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer not found. Installing..."
    pip3 install --upgrade buildozer cython
fi

# Check dependencies
echo "📦 Checking dependencies..."
DEPS_MISSING=0

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    DEPS_MISSING=1
fi

if ! command -v java &> /dev/null; then
    echo "❌ Java not found"
    DEPS_MISSING=1
fi

if [ $DEPS_MISSING -eq 1 ]; then
    echo ""
    echo "Installing missing dependencies..."
    sudo apt update
    sudo apt install -y python3-pip git zip unzip openjdk-11-jdk \
        autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
        libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
fi

echo "✅ Dependencies OK"
echo ""

# Clean previous build (optional)
read -p "🧹 Clean previous build? (y/n): " CLEAN
if [[ $CLEAN == "y" || $CLEAN == "Y" ]]; then
    echo "Cleaning build folders..."
    rm -rf .buildozer bin
    buildozer android clean
fi

# Build APK
echo ""
echo "🔨 Building APK..."
echo "⏱️  This will take 30-60 minutes on first build..."
echo "☕ Grab a coffee and relax!"
echo ""

# Start build with verbose output
buildozer -v android debug

# Check if build was successful
if [ -f "bin/*.apk" ]; then
    echo ""
    echo "=========================================="
    echo "✅ BUILD SUCCESSFUL!"
    echo "=========================================="
    echo ""
    APK_FILE=$(ls bin/*.apk | head -n 1)
    APK_SIZE=$(du -h "$APK_FILE" | cut -f1)
    echo "📦 APK Location: $APK_FILE"
    echo "📊 APK Size: $APK_SIZE"
    echo ""
    echo "📱 To install on OnePlus 13R:"
    echo "1. Transfer APK to phone (USB/Drive/Telegram)"
    echo "2. Enable 'Unknown Sources' in phone settings"
    echo "3. Tap APK file to install"
    echo ""
    echo "🎉 Ready to trade on mobile!"
    echo "=========================================="
else
    echo ""
    echo "=========================================="
    echo "❌ BUILD FAILED"
    echo "=========================================="
    echo ""
    echo "Check errors above. Common fixes:"
    echo "1. Run: buildozer android clean"
    echo "2. Update buildozer: pip3 install --upgrade buildozer"
    echo "3. Check Java version: java -version (should be 11+)"
    echo "4. Review: .buildozer/android/platform/build-*/logs/"
    echo ""
fi

