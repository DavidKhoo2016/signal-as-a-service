import requests
import time

API_URL = "http://localhost:8000/signal"
HEADERS = {"x-api-key": "demo-key-123"}

def verify_signal_rate(duration_sec=30):
    timestamps = []
    for _ in range(duration_sec):
        start = time.time()
        response = requests.get(API_URL, headers=HEADERS)
        data = response.json()
        ts = data["timestamp"]
        signal = data["signal"]
        print(f"{ts:.2f} → Signal: {signal}")
        timestamps.append(ts)
        time.sleep(1 - ((time.time() - start) % 1))  # Align to 1/sec

    # Check spacing
    intervals = [round(timestamps[i+1] - timestamps[i], 2) for i in range(len(timestamps)-1)]
    print("\nIntervals between signals:", intervals)

verify_signal_rate()
