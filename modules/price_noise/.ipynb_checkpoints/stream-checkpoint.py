# modules/price_noise/stream.py

import requests
from .config import CONFIG

def fetch_price():
    url = f"https://api.binance.com/api/v3/ticker/bookTicker?symbol={CONFIG['symbol']}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        # Use mid-price for entropy
        bid = float(data["bidPrice"])
        ask = float(data["askPrice"])
        mid_price = (bid + ask) / 2
        return mid_price
    except Exception as e:
        print(f"[stream] Error fetching price: {e}")
        return None
