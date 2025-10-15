# fusion/health_check.py

import time

class ModuleHealthMonitor:
    def __init__(self):
        self.last_update = {}
        self.health_status = {}

    def update_timestamp(self, module_name):
        self.last_update[module_name] = time.time()
        self.health_status[module_name] = "healthy"

    def check_health(self, module_name, timeout=10):
        now = time.time()
        last = self.last_update.get(module_name)
        if last is None or (now - last) > timeout:
            self.health_status[module_name] = "stale"
            print(f"[health] Module '{module_name}' is stale or unresponsive.")
            return False
        return True

    def get_status(self):
        return self.health_status
