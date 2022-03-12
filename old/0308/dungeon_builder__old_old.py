
from dungeon import Dungeon
import copy
import numpy as np

class DungeonBuilder:
    @staticmethod
    def build_easy_dungeon():
        dun = Dungeon(4,4)
        result = [copy.deepcopy(dun),copy.deepcopy(dun)]
        result = DungeonBuilder.__distribute_entrance_exit(result)
        result = DungeonBuilder.__distribute_pillars(result)
        DungeonBuilder.__build_stairs(result)
        return result

    @staticmethod
    def __distribute_entrance_exit(array):
        winning_path = array[0].dungeon.winning_path
        print(winning_path)
        row, col = winning_path[-1][0], winning_path[-1][1]
        array[0].dungeon.maze[row, col].is_exit = False
        row, col = winning_path[0][0], winning_path[0][1]
        array[1].dungeon.maze[row, col].is_entrance = False
        return  array

    @staticmethod
    def __distribute_pillars(array):
        pillar_positions = array[0].dungeon.pillar_position
        for i in range(len(pillar_positions)):
            if i == 0 or i ==1:
                row, col = pillar_positions[i][0], pillar_positions[i][1]
                array[1].dungeon.maze[row, col].pillar = None
                array[1].dungeon.maze[row, col].monster = None
            if i ==2 or i ==3:
                row, col = row, col = pillar_positions[i][0], pillar_positions[i][1]
                array[0].dungeon.maze[row, col].pillar = None
                array[0].dungeon.maze[row, col].monster = None
        return array

    @staticmethod
    def __build_stairs(array):
        pillar_positions = array[0].dungeon.pillar_position
        row, col = pillar_positions[1][0], pillar_positions[1][1]
        array[0].dungeon.maze[row, col].stairs = array[1].dungeon.maze[row, col]
        array[1].dungeon.maze[row, col].stairs = array[0].dungeon.maze[row, col]


# game = DungeonBuilder.build_easy_dungeon()
# print(game[0])
