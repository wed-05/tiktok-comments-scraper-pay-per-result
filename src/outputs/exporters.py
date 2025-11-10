thonimport json
import pandas as pd
import os

class JSONExporter:
    def __init__(self, filepath):
        self.filepath = filepath

    def export(self, data):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

class CSVExporter:
    def __init__(self, filepath):
        self.filepath = filepath

    def export(self, data):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        df = pd.json_normalize(data)
        df.to_csv(self.filepath, index=False)