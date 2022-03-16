import model
import sprite
import pygame

class Controller:

    """
    Controller class allows the View class to access the underlying game structure within Model such that it knows what
    to display.
    """

    def __init__(self):
        """
        Controller's __init__() instantiates a Model that can then be accessed by View. Also initializes a pygame object
        that will be used to play the game's soundtrack.
        """

        self.model = model.Model()
        pygame.init()

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

    def get_hero_dict_items(self):
        return self.model.hero_dict.items()

    def get_alphanumeric_position(self, rowcolumntuple):
        # print(f"C | calls get_alphanumeric_position({rowcolumntuple}) via Model")
        return self.model.get_alphanumeric_position(rowcolumntuple)

    def get_numeric_notation(self, rowcol):
        # print("C | calls get_numeric_notation via Sprite()")
        return sprite.get_numeric_notation(rowcol)

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)

    def get_model_dict(self):
        return self.model.get_dict()

    def get_hero_dict(self):
        return self.model.get_hero_dict()

    def gather(self, obj, pos):
        curr_pos = self.model.get_curr_pos()
        if obj.name == "healing_potion_y":
            obj.visible = False
            curr_pos.heal = None
            self.model.player.health_potions += 1
            self.model.game_stats["Healing Potions"] = self.model.player.health_potions
            self.view.show_health_button = True
            self.view.health_button.pack()
        if obj.name == "healing_potion_g":
            obj.visible = False
            curr_pos.heal = None
            self.model.player.health_potions += 1
            self.model.game_stats["Healing Potions"] = self.model.player.health_potions
            self.view.show_health_button = True
            self.view.health_button.pack()
        if obj.name == "vision_potion":
            obj.visible = False
            curr_pos.vision = False
            self.model.player.vision_potions += 1
            self.model.game_stats["Vision Potions"] = self.model.player.vision_potions
            self.view.vision = True
            self.view.vision_button.pack()
        if obj.name == "gremlin":
            monster_after_combat = self.combat()
            if monster_after_combat < 0:
                curr_pos.monster = ""
            self.i_fought_a_monster = True
        if obj.name == "skeleton":
            monster_after_combat = self.combat()
            if monster_after_combat < 0:
                curr_pos.monster = ""
            self.i_fought_a_monster = True
        if obj.name == "ogre":
            monster_after_combat = self.combat()
            if monster_after_combat < 0:
                curr_pos.monster = ""
            self.i_fought_a_monster = True
        if obj.name == "abstraction_pillar":
            if self.model.pillars["A"] == "":
                obj.visible = False
                curr_pos.pillar = ""
                self.model.pillars["A"] = True
                self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "A "
        if obj.name == "encapsulation_pillar":
            if self.model.pillars["E"] == "":
                obj.visible = False
                curr_pos.pillar = ""
                self.model.pillars["E"] = True
                self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "E "
        if obj.name == "polymorphism_pillar":
            if self.model.pillars["P"] == "":
                obj.visible = False
                curr_pos.pillar = ""
                self.model.pillars["P"] = True
                self.model.game_stats["Pillars"] = str(self.model.game_stats["Pillars"]) + "P "
        if obj.name == "inheritance_pillar":
            if self.model.pillars["I"] == "":
                obj.visible = False
                curr_pos.pillar = ""
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
        if curr_pos.pit == True:
            self.play("welcome_pit")
        if self.model.player.hp <= 0:
            self.play("game_over")
            self.view.ask_new_game()

    def combat(self):
        curr_pos = self.model.get_curr_pos()
        if curr_pos.monster == "Gremlin" or curr_pos.monster == "Skeleton" or curr_pos.monster == "Ogre":
            print(f"Pre-battle hit points: Player: {self.model.player.hp} | {curr_pos.monster} | {curr_pos.monster_obj.hp}")
            self.model.player.combat(curr_pos.monster_obj)
            print(f"Post-battle hit points: Player: {self.model.player.hp} | {curr_pos.monster} | {curr_pos.monster_obj.hp}")
            if self.model.player.hp <= 0:
                self.model.game_stats["Hit Points"] = self.model.player.hp
                self.view.update_score_label()
                self.play("game_over")
                self.view.ask_new_game()
            return curr_pos.monster_obj.hp

    def pit_fall(self):
        self.model.player.fall_into_pit()
        if self.model.player.hp <= 0:
            self.model.game_stats["Hit Points"] = self.model.player.hp
            self.view.update_score_label()
            self.play("game_over")
            self.view.ask_new_game()

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
        # str_vision = self.model.dungeon.use_vision_potion(room)
        return self.model.dungeon.vision_potion_rooms(room)

    def use_health_potion(self):
        self.model.player.use_health_potion()

    def get_model(self):
        return self.model

    def set_model(self, saved_model):
        self.model = saved_model