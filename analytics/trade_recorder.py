# analytics/trade_recorder.py

from datetime import datetime

class TradeRecorder:
    def __init__(self):
        self.records = []

    def record(self, signal, side, size, entry_price=None, exit_price=None, outcome="executed"):
        timestamp = datetime.utcnow().isoformat()
        record = {
            "time": timestamp,
            "signal": signal,
            "side": side,
            "size": size,
            "entry_price": entry_price,
            "exit_price": exit_price,
            "outcome": outcome
        }
        self.records.append(record)
        print(f"[recorder] Event logged: {record}")

    def get_all(self):
        return self.records

    def export_csv(self, filepath="entropy_events.csv"):
        import csv
        if not self.records:
            print("[recorder] No records to export.")
            return

        keys = self.records[0].keys()
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.records)
        print(f"[recorder] Log exported to {filepath}")
