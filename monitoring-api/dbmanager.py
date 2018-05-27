import sqlite3


class DBManager:

    def __init__(self, path):
        self.path = path
        self.__init_db()

    def __init_db(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
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
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            try:
                cursor.execute("""INSERT INTO 
                data (zone, time, temperature, humidity)
                values (?,?,?,?)""", data)
                db.commit()
            finally:
                cursor.close()

    def retrieve(self, zone, from_date, to_date):
        with sqlite3.connect(self.path) as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            try:
                cursor.execute("""SELECT time, temperature, humidity 
                FROM data
                WHERE zone=? AND time>=? AND time<=?
                ORDER BY time ASC""", (zone, from_date, to_date))
                rows = cursor.fetchall()
                data = [dict(r) for r in rows]
            finally:
                cursor.close()
        return data

    def list_zones(self):
        with sqlite3.connect(self.path) as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            try:
                cursor.execute('SELECT DISTINCT zone FROM data ORDER BY zone')
                zones = [r[0] for r in cursor.fetchall()]
            finally:
                cursor.close()
        return zones
