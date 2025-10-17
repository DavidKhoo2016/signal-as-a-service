import requests

# --- API Configuration ---
API_URL = "http://127.0.0.1:8000/signal"
API_KEY = "demo-key-123"

# --- Request Headers ---
headers = {
    "x-api-key": API_KEY
}

# --- Make the Request ---
try:
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    signal = response.json()
    print("✅ Entropy-Fused Signal Received:")
    print(signal)

except requests.exceptions.HTTPError as err:
    print("❌ API Error:", err)
except Exception as e:
    print("❌ Unexpected Error:", e)
