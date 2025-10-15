# analytics/signal_tracker.py

import time
from modules.price_noise.stream import fetch_price

class SignalTracker:
    def __init__(self):
        self.last_price = None
        self.history = []

    def log_signal(self, signal_value):
        current_price = fetch_price()
        timestamp = time.time()

        if current_price is None:
            print("[tracker] Price fetch failed.")
            return

        if self.last_price is not None:
            price_delta = current_price - self.last_price
            entry = {
                "time": timestamp,
                "signal": signal_value,
                "price": current_price,
                "delta": price_delta,
                "direction": "up" if price_delta > 0 else "down" if price_delta < 0 else "flat"
            }
            self.history.append(entry)
            print(f"[tracker] Logged: {entry}")
        else:
            print(f"[tracker] First price: {current_price}")

        self.last_price = current_price
