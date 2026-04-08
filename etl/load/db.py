import psycopg2

class DatabaseConnector:
    def __init__(self, host, dbname, user, password, port=5432):
        self.connection_params = {
            "host": "localhost",
            "dbname": "alzheimer_db",
            "user": "thaole",
            "password": "alzheimerpassword"
        }

    def connect(self):
        conn = psycopg2.connect(**self.connection_params)