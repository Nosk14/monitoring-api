import sqlite3


class DBManager:

    def __init__(self, path):
        self.path = path
        self.__db = sqlite3.connect(self.path)
        self.__db.row_factory = sqlite3.Row
        self.__init_db()

    def __init_db(self):
        cursor = self.__db.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS data (
                zone STRING NOT NULL,
                time STRING NOT NULL,
                temperature REAL,
                humidity REAL,
                PRIMARY KEY (zone, time)                 
                )""")
        finally:
            cursor.close()

    def store(self, data):
        cursor = self.__db.cursor()
        try:
            cursor.executemany("""INSERT INTO 
            data (zone, time, temperature, humidity)
            values (?,?,?,?)""", data)
            self.__db.commit()
        finally:
            cursor.close()

    def retrieve(self, zone, from_date, to_date):
        cursor = self.__db.cursor()
        try:
            cursor.execute("""SELECT time, temperature, humidity 
            FROM data
            WHERE id=? AND time>=? AND time<=?
            ORDER BY time ASC""", (zone, from_date, to_date))
            rows = cursor.fetchall()
            data = [dict(r) for r in rows]
        finally:
            cursor.close()

        return data

    def list_zones(self):
        cursor = self.__db.cursor()
        try:
            cursor.execute('SELECT DISTINCT zone FROM data ORDER BY zone')
            zones = [r[0] for r in cursor.fetchall()]
        finally:
            cursor.close()

        return zones
