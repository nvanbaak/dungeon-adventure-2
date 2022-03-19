# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random

class CrushingBlow(ABC):
    """has parameters and methods to add the crushing blow power for dungeon character"""
    def __init__(self, **kwargs):
        if issubclass(type(self), DungeonCharacter):
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            raise TypeError("should inherit Dungeonchar class")

    def special_attack(self, target):
        """ the damage given in a crushing blow is 75 to 175, usually deadly
        :param target DungeonChar"""
        damage = random.randint(self.__crushing_blow_min, self.__crushing_blow_max)
        target.take_damage(damage, self.name)

    @abstractmethod
    def attack_target(self, target):
        pass

    def __set_crushing_blow_chance(self, value):
        """setter for __crushing_blow_chance
        :param value Float in range 0.0 to 1.0"""
        if isinstance(value, float) and 0.0 <= value <= 1.0:
            self.__crushing_blow_chance = value
        else:
            raise TypeError(f"{value} is not a float or in range 0.0 to 1.0")


    def __get_crushing_blow_chance(self):
        """getter for __crushing_blow_chance """
        return self.__crushing_blow_chance

    crushing_blow_chance = property(__get_crushing_blow_chance, __set_crushing_blow_chance)


    def __set_crushing_blow_max(self, value):
        """setter for __crushing_blow_max
        :param: int"""
        if isinstance(value, int):
            self.__crushing_blow_max = value

        else:
            raise TypeError(f"{value} not an integer")

    def __get_crushing_blow_max(self):
        """getter for __crushing_blow_max
        :return int """
        return self.__crushing_blow_max

    crushing_blow_max = property(__get_crushing_blow_max, __set_crushing_blow_max)

    def __set_crushing_blow_min(self, value):
        """setter for __crushing_blow_min
            :param: int"""
        if isinstance(value, int) and value < self.__crushing_blow_max:
            self.__crushing_blow_min = value

        else:
            raise TypeError(f"{value} not an integer or greater than crushing_blow_min value : {self.__crushing_blow_max}")

    def __get_crushing_blow_min(self):
        """getter for __crushing_blow_min
        :return int """

        return self.__crushing_blow_min

    crushing_blow_min = property(__get_crushing_blow_min, __set_crushing_blow_min)

