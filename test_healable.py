# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from dungeonchar import DungeonCharacter
from healable import Healable

class MockMonster(DungeonCharacter, Healable):
    """mock hero class to check the save and load of hero objects """

    def __init__(self, name, model):
        super().__init__(name= name, model= model, hp_total = 100, attack_speed = 1, hit_chance = 0.5,
                         damage_max= 30, damage_min= 20, chance_to_block = 0.0)
        super(DungeonCharacter, self).__init__(chance_to_heal =0,min_heal_point = 0,
                         max_heal_point = 1)

    def attack_target(self, target):
        pass

    def combat(self, target):
        pass

    def take_damage(self, dmg, source):
        pass

    def use_health_potion(self):
        pass

    def use_vision_potion(self):
        pass


class MockHealable(Healable):
    def __init__(self):
        super().__init__(args= (0.0,0,0))

    def hp(self, value):
        pass

    def hp_total(self):
        pass



class MyTestCase(unittest.TestCase):

    def test_heal_itself(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0 # setting chance_to_heal as 1
        mock_monster.min_heal_point = 15
        mock_monster.max_heal_point = 30
        mock_monster.hp -= 60
        mock_monster_hp = mock_monster.hp
        mock_monster.heal_itself()
        self.assertGreater(mock_monster.hp, mock_monster_hp) # validate if the mock monster has healed

    def test_heal_itself_with_full_hp(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 0.1
        heal_message = mock_monster.heal_itself()
        self.assertEqual(mock_monster.hp, mock_monster.hp_total)

    def test__set_min_heal_point(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0
        mock_monster.min_heal_point = 15
        self.assertEqual(mock_monster.min_heal_point, 15)

    def test_set_min_heal_point_greater_than_hp(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0
        exception_raised = False
        try:
            mock_monster.min_heal_point = mock_monster.hp + 10
        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)

    def test__set_max_heal_point(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0
        mock_monster.max_heal_point = 30
        self.assertEqual(mock_monster.max_heal_point, 30)

    def test__set_max_heal_point_less_than_min_heal_point(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0
        mock_monster.min_heal_point = 15
        exception_raised = False
        try:
            mock_monster.max_heal_point = 10

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)

    def test_set_max_heal_point_greater_than_hp(self):
        mock_monster = MockMonster("monster1", "model")
        mock_monster.chance_to_heal = 1.0
        exception_raised = False
        try:
            mock_monster.max_heal_point = mock_monster.hp + 10
        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)


    def test_inherit_only_healable(self):
        exception_raised = False

        try:
            mock = MockHealable()
            mock.heal_itself()

        except TypeError:
            exception_raised = True

        self.assertEqual(True, exception_raised)





if __name__ == '__main__':
    unittest.main()
