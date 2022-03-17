
from dungeon import Dungeon

class DungeonBuilder:

    @staticmethod
    def build_single_dungeon():
        """build a single dungeon"""
        dun0 = Dungeon(4,6)
        result=[dun0]
        DungeonBuilder.__update_floor_details(result)
        return result

    @staticmethod
    def build_easy_dungeon():
        dun0 = Dungeon(6,6)
        exit_value = dun0.dungeon.winning_path[-1]
        entrance_row,entrance_col = exit_value[0], exit_value[1]
        dun1 = Dungeon(6,6, entrance = True, entrance_row_value = entrance_row, entrance_col_value = entrance_col)
        result = [dun0, dun1]
        # result = DungeonBuilder.__distribute_entrance_exit(result)
        result = DungeonBuilder.__distribute_pillars(result)
        DungeonBuilder.__build_stairs(result)
        DungeonBuilder.__update_floor_details(result)
        return result

    @staticmethod
    def __distribute_pillars(array):
        pillar_positions = array[0].dungeon.pillar_position
        for i in range(len(pillar_positions)):
            row, col = pillar_positions[i][0], pillar_positions[i][1]
            if array[0].dungeon.maze[row, col].pillar == 'a' or array[0].dungeon.maze[row, col].pillar == 'e':
                array[0].dungeon.maze[row, col].pillar = None
                array[0].dungeon.maze[row, col].monster = None
        pillar_positions = array[1].dungeon.pillar_position
        for i in range(len(pillar_positions)):
            row, col = pillar_positions[i][0], pillar_positions[i][1]
            if array[1].dungeon.maze[row, col].pillar == 'i' or array[1].dungeon.maze[row, col].pillar == 'p':
                array[1].dungeon.maze[row, col].pillar = None
                array[1].dungeon.maze[row, col].monster = None
        return array

    @staticmethod
    def __build_stairs(array):
        winning_path = array[0].dungeon.winning_path
        row, col = winning_path[-1][0], winning_path[-1][1]
        array[0].dungeon.maze[row, col].stairs = array[1].dungeon.maze[row, col]
        array[1].dungeon.maze[row, col].stairs = array[0].dungeon.maze[row, col]

    @staticmethod
    def __update_floor_details(array):
        i = 0
        while i < len(array):
            row_count = array[i].row_Count
            col_count = array[i].col_Count

            for row in range(0, row_count):
                for col in range(0, col_count):
                    array[i].dungeon.maze[row, col].floor = int(i)
            i +=1




# game = DungeonBuilder.build_easy_dungeon()
# print(f"ground_floor path: {game[0].dungeon.winning_path}")
# print(game[0])
# print(f"first_floor path: {game[1].dungeon.winning_path}")
# print(game[1])


