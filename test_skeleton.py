# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from skeleton import Skeleton
from monster import Monster
from dungeonchar_db_access import DungeonCharDb

DB = DungeonCharDb()
class MyTestCase(unittest.TestCase):
    def test_skeleton_init(self):
        skeleton = Skeleton("skeleton", "model", hp_total = DB.get_data_monster("Skeleton", "hp"),
                            attack_speed = DB.get_data_monster("Skeleton", "attack_speed"),
                            hit_chance = DB.get_data_monster("Skeleton", "hit_chance"),
                            damage_max = DB.get_data_monster("Skeleton", "damage_max"),
                            damage_min = DB.get_data_monster("Skeleton", "damage_min"),
                            chance_to_heal = DB.get_data_monster("Skeleton", "chance_to_heal"),
                            min_heal_point = DB.get_data_monster("Skeleton", "min_heal_point"),
                            max_heal_point = DB.get_data_monster("Skeleton", "max_heal_point"))
        self.assertEqual(skeleton.hp_total, 100, " hp_total stats dont match")
        self.assertEqual(skeleton.hp, 100, "hp stats dont match")
        self.assertEqual(skeleton.attack_speed, 3, "attack_speed stats dont match")
        self.assertEqual(skeleton.hit_chance, 0.8, "hit_chance stats dont match")
        self.assertEqual(skeleton.damage_min, 30, "damage_min stats dont match")
        self.assertEqual(skeleton.damage_max, 50, "damage_max stats dont match")
        self.assertEqual(skeleton.chance_to_heal, 0.3, " chance_to_heal stats dont match")
        self.assertEqual(skeleton.min_heal_point, 30, "min_heal_point stats dont match")
        self.assertEqual(skeleton.max_heal_point, 50, "max_heal_point stats dont match")

    def test_if_skeleton_is_subclass_of_monster(self):
        skel = Skeleton("name", "model", hp_total = DB.get_data_monster("Skeleton", "hp"),
                            attack_speed = DB.get_data_monster("Skeleton", "attack_speed"),
                            hit_chance = DB.get_data_monster("Skeleton", "hit_chance"),
                            damage_max = DB.get_data_monster("Skeleton", "damage_max"),
                            damage_min = DB.get_data_monster("Skeleton", "damage_min"),
                            chance_to_heal = DB.get_data_monster("Skeleton", "chance_to_heal"),
                            min_heal_point = DB.get_data_monster("Skeleton", "min_heal_point"),
                            max_heal_point = DB.get_data_monster("Skeleton", "max_heal_point"))
        self.assertEqual(True, issubclass(type(skel), Monster))



if __name__ == '__main__':
    unittest.main()

