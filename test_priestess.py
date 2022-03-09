# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from priestess import Priestess

class MockAnnouncer:
    """
    Mock object for Model/Game reference
    """
    def __init__(self) -> None:
        pass
    def announce(self, message):
        pass

class MyTestCase(unittest.TestCase):
    def test_priestess_stats(self):
        player = Priestess("player1",  MockAnnouncer())
        self.assertEqual(75, player.hp_total)
        self.assertEqual(75, player.hp)
        self.assertEqual(5, player.attack_speed)
        self.assertEqual(0.7, player.hit_chance)
        self.assertEqual(25, player.damage_min)
        self.assertEqual(45, player.damage_max)
        self.assertEqual(0.3, player.chance_to_block)
        self.assertEqual(1.0, player.chance_to_heal)
        self.assertEqual(20, player.min_heal_point)
        self.assertEqual(40, player.max_heal_point)

    def test_priestess_healing_power(self):
        player1 = Priestess("player1", MockAnnouncer())
        player1.chance_to_block = 0.0
        player2 = Priestess("player2", MockAnnouncer())
        player2.hit_chance = 1.0 # always lands a hit
        player2.damage_min = 19
        player2.damage_max = 20
        hp_before = player1.hp
        player2.attack_target(player1)
        self.assertEqual(hp_before, player1.hp,"player1 has not healed")

    def test_priestess_chance_to_block(self):
        player1 = Priestess("player1", MockAnnouncer())
        player1.chance_to_block = 1.0  # always blocks an attack
        player1.chance_to_heal = 0.0 # does not heal
        player2 = Priestess("player2", MockAnnouncer())
        player2.hit_chance = 1.0  # always lands a hit
        player2.damage_min = 19
        player2.damage_max = 20
        hp_before = player1.hp
        player2.attack_target(player1)
        self.assertEqual(hp_before, player1.hp, "player1 has taken a damage")



if __name__ == '__main__':
    unittest.main()
