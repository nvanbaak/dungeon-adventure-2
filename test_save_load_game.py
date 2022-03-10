import unittest
from model import Model
from save_load_game import SaveGame


class MyTestCase(unittest.TestCase):

    def test_save_and_load_game(self):
        m = Model()
        m.player.hp = 50
        curr_room_location = m.dungeon.dungeon.winning_path[3]
        curr_room = m.dungeon.dungeon.maze[curr_room_location[0], curr_room_location[1]]
        m.curr_pos = m.dungeon.re_enter_dungeon(curr_room)
        sg = SaveGame()
        sg.save_game("game1", m)
        mod = sg.load_game("game1")
        self.assertEqual(m.player.hp, mod.player.hp)
        self.assertEqual(m.curr_pos, curr_room)
        self.assertEqual(mod.curr_pos.location, m.curr_pos.location)

    def test_save_duplicate_name(self):
        m = Model()
        sg = SaveGame()
        sg.save_game("game1", m)

        exception_raised = False
        m2 = Model()
        try :
            sg.save_game("game1", m2)

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised)

    def test_delete_saved_game(self):
        m = Model()
        sg = SaveGame()
        sg.save_game("game1", m)
        self.assertEqual(sg.check_in_saved_games("game1"), True)
        sg.delete_saved_game("game1")
        self.assertEqual(sg.check_in_saved_games("game1"), False)

    def test_saved_games(self):
        m1 = Model()
        sg = SaveGame()
        sg.save_game("game1", m1)
        m2 = Model()
        sg.save_game("game2", m2)

        self.assertEqual(sg.saved_games, ["game1","game2"])
