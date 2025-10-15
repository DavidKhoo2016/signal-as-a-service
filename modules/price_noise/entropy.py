# modules/price_noise/entropy.py

from modules.price_noise.stream import fetch_price
import time

class PriceNoiseEntropy:
    def __init__(self):
        self.last_price = None
        self.last_entropy = None
        self.last_update_time = None
        self.name = "price_noise"

    def update(self):
        price = fetch_price()
        if price is None:
            print("[entropy] No price data.")
            return None

        if self.last_price is None:
            self.last_price = price
            self.last_entropy = 0.0
            self.last_update_time = time.time()
            print(f"[entropy] First price: {price}")
            return self.last_entropy

        entropy = price - self.last_price
        self.last_entropy = round(entropy, 8)
        self.last_price = price
        self.last_update_time = time.time()
        return self.last_entropy

    def get_entropy(self):
        return self.last_entropy

    def get_metadata(self):
        return {
            "name": self.name,
            "last_entropy": self.last_entropy,
            "last_price": self.last_price,
            "last_update_time": self.last_update_time
        }
