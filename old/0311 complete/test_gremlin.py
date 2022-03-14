# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from gremlin import Gremlin
from monster import Monster

class MyTestCase(unittest.TestCase):
    def test_ogre_init(self):
        gremlin = Gremlin("gremlin", "model")
        self.assertEqual(gremlin.hp_total, 70, " hp_total stats dont match")
        self.assertEqual(gremlin.hp, 70, "hp stats dont match")
        self.assertEqual(gremlin.attack_speed, 5, "attack_speed stats dont match")
        self.assertEqual(gremlin.hit_chance, 0.8, "hit_chance stats dont match")
        self.assertEqual(gremlin.damage_min, 15, "damage_min stats dont match")
        self.assertEqual(gremlin.damage_max, 30, "damage_max stats dont match")
        self.assertEqual(gremlin.chance_to_heal, 0.4, " chance_to_heal stats dont match")
        self.assertEqual(gremlin.min_heal_point, 20, "min_heal_point stats dont match")
        self.assertEqual(gremlin.max_heal_point, 40, "max_heal_point stats dont match")

    def test_if_ogre_is_subclass_of_monster(self):
        gremlin = Gremlin("name", "model")
        self.assertEqual(True, issubclass(type(gremlin), Monster))


if __name__ == '__main__':
    unittest.main()
