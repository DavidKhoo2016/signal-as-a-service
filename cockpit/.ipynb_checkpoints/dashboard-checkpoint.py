# cockpit/dashboard.py

import os
import time
import json
from fusion.fusion_core import FusionEngine

# === Logging Functions ===

def log_entropy_snapshot(modules, signal):
    snapshot = {
        "timestamp": time.time(),
        "signal": signal,
        "modules": {}
    }
    for name, module in modules.items():
        snapshot["modules"][name] = module.get_entropy()

    with open("logs/entropy_log.ndjson", "a") as f:
        f.write(json.dumps(snapshot) + "\n")

def log_discipline_violation(signal, action):
    violation = {
        "timestamp": time.time(),
        "signal": signal,
        "action": action,
        "violation": "Strong signal ignored"
    }
    with open("logs/discipline_log.ndjson", "a") as f:
        f.write(json.dumps(violation) + "\n")

# === Dashboard Class ===

class Dashboard:
    def __init__(self):
        self.engine = FusionEngine()
        self.engine.load_modules()

    def run_live(self):
        while True:
            self.engine.update_streams()
            signal = self.engine.get_fused_signal()
            action = self.get_action(signal)
            health = self.engine.health_monitor.get_status()
            self.update(signal, action, health)
            time.sleep(5)

    def get_action(self, signal):
        if signal > 60:
            return "ENTER LONG"
        elif signal < 40:
            return "ENTER SHORT"
        else:
            return "EXIT"

    def update(self, signal, action, health):
        os.system("cls" if os.name == "nt" else "clear")
        print("=== ENTROPY COCKPIT ===")
        print(f"Signal Strength : {signal}")
        print(f"Last Action     : {action}")
