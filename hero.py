from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random
from time import *


class Hero(DungeonCharacter, ABC):
    """
    A class representing a character controlled by the player
    """
    def __init__(self, name, model) -> None:
        super().__init__(name, model)
        self.__attack_now = False
        self.__health_potions = 0
        self.__vision_potions = 0
        self.__vision = 3

    def set_attack_now(self, monster, value):
        while True:
            if monster.hp > 0 and self.hp >0:
                # print("i am setting hero to attack")
                self.attack_now = True
                sleep(1)
            else:
                break

    def __set_attack_now(self, t_f):
        if isinstance(t_f, bool):
            self.__attack_now = True

    def __get_attack_now(self):
        return self.__attack_now

    attack_now = property(__get_attack_now, __set_attack_now)

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
        if self.health_potions > 0:
            self.health_potions -= 1
            amount_healed = random.randint(20, 40)
            self.hp += amount_healed

    @abstractmethod
    def use_vision_potion(self):
        """
        Uses a vision potion if available
        """
        if self.vision_potions > 0:
            self.vision_potions -= 1
            self.vision += 5

    @property
    def vision_potions(self):
        return self.__vision_potions
    @vision_potions.setter
    def vision_potions(self, value):
        if value < 0:
            raise ValueError("potion count can't be less than 0!")
        self.__vision_potions = value

    @property
    def health_potions(self):
        return self.__health_potions

    @health_potions.setter
    def health_potions(self, value):
        if value < 0:
            raise ValueError("potion count can't be less than 0!")
        self.__health_potions = value

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