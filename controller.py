import model
import sprite
from playsound import playsound
import pygame
# from game_observer import Publisher, Subscriber
from dungeonchar import DungeonCharacter
from healable import Healable
from hero import Hero
from monster import Monster

class Controller:

    def __init__(self):
        # print("C | __init__ | Controller init calls init of Model")
        self.model = model.Model()
        # self.pub = Publisher()
        # self.view = ""
        pygame.init()

    # def setup_observer(self):
    #     self.pub.register(self.view.subscriber_v)

    def accept_view_reference(self, view_ref):
        self.view = view_ref
        print(" ")

    def get_room_data(self):
        return self.model.get_curr_pos()

    def move_left(self):
        return self.model.move_left()

    def move_right(self):
        return self.model.move_right()

    def move_upper(self):
        return self.model.move_up()

    def move_down(self):
        return self.model.move_down()

    def refresh_room(self):
        return self.model.refresh_room()

    def reset_default_characters(self):
        # print("C | calls model.reset_default_characters() via Controller")
        self.model.reset_default_characters()

    def get_all_peices_on_board(self):
        return self.model.dict.items()

    def get_hero_dict(self):
        return self.model.hero_dict.items()

    def get_alphanumeric_position(self, rowcolumntuple):
        # print(f"C | calls get_alphanumeric_position({rowcolumntuple}) via Model")
        return self.model.get_alphanumeric_position(rowcolumntuple)

    def get_numeric_notation(self, rowcol):
        # print("C | calls get_numeric_notation via Sprite()")
        return sprite.get_numeric_notation(rowcol)

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)

    def get_dict(self):
        return self.model.get_dict()

    def get_hero(self):
        return self.model.get_hero_dict()

    # def dispatch(self):
    #     self.pub.dispatch("Check hp")

    def gather(self):
        curr_pos = self.model.get_curr_pos()
        # self.dispatch()
        if curr_pos.heal == "y":
            self.model.player.health_potions += 1
            self.model.game_stats["Healing Potions"] = self.model.player.health_potions
        if curr_pos.heal == "g":
            self.model.player.health_potions += 1
            self.model.game_stats["Healing Potions"] = self.model.player.health_potions
        if curr_pos.vision == True:
            self.model.player.vision_potions += 1
            self.model.game_stats["Vision Potions"] = self.model.player.vision_potions
            self.view.vision = True
            self.view.vision_button.pack()
        if curr_pos.pit == True:
            pass
        if curr_pos.pillar == "a":
            self.model.pillars["A"] = True
            self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "A "
        if curr_pos.pillar == "e":
            self.model.pillars["E"] = True
            self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "E "
        if curr_pos.pillar == "p":
            self.model.pillars["P"] = True
            self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "P "
        if curr_pos.pillar == "i":
            self.model.pillars["I"] = True
            self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "I "
        self.model.game_stats["Hit Points"] = self.model.player.hp

    def gather_sounds(self):
        curr_pos = self.model.get_curr_pos()
        if curr_pos.heal == "y":
            self.play("magic_harp")
        if curr_pos.heal == "g":
            self.play("magic_harp")
        if curr_pos.vision == True:
            self.play("magic_harp")
        if curr_pos.pillar == "a":
            self.play("pillar")
        if curr_pos.pillar == "e":
            self.play("pillar")
        if curr_pos.pillar == "p":
            self.play("pillar")
        if curr_pos.pillar == "i":
            self.play("pillar")
        if curr_pos.monster == "Gremlin" or curr_pos.monster == "Ogre" or curr_pos.monster == "Skeleton":
            self.play("monster")
            self.combat()
        if curr_pos.pit == True:
            self.play("welcome_pit")
        if self.model.player.hp <= 0:
            self.play("game_over")
            self.view.ask_new_game()

    def combat(self):
        curr_pos = self.model.get_curr_pos()
        if curr_pos.monster == "Gremlin" or curr_pos.monster == "Ogre" or curr_pos.monster == "Skeleton":
            print(f"Pre-battle hit points: {self.model.player.hp}")
            monster = Monster(curr_pos.monster, self.model)
            monster.attack_target(self.model.player)
            self.model.player.combat(monster)
            print(f"Post-battle hit points: Player: {self.model.player.hp} | Monster: {monster.hp}")

        # curr_pos = self.model.get_curr_pos()
        # if curr_pos.monster == "Gremlin":
        #     print(f"Pre-battle hit points: Player: {self.model.player.hp} | Gremlin: {self.model.gremlin.hp}")
        #     self.model.gremlin.attack_target(self.model.player)
        #     self.model.player.combat(self.model.gremlin)
        #     print(f"Post-battle hit points: Player: {self.model.player.hp} | Gremlin: {self.model.gremlin.hp}")
        # if curr_pos.monster == "Ogre":
        #     print(f"Pre-battle hit points: Player: {self.model.player.hp} | Gremlin: {self.model.ogre.hp}")
        #     self.model.ogre.attack_target(self.model.player)
        #     self.model.player.combat(self.model.ogre)
        #     print(f"Post-battle hit points: Player: {self.model.player.hp} | Ogre: {self.model.ogre.hp}")
        # if curr_pos.monster == "Skeleton":
        #     print(f"Pre-battle hit points: Player: {self.model.player.hp} | Skeleton: {self.model.skeleton.hp}")
        #     self.model.skeleton.attack_target(self.model.player)
        #     self.model.player.combat(self.model.skeleton)
        #     print(f"Post-battle hit points: Player: {self.model.player.hp} | Skeleton: {self.model.skeleton.hp}")


    def play(self, file):
        filename = "audio/{}.wav".format(
            file)
        sound = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()

    def load_hit_points(self):
        self.model.game_stats["Hit Points"] = self.model.player.hp

    def expunge(self):
        curr_pos = self.model.get_curr_pos()
        if curr_pos.heal == "y":
            curr_pos.heal = None
        if curr_pos.heal == "g":
            curr_pos.heal = None
        if curr_pos.vision == True:
            curr_pos.vision = False
        if curr_pos.pillar == "a":
            curr_pos.pillar = None
        if curr_pos.pillar == "e":
            curr_pos.pillar = None
        if curr_pos.pillar == "p":
            curr_pos.pillar = None
        if curr_pos.pillar == "i":
            curr_pos.pillar = None

    def get_game_stats (self):
        return self.model.game_stats

    def use_vision_potion(self, room):
        self.model.player.use_vision_potion()
        str_vision = self.model.dungeon.use_vision_potion(room)
        print(str_vision)
        return self.model.dungeon.vision_potion_rooms(room)

    def get_model(self):
        return self.model