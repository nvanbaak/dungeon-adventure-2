# name  : Shoby Gnanasekaran
# net id: shoby

import unittest
from dungeon_builder import DungeonBuilder
from dungeon import Dungeon

class MyTestCase(unittest.TestCase):
    def test_build_easy_dungeon(self):
        game = DungeonBuilder.build_easy_dungeon()

        self.assertEqual(True, isinstance(game[0], Dungeon), "not a dungeon")
        self.assertEqual(True, isinstance(game[1], Dungeon), "not a dungeon")

    def test_stairs_of_ground_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        row, col =game[0].dungeon.winning_path[-1][0],game[0].dungeon.winning_path[-1][1]
        self.assertNotEqual(None, game[0].dungeon.maze[row, col].stairs, "no stair links found")

    def test_stairs_of_first_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        row, col = game[1].dungeon.winning_path[0][0], game[1].dungeon.winning_path[0][1]
        self.assertNotEqual(None, game[0].dungeon.maze[row, col].stairs, "no stair links found")

    def test_entrance_in_ground_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        row, col = game[0].dungeon.winning_path[0][0], game[0].dungeon.winning_path[0][1]
        self.assertEqual(True, game[0].dungeon.maze[row, col].is_entrance, "not the entrance room")

    def test_exit_in_first_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        row, col = game[1].dungeon.winning_path[-1][0], game[1].dungeon.winning_path[-1][1]
        self.assertEqual(True, game[1].dungeon.maze[row, col].is_exit, "not the exit room")

    def test_pillars_ground_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        possible_pillar_rooms = game[0].dungeon.pillar_position
        count = 0
        for i in possible_pillar_rooms:
            row, col = i[0], i[1]
            if game[0].dungeon.maze[row, col].pillar == 'i' or game[0].dungeon.maze[row, col].pillar == 'p':
                count +=1

        self.assertEqual(2, count , "pillars are not correctly distributed" )

    def test_pillars_first_floor(self):
        game = DungeonBuilder.build_easy_dungeon()
        possible_pillar_rooms = game[1].dungeon.pillar_position
        count = 0
        for i in possible_pillar_rooms:
            row, col = i[0], i[1]
            if game[1].dungeon.maze[row, col].pillar == 'a' or game[1].dungeon.maze[row, col].pillar == 'e':
                count += 1

        self.assertEqual(2, count, "pillars are not correctly distributed")



if __name__ == '__main__':
    unittest.main()
