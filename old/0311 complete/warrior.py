# name  : Shoby Gnanasekaran
# net id: shoby

from hero import Hero
from dungeonchar import DungeonCharacter
import random
from dungeonchar_db_access import DungeonCharDb
from crushing_blow import CrushingBlow


class Warrior(Hero, CrushingBlow):
    """ Warrior is a hero character that a player can choose. It is inherited from Hero class
    A warrior has a special attack Crushing Blow which has a 40% chance of succeeding. Warrior has its own stats"""

    def __init__(self, name, model):
        super().__init__(name=name, model=model)
        super(DungeonCharacter, self).__init__()
        self.__update_values_from_db()

    def attack_target(self, target):
        """ check if it can do a crushing blow special attack, else performs a normal attack"""
        special_attack = random.random() < self.crushing_blow_chance
        if special_attack:
            self.special_attack(target)
        else:
            super().attack_target(target)

    def __update_values_from_db(self):
        db = DungeonCharDb()  # connects and accesses monster_stats table of dungeondb
        self.hp_total = db.get_data_hero("Warrior", "hp")
        self.hp = self.hp_total
        self.attack_speed = db.get_data_hero("Warrior", "attack_speed")
        self.hit_chance = db.get_data_hero("Warrior", "hit_chance")
        self.damage_min = db.get_data_hero("Warrior", "damage_min")
        self.damage_max = db.get_data_hero("Warrior", "damage_max")
        self.chance_to_block = db.get_data_hero("Warrior", "chance_to_block")
        self.crushing_blow_chance = db.get_crush_blow_stats("Warrior","crushing_blow_chance")
        self.crushing_blow_max = db.get_crush_blow_stats("Warrior", "crushing_blow_max")
        self.crushing_blow_min = db.get_crush_blow_stats("Warrior", "crushing_blow_min")








