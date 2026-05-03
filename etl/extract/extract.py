import pandas as pd

class Extract:
    def __init__(self, loadpath):
        self.loadpath = loadpath

    def run(self):
        print('Extracting...')
        df = pd.read_csv(self.loadpath)
        return df