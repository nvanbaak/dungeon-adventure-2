from dungeon_builder import DungeonBuilder
from hero_factory import HeroFactory
import sprite
from configurations import *
# from game_observer import Publisher, Subscriber

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
        self.game = DungeonBuilder.build_single_dungeon()
        self.dungeon = self.game[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        if hero == "warrior":
            self.player = HeroFactory.create_warrior(name, self)
        elif hero == "priestess":
            self.player = HeroFactory.create_priestess(name, self)
        else:
            self.player = HeroFactory.create_thief(name, self)
        print(self.dungeon.dungeon.winning_path)
        self.dict = {}
        self.hero_dict = {}
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

    def reset_default_characters(self):
        """
        Clears dictionaries storing alphanumeric position of hero sprites and other game sprites.
        Instantiates sprite objects of the type and location specified in configurations.py.
        Refreshes room by checking underlying data and setting relevant sprite objects to "visible".
        """

        # clear dictionaries storing alphanumeric (center = D4) position of hero sprite and other game sprites
        self.dict.clear()
        self.hero_dict.clear()
        # for each sprite at alphanumeric home position specified in configurations.py, instantiate a Sprite object
        #   of the specified subtype and store it in the dictionary, then pass a Model reference to that Sprite object
        for position, value in START_SPRITES_POSITION.items():
            self.dict[position] = sprite.create_sprite(value)
            self.dict[position].keep_reference(self)
        # creates hero Sprite and stores it in a separate dictionary (so that the player can click on the same
        #  alphanumeric space on the board grid without displacing a sprite that is already there)
        self.hero_dict[HERO_POSITION] = sprite.create_sprite(HERO_SPRITE)
        # check underlying model to verify that all sprites are visible that are supposed to be visible
        self.refresh_room()

    def refresh_room(self):
        for position, value in self.dict.items():
            spr = value
            if value.name == "abstraction_pillar" and self.curr_pos.pillar == "a":
                spr.visible = True
            if value.name == "encapsulation_pillar" and self.curr_pos.pillar == "e":
                spr.visible = True
            if value.name == "polymorphism_pillar" and self.curr_pos.pillar == "p":
                spr.visible = True
            if value.name == "inheritance_pillar" and self.curr_pos.pillar == "i":
                spr.visible = True
            if value.name == "pit" and self.curr_pos.pit == True:
                spr.visible = True
            if value.name == "healing_potion_y" and self.curr_pos.heal == "y":
                spr.visible = True
            if value.name == "healing_potion_g" and self.curr_pos.heal == "g":
                spr.visible = True
            if value.name == "vision_potion" and self.curr_pos.vision == True:
                spr.visible = True
            if value.name == "gremlin" and self.curr_pos.monster == "Gremlin":
                spr.visible = True
            if value.name == "skeleton" and self.curr_pos.monster == "Skeleton":
                spr.visible = True
            if value.name == "ogre" and self.curr_pos.monster == "Ogre":
                spr.visible = True

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
        self.hero_dict[final_pos] = self.hero_dict.pop(start_pos, None)

    def get_dict(self):
        return self.dict

    def get_hero_dict(self):
        return self.hero_dict