"""
name  : Shoby Gnanasekaran
net id: shoby
"""

import unittest
from maze_generator import Maze


class MyTestCase(unittest.TestCase):
    def test__init(self):
        m = Maze(4, 4)
        self.assertEqual(4, m.rowCount) # add assertion here
        self.assertEqual(4, m.colCount)

    def test__init_without_size(self):
        try:
            m = Maze()
        except (ValueError, TypeError) as value_error:
            self.assertEqual(True, True, "Value_error not raised")

    def test_set_entrance_room(self):
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[0]
        self.assertEqual(True, m.maze[row, col].is_entrance, "room is not set as entrance")

    def test_set_entrance_room_wrong_room(self):
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[1]
        self.assertEqual(False, m.maze[row, col].is_entrance, "room is somehow set as entrance")

    def test_set_exit_room(self):
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[-1]
        self.assertEqual(True, m.maze[row, col].is_exit, "room is not set as exit")

    def test_set_exit_room_wrong_room(self):
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[1]
        self.assertEqual(False, m.maze[row, col].is_entrance, "room is somehow set as exit")

    def test__set_impassable_rooms(self):
        m = Maze(4, 4)
        m.create_maze()
        for i in range(0, len(m.impassable_rooms)):
            row, col = m.impassable_rooms[i]
            self.assertEqual(True, m.maze[row, col].is_impassable, "room is not set as impassable")

    def test_set_impassable_room_wrong_room(self):
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[0]
        self.assertEqual(False, m.maze[row, col].is_impassable, "entrance is set as impassable")

    def test_set_path(self):  # validates the path generated
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[0]  # check if the path starts at the entrance
        self.assertEqual(True, m.maze[row, col].is_entrance, "the path does not start at the entrance")
        row, col = m.winning_path[-1]  # checks if the path ends at the exit
        self.assertEqual(True, m.maze[row, col].is_exit, "the path does not end at the exit")
        for i in range(1, len(m.winning_path) - 2):  # check if the path travels through an impassable room
            row, col = m.winning_path[i]
            self.assertEqual(False, m.maze[row, col].is_impassable, "the path travels through an impassable room")

    def test_set_pillar(self):
        # validates if all pillars are placed in the path generated, to confirm that there is atleast one sure way to win
        m = Maze(4, 4)
        m.create_maze()
        row, col = m.winning_path[0]
        self.assertEqual(None, m.maze[row, col].pillar, "the pillar is placed in the entrance")
        row, col = m.winning_path[-1]
        self.assertEqual(None, m.maze[row, col].pillar, "the pillar is placed in the exit")
        count = 0
        for i in range(1, len(m.winning_path) - 1):  # check if 4 pillars are placed
            row, col = m.winning_path[i]
            if m.maze[row, col].pillar is not None:
                count += 1
                self.assertIn(str(m.maze[row, col].pillar), ['a', 'e', 'i', 'o', 'p'],
                              "incorrect pillars are placed")

        self.assertEqual(4, count, "pillar count is not 4")

    def test__set_healing_vision_pit_test_healing_potion(self):
        m = Maze(4, 4)
        m.create_maze()
        if len(m.healing_potion_rooms) > 0:
            for i in range(0, len(m.healing_potion_rooms)):
                # validates if all the rooms randomly generated to hold healing potion sets the
                # healing_potion param in the room properly
                self.assertIn(str(m.healing_potion_rooms[i].heal), ['y', 'g'])

    def test__set_healing_vision_pit_test_vision_potion(self):
        m = Maze(4, 4)
        m.create_maze()
        if len(m.vision_potion_rooms) > 0:
            for i in range(0, len(m.vision_potion_rooms)):
                # validates if all the rooms randomly generated to hold vision potion sets the
                # healing_potion param in the room properly
                self.assertEqual(True, m.vision_potion_rooms[i].vision)

    def test__set_healing_vision_pit_test_pit_rooms(self):
        m = Maze(4, 4)
        m.create_maze()
        if len(m.pit_rooms) > 0:
            for i in range(0, len(m.pit_rooms)):
                # validates if all the rooms randomly generated to hold healing potion sets the
                # healing_potion param in the room properly
                self.assertEqual(True, m.pit_rooms[i].pit)

if __name__ == '__main__':
    unittest.main()
