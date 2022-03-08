import unittest
from hero import Hero

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

class Hero_Tests(unittest.TestCase):
    def test_init(self):
        test_hero = MockHero("Cloud", MockAnnouncer())

        self.assertEqual(test_hero.health_potions, 0)
        self.assertEqual(test_hero.vision_potions, 0)
        self.assertEqual(test_hero.vision, 3)

    def test_health_potion(self):
        test_hero = MockHero("Steve", MockAnnouncer())
        test_hero.hp_total = 200
        test_hero.hp = 100

        # test using health potion without available potions
        test_hero.use_health_potion()
        self.assertEqual(test_hero.hp, 100)
        self.assertEqual(test_hero.health_potions, 0)

        # test operations
        test_hero.health_potions += 10
        self.assertEqual(test_hero.health_potions, 10)
        test_hero.health_potions -= 5
        self.assertEqual(test_hero.health_potions, 5)

        # test health potion use with available potions
        test_hero.use_health_potion()
        hero_was_healed = test_hero.hp > 100
        self.assertTrue(hero_was_healed)
        self.assertEqual(test_hero.health_potions, 4)

        new_hp = test_hero.hp
        test_hero.use_health_potion()
        hero_was_healed_again = test_hero.hp > new_hp
        self.assertTrue(hero_was_healed_again)
        self.assertEqual(test_hero.health_potions, 3)

        # test no overheal
        test_hero.health_potions += 10
        while test_hero.health_potions > 0:
            test_hero.use_health_potion()
        self.assertEqual(test_hero.hp, test_hero.hp_total)
        self.assertEqual(test_hero.health_potions, 0)

    def test_vision_potion(self):
        test_hero = MockHero("Vision", MockAnnouncer())

        # test using vis potion with no potions
        test_hero.use_vision_potion()
        self.assertEqual(test_hero.vision_potions, 0)
        self.assertEqual(test_hero.vision, 3)

        # test operations
        test_hero.vision_potions += 10
        self.assertEqual(test_hero.vision_potions, 10)
        test_hero.vision_potions -= 5
        self.assertEqual(test_hero.vision_potions, 5)

        # test using vis potion with nonzero potions
        test_hero.use_vision_potion()
        self.assertEqual(test_hero.vision_potions, 4)
        self.assertEqual(test_hero.vision, 8)

        test_hero.vision = 5

        test_hero.use_vision_potion()
        self.assertEqual(test_hero.vision_potions, 3)
        self.assertEqual(test_hero.vision, 10)


<<<<<<< HEAD
=======
    def test_chance_to_block_setter_getter(self):
        test_hero = MockHero("Vision", MockAnnouncer())

        self.assertEqual(test_hero.chance_to_block, 0.0)

        test_hero.chance_to_block = 0.8
        self.assertEqual(test_hero.chance_to_block, 0.8)

    def test_chance_to_block_setter_invalid_input(self):
        exception_raised = False

        test_hero = MockHero("Vision", MockAnnouncer())
        try:
            test_hero.chance_to_block = 2.0
        except ValueError:
            exception_raised = True

        self.assertEqual(exception_raised, True)

    def test_chance_to_block_setter_invalid_input_2(self):
        exception_raised = False

        test_hero = MockHero("Vision", MockAnnouncer())
        try:
            test_hero.chance_to_block = "abc"
        except ValueError:
            exception_raised = True

        self.assertEqual(exception_raised, True)

    def test_take_damage_pit(self):
        test_hero = MockHero("Vision", MockAnnouncer())
        hero_hp = test_hero.hp
        test_hero.take_damage(10, "pit")

        self.assertEqual(test_hero.hp, hero_hp - 10 )

    def test_take_damage_chance_to_block_as_1(self):
        # hero always blocks an attack
        test_hero = MockHero("Vision", MockAnnouncer())
        test_hero.chance_to_block = 1.0
        test_hero.take_damage(10, "monster")
        self.assertEqual(test_hero.hp, test_hero.hp_total)

    def test_take_damage_chance_to_block_as_0(self):
        # hero always takes a damage
        test_hero = MockHero("Vision", MockAnnouncer())
        test_hero.chance_to_block = 0.0
        test_hero.take_damage(10, "monster")
        self.assertLess(test_hero.hp, test_hero.hp_total)


    def test_fall_into_pit(self):
        test_hero = MockHero("hero", MockAnnouncer())
        hero_hp_before_fall = test_hero.hp
        test_hero.fall_into_pit()
        self.assertLess(test_hero.hp, hero_hp_before_fall - 9)
        self.assertGreater(test_hero.hp, hero_hp_before_fall - 20)




>>>>>>> sg_hero_chars
if __name__ == "__main__":
    unittest.main()