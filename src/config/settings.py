thonimport json
import os

def load_settings():
    config_path = os.path.join(os.path.dirname(__file__), "settings.example.json")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)