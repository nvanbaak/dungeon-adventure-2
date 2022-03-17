from threading import current_thread
from tkinter.tix import Tree
import pygame

from configurations import START_SPRITES_POSITION

class Controller:

    def __init__(self, view, model):
        """
        Controller class allows the View class to access the underlying game structure within Model such that it knows what
        to display.
        """
        self.model = model
        self.view = view

        # used to track whether we've transitioned to a new room since the View class checked last
        self.__room_transition = False

        # gets set to True upon entering a room with a monster
        self.__monster_blocking_exit = False

        self.door_dict = {
            "C1" : self.move_down,
            "D1" : self.move_down,
            "E1" : self.move_down,
            "G3" : self.move_right,
            "G4" : self.move_right,
            "G5" : self.move_right,
            "A3" : self.move_left,
            "A4" : self.move_left,
            "A5" : self.move_left,
            "C7" : self.move_up,
            "D7" : self.move_up,
            "E7" : self.move_up,
        }

        # required for sound effects to function
        pygame.init()

    def get_model(self):
        return self.model

    def set_model(self, saved_model):
        self.model = saved_model

    ##################################
    #        MOVEMENT FUNCTIONS      #
    ##################################

    def move_left(self):
        return self.model.move_left()

    def move_right(self):
        return self.model.move_right()

    def move_up(self):
        return self.model.move_up()

    def move_down(self):
        return self.model.move_down()

    def reset_default_characters(self):
        print("TODO: Make this reset the game state")

    def check_for_room_transition(self):
        """
        Returns True if we've transitioned to a new room, False otherwise.
        """
        output = self.__room_transition
        self.__room_transition = False
        return output

    ##################################
    #          GAME MECHANICS        #
    ##################################

    def activate_square(self, alphanum):
        """
        Resolves whatever actions are appropriate for the objects located at the designated square.
        """
        move_succeeds = True
        curr_room = self.model.get_curr_pos()

        # determine which objects if any to interact with
        if alphanum in START_SPRITES_POSITION:
            candidate = START_SPRITES_POSITION[alphanum]

            print(f"candidate: {candidate}")

            # fight monster if applicable
            if curr_room.monster:
                if candidate == curr_room.monster.lower():
                    monster_hp = self.combat()
                    if monster_hp > 0:
                        move_succeeds = False

            # potions
            print(f"vision potion: {curr_room.vision}")
            if curr_room.vision and candidate == "vision_potion":
                curr_room.vision = False
                self.model.player.vision_potions += 1

            print(f"health potion: {curr_room.heal}")
            if curr_room.heal and "health_potion" in candidate:
                curr_room.heal = False
                self.model.player.health_potions += 1

            # pillars
            print(f"pillar: {curr_room.pillar}")
            if curr_room.pillar and "pillar" in candidate:
                self.model.pillars[curr_room.pillar] = True
                curr_room.pillar = None

        


        # resolve room transition if appropriate
        if alphanum in self.door_dict:
            if self.__monster_blocking_exit:
                self.announce("Your debilitating sense of honor won't let you leave without fighting this room's guardian at least once!")
            else:
                self.__room_transition = self.door_dict[alphanum]()
                if self.__room_transition:
                    self.resolve_transition()

        return move_succeeds

    def resolve_transition(self):
        """
        This method is called when the player enters a new room and resolves whatever game behavior is appropriate for that transition.
        """
        current_room = self.model.get_curr_pos()
        if current_room.monster is not None:
            self.__monster_blocking_exit = True
        if current_room.pit:
            self.pit_fall()
        current_room.is_visited = True

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
        if self.model.player.hp <= 0:
            self.play("game_over")
            self.view.ask_new_game()

    def combat(self):
        curr_pos = self.model.get_curr_pos()
        monster_name = curr_pos.monster

        # fighting the monster enables escape
        self.__monster_blocking_exit = False

        # resolve combat
        self.announce(f"Pre-battle hit points: Player: {self.model.player.hp} | {monster_name} | {curr_pos.monster_obj.hp}")

        self.model.player.combat(curr_pos.monster_obj)

        self.announce(f"Post-battle hit points: Player: {self.model.player.hp} | {monster_name} | {curr_pos.monster_obj.hp}")

        # resolve monster death is applicable
        monster_hp = curr_pos.monster_obj.hp
        if monster_hp <= 0:
            self.announce(f"{monster_name} was defeated!")
            curr_pos.monster = None 

        # resolve player death if applicable
        if self.model.player.hp <= 0:
            self.model.game_stats["Hit Points"] = self.model.player.hp
            self.view.update_score_label()
            self.play("game_over")
            self.view.ask_new_game()

        return monster_hp

    def pit_fall(self):
        self.model.player.fall_into_pit()
        self.play("welcome_pit")
        if self.model.player.hp <= 0:
            self.model.game_stats["Hit Points"] = self.model.player.hp
            self.view.update_score_label()
            self.play("game_over")
            self.view.ask_new_game()

    def use_vision_potion(self, room):
        self.model.player.use_vision_potion()
        # str_vision = self.model.dungeon.use_vision_potion(room)
        return self.model.dungeon.vision_potion_rooms(room)

    def use_health_potion(self):
        self.model.player.use_health_potion()

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

    def announce(self, message):
        """
        TODO passes announcement to game log
        """
        print(message)