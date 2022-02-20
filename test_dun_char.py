from logging import exception
import unittest
from dungeonchar import DungeonCharacter

class MockDC(DungeonCharacter):
    """
    A concrete version of the normally abstract DungeonCharacter for testing purposes
    """
    def __init__(self, name, model) -> None:
        super().__init__(name, model)

    def attack(self, ch):
        return super().attack(ch)
    def take_damage(self, dmg):
        return super().take_damage(dmg)

class MockAnnouncer:
    """
    Mock object for Model/Game reference
    """
    def __init__(self) -> None:
        pass
    def announce(self, message):
        print(message)

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


if __name__ == "__main__":
    unittest.main()