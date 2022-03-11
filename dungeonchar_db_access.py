
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

    def get_data_monster(self, monster_name, value_name):
        """ get monster stats from db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM monster_stats WHERE name =?", (monster_name,) )
        value = cur.fetchone()
        return value[0]

    def get_data_hero(self, hero_name, value_name):
        """ get hero stats from db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM hero_stats WHERE name =?", (hero_name,))
        value = cur.fetchone()
        return value[0]

    def get_crush_blow_stats(self, name, value_name):
        """ gets crushing blow stats from db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM crushing_blow_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]

    def get_healable_stats(self, name, value_name):
        """ gets healable stats from db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM healable_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]

    def get_special_attack_stats(self, name, value_name):

        """ gets the special attack stats from db"""

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM special_attack_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]


if __name__ == '__main__':
    db = DungeonCharDb()
    print(db.get_data_monster("Ogre", "hp"))
    print(db.get_data_hero("Warrior", "attack_speed"))
    print(db.get_crush_blow_stats("Warrior","crushing_blow_min"))
    print(db.get_healable_stats("Priestess", "chance_to_heal"))
    print(db.get_special_attack_stats("Thief", "caught_chance"))


