# name  : Shoby Gnanasekaran
# net id: shoby

import sqlite3
from sqlite3 import Error

class DungeonCharDb:
    """ Class to access, insert and delete from dungeondb.db database.
    the character stats are only accessed from this class
    saved_games table data is added, accessed and deleted through various methods of this class"""

    def __init__(self):
        self.__dungeon_db = r"dungeondb.db"

    def create_connection(self):
        """ creates a connection to dungeondb.db
        if failed to connect returns None
        :return connection"""

        conn = None
        try:
            conn = sqlite3.connect(self.__dungeon_db)
            return conn
        except Error as e:
            error = str(e)

        return conn

    def get_data_monster(self, monster_name, value_name):
        """ get monster stats from monster_stats table of dungeondb.db
        :return other """

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM monster_stats WHERE name =?", (monster_name,) )
        value = cur.fetchone()
        return value[0]

    def get_data_hero(self, hero_name, value_name):
        """ get hero stats from hero_stats table of dungeondb.db
        :return other """

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM hero_stats WHERE name =?", (hero_name,))
        value = cur.fetchone()
        return value[0]

    def get_crush_blow_stats(self, name, value_name):
        """ gets crushing blow stats from crushing_blow_stats table of dungeondb.db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM crushing_blow_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]

    def get_healable_stats(self, name, value_name):
        """ gets healable stats from healable_stats table of dungeondb.db"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM healable_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]

    def get_special_attack_stats(self, name, value_name):

        """ gets the special attack stats from special_attack_stats table of dungeondb.db"""

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {value_name} FROM special_attack_stats WHERE name =?", (name,))
        value = cur.fetchone()
        return value[0]

    def select_column_from_table(self, table_name, column_name):
        """ return entire column values from the column_name col of table_name table
         :return list"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT {column_name} FROM {table_name}")
        value = cur.fetchall()
        return value

    def save_game(self, name, game_file):
        """ Saves the game_file in the name """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO saved_games(name,game_file) VALUES(?,?)",(name,game_file))
        conn.commit()

    def load_game(self, game_name):
        """ returns a binary file saved in the game_name"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT game_file FROM saved_games WHERE name =?", (game_name,))
        value = cur.fetchone()
        return value

    def delete_single_game(self, game_name):
        """ deletes the single row with the game_name"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM saved_games WHERE name=?",(game_name,))
        conn.commit()

    def delete_all_saved_games(self):
        """ deletes all rows of the saved_games table"""
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM saved_games")
        conn.commit()




