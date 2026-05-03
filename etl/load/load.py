import psycopg2
from psycopg2.extras import execute_batch

from etl.load.db import DatabaseConnector

class Load:
    def __init__(self, db_config):
        self.db = DatabaseConnector(**db_config)

    def run(self, df):
        print("Loading data into PostgreSQL...")

        conn = self.db.connect()
        cur = conn.cursor()

        execute_batch(cur, """
            INSERT INTO alzheimer_data (age, gender, bmi, risk_score)
            VALUES (%s, %s, %s, %s, %s)
        """, df[['Age', 'Gender', 'BMI', 'RiskScore']].values.tolist())

        conn.commit()
        cur.close()
        conn.close()
