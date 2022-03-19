# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
from healable import Healable
import random

class Monster(DungeonCharacter, Healable, ABC):
    """
    Abstract base class used for all monster. They attack the hero and heal itself based on chance to heal after taking damage
    """

    def __init__(self, name, model, **kwargs):
        super().__init__(name = name, model = model, **kwargs)
        super(DungeonCharacter, self).__init__(**kwargs)

    def take_damage(self, dmg, source):
        """ after taking damage, if the monster is not dead, it tries to heal itself
        :param dmg int
        :param source dungeon char"""
        hp_before_attack = self.hp
        super().take_damage(dmg, source)
        if self._is_alive and hp_before_attack > self.hp:
            heal_message = self.heal_itself()
            self.model.announce(f"{self.name}: {heal_message}")





