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
        self.game_over = False

        # gets set to True upon entering a room with a monster
        self.__monster_blocking_exit = False
        self.announcements = []

        self.door_dict = {
            "C1" : self.model.move_down,
            "D1" : self.model.move_down,
            "E1" : self.model.move_down,
            "G3" : self.model.move_right,
            "G4" : self.model.move_right,
            "G5" : self.model.move_right,
            "A3" : self.model.move_left,
            "A4" : self.model.move_left,
            "A5" : self.model.move_left,
            "C7" : self.model.move_up,
            "D7" : self.model.move_up,
            "E7" : self.model.move_up,
        }
        self.sfx_dict = {}

        # required for sound effects to function
        pygame.init()

    def get_model(self):
        return self.model

    def set_model(self, saved_model):
        self.model = saved_model

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

            # fight monster if applicable
            if curr_room.monster:
                if candidate == curr_room.monster.lower():
                    monster_hp = self.combat()
                    if monster_hp > 0:
                        move_succeeds = False

            # potions
            if curr_room.vision and candidate == "vision_potion":
                curr_room.vision = False
                self.model.player.vision_potions += 1
                self.announce("Picked up a vision potion!")
                self.play("magic_harp")

            if curr_room.heal and candidate in ["healing_potion_g", "healing_potion_y"]:
                curr_room.heal = None
                self.model.player.health_potions += 1
                self.announce("Picked up a health potion!")
                self.play("magic_harp")

            # pillars
            if curr_room.pillar and "pillar" in candidate:
                self.model.pillars[curr_room.pillar] = True
                self.model.game_stats["Pillars"] += f"{curr_room.pillar.upper()} "
                curr_room.pillar = None
                self.play("pillar")

            if curr_room.is_entrance and candidate == "entrance":
                move_succeeds = False

            if curr_room.is_exit and candidate == "exit":
                if self.model.player_has_all_pillars():
                    self.announce(f"{self.model.player_name} has won the game!")
                    self.play("yay")
                    self.game_over = True

        # resolve room transition if appropriate
        if alphanum in self.door_dict:
            if self.__monster_blocking_exit:
                self.announce("Your debilitating sense of honor won't let you leave without fighting this room's guardian at least once!")
            else:
                self.__room_transition = self.door_dict[alphanum]()
                if self.__room_transition:
                    self.resolve_transition()

        # retrieve any messages from Model
        self.get_messages_from_model()

        return move_succeeds

    def resolve_transition(self):
        """
        This method is called when the player enters a new room and resolves whatever game behavior is appropriate for that transition.
        """
        current_room = self.model.get_curr_pos()
        current_room.is_visited = True

        # stop all playback from previous room
        for sfx in self.sfx_dict:
            self.sfx_dict[sfx].set_volume(0)

        if current_room.monster is not None:
            self.__monster_blocking_exit = True

        if current_room.pit:
            self.pit_fall()

        if current_room.is_exit:
            self.announce("You've reached the exit!")
            if self.model.player_has_all_pillars():
                self.announce("You've won!")
                self.game_over = True
            else:
                self.announce("You need to find more pillars before you can leave.")

    def combat(self):
        curr_pos = self.model.get_curr_pos()
        monster_name = curr_pos.monster

        # fighting the monster enables escape
        self.__monster_blocking_exit = False

        # resolve combat
        self.announce(f"Initiating combat! {self.model.player_name}: {self.model.player.hp} | {monster_name} | {curr_pos.monster_obj.hp}")

        self.model.player.combat(curr_pos.monster_obj)

        # combat generates messages we'll want to grab before making more announcements
        self.get_messages_from_model()

        self.announce(f"Post-battle hit points: Player: {self.model.player.hp} | {monster_name} | {curr_pos.monster_obj.hp}")

        # resolve monster death is applicable
        monster_hp = curr_pos.monster_obj.hp
        if monster_hp <= 0:
            self.announce(f"{monster_name} was defeated!")
            curr_pos.monster = None 

        # resolve player death if applicable
        if self.model.player.hp <= 0:
            self.model.game_stats["Hit Points"] = self.model.player.hp
            self.view.update_frame_info()
            self.play("wilhelm_scream")
            self.game_over = True

        return monster_hp

    def pit_fall(self):
        self.model.player.fall_into_pit()
        self.play("welcome_pit")
        if self.model.player.hp <= 0:
            self.model.game_stats["Hit Points"] = self.model.player.hp
            self.view.update_frame_info()
            self.play("wilhelm_scream")
            self.view.ask_new_game()

    def use_vision_potion(self, room):
        self.model.player.use_vision_potion()
        return self.model.dungeon.vision_potion_rooms(room)

    def use_health_potion(self):
        self.model.player.use_health_potion()

    def play(self, file):
        """
        plays a sound.  If the sound is already playing it stops it before playing a new one.
        params:
        :file: a string corresponding to a .wav file in the audio folder
        """
        if file in self.sfx_dict:
            self.sfx_dict[file].set_volume(0)
        filename = f"audio/{file}.wav"
        self.sfx_dict[file] = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(self.sfx_dict[file])

    def announce(self, message):
        """
        Adds this message to announcements list.
        """
        self.announcements.append(message)

    def get_messages_from_model(self):
        """
        Gets any announcements in Model and adds them to a list in this class.
        """
        while self.model.announcements:
            msg = self.model.announcements.pop(0)
            self.announcements.append(msg)