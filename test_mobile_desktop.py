# Test the mobile app on desktop before building APK
    VCUMobileApp().run()
    from main import VCUMobileApp
if __name__ == '__main__':
# Run the mobile app

os.environ['KIVY_WINDOW'] = 'sdl2'
# Set window size for testing

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add parent directory to path

import sys
import os

# Run: python test_mobile_desktop.py

