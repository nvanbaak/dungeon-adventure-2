# name  : Shoby Gnanasekaran
# net id: shoby

from monster import Monster
from dungeonchar_db_access import DungeonCharDb

class Ogre(Monster):
    """ Ogre is a monster with it own statistics. The behaviour is same as the monsters"""
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__update_values_from_db()

    def __update_values_from_db(self):
        """ Updates the parameters of an Ogre from dungeondb"""

        db = DungeonCharDb() #connects and accesses monster_stats table of dungeondb
        self.hp_total = db.get_data_monster("Ogre", "hp")
        self.hp = self.hp_total
        self.attack_speed = db.get_data_monster("Ogre", "attack_speed")
        self.hit_chance = db.get_data_monster("Ogre", "hit_chance")
        self.damage_min = db.get_data_monster("Ogre", "damage_min")
        self.damage_max = db.get_data_monster("Ogre", "damage_max")
        self.chance_to_heal = db.get_data_monster("Ogre", "chance_to_heal")
        self.min_heal_point = db.get_data_monster("Ogre", "min_heal_point")
        self.max_heal_point = db.get_data_monster("Ogre", "max_heal_point")




