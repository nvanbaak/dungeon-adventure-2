# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random

class CrushingBlow(ABC):
    def __init__(self):
        if issubclass(type(self), DungeonCharacter):
            self.__crushing_blow_chance = 0.0
            self.__crushing_blow_min = 0
            self.__crushing_blow_max = 0

        else:
            raise TypeError("should inherit Dungeonchar class")

    def special_attack(self, target):
        """ the damage given in a crushing blow is 75 to 175, usually deadly"""
        damage = random.randint(self.__crushing_blow_min, self.__crushing_blow_max)
        target.take_damage(damage, self.name)

    @abstractmethod
    def attack_target(self, target):
        pass

    def __set_crushing_blow_chance(self, value):
        if isinstance(value, float) and 0.0 <= value <= 1.0:
            self.__crushing_blow_chance = value
        else:
            raise TypeError(f"{value} is not a float or in range 0.0 to 1.0")


    def __get_crushing_blow_chance(self):
        return self.__crushing_blow_chance

    crushing_blow_chance = property(__get_crushing_blow_chance, __set_crushing_blow_chance)


    def __set_crushing_blow_max(self, value):
        if isinstance(value, int) and value > self.__crushing_blow_min:
            self.__crushing_blow_max = value

        else:
            raise TypeError(f"{value} not an integer or less than crushing_blow_min value : {self.__crushing_blow_min}")

    def __get_crushing_blow_max(self):
        return self.__crushing_blow_max

    crushing_blow_max = property(__get_crushing_blow_max, __set_crushing_blow_max)

    def __set_crushing_blow_min(self, value):
        if isinstance(value, int) and value < self.__crushing_blow_max:
            self.__crushing_blow_min = value

        else:
            raise TypeError(f"{value} not an integer or greater than crushing_blow_min value : {self.__crushing_blow_max}")

    def __get_crushing_blow_min(self):
        return self.__crushing_blow_min

    crushing_blow_min = property(__get_crushing_blow_min, __set_crushing_blow_min)

