# analytics/entropy_analyzer.py

import time
from collections import deque
import numpy as np

class EntropyAnalyzer:
    def __init__(self, window_size=100):
        self.entropy_window = deque(maxlen=window_size)
        self.timestamps = deque(maxlen=window_size)
        self.last_alert = None

    def update(self, entropy_value):
        now = time.time()
        self.entropy_window.append(entropy_value)
        self.timestamps.append(now)

    def get_metrics(self):
        if len(self.entropy_window) < 2:
            return {}

        values = np.array(self.entropy_window)
        deltas = np.diff(values)
        volatility = np.std(values)
        density = np.count_nonzero(np.abs(deltas) > 1e-6) / len(deltas)

        return {
            "volatility": round(volatility, 8),
            "density": round(density, 4),
            "latest": self.entropy_window[-1],
            "samples": len(self.entropy_window)
        }

    def is_stale(self, volatility_threshold=1e-6, density_threshold=0.05):
        metrics = self.get_metrics()
        if not metrics:
            return False

        stale = (
            metrics["volatility"] < volatility_threshold or
            metrics["density"] < density_threshold
        )

        if stale and self.last_alert != metrics["latest"]:
            print(f"[analyzer] ⚠️ Entropy stale: {metrics}")
            self.last_alert = metrics["latest"]

        return stale
