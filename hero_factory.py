from warrior import Warrior
from priestess import Priestess
from thief import Thief
from dungeonchar_db_access import DungeonCharDb


DB = DungeonCharDb()
class HeroFactory:
    """ Factory class to create all hero characters"""

    @staticmethod
    def create_warrior(name, model):
        """ creates a warrior hero with the name and model passed and other stats from dungeondb.db """
        warrior = Warrior(name, model,hp_total = DB.get_data_hero("Warrior", "hp"),
                         attack_speed = DB.get_data_hero("Warrior", "attack_speed"),
                         hit_chance = DB.get_data_hero("Warrior", "hit_chance"),
                         damage_max = DB.get_data_hero("Warrior", "damage_max"),
                         damage_min = DB.get_data_hero("Warrior", "damage_min"),
                         chance_to_block = DB.get_data_hero("Warrior", "chance_to_block"),
                         crushing_blow_chance = DB.get_crush_blow_stats("Warrior", "crushing_blow_chance"),
                         crushing_blow_max = DB.get_crush_blow_stats("Warrior", "crushing_blow_max"),
                         crushing_blow_min = DB.get_crush_blow_stats("Warrior", "crushing_blow_min")
                          )
        return warrior


    @staticmethod
    def create_priestess(name, model):
        """ creates a priestess hero with the name and model passed and other stats from dungeondb.db """

        priestess = Priestess(name, model, hp_total = DB.get_data_hero("Priestess", "hp"),
                 attack_speed = DB.get_data_hero("Priestess", "attack_speed"),
                 hit_chance = DB.get_data_hero("Priestess", "hit_chance"),
                 damage_max = DB.get_data_hero("Priestess", "damage_max"),
                 damage_min = DB.get_data_hero("Priestess", "damage_min"),
                 chance_to_block = DB.get_data_hero("Priestess", "chance_to_block"),
                 chance_to_heal=DB.get_healable_stats("Priestess", "chance_to_heal"),
                 min_heal_point=DB.get_healable_stats("Priestess", "min_heal_point"),
                 max_heal_point=DB.get_healable_stats("Priestess", "max_heal_point")
                              )
        return priestess

    @staticmethod
    def create_thief(name, model):
        """ creates a thief hero with the name and model passed and other stats from dungeondb.db """
        thief = Thief(name, model, hp_total = DB.get_data_hero("Thief", "hp"),
                         attack_speed = DB.get_data_hero("Thief", "attack_speed"),
                         hit_chance = DB.get_data_hero("Thief", "hit_chance"),
                         damage_max = DB.get_data_hero("Thief", "damage_max"),
                         damage_min = DB.get_data_hero("Thief", "damage_min"),
                         chance_to_block = DB.get_data_hero("Thief", "chance_to_block"),
                         extra_attack_chance = DB.get_special_attack_stats("Thief", "extra_attack_chance"),
                         caught_chance = DB.get_special_attack_stats("Thief", "caught_chance")
                      )
        return thief