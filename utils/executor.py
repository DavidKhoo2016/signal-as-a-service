# utils/executor.py

def execute_trade(signal_value, symbol="BTCUSDT", side="BUY", size=0.001):
    # Placeholder for real exchange integration
    print(f"[executor] Executing {side} order for {size} {symbol} at signal {signal_value}")
    # TODO: Replace with real API call (e.g., Binance, Bybit, etc.)
    return {
        "status": "executed",
        "symbol": symbol,
        "side": side,
        "size": size,
        "signal": signal_value
    }
