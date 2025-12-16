# APK Build Solutions for VCU Trading Bot

## Current Issue
Building APK locally on Windows using WSL2 is encountering a known buildozer issue with git on NTFS filesystem.
Error: `AttributeError: 'NoneType' object has no attribute 'split'` when buildozer tries to detect git branch.

## ✅ RECOMMENDED SOLUTIONS (Easiest to Hardest)

### Solution 1: GitHub Actions (RECOMMENDED - No Local Setup Required)
**This is the easiest and most reliable method!**

#### Steps:
1. Create a GitHub account at https://github.com
2. Create a new private repository called `vcu-trading-bot-mobile`
3. Upload all files from `C:\Users\Chaarvi D\Desktop\android\mobile_app\` to the repository
4. Create `.github/workflows/build-apk.yml` with the following content:

```yaml
name: Build Android APK

on:
  workflow_dispatch:
  push:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
        pip install --upgrade buildozer cython
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: vcutradingbot-apk
        path: bin/*.apk
```

5. Go to "Actions" tab → "Build Android APK" → "Run workflow"
6. Wait 30-40 minutes for the build to complete
7. Download the APK from the "Artifacts" section

**Pros:** No local setup, reliable, automated
**Time:** 30-40 minutes per build
**Success Rate:** 95%+

---

### Solution 2: Use Native Linux (Virtual Machine or Dual Boot)

If you have access to native Ubuntu Linux:

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev python3-pip

# Install buildozer
pip3 install --user buildozer cython

# Copy your project to Linux
# Then cd to project directory
cd /path/to/mobile_app

# Build
buildozer android debug
```

**Pros:** Fast, reliable, full control
**Time:** 1-2 hours setup, then 30-60 min per build
**Success Rate:** 90%+

---

### Solution 3: Fix WSL2 Build (Advanced)

Try building from WSL's native filesystem instead of Windows NTFS:

```bash
# In WSL terminal:
cd ~
mkdir mobile_app_build
cd mobile_app_build

# Copy all files from Windows to WSL
cp /mnt/c/Users/"Chaarvi D"/Desktop/android/mobile_app/* .

# Ensure buildozer is in PATH
export PATH=$PATH:~/.local/bin

# Build
buildozer android debug

# Copy APK back to Windows when done
cp bin/*.apk /mnt/c/Users/"Chaarvi D"/Desktop/
```

**Pros:** Local build, keeps files accessible in Windows
**Time:** 30-60 minutes
**Success Rate:** 70% (git issues may persist)

---

### Solution 4: Use Docker

```powershell
# Install Docker Desktop for Windows first
# Then run:

docker run --rm -v "${PWD}:/app" -w /app kivy/buildozer android debug

# This creates an isolated Linux environment for building
```

**Pros:** Consistent environment, no WSL issues
**Time:** Initial download 30 min, then 30-60 min per build
**Success Rate:** 85%

---

### Solution 5: Cloud Build Services

Use services like:
- **Buildozer Web** (if available)
- **CircleCI** (free tier available)
- **Travis CI** (free for open source)

Similar setup to GitHub Actions but with different platforms.

---

## Quick Test Before Building APK

Test the app on your Windows desktop first:

```powershell
cd "C:\Users\Chaarvi D\Desktop\android\mobile_app"
pip install -r requirements_mobile.txt
python test_mobile_desktop.py
```

This runs the mobile interface on your desktop to verify functionality before building APK.

---

## What You Need After Building

Once you have the APK:

1. **Transfer to OnePlus 13R:**
   - USB cable
   - Google Drive/Dropbox
   - Telegram/WhatsApp (send to yourself)
   - Email attachment

2. **Install on Phone:**
   - Enable "Install from Unknown Sources" in Settings
   - Open the APK file
   - Follow installation prompts

3. **Configure App:**
   - Enter your Angel One credentials
   - Set trading parameters
   - Test with small quantities first!

---

## Need Help?

If you want to proceed with GitHub Actions (recommended), I can help you:
1. Create the repository
2. Set up the workflow file
3. Monitor the build
4. Download the APK

Just let me know which solution you'd like to pursue!

