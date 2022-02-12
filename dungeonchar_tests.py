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
    def get_model(self):
        return self.__model

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
        self.assertIsInstance(test_dc.get_model(), MockAnnouncer)



if __name__ == "__main__":
    unittest.main()