# name  : Shoby Gnanasekaran
# net id: shoby

from hero import Hero
from dungeonchar import DungeonCharacter
import random
from dungeonchar_db_access import DungeonCharDb
from special_attack import SpecialAttack

class Thief(Hero, SpecialAttack):
    def __init__(self, name, model):
        super().__init__(name=name, model=model)
        super(DungeonCharacter, self).__init__()
        self.__update_values_from_db()


    def __update_values_from_db(self):
        db = DungeonCharDb()  # connects and accesses monster_stats table of dungeondb
        self.hp_total = db.get_data_hero("Thief", "hp")
        self.hp = self.hp_total
        self.attack_speed = db.get_data_hero("Thief", "attack_speed")
        self.hit_chance = db.get_data_hero("Thief", "hit_chance")
        self.damage_min = db.get_data_hero("Thief", "damage_min")
        self.damage_max = db.get_data_hero("Thief", "damage_max")
        self.chance_to_block = db.get_data_hero("Thief", "chance_to_block")
        self.extra_attack_chance = db.get_special_attack_stats("Thief","extra_attack_chance")
        self.caught_chance = db.get_special_attack_stats("Thief", "caught_chance")


    def attack_target(self, target):
        """ check if thief can have an extra attack or get caught , else performs a normal attack"""
        extra_attack = random.random() < self.extra_attack_chance
        got_caught = random.random() < self.caught_chance
        if extra_attack:
            super().attack_target(target)
            super().attack_target(target)

        elif got_caught:
            self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name} is caught!! can't attack now")

        else:
            super().attack_target(target)






