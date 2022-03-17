# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from ogre import Ogre
from monster import Monster
from dungeonchar_db_access import DungeonCharDb

DB = DungeonCharDb()

class MyTestCase(unittest.TestCase):
    def test_ogre_init(self):
        ogre = Ogre("ogre", "model", hp_total = DB.get_data_monster("Ogre", "hp"),
                    attack_speed = DB.get_data_monster("Ogre", "attack_speed"),
                    hit_chance = DB.get_data_monster("Ogre", "hit_chance"),
                    damage_max = DB.get_data_monster("Ogre", "damage_max"),
                    damage_min = DB.get_data_monster("Ogre", "damage_min"),
                    chance_to_heal = DB.get_data_monster("Ogre", "chance_to_heal"),
                    min_heal_point = DB.get_data_monster("Ogre", "min_heal_point"),
                    max_heal_point = DB.get_data_monster("Ogre", "max_heal_point"))

        self.assertEqual(ogre.hp_total, 200, " hp_total stats dont match")
        self.assertEqual(ogre.hp, 200, "hp stats dont match")
        self.assertEqual(ogre.attack_speed, 2, "attack_speed stats dont match")
        self.assertEqual(ogre.hit_chance, 0.6, "hit_chance stats dont match")
        self.assertEqual(ogre.damage_min, 30, "damage_min stats dont match")
        self.assertEqual(ogre.damage_max, 60, "damage_max stats dont match")
        self.assertEqual(ogre.chance_to_heal, 0.1, " chance_to_heal stats dont match")
        self.assertEqual(ogre.min_heal_point, 30, "ogre.min_heal_point stats dont match")
        self.assertEqual(ogre.max_heal_point, 60, "max_heal_point stats dont match")

    def test_if_ogre_is_subclass_of_monster(self):
        ogre = Ogre("name", "model", hp_total = DB.get_data_monster("Ogre", "hp"),
                    attack_speed = DB.get_data_monster("Ogre", "attack_speed"),
                    hit_chance = DB.get_data_monster("Ogre", "hit_chance"),
                    damage_max = DB.get_data_monster("Ogre", "damage_max"),
                    damage_min = DB.get_data_monster("Ogre", "damage_min"),
                    chance_to_heal = DB.get_data_monster("Ogre", "chance_to_heal"),
                    min_heal_point = DB.get_data_monster("Ogre", "min_heal_point"),
                    max_heal_point = DB.get_data_monster("Ogre", "max_heal_point"))

        self.assertEqual(True, issubclass(type(ogre), Monster))


if __name__ == '__main__':
    unittest.main()
