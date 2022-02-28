import unittest
from monster import Monster
from healable import Healable
from hero import Hero
from dungeonchar import DungeonCharacter


class MockMonster(Monster):
    def __init__(self, name, model, chance_to_heal):
        super().__init__(name, model, chance_to_heal)
        self.my_turn = True

    def attack_target(self, target):
        return super().attack_target(target)

    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)


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


class MockHealableHero(Hero, Healable):

    def __init__(self, name, model, chance_to_heal):
        super().__init__(name = name, model= model)
        super(Hero, self).__init__(name = name, model= model)
        super(DungeonCharacter, self).__init__(chance_to_heal)
        self.healable = True

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
        monster = MockMonster("monster",MockAnnouncer(),0.1)
        monster.hp_total = 200
        monster.hp = monster.hp_total
        self.assertEqual(monster.hp, 200,"hp not reset to 200")
        self.assertEqual(monster.hp_total, 200, "hp_total not reset to 200")
        self.assertEqual(monster.attack_speed, 1,"attach speed not reset to 2")
        self.assertEqual(monster.hit_chance, 0.5, "hit_chance not set to 0.6")
        self.assertEqual(monster.damage_min, 20, "damage_min not set to 30")
        self.assertEqual(monster.damage_max, 30, "damage_max not set to 40")


    def test_monster_self_heal_after_attack(self):
        """
        creating a combat with attack speed 1. hp of monster and hero are 50. Both can give a damage of 10 or 11
        Hero lands the first attack. The monster always heals 10(min_heal) or 11(max_heal)

        So the monster hit point should always be equal to total_hp after healing
        And the hero hp should be always 10 or 11 less than the total hp
        """

        monster = MockMonster("monster", MockAnnouncer(), 1.0)  # always heals after being attacked
        monster.hp_total = 50
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
        self.assertLess(hero.hp, hero.hp_total) # hero is not healable, so current hp should be less

    def test_combat_self_heal_hero_after_attack(self):
        """
        creating a combat with attack speed 1. hp of monster and hero are 50. Both can give a damage of 10 or 11
        Hero lands the first attack. The monster and the hero always heals 11(min_heal) or 12(max_heal)

        So the monster and hero hit point should always be equal to total_hp after healing
        And the hero hp should be always 10 or 11 less than the total hp
        """

        monster = MockMonster("monster", MockAnnouncer(), 1.0)  # always heals after being attacked
        monster.hp_total = 50
        monster.hp = monster.hp_total
        monster.attack_speed = 1
        monster.hit_chance = 1.0  # always lands an attack
        monster.damage_min = 10
        monster.damage_max = 11
        monster.min_heal_point = 11
        monster.max_heal_point = 12

        hero = MockHealableHero("hero",MockAnnouncer(), 1.0) # always heals after being attacked
        hero.hp_total = 50
        hero.hp = hero.hp_total
        hero.attack_speed = 1
        hero.hit_chance = 1.0  # always lands an attack
        hero.damage_min = 10
        hero.damage_max = 11
        hero.min_heal_point = 11
        hero.max_heal_point = 12
        monster.combat(hero)
        self.assertEqual(monster.hp, monster.hp_total)  # the monster hit point should always be equal to total_hp after healing
        self.assertEqual(hero.hp, hero.hp_total) # the hero hit point should always be equal to total_hp after healing

if __name__ == '__main__':
    unittest.main()
