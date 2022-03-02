# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
from healable import Healable
import random

class Monster(DungeonCharacter, Healable, ABC):
    """
    Abstract base class used for all monster. They attach the hero and heal itself after every time taking damage
    """

    def __init__(self, name = "name", model = None):
        super().__init__(name = name, model = model)
        super(DungeonCharacter, self).__init__()

    def take_damage(self, dmg, source):
        """ after taking damage, if the monster is not dead, it tries to heal itself"""
        hp_before_attack = self.hp
        self.hp -= dmg

        self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name} took {dmg} dmg from {source}!")

        if not self._is_alive:
            self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name} has died!")
        elif hp_before_attack > self.hp:
            heal_message = self.heal_itself()
            self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name}: {heal_message}")





