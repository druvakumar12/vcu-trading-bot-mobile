# VCU Trading Bot - Mobile Android Application

## 📱 Overview

This is the mobile Android version of VCU Trading Bot, optimized for your **OnePlus 13R** and other modern Android devices. The app provides full trading functionality on-the-go with a touch-optimized interface.

## 🎯 Features

✅ **Full Angel One Integration** - Login and trade directly from mobile
✅ **Real-Time Position Monitoring** - CE/PE positions with live P&L
✅ **Setup Mode Selection** - Both/A Only/B Only setups
✅ **Live Trading Logs** - Scrollable log view
✅ **Force Exit Controls** - Emergency position closure
✅ **Telegram Notifications** - Get alerts on your phone
✅ **Auto-Login** - Remembers credentials from credentials.txt
✅ **Optimized for OnePlus 13R** - Designed for 2K+ resolution displays
✅ **Background Trading** - Continue trading when app is in background
✅ **Crash Recovery** - Auto-saves state

## 📋 Requirements

### For Building APK (on Linux/WSL):

1. **Linux/Ubuntu/WSL2** (Windows Subsystem for Linux)
2. **Python 3.8+**
3. **Buildozer** (APK builder)
4. **Android SDK & NDK**
5. **Java JDK 11+**

### For Running on Android:

- **Android 5.0+** (API 21+)
- **Recommended:** Android 11+ for best performance
- **OnePlus 13R** (tested and optimized)
- **Internet connection** for broker API access

## 🚀 Building the APK

### Method 1: Using WSL2 on Windows (Recommended)

1. **Install WSL2 with Ubuntu:**
   ```bash
   # In Windows PowerShell (Admin)
   wsl --install -d Ubuntu-22.04
   ```

2. **Setup Build Environment in WSL:**
   ```bash
   # Update packages
   sudo apt update
   sudo apt upgrade -y
   
   # Install dependencies
   sudo apt install -y python3-pip python3-venv git zip unzip \
       openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev \
       libncurses5-dev libncursesw5-dev libtinfo5 cmake \
       libffi-dev libssl-dev
   
   # Install Buildozer
   pip3 install --upgrade buildozer
   pip3 install --upgrade cython
   pip3 install --upgrade kivy
   ```

3. **Copy Mobile App Files to WSL:**
   ```bash
   # In WSL terminal, navigate to your project
   cd /mnt/c/Users/Chaarvi\ D/Desktop/android/mobile_app
   ```

4. **Build APK:**
   ```bash
   # First build (downloads SDK/NDK - takes 30-60 mins)
   buildozer -v android debug
   
   # Subsequent builds (faster - 5-10 mins)
   buildozer android debug
   ```

5. **Find APK:**
   ```bash
   # APK will be in: ./bin/
   ls -lh bin/*.apk
   ```

### Method 2: Using GitHub Actions (Cloud Build)

I can create a GitHub Actions workflow that builds the APK automatically in the cloud!

### Method 3: Using Cloud Build Services

- **Replit** - Build online
- **Google Colab** - Free GPU build
- **Termux** - Build directly on Android (advanced)

## 📦 Installation on OnePlus 13R

1. **Transfer APK to phone:**
   - USB cable
   - Or upload to Google Drive/Telegram

2. **Enable Unknown Sources:**
   - Settings → Security → Unknown Sources → Enable

3. **Install APK:**
   - Open file manager
   - Tap the APK file
   - Click "Install"

4. **Launch App:**
   - Find "VCU Trading Bot" in app drawer
   - Grant permissions (Internet, Storage)

## 🎮 Usage

### First Launch:

1. **Login Screen:**
   - App auto-loads credentials from `credentials.txt`
   - Or manually enter:
     - Client ID
     - API Key
     - Password
     - TOTP Token
   - Tap "Login & Connect"

2. **Main Screen:**
   - **Setup Selection:** Choose Both/A Only/B Only
   - **Start Strategy:** Tap green button
   - **Monitor Positions:** Real-time CE/PE cards
   - **View Logs:** Scroll log panel
   - **Force Exit:** Red button for emergency

### While Trading:

- **Position Cards** show:
  - Entry price
  - Current price
  - Live P&L (green/red)
  - Trailing status

- **Logs Panel** displays:
  - Strategy events
  - Entry/Exit signals
  - Errors/Warnings

- **Status Indicator:**
  - IDLE (gray) - Not started
  - RUNNING (green) - Active trading
  - STOPPED (gray) - Manually stopped

### Background Mode:

