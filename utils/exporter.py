# utils/exporter.py

import json
import socket
import requests
from datetime import datetime

class EntropyExporter:
    def __init__(self, mode="file", filepath="entropy_stream.json", socket_config=None, api_url=None):
        self.mode = mode
        self.filepath = filepath
        self.socket_config = socket_config
        self.api_url = api_url

    def export(self, entropy_value):
        payload = {
            "time": datetime.utcnow().isoformat(),
            "entropy": entropy_value
        }

        if self.mode == "file":
            self._export_to_file(payload)
        elif self.mode == "socket":
            self._export_to_socket(payload)
        elif self.mode == "api":
            self._export_to_api(payload)

    def _export_to_file(self, payload):
        try:
            with open(self.filepath, "a") as f:
                f.write(json.dumps(payload) + "\n")
            print(f"[exporter] Entropy written to {self.filepath}")
        except Exception as e:
            print(f"[exporter] File export failed: {e}")

    def _export_to_socket(self, payload):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.socket_config["host"], self.socket_config["port"]))
            s.sendall(json.dumps(payload).encode())
            s.close()
            print(f"[exporter] Entropy sent to socket")
        except Exception as e:
            print(f"[exporter] Socket export failed: {e}")

    def _export_to_api(self, payload):
        try:
            response = requests.post(self.api_url, json=payload)
            print(f"[exporter] API response: {response.status_code}")
        except Exception as e:
            print(f"[exporter] API export failed: {e}")
