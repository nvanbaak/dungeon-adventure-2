import unittest
from dungeonchar import DungeonCharacter

class MockDC(DungeonCharacter):
    def __init__(self, name, model) -> None:
        super().__init__(name, model)

    def attack(self, ch):
        return super().attack(ch)
    def take_damage(self, dmg):
        return super().take_damage(dmg)


class DungeonCharTests(unittest.TestCase):
    def test_init(self):
        bob_the_adventurer = MockDC("Bob", None)
        print(bob_the_adventurer)

if __name__ == "__main__":
    unittest.main()