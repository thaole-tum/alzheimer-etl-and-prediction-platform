import psycopg2


class DatabaseConnector:
    def __init__(self, host, dbname, user, password, port=5432):
        self.connection_params = {
            "host": host,
            "dbname": dbname,
            "user": user,
            "password": password,
            "port": port,
        }

    def connect(self):
        return psycopg2.connect(**self.connection_params)
