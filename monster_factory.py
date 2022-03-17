from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton
from dungeonchar_db_access import DungeonCharDb

DB = DungeonCharDb()

class MonsterFactory:
    """ Factory class to create all monster characters"""

    @staticmethod
    def create_ogre(name, model):
        """ creates an ogre monster  with the name and model passed and other stats from dungeondb.db """
        ogre = Ogre(name, model, hp_total = DB.get_data_monster("Ogre", "hp"),
                    attack_speed = DB.get_data_monster("Ogre", "attack_speed"),
                    hit_chance = DB.get_data_monster("Ogre", "hit_chance"),
                    damage_max = DB.get_data_monster("Ogre", "damage_max"),
                    damage_min = DB.get_data_monster("Ogre", "damage_min"),
                    chance_to_heal = DB.get_data_monster("Ogre", "chance_to_heal"),
                    min_heal_point = DB.get_data_monster("Ogre", "min_heal_point"),
                    max_heal_point = DB.get_data_monster("Ogre", "max_heal_point"))

        return ogre

    @staticmethod
    def create_gremlin(name, model):
        """ creates a gremlin monster  with the name and model passed and other stats from dungeondb.db """
        gremlin = Gremlin(name, model, hp_total = DB.get_data_monster("Gremlin", "hp"),
                         attack_speed = DB.get_data_monster("Gremlin", "attack_speed"),
                         hit_chance = DB.get_data_monster("Gremlin", "hit_chance"),
                         damage_max = DB.get_data_monster("Gremlin", "damage_max"),
                         damage_min = DB.get_data_monster("Gremlin", "damage_min"),
                         chance_to_heal = DB.get_data_monster("Gremlin", "chance_to_heal"),
                         min_heal_point = DB.get_data_monster("Gremlin", "min_heal_point"),
                         max_heal_point = DB.get_data_monster("Gremlin", "max_heal_point") )

        return gremlin

    @staticmethod
    def create_skeleton(name, model):
        """ creates a skeleton monster  with the name and model passed and other stats from dungeondb.db """
        skeleton = Skeleton(name, model, hp_total = DB.get_data_monster("Skeleton", "hp"),
                         attack_speed = DB.get_data_monster("Skeleton", "attack_speed"),
                         hit_chance = DB.get_data_monster("Skeleton", "hit_chance"),
                         damage_max = DB.get_data_monster("Skeleton", "damage_max"),
                         damage_min = DB.get_data_monster("Skeleton", "damage_min"),
                         chance_to_heal = DB.get_data_monster("Skeleton", "chance_to_heal"),
                         min_heal_point = DB.get_data_monster("Skeleton", "min_heal_point"),
                         max_heal_point = DB.get_data_monster("Skeleton", "max_heal_point"))
        return skeleton

