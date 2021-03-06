from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
import random

class Hero(DungeonCharacter, ABC):
    """
    A class representing a character controlled by the player
    """
    def __init__(self, name, model, **kwargs) -> None:
        super().__init__(name, model, **kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__health_potions = 0
        self.__vision_potions = 0
        self.__vision = 3

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
        self.model.announce(f"{self.name} took {dmg} dmg from {source}!")
        if not self._is_alive:
            self.model.announce(f"{self.name} has died!")


    def take_damage(self, dmg, source):

        """ If the damage is not from pit the hero gets a chance to block the damage """
        if source == "pit":
            self.__take_damage(dmg, source)
        else:
            if self.chance_to_block < random.random():
                self.__take_damage(dmg, source)
            else:
                self.model.announce(f" {self.name} has blocked the attack " )

    def fall_into_pit(self):
        """generates a random value range 10 to 20 and reduce it from the hero's hp"""
        ret = random.randint(10, 20)
        self.take_damage(ret, "pit")
