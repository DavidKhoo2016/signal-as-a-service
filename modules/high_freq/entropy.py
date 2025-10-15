import os
import time
import hashlib
import subprocess
import psutil

class HighFreqEntropy:
    def __init__(self):
        self.name = "high_freq_entropy"

    def get_entropy(self):
        seed = f"{os.urandom(16)}-{time.time_ns()}"
        sys_entropy = int(hashlib.sha256(seed.encode()).hexdigest(), 16) % 100

        clock_entropy = int(str(time.time_ns())[-5:]) % 100

        try:
            result = subprocess.run(["ping", "-c", "1", "1.1.1.1"], capture_output=True, text=True, timeout=1)
            ms = float(result.stdout.split("time=")[-1].split(" ms")[0])
            ping_entropy = int(ms * 10) % 100
        except Exception:
            ping_entropy = 50

        try:
            cpu_load = psutil.cpu_percent(interval=0.1)
            cpu_entropy = int(cpu_load * 1.5) % 100
        except Exception:
            cpu_entropy = 50

        raw = f"{sys_entropy}-{clock_entropy}-{ping_entropy}-{cpu_entropy}-{time.time_ns()}"
        fused = int(hashlib.sha256(raw.encode()).hexdigest(), 16) % 100
        return fused

    def update(self):
        entropy = self.get_entropy()
        print(f"[high_freq_entropy] Entropy: {entropy}")
        return entropy
