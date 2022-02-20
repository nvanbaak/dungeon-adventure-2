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
        self.assertEquals("Bob", test_dc.name)
        self.assertIsNotNone(test_dc.hp)
        self.assertEquals(test_dc.hp, test_dc.hp_total)
        self.assertEquals(test_dc.attack_speed, 1)
        self.assertEquals(test_dc.damage_min, 20)
        self.assertEquals(test_dc.damage_max, 30)

    def test_hp(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # Test operations
        old_hp = test_dc.hp
        test_dc.hp -= 10
        self.assertEquals(test_dc, old_hp - 10)

        # Test assignment
        test_dc.hp = 777
        self.assertEquals(test_dc, 777)

        # Test exception handling
        exception_raised = False
        try:
            self.hp = "doggo"
        except ValueError:
            exception_raised = True
        self.assertTrue(exception_raised)

    def test_hp_total(self):
        test_dc = MockDC("Bob", MockAnnouncer)

        # test operations
        old_total = test_dc.hp_total
        test_dc.hp_total += 100
        self.assertEquals(test_dc, old_total + 100)



if __name__ == "__main__":
    unittest.main()