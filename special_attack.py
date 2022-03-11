# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter

class SpecialAttack(ABC):
    """"
    Special skill is surprise attack--extra_attack_chance (0.0 to 1.0) it is successful.
    If it is successful, the character gets an attack and another turn (extra attack) in the current round.
    There is a caught_chance, the character is caught in which case no attack at all is rendered.
    If not rendered an extra attack or caught, the character does the normal attack.
    """

    def __init__(self):
        if issubclass(type(self), DungeonCharacter):
            self.__extra_attack_chance = 0.0
            self.__caught_chance = 0.0
        else:
            raise TypeError("should inherit Dungeonchar class")


    def __set_extra_attack_chance(self, value):
        if isinstance(value, float) and 0.0 <= value <= 1.0:
            self.__extra_attack_chance = value

        else:
            raise TypeError(f"value:{value} is not a float or not in range 0.0 to 1.0")

    def __get_extra_attack(self):
        return self.__extra_attack_chance

    extra_attack_chance = property(__get_extra_attack, __set_extra_attack_chance)

    def __set_caught_chance(self, value):
        if isinstance(value, float) and 0.0 <= value <= 1.0:
            self.__caught_chance = value

        else:
            raise TypeError(f"value:{value} is not a float or not in range 0.0 to 1.0")


    def __get_caught_chance(self):
        return self.__caught_chance

    caught_chance = property(__get_caught_chance, __set_caught_chance)


    @abstractmethod
    def attack_target(self, target):
        pass






