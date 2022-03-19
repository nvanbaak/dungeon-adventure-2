import unittest
from hero_factory import HeroFactory

class MyTestCase(unittest.TestCase):
    def test_create_warrior(self):
        player = HeroFactory.create_warrior("warrior", "model")
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

    def test_create_priestess(self):
        player = HeroFactory.create_priestess("priestess","model")
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

    def test_create_thief(self):
        player = HeroFactory.create_thief("thief", "model")
        self.assertEqual(75, player.hp_total)
        self.assertEqual(75, player.hp)
        self.assertEqual(6, player.attack_speed)
        self.assertEqual(0.8, player.hit_chance)
        self.assertEqual(20, player.damage_min)
        self.assertEqual(40, player.damage_max)
        self.assertEqual(0.4, player.chance_to_block)
        self.assertEqual(0.4, player.extra_attack_chance)
        self.assertEqual(0.2, player.caught_chance)


if __name__ == '__main__':
    unittest.main()
