from dungeon_builder import DungeonBuilder
from test_hero import MockHero
import sprite
from configurations import *

class Model():

    # print("M | class variables initialized before __init__")
    dict = {}

    def __init__(self):
        d_list = DungeonBuilder.build_easy_dungeon()
        self.dungeon = d_list[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        self.player = MockHero("Test", self)

    def get_curr_pos(self):
        return self.curr_pos

    def move_left(self):
        self.curr_pos = self.curr_pos.left_room

    def move_right(self):
        self.curr_pos = self.curr_pos.right_room

    def move_up(self):
        self.curr_pos = self.curr_pos.upper_room

    def move_down(self):
        self.curr_pos = self.curr_pos.down_room

    def reset_default_characters(self):
        self.dict.clear()
        # print("M | loops through START_SPRITES_POSITION dict (model has access via import config.py)")
        # print("M | creates Sprite objects based on value in S_P_P, then keeps reference. stores in self.dict[position]")
        for position, value in START_SPRITES_POSITION.items():
            self.dict[position] = sprite.create_sprite(value)
            self.dict[position].keep_reference(self)
        print(f"M | {self.dict}")
        # pcs_list = list(self.dict.items())
        # print(f"Ml | {pcs_list}")
        # nw_dct = {pcs_list[i]: pcs_list[i + 1] for i in range (0, len(pcs_list), 2)}
        # print(f"Mn | {nw_dct}")
        # self.update_dict(nw_dct)

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

    def update_dict(self, new_dict):
        self.dict = new_dict
        print(f"n | {self.dict}")

    def get_dict(self):
        return self.dict