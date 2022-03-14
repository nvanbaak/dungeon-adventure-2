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
        self.__chance_to_block = 0.0
        self.__health_potions = 0
        self.__vision_potions = 0
        self.__vision = 3

    def set_attack_now(self, t_f = False):
            if self.hp > 0:
                # print(f" setting hero to attack :{t_f}")
                    # print("i am setting hero to attack")
                self.attack_now = t_f

    def __set_attack_now(self, t_f):
        if isinstance(t_f, bool):
            self.__attack_now = t_f
        else:
            raise TypeError(f"{t_f} not a boolean")

    def __get_attack_now(self):
        return self.__attack_now
    attack_now = property(__get_attack_now, __set_attack_now)

    def use_health_potion(self):
        """
        Uses a health potion if available
        """
        if self.health_potions > 0:
            self.health_potions -= 1
            amount_healed = random.randint(20, 40)
            self.hp += amount_healed

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

    def __set_chance_to_block(self, value):
        """ validates and sets the value for chance_to_block"""

        if isinstance(value, float) and 0.0 <= value <= 1.0 :
            self.__chance_to_block = value
        else:
            raise ValueError("chance to block should be a float in the range 0.0 to 1.0")

    def __get_chance_to_block(self):

        """ getter method returns the chance to block value"""
        return self.__chance_to_block

    chance_to_block = property(__get_chance_to_block, __set_chance_to_block)

    def __take_damage(self, dmg, source):
        """ Reduces the hp by the dmg value"""

        self.hp -= dmg
        self._DungeonCharacter__model.announce(f"{self.name} took {dmg} dmg from {source}!")
        if not self._is_alive:
            self._DungeonCharacter__model.announce(f"{self.name} has died!")


    def take_damage(self, dmg, source):

        """ If the damage is not from pit the hero gets a chance to block the damage """
        if source == "pit":
            self.__take_damage(dmg, source)
        else:
            if self.chance_to_block < random.random():
                self.__take_damage(dmg, source)

    def fall_into_pit(self):
        """generates a random value range 10 to 20 and reduce it from the hero's hp"""
        ret = random.randint(10, 20)
        self.take_damage(ret, "pit")
