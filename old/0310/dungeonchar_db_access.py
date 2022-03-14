

import sqlite3
from sqlite3 import Error

class DungeonCharDb:
    def __init__(self):
        self.__dungeon_db = r"dungeondb.db"

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.__dungeon_db)
            return conn
        except Error as e:
            error = str(e)

        return conn

    def get_data(self, monster_name, value_name):
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM monster_stats WHERE name =?", (monster_name,) )
        value = cur.fetchone()
        return value[0]


if __name__ == '__main__':
    db = DungeonCharDb()
    print(db.get_data("Ogre", "hp"))





