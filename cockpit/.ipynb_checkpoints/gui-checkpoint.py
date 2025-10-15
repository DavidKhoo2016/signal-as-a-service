# cockpit/gui.py

import os
import time

class CockpitGUI:
    def __init__(self, refresh_rate=1.0):
        self.refresh_rate = refresh_rate
        self.last_signal = None
        self.last_action = None
        self.last_health = {}

    def update(self, signal, action, health):
        self.last_signal = signal
        self.last_action = action
        self.last_health = health
        self.render()

    def render(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("=== ENTROPY COCKPIT ===")
        print(f"Signal Strength : {round(self.last_signal, 8)}")
        print(f"Last Action     : {self.last_action}")
        print(f"Module Health   : {self.last_health}")
        print("========================")
        time.sleep(self.refresh_rate)
