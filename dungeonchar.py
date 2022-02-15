# nvb / 7 Feb 2022
from abc import ABC, abstractmethod
import random

class DungeonCharacter(ABC):
    """
    Abstract base class used for all dungeon characters
    """
    def __init__(self, name, model) -> None:
        self.__name = name
        self.__hp_total = random.choice(range(50, 100))
        self.__hp = self.hp_total
        self.__attack_speed = 1
        self.__hit_chance = .5
        self.__damage_min = 20
        self.__damage_max = 30
        self.__model = model

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        if not isinstance(value, int):
            raise TypeError("hp must be a number!")
        self.__hp = value

    @property
    def hp_total(self):
        return self.__hp_total
    @hp_total.setter
    def hp_total(self, value):
        if value < 1:
            raise ValueError("hp total must be positive!")
        elif not isinstance(self.hp_total, int):
            raise TypeError("hp total must be a number!")
        else: 
            self.__hp_total = value

    @property
    def attack_speed(self):
        return self.__attack_speed
    @attack_speed.setter
    def attack_speed(self, value):
        if value < 1:
            raise ValueError("attack speed cannot be less than 1")
        elif not isinstance(self.__attack_speed, int):
            raise TypeError("attack speed must be a number!")
        else:
            self.__attack_speed = value

    @property
    def hit_chance(self):
        return self.__hit_chance
    @hit_chance.setter
    def hit_chance(self, value):
        if not isinstance(self.__hit_chance, float):
            raise TypeError("hit change must be a number between 0 and 1")

    @property
    def damage_min(self):
        return self.__damage_min
    @damage_min.setter
    def damage_min(self, value):
        if not isinstance(self.__damage_min, int):
            raise TypeError("damage min must be an integer!")
        # min can't be higher than max
        if self.__damage_max < value:
            self.__damage_max = value
        self.__damage_min = value

    @property
    def damage_max(self):
        return self.__damage_max
    @damage_max.setter
    def damage_max(self, value):
        if not isinstance(self.__damage_max, int):
            raise TypeError("damage max must be an integer!")
        # max can't be lower than min
        if self.__damage_min > value:
            self.__damage_min = value
        self.__damage_max = value

    @property
    def _is_alive(self):
        return self.__hp > 0


    @abstractmethod
    def attack(self, ch):
        """
        Method for engaging of one round of combat with a target
        """
        my_attacks = 0
        target_attacks = 0
        my_turn = True
        while my_attacks < self.attack_speed and target_attacks < ch.attack_speed:
            # characters alternate attacking until one of them dies
            # or they both run out of attacks
            if my_turn:
                if my_attacks < self.attack_speed:
                    hit = random.random() < self.hit_chance
                    if hit:
                        damage = random.randint(self.damage_min, self.damage_max)
                        ch.take_damage(damage)
                    my_turn = False
                    my_attacks += 1
                    if not ch.alive:
                        break
            else:
                if target_attacks < ch.attack_speed:
                    hit = random.random() < ch.hit_chance
                    if hit:
                        damage = random.randrange(self.damage_min, self.damage_max)
                        self.take_damage(damage)
                    my_turn = True
                    target_attacks += 1
                    if not self.alive:
                        break

    @abstractmethod
    def take_damage(self, dmg):
        self.hp -= dmg
