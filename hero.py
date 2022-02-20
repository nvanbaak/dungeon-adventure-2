from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random

class Hero(DungeonCharacter, ABC):
    """
    A class representing a character controlled by the player
    """
    def __init__(self, name, model) -> None:
        super().__init__(name, model)
        self.__health_potion_count = 0
        self.__vision_potion_count = 0
        self.__vision = 3

    @abstractmethod
    def attack_target(self, target):
        return super().attack_target(target)

    @abstractmethod
    def combat(self, target):
        return super().combat(target)

    @abstractmethod
    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)

    @abstractmethod
    def use_health_potion(self):
        """
        Uses a health potion if available
        """
        if self.__health_potion_count > 0:
            self.__health_potion_count -= 1
            amount_healed = random.randint(20, 40)
            self.hp += amount_healed

    @abstractmethod
    def get_health_potion(self):
        """
        Adds a health potion to hero's inventory
        """
        self.__health_potion_count += 1

    @abstractmethod
    def use_vision_potion(self):
        """
        Uses a vision potion if available
        """
        if self.__vision_potion_count > 0:
            self.__vision_potion_count -= 1
            self.__vision += 5

    @abstractmethod
    def get_vision_potion(self):
        """
        Adds a vision potion to the Hero's inventory
        """
        self.__vision_potion_count += 1

    @property
    def vision(self):
        return self.__vision
    @vision.setter
    def vision(self, value):
        if not isinstance(value, int):
            raise TypeError("vision must be an integer!")
        if value > 0:
            self.__vision = value
        else:
            raise ValueError("vision range must be greater than 0!")

