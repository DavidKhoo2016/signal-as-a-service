# api_server.py

from fastapi import FastAPI, Request, HTTPException
from fusion.fusion_core import FusionEngine
from csv_logger.entropy_logger import init_entropy_log, log_entropy_tick
import threading
import time

VALID_KEYS = {
    "demo-key-123",
    "client-key-456",
    "institutional-789"
}

app = FastAPI()
engine = FusionEngine()
engine.load_modules()

latest_signal = None

# === INIT CSV LOG ON STARTUP ===
init_entropy_log("entropy_log.csv")

def signal_loop():
    global latest_signal
    while True:
        engine.update_streams()
        latest_signal = engine.get_fused_signal()

        # Log each module's entropy value
        for name, module in engine.modules.items():
            entropy_value = module.get_entropy()
            log_entropy_tick(
                source=name,
                value=entropy_value,
                fused_entropy=latest_signal,
                decision="loop",  # or "tick", if no trade decision yet
                operator_override=False,
                notes="auto-logged from signal loop",
                filepath="entropy_log.csv"
            )

        print(f"[{time.strftime('%X')}] → Signal: {latest_signal}")
        time.sleep(1)

threading.Thread(target=signal_loop, daemon=True).start()

@app.get("/signal")
def get_signal(request: Request):
    key = request.headers.get("x-api-key")
    if key not in VALID_KEYS:
        raise HTTPException(status_code=401, detail="Unauthorized")

    modules = {
        name: module.get_entropy()
        for name, module in engine.modules.items()
    }

    return {
        "timestamp": time.time(),
        "signal": latest_signal,
        "modules": modules
    }
