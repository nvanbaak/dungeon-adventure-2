# name  : Shoby Gnanasekaran
# net id: shoby

from hero import Hero
from dungeonchar import DungeonCharacter
import random
from special_attack import SpecialAttack

class Thief(Hero, SpecialAttack):
    """ Warrior is a hero character that a player can choose. It is inherited from Hero class
        A warrior has a special attack Crushing Blow which has a 40% chance of succeeding. Warrior has its own stats"""

    def __init__(self, name, model, **kwargs):
        super().__init__(name=name, model=model, **kwargs)
        super(DungeonCharacter, self).__init__(**kwargs)

    def attack_target(self, target):
        """ check if thief can have an extra attack or get caught , else performs a normal attack"""
        extra_attack = random.random() <= self.extra_attack_chance
        got_caught = random.random() <= self.caught_chance
        if extra_attack:
            super().attack_target(target)
            super().attack_target(target)

        elif got_caught:
            self.model.announce(f"{self.name} is caught!! can't attack now")

        else:
            super().attack_target(target)






