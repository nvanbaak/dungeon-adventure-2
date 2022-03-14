# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random

class Healable(ABC):
    def __init__(self):
        if issubclass(type(self), DungeonCharacter):
            self.__chance_to_heal = 0.0
            self.__min_heal_point = 0
            self.__max_heal_point = 0

        else:
            raise TypeError("should inherit Dungeonchar class")


    def __set_chance_to_heal(self, chance_to_heal):
        if isinstance(chance_to_heal, float) and 0 < chance_to_heal <= 1:
            self.__chance_to_heal = chance_to_heal

    def __get_chance_to_heal(self):
        return self.__chance_to_heal

    chance_to_heal = property(__get_chance_to_heal, __set_chance_to_heal)

    def __set_min_heal_point(self, value):
        if isinstance(value, int) and value < self.hp_total:
            self.__min_heal_point = value
        else:
            raise ValueError(f"input : {value} should be an integer and less that total hp : {self.hp_total}")

    def __get_min_heal_point(self):
        return self.__min_heal_point

    min_heal_point = property(__get_min_heal_point, __set_min_heal_point)

    def __set_max_heal_point(self, value):
        if isinstance(value, int) and self.hp_total > value > self.__min_heal_point:
            self.__max_heal_point = value
        else:
            raise ValueError(f"input : {value} should be an integer and less that total hp : {self.hp_total} \
            and min_heal_point :{self.__min_heal_point}")

    def __get_max_heal_point(self):
        return self.__max_heal_point

    max_heal_point = property(__get_max_heal_point, __set_max_heal_point)


    @abstractmethod
    def hp(self, value):
        pass

    @abstractmethod
    def hp_total(self):
        pass

    def heal_itself(self):
        heal_chance = random.random()
        if heal_chance  <= self.__chance_to_heal:
            healable = random.randint(self.__min_heal_point, self.__max_heal_point)
            if self.hp + healable <= self.hp_total:
                self.hp += healable
                return str(f"{healable} hp is healed")
            else:
                self.hp = self.hp_total
                return str(f"{healable} hp is healed")
        else:
            return str("not healed")


    @abstractmethod
    def take_damage(self, dmg, source):
        pass





