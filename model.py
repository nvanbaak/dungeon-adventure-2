"""
"""
from copy import deepcopy
import exceptions
import piece
from dungeon import Dungeon
from dungeon_builder import DungeonBuilder
from dungeonchar import DungeonCharacter
from test_hero import MockHero
from configurations import *


class Model():

    # print("M | class variables initialized before __init__")
    dict = {}

    def __init__(self):
        d_list = DungeonBuilder.build_easy_dungeon()
        self.dungeon = d_list[0]
        self.dungeon.enter_dungeon()
        self.reset_default_characters()
        self.player = MockHero("Test", self)

    def reset_game_data(self):
        # print("M | reset_game_data() | resets Model's class variables")
        pass

    def reset_default_characters(self):
        self.dict.clear()
        # print("M | loops through START_PIECES_POSITION dict (model has access via import config.py)")
        # print("M | creates Piece objects based on value in S_P_P, then keeps reference. stores in self.dict[position]")
        for position, value in START_PIECES_POSITION.items():
            self.dict[position] = piece.create_piece(value, True)
            self.dict[position].keep_reference(self)
        # print(f"M | Model dictionary after iterating S_P_P: {self.dict.items()}")

    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])

    def is_on_board(self, rowcol):
        row, col = rowcol
        return 0 <= row <= 6 and 0 <= col <= 6

    def pre_move_validation(self, initial_pos, final_pos):
        self.move(initial_pos, final_pos)

    def move(self, start_pos, final_pos):
        # print(f"M | move(start, final) | self[{final_pos}] = self.dict.pop({start_pos}, None)")
        self.dict[final_pos] = self.dict.pop(start_pos, None)
