# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from gremlin import Gremlin
from monster import Monster
from dungeonchar_db_access import DungeonCharDb

DB = DungeonCharDb()
class MyTestCase(unittest.TestCase):
    def test_gremlin_init(self):
        gremlin = Gremlin("gremlin", "model", hp_total = DB.get_data_monster("Gremlin", "hp"),
                         attack_speed = DB.get_data_monster("Gremlin", "attack_speed"),
                         hit_chance = DB.get_data_monster("Gremlin", "hit_chance"),
                         damage_max = DB.get_data_monster("Gremlin", "damage_max"),
                         damage_min = DB.get_data_monster("Gremlin", "damage_min"),
                         chance_to_heal = DB.get_data_monster("Gremlin", "chance_to_heal"),
                         min_heal_point = DB.get_data_monster("Gremlin", "min_heal_point"),
                         max_heal_point = DB.get_data_monster("Gremlin", "max_heal_point") )
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
        gremlin = Gremlin("name", "model", hp_total = DB.get_data_monster("Gremlin", "hp"),
                         attack_speed = DB.get_data_monster("Gremlin", "attack_speed"),
                         hit_chance = DB.get_data_monster("Gremlin", "hit_chance"),
                         damage_max = DB.get_data_monster("Gremlin", "damage_max"),
                         damage_min = DB.get_data_monster("Gremlin", "damage_min"),
                         chance_to_heal = DB.get_data_monster("Gremlin", "chance_to_heal"),
                         min_heal_point = DB.get_data_monster("Gremlin", "min_heal_point"),
                         max_heal_point = DB.get_data_monster("Gremlin", "max_heal_point"))
        self.assertEqual(True, issubclass(type(gremlin), Monster))


if __name__ == '__main__':
    unittest.main()
