# fusion/fusion_core.py (public stub for Render deployment)

import time

# Stubbed module registry for public onboarding
def get_all_modules():
    return [
        SimulatedModule("high_freq_entropy", 0.66),
        SimulatedModule("volume_spike", 0.28),
    ]

class FusionEngine:
    def __init__(self):
        self.modules = {}
        self.last_fused_signal = None
        self.last_update_time = None
        self.health_monitor = ModuleHealthMonitor()

    def load_modules(self):
        modules = get_all_modules()
        for module in modules:
            if module is None:
                print("[fusion] ⚠️ Skipping null module")
                continue
            name = module.name
            self.modules[name] = module
            print(f"[fusion] ✅ Loaded module: {name}")

    def update_streams(self):
        weighted_sum = 0.0
        total_weight = 0.0

        weights = {
            "high_freq_entropy": 0.7,
            "volume_spike": 0.3
        }

        for name, module in self.modules.items():
            try:
                entropy = module.update()
                weight = weights.get(name, 0.0)

                if entropy is not None:
                    weighted_sum += entropy * weight
                    total_weight += weight
                    self.health_monitor.mark_healthy(name)
                    print(f"[fusion] ✅ {name}: {entropy:.2f} (weight {weight})")
                else:
                    self.health_monitor.mark_stale(name)
                    print(f"[fusion] ⚠️ {name}: returned None")

            except Exception as e:
                print(f"[fusion] ❌ Error in module '{name}': {e}")
                self.health_monitor.mark_stale(name)

        if total_weight > 0:
            self.last_fused_signal = round(weighted_sum / total_weight, 8)
        else:
            self.last_fused_signal = 0.0

        self.last_update_time = time.time()
        print(f"[fusion] 🔄 Fused signal: {self.last_fused_signal:.8f}")

    def get_fused_signal(self):
        return self.last_fused_signal


class ModuleHealthMonitor:
    def __init__(self):
        self.status = {}

    def mark_healthy(self, name):
        self.status[name] = "healthy"

    def mark_stale(self, name):
        self.status[name] = "stale"

    def get_status(self):
        return self.status


class SimulatedModule:
    def __init__(self, name, fixed_entropy):
        self.name = name
        self.fixed_entropy = fixed_entropy

    def update(self):
        return self.fixed_entropy
