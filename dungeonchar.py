# nvb / 7 Feb 2022
from abc import ABC, abstractmethod
import random
from time import *
import time


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
        self.__healable = False
        self.__model = model

    def __set_healable(self, t_f):
        ##
        if isinstance(t_f, bool):
            self.__healable = t_f

    def __get_healable(self):
        ##
        return self.__healable

    healable = property(__get_healable, __set_healable)


    @staticmethod
    def combat_with_time(hero, monster):
        ##
        if issubclass(type(hero), DungeonCharacter) and issubclass(type(monster), DungeonCharacter):
            while hero._is_alive and monster._is_alive:
                # print("i am here")
                combat_time = max(hero.attack_speed, monster.attack_speed)
                t_hero_now = time.time()
                t_mons_now = time.time()
                t_end = time.time() + (1.5 * combat_time)
                # adding 2sec so that the character with high attach speed gets to complete all attacks for the round even with sleep
                while time.time() < t_end:
                    monster_attack_time = combat_time / monster.attack_speed
                    hero_attack_time = combat_time / hero.attack_speed
                    if time.time() >= t_mons_now + monster_attack_time:
                        hp_before_attack = hero.hp
                        # print("monster is attacking")
                        monster.attack_target(hero)
                        if not hero._is_alive:
                            break
                        # print(f"hero hp:{hero.hp}")
                        if hero.healable and hero.hp < hp_before_attack: # hero is healable and has been attacked
                            heal_message = hero.heal_itself()
                            hero._DungeonCharacter__model.announce(f"{hero._DungeonCharacter__name}: {heal_message}")

                        sleep(1) #to multi thread

                        t_mons_now = time.time()

                    if time.time() >= t_hero_now + hero_attack_time and hero.attack_now :
                        hp_before_attack = monster.hp
                        # print("hero is attacking")
                        hero.attack_target(monster)
                        if not monster._is_alive:
                            break
                        # print(f"monster hp:{monster.hp}")
                        hero.attack_now = False
                        if monster.healable and monster.hp < hp_before_attack:  # hero is healable and has been attacked
                            heal_message = hero.heal_itself()
                            monster._DungeonCharacter__model.announce(f"{monster._DungeonCharacter__name}: {heal_message}")

                        t_hero_now = time.time()

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if not isinstance(value, int):
            raise TypeError("hp must be an integer!")
        else:
            self.__hp = self.__hp_total if value > self.__hp_total else value

    @property
    def hp_total(self):
        return self.__hp_total

    @hp_total.setter
    def hp_total(self, value):
        if value < 1:
            raise ValueError("hp total must be positive!")
        elif not isinstance(value, int):
            raise TypeError("hp total must be a number!")
        else:
            self.__hp_total = value
            # hp can't be higher than hp_total
            if self.__hp > self.__hp_total:
                self.__hp = value

    @property
    def attack_speed(self):
        return self.__attack_speed

    @attack_speed.setter
    def attack_speed(self, value):
        if value < 1:
            raise ValueError("attack speed cannot be less than 1")
        elif isinstance(value, int):
            self.__attack_speed = value
        else:
            raise TypeError("attack speed must be a number!")

    @property
    def hit_chance(self):
        return self.__hit_chance

    @hit_chance.setter
    def hit_chance(self, value):
        if not isinstance(value, float):
            raise TypeError("hit chance must be a float")
        elif value < 0:
            raise ValueError("hit chance must be at least 0")
        self.__hit_chance = value

    @property
    def damage_min(self):
        return self.__damage_min

    @damage_min.setter
    def damage_min(self, value):
        if not isinstance(value, int):
            raise TypeError("damage min must be an integer!")
        if value < 0:
            raise ValueError("damage min can't be less than 0!")
        # min can't be higher than max
        if self.__damage_max < value:
            self.__damage_max = value
        self.__damage_min = value

    @property
    def damage_max(self):
        return self.__damage_max

    @damage_max.setter
    def damage_max(self, value):
        if not isinstance(value, int):
            raise TypeError("damage max must be an integer!")
        if value < 0:
            raise ValueError("damage min can't be less than 0!")
        # max can't be lower than min
        if self.__damage_min > value:
            self.__damage_min = value
        self.__damage_max = value

    @property
    def _is_alive(self):
        return self.__hp > 0

    @abstractmethod
    def attack_target(self, target):
        """
        Method for attacking a target
        """
        hit_landed = random.random() < self.hit_chance
        if hit_landed:
            damage = random.randint(self.damage_min, self.damage_max)
            target.take_damage(damage, self.name)

    @abstractmethod
    def combat(self, target):
        """
        Method for executing a full round of combat where this character attacks first
        """
        my_attacks = 0
        target_attacks = 0
        my_turn = True
        while my_attacks < self.attack_speed or target_attacks < target.attack_speed:
            # characters alternate attacking until one of them dies
            # or they both run out of attacks
            if my_turn:
                if my_attacks < self.attack_speed:
                    self.attack_target(target)
                    my_turn = False
                    my_attacks += 1
                    if not target._is_alive:
                        break
            else:
                if target_attacks < target.attack_speed:
                    target.attack_target(self)
                    my_turn = True
                    target_attacks += 1
                    if not self._is_alive:
                        break

    @abstractmethod
    def take_damage(self, dmg, source):
        self.hp -= dmg
        self.__model.announce(f"{self.__name} took {dmg} dmg from {source}!")
        if not self._is_alive:
            self.__model.announce(f"{self.__name} has died!")
