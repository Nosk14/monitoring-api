import sqlite3


class DBManager:

    def __init__(self):
        self.NAME = 'monitored_data.db'
        self.__db = sqlite3.connect(self.NAME)
        self.__db.row_factory = sqlite3.Row
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

    def store(self, data):
        cursor = self.__db.cursor()
        try:
            cursor.executemany("""INSERT INTO 
            data (id, time, temperature, humidity)
            values (?,?,?,?)""", data)
            self.__db.commit()
        finally:
            cursor.close()

    def retrieve(self, id, from_date, to_date):
        data = []
        cursor = self.__db.cursor()
        try:
            cursor.execute("""SELECT time, temperature, humidity 
            FROM data
            WHERE id=? AND time>=? AND time<=?
            ORDER BY time ASC""", (id, from_date, to_date))
            rows = cursor.fetchall()
            data = [dict(r) for r in rows]
        finally:
            cursor.close()

        return data

    def list_ids(self):
        ids = []
        cursor = self.__db.cursor()
        try:
            cursor.execute('SELECT DISTINCT id FROM data ORDER BY id')
            ids = cursor.fetchall()
        finally:
            cursor.close()

        return ids
