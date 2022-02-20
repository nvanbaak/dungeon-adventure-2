from logging import exception
import unittest
from unittest.mock import Mock
from dungeonchar import DungeonCharacter

class MockDC(DungeonCharacter):
    """
    A concrete version of the normally abstract DungeonCharacter for testing purposes
    """
    def __init__(self, name, model) -> None:
        super().__init__(name, model)

    def attack_target(self, target):
        return super().attack_target(target)
    def combat(self, target):
        return super().combat(target)
    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)

class MockAnnouncer:
    """
    Mock object for Model/Game reference
    """
    def __init__(self) -> None:
        pass
    def announce(self, message):
        pass
        # print(message)

class DungeonCharTests(unittest.TestCase):
    def test_init(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        self.assertIsNotNone(test_dc)
        self.assertEqual("Bob", test_dc.name)
        self.assertIsNotNone(test_dc.hp)
        self.assertEqual(test_dc.hp, test_dc.hp_total)
        self.assertEqual(test_dc.attack_speed, 1)
        self.assertEqual(test_dc.damage_min, 20)
        self.assertEqual(test_dc.damage_max, 30)

    def test_hp(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        old_hp = test_dc.hp
        test_dc.hp -= 10
        self.assertEqual(test_dc.hp, old_hp - 10)

        # Test assignment
        test_dc.hp = 777
        self.assertEqual(test_dc.hp, 777)

        # Test exception handling
        exception_raised = False
        try:
            test_dc.hp = "doggo"
        except TypeError:
            exception_raised = True
        self.assertTrue(exception_raised)

    def test_hp_total(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # test operations
        old_total = test_dc.hp_total
        test_dc.hp_total += 100
        self.assertEqual(test_dc.hp_total, old_total + 100)
        test_dc.hp_total -= 100
        self.assertEqual(test_dc.hp_total, old_total)

        # Test assignment
        test_dc.hp_total = 200
        self.assertEqual(test_dc.hp_total, 200)
        test_dc.hp_total = 400
        self.assertEqual(test_dc.hp_total, 400)

        # test reducing hp_total below hp also reduces hp
        test_dc.hp = 50
        test_dc.hp_total = 20
        self.assertEqual(test_dc.hp, 20)

        # Test exception handling
        excepts_floats = False
        excepts_nonints = False
        excepts_zero = False
        excepts_negatives = False

        try:
            test_dc.hp_total = 4.20
        except TypeError:
            excepts_floats = True
        try:
            test_dc.hp_total = "fish"
        except TypeError:
            excepts_nonints = True
        try:
            test_dc.hp_total = 0
        except ValueError:
            excepts_zero = True
        try:
            test_dc.hp_total = -10
        except ValueError:
            excepts_negatives = True

        self.assertEqual(excepts_floats, True)
        self.assertEqual(excepts_nonints, True)
        self.assertEqual(excepts_zero, True)
        self.assertEqual(excepts_negatives, True)

    def test_attack_speed(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        # =
        old_a_s = test_dc.attack_speed
        test_dc.attack_speed = 10
        self.assertEqual(test_dc.attack_speed, 10)
        test_dc.attack_speed = old_a_s
        self.assertEqual(test_dc.attack_speed, old_a_s)

        # +-
        test_dc.attack_speed += 15
        self.assertEqual(test_dc.attack_speed, old_a_s + 15)
        test_dc.attack_speed -= 15
        self.assertEqual(test_dc.attack_speed, old_a_s)

        # Test exception handling
        excepts_floats = False
        excepts_nonints = False
        excepts_zero = False
        excepts_negatives = False

        try:
            test_dc.attack_speed = 4.20
        except TypeError:
            excepts_floats = True
        try:
            test_dc.attack_speed = "fish"
        except TypeError:
            excepts_nonints = True
        try:
            test_dc.attack_speed = 0
        except ValueError:
            excepts_zero = True
        try:
            test_dc.attack_speed = -10
        except ValueError:
            excepts_negatives = True

        self.assertEqual(excepts_floats, True)
        self.assertEqual(excepts_nonints, True)
        self.assertEqual(excepts_zero, True)
        self.assertEqual(excepts_negatives, True)

    def test_hit_chance(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        # =
        old_hc = test_dc.hit_chance
        test_dc.hit_chance = .69
        self.assertEqual(test_dc.hit_chance, .69)
        test_dc.hit_chance = old_hc
        self.assertEqual(test_dc.hit_chance, old_hc)

        # +-
        test_dc.hit_chance += 0.1
        self.assertEqual(test_dc.hit_chance, old_hc + 0.1)
        test_dc.hit_chance -= 0.1
        self.assertEqual(test_dc.hit_chance, old_hc)

        # Test exception handling
        excepts_nonfloats = False
        excepts_negatives = False

        try:
            test_dc.hit_chance = "fish"
        except TypeError:
            excepts_nonfloats = True
        try:
            test_dc.hit_chance = -10.0
        except ValueError:
            excepts_negatives = True

        self.assertEqual(excepts_nonfloats, True)
        self.assertEqual(excepts_negatives, True)

    def test_dmg_min(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        # =
        old_dm = test_dc.damage_min
        test_dc.damage_min = 5
        self.assertEqual(test_dc.damage_min, 5)
        test_dc.damage_min = old_dm
        self.assertEqual(test_dc.damage_min, old_dm)

        # +-
        test_dc.damage_min += 40
        self.assertEqual(test_dc.damage_min, old_dm + 40)
        test_dc.damage_min -= 40
        self.assertEqual(test_dc.damage_min, old_dm)

        # test damage_max gets updated
        test_dc.damage_min = 20
        test_dc.damage_max = 30
        test_dc.damage_min += 40
        self.assertEqual(test_dc.damage_min, test_dc.damage_min)

        # Test exception handling
        excepts_floats = False
        excepts_nonints = False
        excepts_negatives = False

        try:
            test_dc.damage_min = 4.20
        except TypeError:
            excepts_floats = True
        try:
            test_dc.damage_min = "fish"
        except TypeError:
            excepts_nonints = True
        try:
            test_dc.damage_min = -10
        except ValueError:
            excepts_negatives = True

        self.assertEqual(excepts_floats, True)
        self.assertEqual(excepts_nonints, True)
        self.assertEqual(excepts_negatives, True)

    def test_dmg_max(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        # =
        old_dm = test_dc.damage_max
        test_dc.damage_max = 5
        self.assertEqual(test_dc.damage_max, 5)
        test_dc.damage_max = old_dm
        self.assertEqual(test_dc.damage_max, old_dm)

        # +-
        test_dc.damage_max += 40
        self.assertEqual(test_dc.damage_max, old_dm + 40)
        test_dc.damage_max -= 40
        self.assertEqual(test_dc.damage_max, old_dm)

        # test damage_max gets updated
        test_dc.damage_max = 40
        test_dc.damage_min = 20
        test_dc.damage_max -= 40
        self.assertEqual(test_dc.damage_max, test_dc.damage_min)

        # Test exception handling
        excepts_floats = False
        excepts_nonints = False
        excepts_negatives = False

        try:
            test_dc.damage_max = 4.20
        except TypeError:
            excepts_floats = True
        try:
            test_dc.damage_max = "fish"
        except TypeError:
            excepts_nonints = True
        try:
            test_dc.damage_max = -10
        except ValueError:
            excepts_negatives = True

        self.assertEqual(excepts_floats, True)
        self.assertEqual(excepts_nonints, True)
        self.assertEqual(excepts_negatives, True)

    def test_aliveness(self):
        test_dc = MockDC("Bob", MockAnnouncer())

        self.assertTrue(test_dc._is_alive)
        test_dc.take_damage(600, "the developers")
        self.assertFalse(test_dc._is_alive)

    def test_attack(self):
        # two fighters, one of which does no damage, the other of which always deals 1/turn
        fighter1 = MockDC("fighter 1", MockAnnouncer())
        fighter1.damage_max = 1
        fighter1.hit_chance = 1.0
        fighter1.hp_total = 10

        fighter2 = MockDC("fighter 2", MockAnnouncer())
        fighter2.damage_max = 0
        fighter2.hp_total = 10

        # one round of combat should leave fighter1 at full health and 2 at 9
        fighter1.attack_target(fighter2)
        self.assertEqual(fighter1.hp, 10)
        self.assertEqual(fighter2.hp, 9)

        # fighting until one of them dies should leave figter1 at 2 hp
        fighter2.damage_min = 1
        fighter2.hit_chance = 1.0

        for _ in range(0, 10):
            fighter1.attack_target(fighter2)
            if fighter2._is_alive:
                fighter2.attack_target(fighter1)
        self.assertEqual(fighter1.hp, 2)
        self.assertFalse(fighter2._is_alive)

    def test_attack_speed(self):
        fast_fighter = MockDC("fastguy", MockAnnouncer())
        fast_fighter.hp_total = 10
        fast_fighter.damage_max = 1
        fast_fighter.hit_chance = 1.0
        fast_fighter.attack_speed = 2

        slow_fighter = MockDC("slowguy", MockAnnouncer())
        slow_fighter.hp_total = 10
        slow_fighter.damage_max = 1
        slow_fighter.hit_chance = 1.0

        # fighting to the death should leave fastguy at 6HP
        while slow_fighter._is_alive:
            fast_fighter.combat(slow_fighter)
        self.assertEqual(fast_fighter.hp, 5)

    def test_hit_chance(self):
        accurate_dude = MockDC("accuratedude", MockAnnouncer())
        accurate_dude.hp_total = 1000
        accurate_dude.hp = 1000
        accurate_dude.damage_max = 1
        accurate_dude.hit_chance = 0.8

        drunk_dude = MockDC("drunkdude", MockAnnouncer())
        drunk_dude.hp_total = 1000
        drunk_dude.hp = 1000
        drunk_dude.damage_max = 1
        drunk_dude.hit_chance = 0.2

        for _ in range(0, 1000):
            accurate_dude.combat(drunk_dude)

        # statistically speaking drunk dude should have missed more
        probability_isnt_a_lie = accurate_dude.hp > drunk_dude.hp
        self.assertTrue(probability_isnt_a_lie)







if __name__ == "__main__":
    unittest.main()