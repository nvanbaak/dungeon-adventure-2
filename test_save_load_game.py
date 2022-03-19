import unittest
from model import Model
from save_load_game import SaveGame


class MyTestCase(unittest.TestCase):
    def test_saved_load_game(self):
        m = Model()
        m.player.hp = 10
        sg = SaveGame()
        sg.delete_all_saved_games()
        sg.save_game(sg.game_name_generator(), m)
        m1 = sg.load_game("Game1")
        self.assertEqual(m1.player.hp, 10)
        sg.delete_single_game("Game1")

    def test_saved_duplicate_save(self):
        m = Model()
        m.player.hp = 10
        sg = SaveGame()
        sg.delete_all_saved_games()
        sg.save_game(sg.game_name_generator(), m)
        m1 = sg.load_game("Game1")
        self.assertEqual(m1.player.hp, 10)
        exception_raised = False
        m2 = Model()
        try:
            sg.save_game("Game1", m2)

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)
        sg.delete_single_game("Game1")

    def test_delete_saved_game(self):
        m = Model()
        m.player.hp = 10
        sg = SaveGame()
        sg.delete_all_saved_games()
        sg.save_game(sg.game_name_generator(), m)
        m1 = sg.load_game("Game1")
        self.assertEqual(m1.player.hp, 10)
        sg.delete_single_game("Game1")

        exception_raised = False

        try:
            m = sg.load_game("Game1")

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)









