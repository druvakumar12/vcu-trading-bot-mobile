# -*- coding: utf-8 -*-
    VCUMobileApp().run()
if __name__ == '__main__':


        pass
        """Handle app resume (Android)"""
    def on_resume(self):

        return True
        """Handle app pause (Android)"""
    def on_pause(self):

        return sm

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(LoginScreen(name='login'))
        sm = ScreenManager()
        # Create screen manager

            ])
                Permission.READ_EXTERNAL_STORAGE
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.INTERNET,
            request_permissions([
            from android.permissions import request_permissions, Permission
        if platform == 'android':
        # Request permissions on Android

        self.title = 'VCU Trading Bot Mobile'
        """Build the app"""
    def build(self):

        self.credentials = None
        self.api_object = None
        super().__init__(**kwargs)
    def __init__(self, **kwargs):

    """Main application class"""
class VCUMobileApp(App):


        self.manager.current = 'login'

        app.credentials = None
        app.api_object = None
        app = App.get_running_app()

            self.stop_strategy()
        if self.strategy_running:
        """Logout and return to login screen"""
    def logout(self, instance):

            self.log_label.text = '\n'.join(lines[-100:])
        if len(lines) > 100:
        lines = self.log_label.text.split('\n')
        # Limit log size

        self.log_label.text += f"[{timestamp}] {message}\n"
        timestamp = DT.now().strftime("%H:%M:%S")
        """Add log message"""
    def add_log(self, message):

            self.pe_status_label.markup = True
                self.pe_status_label.text = '[color=00ff00]✅ Position Open[/color]'
            else:
                self.pe_status_label.text = '[color=00ffff]📈 Trailing Active[/color]'
            if data.get('trailing'):

            self.pe_pnl_label.markup = True
            self.pe_pnl_label.text = f"[color={color}]₹{pnl:.2f}[/color]"
            color = '00ff00' if pnl >= 0 else 'ff0000'
            pnl = data.get('pnl', 0)

            self.pe_current_label.text = f"₹{data.get('current', 0):.2f}"
            self.pe_entry_label.text = f"₹{data.get('entry', 0):.2f}"
        elif strike_type == 'PE':

            self.ce_status_label.markup = True
                self.ce_status_label.text = '[color=00ff00]✅ Position Open[/color]'
            else:
                self.ce_status_label.text = '[color=00ffff]📈 Trailing Active[/color]'
            if data.get('trailing'):

            self.ce_pnl_label.markup = True
            self.ce_pnl_label.text = f"[color={color}]₹{pnl:.2f}[/color]"
            color = '00ff00' if pnl >= 0 else 'ff0000'
            pnl = data.get('pnl', 0)

            self.ce_current_label.text = f"₹{data.get('current', 0):.2f}"
            self.ce_entry_label.text = f"₹{data.get('entry', 0):.2f}"
        if strike_type == 'CE':

        strike_type = data.get('strike_type')
        """Update position card with new data"""
    def update_position(self, data):

            pass
        except:
                    self.update_position(data)
                if data.get('type') == 'position':

                data = self.data_queue.get_nowait()
            while not self.data_queue.empty():
        try:
        # Process data updates

            pass
        except:
                self.add_log(f"[{timestamp}] {message}")
                timestamp, message, color = self.log_queue.get_nowait()
            while not self.log_queue.empty():
        try:
        # Process logs
        """Update UI from queues"""
    def update_ui(self, dt):

            self.add_log("Force exit all requested")
            self.command_queue.put({'type': 'force_exit_all'})
        if hasattr(self, 'bot') and self.bot:
        """Force exit all positions"""
    def force_exit_all(self, instance):

        self.add_log("Strategy stopped")
        self.status_label.markup = True
        self.status_label.text = '[color=808080]STOPPED[/color]'
        self.start_btn.background_color = (0.2, 0.8, 0.4, 1)
        self.start_btn.text = '▶ Start Strategy'
        self.strategy_running = False
        """Stop trading strategy"""
    def stop_strategy(self):

            self.start_btn.background_color = (0.2, 0.8, 0.4, 1)
            self.start_btn.text = '▶ Start Strategy'
            self.strategy_running = False
            self.add_log(f"Error: {str(e)}")
        except Exception as e:

            self.bot_thread.start()
            )
                daemon=True
                args=(lambda: self.strategy_running,),
                target=self.bot.run,
            self.bot_thread = threading.Thread(
            # Start bot thread

            )
                telegram_notifier
                strike_config,
                self.setup_mode,
                self.command_queue,
                self.data_queue,
                self.log_queue,
                app.api_object,
            self.bot = TradingBot(

                pass
            except:
                        self.add_log("Telegram enabled")
                        telegram_notifier = TelegramNotifier(telegram_token, telegram_chatid)
                    if telegram_token and telegram_chatid:

                    telegram_chatid = creds.get('Telegram_ChatID')
                    telegram_token = creds.get('Telegram_Token')

                                creds[key.strip()] = value.strip()
                                key, value = line.split('=', 1)
                            if '=' in line and not line.startswith('#'):
                            line = line.strip()
                        for line in f:
                    with open(creds_file, 'r', encoding='utf-8') as f:
                    creds = {}
                if os.path.exists(creds_file):
                creds_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.txt')
            try:
            telegram_notifier = None
            # Initialize Telegram

            }
                'quantity': 150
                'lot_size': 2,
                'max_premium': 190,
                'min_premium': 170,
                'mode': 'Auto',
            strike_config = {
            # Initialize backend

            self.add_log("Strategy started...")

            self.status_label.markup = True
            self.status_label.text = '[color=00ff00]RUNNING[/color]'
            self.start_btn.background_color = (0.8, 0.4, 0.2, 1)
            self.start_btn.text = '⏸ Stop Strategy'
            self.strategy_running = True

                return
                self.add_log("Error: Not logged in!")
            if not hasattr(app, 'api_object') or app.api_object is None:

            app = App.get_running_app()
        try:
        """Start trading strategy"""
    def start_strategy(self):

            self.stop_strategy()
        else:
            self.start_strategy()
        if not self.strategy_running:
        """Start/Stop strategy"""
    def toggle_strategy(self, instance):

        self.add_log(f"Setup mode: {mode}")
        self.setup_mode = mode
        """Set setup mode"""
    def set_setup(self, mode):

        return card

            self.pe_status_label = status_label
            self.pe_pnl_label = pnl_label
            self.pe_current_label = current_label
            self.pe_entry_label = entry_label
        else:
            self.ce_status_label = status_label
            self.ce_pnl_label = pnl_label
            self.ce_current_label = current_label
            self.ce_entry_label = entry_label
        if strike_type == 'CE':
        # Store references

        card.add_widget(status_label)
        )
            font_size='13sp'
            size_hint=(1, 0.3),
            markup=True,
            text='[color=808080]⏸ No Position[/color]',
        status_label = Label(
        # Status

        card.add_widget(info_grid)

        info_grid.add_widget(pnl_label)
        info_grid.add_widget(current_label)
        info_grid.add_widget(entry_label)

        pnl_label = Label(text='₹0', font_size='14sp', bold=True)
        current_label = Label(text='-', font_size='14sp', bold=True)
        entry_label = Label(text='-', font_size='14sp')

        info_grid.add_widget(Label(text='P&L', font_size='12sp', color=(0.7, 0.7, 0.7, 1)))
        info_grid.add_widget(Label(text='Current', font_size='12sp', color=(0.7, 0.7, 0.7, 1)))
        info_grid.add_widget(Label(text='Entry', font_size='12sp', color=(0.7, 0.7, 0.7, 1)))
        # Entry

        info_grid = GridLayout(cols=3, size_hint=(1, 0.5), spacing=5)
        # Info grid

        card.add_widget(header)
        )
            font_size='16sp'
            size_hint=(1, 0.2),
            markup=True,
            text=f'[b]{strike_type} Position[/b]',
        header = Label(
        # Header

        )
            spacing=5
            padding=10,
            height=180,
            size_hint=(1, None),
            orientation='vertical',
        card = BoxLayout(
        """Create position card for CE or PE"""
    def create_position_card(self, strike_type):

        self.add_widget(layout)

        layout.add_widget(log_scroll)
        log_scroll.add_widget(self.log_label)
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        )
            valign='top'
            halign='left',
            text_size=(Window.width - 40, None),
            size_hint_y=None,
            markup=True,
            text='Ready to start trading...\n',
        self.log_label = Label(
        log_scroll = ScrollView(size_hint=(1, 0.34))

        layout.add_widget(log_header)
        )
            font_size='16sp'
            size_hint=(1, 0.05),
            markup=True,
            text='[b]Trading Logs[/b]',
        log_header = Label(
        # Log Panel

        layout.add_widget(positions_scroll)
        positions_scroll.add_widget(positions_layout)

        positions_layout.add_widget(self.pe_card)
        self.pe_card = self.create_position_card('PE')
        # PE Position Card

        positions_layout.add_widget(self.ce_card)
        self.ce_card = self.create_position_card('CE')
        # CE Position Card

        positions_layout.bind(minimum_height=positions_layout.setter('height'))
        positions_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        positions_scroll = ScrollView(size_hint=(1, 0.35))
        # Position Cards

        self.setup_mode = 'A Setup Only'  # Default
        layout.add_widget(setup_panel)

        setup_panel.add_widget(setup_btns)
        setup_btns.add_widget(self.setup_b_btn)
        setup_btns.add_widget(self.setup_a_btn)
        setup_btns.add_widget(self.setup_both_btn)

        self.setup_b_btn.bind(on_press=lambda x: self.set_setup('B Setup Only'))
        self.setup_a_btn.bind(on_press=lambda x: self.set_setup('A Setup Only'))
        self.setup_both_btn.bind(on_press=lambda x: self.set_setup('Both Setup'))

        self.setup_b_btn = Button(text='B Only', background_color=(0.8, 0.5, 0.2, 1))
        self.setup_a_btn = Button(text='A Only', background_color=(0.3, 0.8, 0.3, 1))
        self.setup_both_btn = Button(text='Both', background_color=(0.3, 0.3, 0.8, 1))
        setup_btns = BoxLayout(orientation='horizontal', size_hint=(0.7, 1), spacing=5)

        setup_panel.add_widget(Label(text='Setup:', size_hint=(0.3, 1)))
        setup_panel = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        # Setup selector

        layout.add_widget(control_panel)

        control_panel.add_widget(self.force_exit_btn)
        self.force_exit_btn.bind(on_press=self.force_exit_all)
        )
            background_color=(0.8, 0.2, 0.2, 1)
            size_hint=(0.4, 1),
            text='🚨 Exit All',
        self.force_exit_btn = Button(

        control_panel.add_widget(self.start_btn)
        self.start_btn.bind(on_press=self.toggle_strategy)
        )
            font_size='16sp'
            background_color=(0.2, 0.8, 0.4, 1),
            size_hint=(0.6, 1),
            text='▶ Start Strategy',
        self.start_btn = Button(

        control_panel = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        # Control Panel

        layout.add_widget(header)

        header.add_widget(logout_btn)
        logout_btn.bind(on_press=self.logout)
        )
            background_color=(0.8, 0.2, 0.2, 1)
            size_hint=(0.2, 1),
            text='Logout',
        logout_btn = Button(
        # Logout button

        header.add_widget(self.status_label)
        )
            font_size='16sp'
            size_hint=(0.4, 1),
            markup=True,
            text='[color=808080]IDLE[/color]',
        self.status_label = Label(

        ))
            font_size='20sp'
            size_hint=(0.4, 1),
            markup=True,
            text='[b]VCU Mobile[/b]',
        header.add_widget(Label(

        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        # Header

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    def build_ui(self):

        Clock.schedule_interval(self.update_ui, 0.5)
        # Start update loop

        self.build_ui()

        self.command_queue = queue.Queue()
        self.data_queue = queue.Queue()
        self.log_queue = queue.Queue()
        self.bot_thread = None
        self.strategy_running = False
        super().__init__(**kwargs)
    def __init__(self, **kwargs):

    """Main trading screen"""
class MainScreen(Screen):


        self.status_label.color = (1, 0, 0, 1)
        self.status_label.text = f'Error: {message}'
        """Show error message"""
    def show_error(self, message):

        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'main'), 0.5)
        self.status_label.color = (0, 1, 0, 1)
        self.status_label.text = 'Login Successful!'
        """Navigate to main screen on successful login"""
    def login_success(self):

            Clock.schedule_once(lambda dt: self.show_error(str(e)))
        except Exception as e:

                Clock.schedule_once(lambda dt: self.show_error("Invalid credentials"))
            else:
                Clock.schedule_once(lambda dt: self.login_success())

                }
                    'token': totp_token
                    'password': password,
                    'client_id': client_id,
                    'api_key': api_key,
                app.credentials = {
                app.api_object = obj
                app = App.get_running_app()
                # Store credentials in app
            if data and 'data' in data:

            data = obj.generateSession(client_id, password, pyotp.TOTP(totp_token).now())
            obj = SmartConnect(api_key=api_key)
            # Initialize SmartConnect

                return
                Clock.schedule_once(lambda dt: self.show_error("Please fill all fields"))
            if not all([api_key, client_id, password, totp_token]):

            totp_token = self.totp_input.text.strip()
            password = self.pass_input.text.strip()
            client_id = self.client_input.text.strip()
            api_key = self.api_input.text.strip()
        try:
        """Background thread for login"""
    def _login_thread(self):

        threading.Thread(target=self._login_thread, daemon=True).start()
        # Run login in background thread

        self.status_label.color = (1, 1, 0, 1)
        self.status_label.text = 'Connecting...'
        """Handle login process"""
    def do_login(self, instance):

            print(f"Error loading credentials: {e}")
        except Exception as e:
                self.totp_input.text = creds.get('TOKEN', '')
                self.pass_input.text = creds.get('PASSWORD', '')
                self.api_input.text = creds.get('API_KEY', '')
                self.client_input.text = creds.get('Client_id', '')

                            creds[key.strip()] = value.strip()
                            key, value = line.split('=', 1)
                        if '=' in line and not line.startswith('#'):
                        line = line.strip()
                    for line in f:
                with open(creds_file, 'r', encoding='utf-8') as f:
                creds = {}
            if os.path.exists(creds_file):
            creds_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.txt')
        try:
        """Load saved credentials from file"""
    def load_credentials(self):

        self.load_credentials()
        # Auto-load credentials if available

        self.add_widget(layout)

        layout.add_widget(login_btn)
        login_btn.bind(on_press=self.do_login)
        )
            font_size='18sp'
            background_color=(0.2, 0.8, 0.4, 1),
            size_hint=(1, 0.12),
            text='Login & Connect',
        login_btn = Button(
        # Login button

        layout.add_widget(self.status_label)
        )
            color=(1, 1, 0, 1)
            size_hint=(1, 0.08),
            text='',
        self.status_label = Label(
        # Status label

        layout.add_widget(form_layout)

        form_layout.add_widget(self.totp_input)
        )
            size_hint=(1, 0.12)
            multiline=False,
            hint_text='Enter TOTP Secret',
        self.totp_input = TextInput(
        form_layout.add_widget(Label(text='TOTP Token:', size_hint=(1, 0.12), halign='left'))
        # TOTP Token

        form_layout.add_widget(self.pass_input)
        )
            size_hint=(1, 0.12)
            multiline=False,
            password=True,
            hint_text='Enter Password',
        self.pass_input = TextInput(
        form_layout.add_widget(Label(text='Password:', size_hint=(1, 0.12), halign='left'))
        # Password

        form_layout.add_widget(self.api_input)
        )
            size_hint=(1, 0.12)
            multiline=False,
            hint_text='Enter API Key',
        self.api_input = TextInput(
        form_layout.add_widget(Label(text='API Key:', size_hint=(1, 0.12), halign='left'))
        # API Key

        form_layout.add_widget(self.client_input)
        )
            size_hint=(1, 0.12)
            multiline=False,
            hint_text='Enter Client ID',
        self.client_input = TextInput(
        form_layout.add_widget(Label(text='Client ID:', size_hint=(1, 0.12), halign='left'))
        # Client ID

        form_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.6))
        # Form container

        layout.add_widget(subtitle)
        )
            color=(0.7, 0.7, 0.7, 1)
            font_size='16sp',
            size_hint=(1, 0.08),
            text='Mobile Edition for Android',
        subtitle = Label(
        # Subtitle

        layout.add_widget(title)
        )
            color=(0.2, 0.8, 1, 1)
            font_size='28sp',
            size_hint=(1, 0.15),
            markup=True,
            text='[b]🚀 VCU Trading Bot[/b]',
        title = Label(
        # Title

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
    def build_ui(self):

        self.build_ui()
        super().__init__(**kwargs)
    def __init__(self, **kwargs):

    """Login screen for Angel One credentials"""
class LoginScreen(Screen):


    Window.size = (400, 800)
if platform != 'android':
# Set window size for development (will be fullscreen on Android)

    TelegramNotifier = None
    TradingBot = None
    print(f"Import Error: {e}")
except ImportError as e:
    import pyotp
    from SmartApi import SmartConnect
    from telegram_notifier import TelegramNotifier
    from trading_bot_backend import TradingBot
try:
# Import backend trading logic

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add parent directory to path for imports

import sys
import os
from datetime import datetime as DT
import json
import queue
import threading

from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

"""
Optimized for OnePlus 13R and modern Android devices
VCU Trading Bot - Mobile Android Application
"""

