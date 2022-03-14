from dungeon_builder import DungeonBuilder
from hero import Hero
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton
import sprite
from configurations import *
from time import *
import time
# from game_observer import Publisher, Subscriber

class Model:

    # print("M | class variables initialized before __init__")
    dict = {}
    hero_dict = {}

    def __init__(self, hero = "warrior"):
        self.game = DungeonBuilder.build_single_dungeon()
        self.dungeon = self.game[0]
        self.curr_pos = self.dungeon.enter_dungeon()
        if hero == "warrior":
            self.player = Warrior("TestWarrior", self)
        elif hero == "priestess":
            self.player = Priestess("TestPriestess", self)
        else:
            self.player = Thief("TestThief", self)
        print(self.dungeon.dungeon.winning_path)
        print(self.dungeon)
        # self.subscriber_m = Subscriber(self)
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
        self.dict.clear()
        self.hero_dict.clear()
        for position, value in START_SPRITES_POSITION.items():
            self.dict[position] = sprite.create_sprite(value)
            self.dict[position].keep_reference(self)
        self.hero_dict[HERO_POSITION] = sprite.create_sprite(HERO_SPRITE)
        # print(f"M | {self.dict}")
        # print(f"M | {self.hero_dict}")
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


    # def combat_with_time(self):
    #     ##
    #
    #     while self.player._is_alive and self.curr_pos.monster_obj._is_alive:
    #         # print("i am here")
    #         combat_time = max(self.player.attack_speed, self.curr_pos.monster_obj.attack_speed)
    #         t_hero_now = time.time()
    #         t_mons_now = time.time()
    #         t_end = time.time() + (1.5 * combat_time)
    #         # adding 2sec so that the character with high attach speed gets to complete all attacks for the round even with sleep
    #         while time.time() < t_end:
    #             monster_attack_time = combat_time / self.curr_pos.monster_obj.attack_speed
    #             hero_attack_time = combat_time / self.player.attack_speed
    #             if time.time() >= t_mons_now + monster_attack_time:
    #                 print("monster is attacking")
    #                 self.curr_pos.monster_obj.attack_target(self.player)
    #                 if not self.player._is_alive:
    #                     break
    #                 print(f"hero hp:{self.player.hp}")
    #                 sleep(1)  # to multi thread
    #                 t_mons_now = time.time()
    #
    #             if time.time() >= t_hero_now + hero_attack_time and self.player.attack_now:
    #                 print("hero is attacking")
    #                 self.player.attack_target(self.curr_pos.monster_obj)
    #                 if not self.curr_pos.monster_obj._is_alive:
    #                     self.curr_pos.monster = ""
    #                     break
    #                 # print(f"monster hp:{monster.hp}")
    #                 self.player.attack_now = False
    #                 t_hero_now = time.time()
