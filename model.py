from dungeon_builder import DungeonBuilder
from test_hero import MockHero
import sprite
from configurations import *
# from game_observer import Publisher, Subscriber

class Model():

    # print("M | class variables initialized before __init__")
    dict = {}
    hero_dict = {}
    pillars = {"A": "", "E": "", "P": "", "I": ""}
    game_stats = {"Hit Points": 0, "Pillars": "", "Healing Potions": 0, "Vision Potions": 0}

    def __init__(self):
        d_list = DungeonBuilder.build_single_dungeon()
        self.dungeon = d_list[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        self.player = MockHero("Test", self)
        print(self.dungeon.dungeon.winning_path)
        # self.subscriber_m = Subscriber(self)

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
        self.hero_dict.clear()
        for position, value in START_SPRITES_POSITION.items():
            self.dict[position] = sprite.create_sprite(value)
            self.dict[position].keep_reference(self)
        self.hero_dict[HERO_POSITION] = sprite.create_sprite(HERO_SPRITE)

        # print(f"M | {self.dict}")
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