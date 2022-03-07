import unittest
from warrior import Warrior

class MockAnnouncer:
    """
    Mock object for Model/Game reference
    """
    def __init__(self) -> None:
        pass
    def announce(self, message):
        pass


class MyTestCase(unittest.TestCase):
    def test_warrior_stats(self):
        player = Warrior("player1",  MockAnnouncer())
        self.assertEqual(125, player.hp_total)
        self.assertEqual(125, player.hp)
        self.assertEqual(4, player.attack_speed)
        self.assertEqual(0.8, player.hit_chance)
        self.assertEqual(35, player.damage_min)
        self.assertEqual(60, player.damage_max)
        self.assertEqual(0.2, player.chance_to_block)
        self.assertEqual(0.4, player.crushing_blow_chance)
        self.assertEqual(75, player.crushing_blow_min)
        self.assertEqual(175, player.crushing_blow_max)


    def test_crushing_blow_chance_property(self):
        player = Warrior("player1", MockAnnouncer())
        player.crushing_blow_chance = 0.5
        self.assertEqual(0.5, player.crushing_blow_chance)


    def test_crushing_blow_max_property(self):
        player = Warrior("player1", MockAnnouncer())
        player.crushing_blow_max = 100
        self.assertEqual(100, player.crushing_blow_max)

    def test_crushing_blow_min_property(self):
        player = Warrior("player1", MockAnnouncer())
        player.crushing_blow_min = 35
        self.assertEqual(35, player.crushing_blow_min)

    def test_crushing_blow_max_property_invalid_input(self):
        player = Warrior("player1", MockAnnouncer())
        exception_raised = False
        try:
            player.crushing_blow_max = 10
        except TypeError:
            exception_raised = True

        self.assertEqual(True, exception_raised)

    def test_crushing_blow_min_property_invalid_input(self):
        player = Warrior("player1", MockAnnouncer())
        exception_raised = False
        try:
            player.crushing_blow_min = 350
        except TypeError:
            exception_raised = True

        self.assertEqual(True, exception_raised)


    def test_special_attack(self):

        player1 = Warrior("player1", MockAnnouncer())
        player1.crushing_blow_chance = 1.0
        player2 = Warrior("player2", MockAnnouncer())
        player2.chance_to_block = 0.0 # player2 does not block the attack
        player2_hp = player2.hp   # player2 initial hp

        player1.attack_target(player2)
        self.assertLess(player2.hp, player2_hp - 74)  # player2 should have taken a min-damage of 75





if __name__ == '__main__':
    unittest.main()
