from dungeon_builder import DungeonBuilder
from hero_factory import HeroFactory
from sprite import Sprite
from configurations import *

class Model:

    """
    Model class instantiates a Dungeon object, which holds most of the game's underlying logic. It contains game
    navigation methods that Controller can access and pass along the results to View for display.
    """

    def __init__(self, hero_class = "warrior", name="Player"):
        """
        Model's __init__() instantiates a Dungeon via DungeonBuilder.
        Dungeon size and difficulty level can also be specified here via DungeonBuilder.
        The dungeon's first room is entered and the location is saved such that it can be displayed.
        The hero type is specified as a parameter, which is to be chosen by the user.
        Two dictionaries to document the grid location of the hero and sprites respectively are also instantiated.
        Finally, Monster objects are created and placed in the rooms where they were identified at dungeon creation.

        :param hero:
        """
        self.hero = hero_class
        self.player_name = name
        self.game = DungeonBuilder.build_single_dungeon()
        self.dungeon = self.game[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        if hero_class == "warrior":
            self.player = HeroFactory.create_warrior(name, self)
        elif hero_class == "priestess":
            self.player = HeroFactory.create_priestess(name, self)
        else:
            self.player = HeroFactory.create_thief(name, self)

        self.pillars = {"A": "", "E": "", "P": "", "I": ""}
        self.game_stats = {"Hit Points": 0, "Pillars": "", "Healing Potions": 0, "Vision Potions": 0}
        self.dungeon.update_monsters_to_room(self)

    def get_game_stats(self):
        return self.game_stats

    def player_has_all_pillars(self):
        """
        Returns True if the player has picked up all of
        the pillars; False otherwise
        """
        for pillar in self.pillars:
            if not self.pillars[pillar]:
                return False
        return True

    def player_is_dead(self):
        """
        returns True if hp is <= 0, False otherwise
        """
        return self.player.hp <= 0

    def announce(self, message):
        print(message)

    def get_curr_pos(self):
        return self.curr_pos

    def move_left(self):
        """
        Moves the pointer for the current room to the left if a door exists.
        :returns: True if door exists, False otherwise.
        """
        if self.curr_pos.door_value["Left"]:
            self.curr_pos = self.curr_pos.left_room
            return True
        else:
            return False

    def move_right(self):
        """
        Moves the pointer for the current room to the right if a door exists.
        :returns: True if door exists, False otherwise.
        """
        if self.curr_pos.door_value["Right"]:
            self.curr_pos = self.curr_pos.right_room
            return True
        else:
            return False

    def move_up(self):
        """
        Moves the pointer for the current room to the north if a door exists.
        :returns: True if door exists, False otherwise.
        """
        if self.curr_pos.door_value["Up"]:
            self.curr_pos = self.curr_pos.upper_room
            return True
        else:
            return False

    def move_down(self):
        """
        Moves the pointer for the current room to the down if a door exists.
        :returns: True if door exists, False otherwise.
        """
        if self.curr_pos.door_value["Down"]:
            self.curr_pos = self.curr_pos.down_room
            return True
        else:
            return False

    def get_current_room_contents(self):
        """
        Returns a list of all items in the room the player is in
        """
        current_room = self.curr_pos
        return current_room.list_room_contents()

    def pre_move_validation(self, initial_pos, final_pos):
        self.move(initial_pos, final_pos)

    def move(self, start_pos, final_pos):
        self.hero_dict[final_pos] = self.hero_dict.pop(start_pos, None)