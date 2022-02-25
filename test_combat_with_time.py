import unittest
from dungeonchar import DungeonCharacter
from healable import Healable
from hero import Hero
import threading


class MockMonster(DungeonCharacter, Healable):
    def __init__(self, name, model, chance_to_heal):
        super().__init__(name, model)
        super(DungeonCharacter, self).__init__(chance_to_heal)
        # self.my_turn = True

    def attack_target(self, target):
        return super().attack_target(target)

    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)

    def combat(self, target):
        pass


class MockHero(Hero):
    """
    concrete implementation of abstract Hero class
    """
    def __init__(self, name, model) -> None:
        super().__init__(name, model)

    def attack_target(self, target):
        return super().attack_target(target)

    def combat(self, target):
        return super().combat(target)

    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)

    def use_health_potion(self):
        return super().use_health_potion()

    def use_vision_potion(self):
        return super().use_vision_potion()

class MockAnnouncer:
    """
    Mock object for Model/Game reference
    """

    def __init__(self) -> None:
        pass

    def announce(self, message):
        pass
        # print(message)


class MyTestCase(unittest.TestCase):
    def test_combat_no_hero_input(self):

        monster = MockMonster("monster", MockAnnouncer(), 1.0)
        monster.hp_total = 50
        monster.hp = monster.hp_total
        monster.attack_speed = 5
        monster.hit_chance = 1.0  # always lands an attack
        monster.damage_min = 10
        monster.damage_max = 11

        hero = MockHero("hero", MockAnnouncer())
        hero.hp_total = 50
        hero.hp = hero.hp_total
        hero.attack_speed = 5
        hero.hit_chance = 1.0  # always lands an attack
        hero.damage_min = 10
        hero.damage_max = 11

        monster.combat_with_time(hero, monster)

        self.assertGreater(monster.hp, 0)
        self.assertLessEqual(hero.hp, 0)


    def test_combat_only_hero_attacks(self):
        monster = MockMonster("monster", MockAnnouncer(), 1.0)
        monster.hp_total = 50
        monster.hp = monster.hp_total
        monster.attack_speed = 5
        monster.hit_chance = 0.0  # does not attack
        monster.damage_min = 10
        monster.damage_max = 11

        hero = MockHero("hero", MockAnnouncer())
        hero.hp_total = 50
        hero.hp = hero.hp_total
        hero.attack_speed = 5
        hero.hit_chance = 1.0  # always lands an attack
        hero.damage_min = 10
        hero.damage_max = 11

        p1 = threading.Thread(target= hero.set_attack_now, args=(monster,1))

        p2 = threading.Thread(target= monster.combat_with_time, args=(hero, monster))
        p1.start();p2.start()
        p2.join()
        p1.join()

        self.assertGreater(hero.hp, 0)
        self.assertLessEqual(monster.hp, 0)

    def test_hero_higher_attack_speed(self):
        monster = MockMonster("monster", MockAnnouncer(), 1.0)
        monster.hp_total = 50
        monster.hp = monster.hp_total
        monster.attack_speed = 3
        monster.hit_chance = 1.0  # always lands attack
        monster.damage_min = 10
        monster.damage_max = 11

        hero = MockHero("hero", MockAnnouncer())
        hero.hp_total = 50
        hero.hp = hero.hp_total
        hero.attack_speed = 5
        hero.hit_chance = 1.0  # always lands an attack
        hero.damage_min = 10
        hero.damage_max = 11

        p1 = threading.Thread(target=hero.set_attack_now, args=(monster, 1))

        p2 = threading.Thread(target=monster.combat_with_time, args=(hero, monster))
        p1.start();p2.start()
        p2.join()
        p1.join()

        self.assertGreater(hero.hp, 0)
        self.assertLessEqual(monster.hp, 0)


if __name__ == '__main__':
    unittest.main()
