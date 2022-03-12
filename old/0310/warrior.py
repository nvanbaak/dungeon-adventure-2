# name  : Shoby Gnanasekaran
# net id: shoby

from hero import Hero
import random


class Warrior(Hero):
    """ Warrior is a hero character that a player can choose. It is inherited from Hero class
    A warrior has a special attack Crushing Blow which has a 40% chance of succeeding. Warrior has its own stats"""

    def __init__(self, name, model):
        super().__init__(name, model)
        self.hp_total = 125
        self.hp = self.hp_total
        self.attack_speed = 4
        self.hit_chance = 0.8
        self.damage_min = 35
        self.damage_max = 60
        self.chance_to_block = 0.2
        self.__crushing_blow_chance = 0.4
        self.__crushing_blow_min = 75
        self.__crushing_blow_max = 175

    def __special_attack(self, target):

        """ the damage given in a crushing blow is 75 to 175, usually deadly"""
        damage = random.randint(self.__crushing_blow_min, self.__crushing_blow_max)
        target.take_damage(damage, self.name)

    def attack_target(self, target):
        """ check if it can do a crushing blow special attack, else performs a normal attack"""
        special_attack = random.random() < self.__crushing_blow_chance
        if special_attack:
            self.__special_attack(target)
        else:
            super().attack_target(target)

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











