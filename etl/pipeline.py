from etl.extract.extract import Extract
from etl.transform.transform import Transform
from etl.load.load import Load

class DataPipeline:
    def __init__(self, input_path):
        self.extract = Extract(input_path)
        self.transform = Transform()
        self.load = Load({
            "host": "localhost",
            "dbname": "alzheimer_db",
            "user": "thaole",
            "password": "alzheimerpassword",
            "port": 5432
        })

    def run(self):
        data = self.extract.run()
        data = self.transform.run(data)
        self.load.run(data)

if __name__ == '__main__':
    pipeline = DataPipeline(
        input_path='data/raw/alzheimers_disease_data.csv'
    )
    pipeline.run()