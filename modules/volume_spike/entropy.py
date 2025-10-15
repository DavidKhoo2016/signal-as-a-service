# modules/volume_spike/entropy.py

import random
import time

class VolumeSpikeEntropy:
    def __init__(self):
        self.name = "volume_spike"
        self.last_entropy = 0.0
        self.last_update_time = 0

    def update(self):
        # Simulate volume-based entropy (replace with real logic later)
        self.last_entropy = round(random.uniform(0, 100), 4)
        self.last_update_time = time.time()
        return self.last_entropy

    def get_entropy(self):
        return self.last_entropy

    def get_metadata(self):
        return {
            "name": self.name,
            "last_entropy": self.last_entropy,
            "last_update_time": self.last_update_time
        }