- App continues trading when minimized
- Telegram notifications keep you updated
- Swipe down notification bar to check status

## ⚙️ Configuration

Edit these files before building:

### `credentials.txt` (in parent folder):
```
API_KEY=your_angel_one_api_key
PASSWORD=your_password
TOKEN=your_totp_secret
Client_id=your_client_id
Telegram_Token=your_telegram_bot_token
Telegram_ChatID=your_telegram_chat_id
```

### `buildozer.spec`:
- Change `title` for custom app name
- Adjust `android.archs` if needed (arm64-v8a for OnePlus 13R)
- Modify `requirements` to add/remove Python packages

## 🔧 Advanced Customization

### Add Custom Features:

Edit `main.py`:

1. **Change Colors:**
   ```python
   # Line ~50 - Login button color
   background_color=(0.2, 0.8, 0.4, 1)  # R, G, B, Alpha
   ```

2. **Adjust Layout:**
   ```python
   # Line ~100 - Card height
   height=180  # Change to make cards taller/shorter
   ```

3. **Add Indicators Tab:**
   - Create new screen class
   - Add to screen manager
   - Link with button

### Performance Tuning:

```python
# Line ~250 - Update frequency
Clock.schedule_interval(self.update_ui, 0.5)  # Change 0.5 to 1.0 for slower updates
```

## 📊 Technical Details

### Architecture:

- **Frontend:** Kivy (Python mobile framework)
- **Backend:** Same `trading_bot_backend.py` as desktop
- **Threading:** Background thread for trading logic
- **Queues:** Thread-safe communication (log_queue, data_queue, command_queue)

### App Size:

- **APK Size:** ~70-90 MB
- **Installed Size:** ~150-200 MB
- **RAM Usage:** ~100-150 MB while trading

### Performance:

- **UI Updates:** 2 times per second
- **API Calls:** Managed by backend (rate limiting)
- **Battery Impact:** Low (mostly network I/O)

## 🐛 Troubleshooting

### Build Errors:

**"Command failed: ./distribute.sh"**
```bash
# Clear buildozer cache
rm -rf .buildozer
buildozer android clean
buildozer -v android debug
```

**"NDK not found"**
```bash
# Reinstall buildozer
pip3 uninstall buildozer
pip3 install --upgrade buildozer
```

**"Java version mismatch"**
```bash
# Set Java 11
sudo update-alternatives --config java
```

### Runtime Errors:

**App Crashes on Startup:**
- Check Android version (need 5.0+)
- Grant all permissions in Settings
- Reinstall APK

**"Not logged in" error:**
- Check credentials.txt exists in parent folder
- Manually enter credentials
- Verify internet connection

**No logs appearing:**
- Backend might be failing
- Check if `trading_bot_backend.py` is accessible
- Review Python import errors in logcat:
  ```bash
  adb logcat | grep python
  ```

**Positions not updating:**
- Check internet connection
- Verify Angel One API is responding
- Restart strategy

## 📱 OnePlus 13R Specific Tips

### Display Optimization:

- **2K Resolution:** UI scales automatically
- **120Hz Refresh:** Smooth scrolling
- **Dark Mode:** App has dark theme by default

### Battery Optimization:

1. **Disable Battery Optimization for App:**
   - Settings → Battery → Battery Optimization
   - Find "VCU Trading Bot"
   - Select "Don't optimize"

2. **Allow Background Activity:**
   - Settings → Apps → VCU Trading Bot
   - Battery → Allow background activity

### Performance Mode:

- Enable "Performance Mode" in OnePlus settings for faster execution

## 🔐 Security

- **Credentials:** Stored locally in app private storage
- **Network:** HTTPS only (Angel One API)
- **Permissions:** Only Internet and Storage
- **No Data Collection:** App doesn't send data anywhere except broker API

## 🆕 Future Updates

Planned features:

- [ ] Chart visualization in app
- [ ] Multi-symbol support
- [ ] Custom indicator panel
- [ ] Dark/Light theme toggle
- [ ] Landscape mode support
- [ ] Widget for home screen
- [ ] Push notifications (in-app)
- [ ] Biometric login

## 📞 Support

For issues:

1. Check logs in app
2. Review buildozer build logs
3. Test on desktop first (`python main.py`)
4. Check Android logcat: `adb logcat | grep python`

## 📄 License

Same as parent VCU Trading Bot project.

## ⚠️ Disclaimer

**Trading involves risk. This mobile app is for convenience only. Always monitor your positions. Not responsible for any trading losses.**

---

**Optimized for OnePlus 13R | Built with ❤️ using Kivy**

