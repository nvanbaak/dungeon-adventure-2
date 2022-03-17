import unittest
from monster_factory import MonsterFactory


class MyTestCase(unittest.TestCase):
    def test_create_ogre(self):
        ogre = MonsterFactory.create_ogre("Ogre","model")
        self.assertEqual(ogre.hp_total, 200, " hp_total stats dont match")
        self.assertEqual(ogre.hp, 200, "hp stats dont match")
        self.assertEqual(ogre.attack_speed, 2, "attack_speed stats dont match")
        self.assertEqual(ogre.hit_chance, 0.6, "hit_chance stats dont match")
        self.assertEqual(ogre.damage_min, 30, "damage_min stats dont match")
        self.assertEqual(ogre.damage_max, 60, "damage_max stats dont match")
        self.assertEqual(ogre.chance_to_heal, 0.1, " chance_to_heal stats dont match")
        self.assertEqual(ogre.min_heal_point, 30, "ogre.min_heal_point stats dont match")
        self.assertEqual(ogre.max_heal_point, 60, "max_heal_point stats dont match")


    def test_create_gremlin(self):
        gremlin = MonsterFactory.create_gremlin("gremlin", "model")
        self.assertEqual(gremlin.hp_total, 70, " hp_total stats dont match")
        self.assertEqual(gremlin.hp, 70, "hp stats dont match")
        self.assertEqual(gremlin.attack_speed, 5, "attack_speed stats dont match")
        self.assertEqual(gremlin.hit_chance, 0.8, "hit_chance stats dont match")
        self.assertEqual(gremlin.damage_min, 15, "damage_min stats dont match")
        self.assertEqual(gremlin.damage_max, 30, "damage_max stats dont match")
        self.assertEqual(gremlin.chance_to_heal, 0.4, " chance_to_heal stats dont match")
        self.assertEqual(gremlin.min_heal_point, 20, "min_heal_point stats dont match")
        self.assertEqual(gremlin.max_heal_point, 40, "max_heal_point stats dont match")

    def test_create_skeleton(self):
        skeleton = MonsterFactory.create_skeleton("skeleton", "model")
        self.assertEqual(skeleton.hp_total, 100, " hp_total stats dont match")
        self.assertEqual(skeleton.hp, 100, "hp stats dont match")
        self.assertEqual(skeleton.attack_speed, 3, "attack_speed stats dont match")
        self.assertEqual(skeleton.hit_chance, 0.8, "hit_chance stats dont match")
        self.assertEqual(skeleton.damage_min, 30, "damage_min stats dont match")
        self.assertEqual(skeleton.damage_max, 50, "damage_max stats dont match")
        self.assertEqual(skeleton.chance_to_heal, 0.3, " chance_to_heal stats dont match")
        self.assertEqual(skeleton.min_heal_point, 30, "min_heal_point stats dont match")
        self.assertEqual(skeleton.max_heal_point, 50, "max_heal_point stats dont match")


if __name__ == '__main__':
    unittest.main()
