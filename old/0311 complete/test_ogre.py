# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from ogre import Ogre
from monster import Monster

class MyTestCase(unittest.TestCase):
    def test_ogre_init(self):
        ogre = Ogre("ogre", "model")
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
        ogre = Ogre("name", "model")
        self.assertEqual(True, issubclass(type(ogre), Monster))


if __name__ == '__main__':
    unittest.main()
