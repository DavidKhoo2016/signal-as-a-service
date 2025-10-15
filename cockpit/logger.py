# cockpit/logger.py

import datetime

class OperatorLogger:
    def __init__(self):
        self.log = []

    def record_action(self, action_type, signal_value, override=False):
        timestamp = datetime.datetime.now().isoformat()
        entry = {
            "time": timestamp,
            "action": action_type,
            "signal": signal_value,
            "override": override
        }
        self.log.append(entry)
        print(f"[logger] Action recorded: {entry}")
