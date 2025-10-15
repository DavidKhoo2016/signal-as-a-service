import csv
from datetime import datetime
import os

# === CONFIG ===
DEFAULT_LOG_PATH = "entropy_log.csv"
HEADERS = [
    "timestamp",
    "source",
    "value",
    "fused_entropy",
    "decision",
    "operator_override",
    "notes"
]

# === INITIALIZATION ===
def init_entropy_log(filepath=DEFAULT_LOG_PATH):
    """Initialize the log file with headers if it doesn't exist."""
    if not os.path.exists(filepath):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

# === LOGGING FUNCTION ===
def log_entropy_tick(
    source: str,
    value: float,
    fused_entropy: float,
    decision: str,
    operator_override: bool = False,
    notes: str = "",
    filepath: str = DEFAULT_LOG_PATH
):
    """Append a single entropy tick to the log file."""
    timestamp = datetime.utcnow().isoformat() + "Z"
    row = [
        timestamp,
        source,
        round(value, 6),
        round(fused_entropy, 6),
        decision,
        operator_override,
        notes
    ]
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

# === OPTIONAL: BULK LOGGING ===
def log_multiple_entropy_ticks(ticks: list, filepath: str = DEFAULT_LOG_PATH):
    """
    Log multiple entropy ticks at once.
    Each tick should be a dict with keys matching the log_entropy_tick parameters.
    """
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        for tick in ticks:
            timestamp = datetime.utcnow().isoformat() + "Z"
            row = [
                timestamp,
                tick.get("source", ""),
                round(tick.get("value", 0.0), 6),
                round(tick.get("fused_entropy", 0.0), 6),
                tick.get("decision", ""),
                tick.get("operator_override", False),
                tick.get("notes", "")
            ]
            writer.writerow(row)
