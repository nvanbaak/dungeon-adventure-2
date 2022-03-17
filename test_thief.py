# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from thief import Thief
from dungeonchar_db_access import DungeonCharDb
DB = DungeonCharDb()

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
        player = Thief("player1",  MockAnnouncer(), hp_total = DB.get_data_hero("Thief", "hp"),
                         attack_speed = DB.get_data_hero("Thief", "attack_speed"),
                         hit_chance = DB.get_data_hero("Thief", "hit_chance"),
                         damage_max = DB.get_data_hero("Thief", "damage_max"),
                         damage_min = DB.get_data_hero("Thief", "damage_min"),
                         chance_to_block = DB.get_data_hero("Thief", "chance_to_block"),
                         extra_attack_chance = DB.get_special_attack_stats("Thief", "extra_attack_chance"),
                         caught_chance = DB.get_special_attack_stats("Thief", "caught_chance"))
        self.assertEqual(75, player.hp_total)
        self.assertEqual(75, player.hp)
        self.assertEqual(6, player.attack_speed)
        self.assertEqual(0.8, player.hit_chance)
        self.assertEqual(20, player.damage_min)
        self.assertEqual(40, player.damage_max)
        self.assertEqual(0.4, player.chance_to_block)
        self.assertEqual(0.4, player.extra_attack_chance)
        self.assertEqual(0.2, player.caught_chance)

    def test_extra_attack(self):
        player1 = Thief("player1", MockAnnouncer(), hp_total = DB.get_data_hero("Thief", "hp"),
                         attack_speed = DB.get_data_hero("Thief", "attack_speed"),
                         hit_chance = DB.get_data_hero("Thief", "hit_chance"),
                         damage_max = DB.get_data_hero("Thief", "damage_max"),
                         damage_min = DB.get_data_hero("Thief", "damage_min"),
                         chance_to_block = DB.get_data_hero("Thief", "chance_to_block"),
                         extra_attack_chance = DB.get_special_attack_stats("Thief", "extra_attack_chance"),
                         caught_chance = DB.get_special_attack_stats("Thief", "caught_chance"))
        player1.extra_attack_chance = 1.0 # always lands an extra attack
        player1.hit_chance = 1.0 #always lays the attack
        player1.damage_max = 21 # damage given will be always 20 or 21

        player2 = Thief("player2", MockAnnouncer(), hp_total = DB.get_data_hero("Thief", "hp"),
                         attack_speed = DB.get_data_hero("Thief", "attack_speed"),
                         hit_chance = DB.get_data_hero("Thief", "hit_chance"),
                         damage_max = DB.get_data_hero("Thief", "damage_max"),
                         damage_min = DB.get_data_hero("Thief", "damage_min"),
                         chance_to_block = DB.get_data_hero("Thief", "chance_to_block"),
                         extra_attack_chance = DB.get_special_attack_stats("Thief", "extra_attack_chance"),
                         caught_chance = DB.get_special_attack_stats("Thief", "caught_chance"))
        player2.chance_to_block = 0.0 # does not block an attack
        hp_before = player2.hp

        # as player1 always gets an extra attack, the damage received by player2 will be more than 39 and less than 43
        player1.attack_target(player2)
        self.assertEqual(player1.extra_attack_chance, 1.0)
        self.assertEqual(player2.chance_to_block, 0.0)
        self.assertLessEqual(player2.hp, hp_before - 40)
        self.assertGreaterEqual(player2.hp, hp_before - 42)


if __name__ == '__main__':
    unittest.main()
