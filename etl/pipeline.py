from pathlib import Path
import os

from etl.extract.extract import Extract
from etl.transform.transform import Transform
from etl.load.load import Load


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "raw" / "alzheimers_disease_data.csv"


class DataPipeline:
    def __init__(self, input_path, db_config):
        self.extract = Extract(input_path)
        self.transform = Transform()
        self.load = Load(db_config)

    def run(self):
        data = self.extract.run()
        data = self.transform.run(data)
        self.load.run(data)


if __name__ == "__main__":
    db_config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "dbname": os.getenv("DB_NAME", "alzheimer_db"),
        "user": os.getenv("DB_USER", "thaole"),
        "password": os.getenv("DB_PASSWORD", "alzheimerpassword"),
        "port": int(os.getenv("DB_PORT", "5432")),
    }

    pipeline = DataPipeline(
        input_path=os.getenv("INPUT_PATH", str(DEFAULT_INPUT_PATH)),
        db_config=db_config,
    )
    pipeline.run()
