# cockpit/discipline.py

class DisciplineLayer:
    def __init__(self, threshold=0.001, cooldown=5):
        self.last_action_time = None
        self.threshold = threshold
        self.cooldown = cooldown  # seconds

    def can_execute(self, signal, current_time):
        if signal is None or abs(signal) < self.threshold:
            print("[discipline] Signal too weak. Execution blocked.")
            return False

        if self.last_action_time and (current_time - self.last_action_time) < self.cooldown:
            print("[discipline] Cooldown active. Execution blocked.")
            return False

        self.last_action_time = current_time
        print("[discipline] Signal approved. Execution allowed.")
        return True
