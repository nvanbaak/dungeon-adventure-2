from dungeon_builder import DungeonBuilder
from hero_factory import HeroFactory
from sprite import Sprite
from configurations import *

class Model:

    """
    Model class instantiates a Dungeon object, which holds most of the game's underlying logic. It contains game
    navigation methods that Controller can access and pass along the results to View for display.
    """

    def __init__(self, hero = "warrior", name="Player"):
        """
        Model's __init__() instantiates a Dungeon via DungeonBuilder.
        Dungeon size and difficulty level can also be specified here via DungeonBuilder.
        The dungeon's first room is entered and the location is saved such that it can be displayed.
        The hero type is specified as a parameter, which is to be chosen by the user.
        Two dictionaries to document the grid location of the hero and sprites respectively are also instantiated.
        Finally, Monster objects are created and placed in the rooms where they were identified at dungeon creation.

        :param hero:
        """
        self.hero = hero
        self.game = DungeonBuilder.build_single_dungeon()
        self.dungeon = self.game[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        if hero == "warrior":
            self.player = HeroFactory.create_warrior(name, self)
        elif hero == "priestess":
            self.player = HeroFactory.create_priestess(name, self)
        else:
            self.player = HeroFactory.create_thief(name, self)

        self.pillars = {"A": "", "E": "", "P": "", "I": ""}
        self.game_stats = {"Hit Points": 0, "Pillars": "", "Healing Potions": 0, "Vision Potions": 0}
        self.dungeon.update_monsters_to_room(self)

    def announce(self, message):
        print(message)

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

    def get_current_room_contents(self):
        """
        Returns a list of all items in the room the player is in
        """
        room_contents = self.curr_pos.room_contents

        output_list = []

        for game_object, contents in room_contents.items():
            if contents:
                output_list.append(contents)

        return output_list

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
        self.hero_dict[final_pos] = self.hero_dict.pop(start_pos, None)