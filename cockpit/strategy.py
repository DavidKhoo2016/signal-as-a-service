# cockpit/strategy.py

class StrategyEngine:
    def __init__(self, entry_threshold=0.00005, exit_threshold=0.00001, base_size=0.001):
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold
        self.base_size = base_size
        self.last_signal = None

    def evaluate(self, signal_value):
        if signal_value is None:
            return None

        action = "HOLD"
        side = None
        size = 0

        if abs(signal_value) >= self.entry_threshold:
            side = "BUY" if signal_value > 0 else "SELL"
            action = "ENTER"
            size = self.base_size * abs(signal_value) * 10000  # scale size by signal strength
        elif abs(signal_value) <= self.exit_threshold:
            action = "EXIT"

        instruction = {
            "action": action,
            "side": side,
            "size": round(size, 6),
            "signal": signal_value
        }

        self.last_signal = signal_value
        return instruction
