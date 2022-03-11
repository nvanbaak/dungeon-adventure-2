# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from skeleton import Skeleton
from monster import Monster

class MyTestCase(unittest.TestCase):
    def test_ogre_init(self):
        skeleton = Skeleton("skeleton", "model")
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
        skel = Skeleton("name", "model")
        self.assertEqual(True, issubclass(type(skel), Monster))



if __name__ == '__main__':
    unittest.main()

