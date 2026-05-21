from pathlib import Path

import pandas as pd


class Extract:
    def __init__(self, loadpath):
        self.loadpath = Path(loadpath)

    def run(self):
        if not self.loadpath.exists():
            raise FileNotFoundError(f"Input file not found: {self.loadpath}")

        print(f"Extracting data from {self.loadpath}...")
        return pd.read_csv(self.loadpath)
