import unittest
from monster import Monster
from hero import Hero


class MockMonster(Monster):

    def __init__(self, name, model):
        super().__init__(name, model)
        self.my_turn = True

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

    def test_monster__init__values(self):
        monster = MockMonster("monster",MockAnnouncer())
        monster.chance_to_heal = 0.1
        monster.hp_total = 200
        monster.hp = monster.hp_total
        monster.min_heal_point = 15
        monster.max_heal_point = 30
        self.assertEqual(monster.hp, 200,"hp not reset to 200")
        self.assertEqual(monster.hp_total, 200, "hp_total not reset to 200")
        self.assertEqual(monster.attack_speed, 1,"attach speed not reset to 1")
        self.assertEqual(monster.hit_chance, 0.5, "hit_chance not set to 0.5")
        self.assertEqual(monster.damage_min, 20, "damage_min not set to 20")
        self.assertEqual(monster.damage_max, 30, "damage_max not set to 30")
        self.assertEqual(monster.min_heal_point, 15, "min heal point not set to 15")
        self.assertEqual(monster.max_heal_point, 30, "max heal point not set to 30")


    def test_monster_self_heal_after_attack(self):
        """
        creating a combat with attack speed 1. hp of monster and hero are 50. Both can give a damage of 10 or 11
        Hero lands the first attack. The monster always heals 10(min_heal) or 11(max_heal)

        So the monster hit point should always be equal to total_hp after healing
        And the hero hp should be always 10 or 11 less than the total hp
        """

        monster = MockMonster("monster", MockAnnouncer())  # always heals after being attacked
        monster.hp_total = 50
        monster.chance_to_heal = 1.0
        monster.min_heal_point = 11
        monster.max_heal_point = 12
        monster.hp = monster.hp_total
        monster.attack_speed = 1
        monster.hit_chance = 1.0  # always lands an attack
        monster.damage_min = 10
        monster.damage_max = 11

        hero = MockHero("hero", MockAnnouncer())
        hero.hp_total = 50
        hero.hp = hero.hp_total
        hero.attack_speed = 1
        hero.hit_chance = 1.0  # always lands an attack
        hero.damage_min = 10
        hero.damage_max = 11
        monster.combat(hero)
        self.assertEqual(monster.hp, monster.hp_total) # the monster hit point should always be equal to total_hp after healing

if __name__ == '__main__':
    unittest.main()
