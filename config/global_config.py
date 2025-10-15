# config/global_config.py

GLOBAL_CONFIG = {
    # Logging and cockpit behavior
    "log_level": "INFO",                  # Options: DEBUG, INFO, WARNING, ERROR
    "dashboard_refresh_rate": 2.0,        # Seconds between cockpit loop cycles
    "operator_mode": "semi-passive",      # Options: manual, semi-passive, auto

    # Entropy engine settings
    "max_active_modules": 16,             # Max entropy modules loaded at once
    "fallback_rng": True,                 # Use backup randomness if entropy fails
    "entropy_alerts": True,               # Warn if entropy stream goes stale

    # Exporter settings
    "export_mode": "file",                # Options: file, socket, api
    "export_path": "entropy_stream.json", # File path for export mode "file"
    "api_endpoint": "",                   # Optional: URL for export mode "api"
    "socket_config": {                    # Optional: host/port for export mode "socket"
        "host": "127.0.0.1",
        "port": 9000
    },

    # GUI settings
    "gui_enabled": True,                  # Toggle cockpit GUI rendering
    "gui_refresh_rate": 2.0,              # Seconds between GUI updates

    # Strategy and discipline
    "entry_threshold": 0.00005,           # Signal strength to trigger entry
    "exit_threshold": 0.00001,            # Signal strength to trigger exit
    "base_trade_size": 0.001,             # Base size multiplier for trades
    "cooldown_seconds": 5,                # Minimum time between executions
}
