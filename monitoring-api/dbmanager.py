import sqlite3


class DBManager:

    def __init__(self):
        self.NAME = 'monitored_data.db'
        self.__db = sqlite3.connect(self.NAME)
        self.__init_db()

    def __init_db(self):
        cursor = self.__db.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS data (
                id STRING NOT NULL,
                time STRING NOT NULL,
                temperature REAL,
                humidity REAL,
                PRIMARY KEY (id, time)                 
                )""")
        finally:
            cursor.close()

    def store(self, id, data):
        pass

    def retrieve(self, id, from_date, to_date):
        pass

    def list_ids(self):
        pass
