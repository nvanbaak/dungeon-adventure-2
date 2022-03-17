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

    def __init__(self, name, model, **kwargs):
        super().__init__(name=name, model=model, **kwargs)
        super(DungeonCharacter, self).__init__(**kwargs)

    def attack_target(self, target):
        """ check if it can do a crushing blow special attack, else performs a normal attack"""
        special_attack = random.random() < self.crushing_blow_chance
        if special_attack:
            self.special_attack(target)
        else:
            super().attack_target(target)









