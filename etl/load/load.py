import psycopg2
from psycopg2.extras import execute_batch

from etl.load.db import DatabaseConnector


class Load:
    def __init__(self, db_config):
        self.db = DatabaseConnector(**db_config)

    def run(self, df):
        print("Loading data into PostgreSQL...")

        conn = self.db.connect()
        try:
            required_columns = ["age", "gender", "bmi", "cognitive_score", "risk_score"]
            missing = [column for column in required_columns if column not in df.columns]
            if missing:
                raise KeyError(f"Missing required load columns: {', '.join(missing)}")

            records = df[["age", "gender", "bmi", "cognitive_score", "risk_score"]].itertuples(
                index=False,
                name=None,
            )

            with conn.cursor() as cur:
                execute_batch(
                    cur,
                    """
                    INSERT INTO alzheimer_data (age, gender, bmi, cognitive_score, risk_score)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    list(records),
                )

            conn.commit()
        finally:
            conn.close()
