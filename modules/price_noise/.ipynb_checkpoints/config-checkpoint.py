# modules/price_noise/config.py

CONFIG = {
    "module_name": "price_noise",
    "source": "binance",
    "symbol": "BTCUSDT",
    "refresh_interval": 1.0,
    "entropy_threshold": 0.00005,  # more sensitive
    "max_buffer_size": 100,
}
