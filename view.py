import tkinter as tk
from tkinter import Tk, Menu, Button, Label, Frame, Canvas, FLAT, SW, W, E, RIGHT, TOP, PhotoImage, messagebox
from tkinter import TclError
from PIL import Image, ImageTk, ImageOps

from configurations import *
from controller import Controller
from model import Model
from preferenceswindow import PreferencesWindow
from musicplayer import MusicPlayer
from sprite import Sprite
import save_load_game

import sys
import time


class View:
    """
    View class holds the entirety of the game's GUI elements.
    """
    def __init__(self, parent, root, hero_class, player_name):

        # misc object references
        self.parent = parent
        self.root = root

        # utility classes
        self.model = Model(hero_class, player_name)
        self.controller = Controller(self, self.model)
        self.music_player = MusicPlayer()

        # TODO these variables will be deprecated
        self.vision = False
        self.show_health_button = False

        # tk parameters
        self.room_size = ROW_COUNT * SQUARE_SIZE
        self.canvas_width = self.room_size
        self.canvas_height = self.room_size
        self.canvas = None

        self.root.protocol("WM_DELETE_WINDOW", self.on_close_window)

        # init
        self.create_top_menu()
        self.setup_gui()

        self.interactables = {}

        self.hero_sprite = Sprite(hero_class, self.canvas, HERO_POSITION)
        self.sprite_dict = {}
        self.load_sprites()

        self.start_new_game()

    ##################################
    #       MENU BUILD METHODS       #
    ##################################

    def create_top_menu(self):
        """
        Create game menu bar. Create file and edit submenus.
        """
        self.menu_bar = Menu(self.root)
        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        """
        Create File submenus for New Game, Save Game, Load Game, and Delete All Saved Games.
        """
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label="New Game", command=self.on_new_game_menu_clicked)
        self.file_menu.add_command(
            label="Save Game", command=self.on_save_game_menu_clicked)
        self.file_menu.add_command(
            label="Load Game", command=self.on_load_game_menu_clicked)
        self.file_menu.add_command(
            label="Delete All Saved Games", command=self.on_delete_games_menu_clicked)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def create_edit_menu(self):
        """
        Create Edit submenus for Sound and Background Color preferences.
        """
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(
            label="Background Color", command=self.on_preference_menu_clicked)
        self.edit_menu.add_command(
            label="Sound", command=self.music_player.toggle_music)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.root.config(menu=self.menu_bar)


    ##################################
    #       MENU FUNCTIONALITY       #
    ##################################

    def on_new_game_menu_clicked(self):
        self.root.destroy()
        self.music_player.stop_music()
        self.root.quit()
        init_new_game()

    def on_save_game_menu_clicked(self):
        saveload_window = tk.Tk()
        saveload_canvas_width = 100
        saveload_canvas_height = 40
        saveload_canvas = Canvas(
            saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=self.board_color_1)
        saveload_label = Label(saveload_canvas)
        sg = save_load_game.SaveGame()
        game_name = sg.game_name_generator()
        sg.save_game(game_name, self.controller.get_model())
        lbltxt = f"{game_name} successfully saved!"
        saveload_label.config(text = lbltxt)
        saveload_label.pack()
        saveload_canvas.pack(padx=8, pady=8)

    def on_load_game_menu_clicked(self):
        saveload_window = tk.Tk()
        saveload_canvas_width = 50
        saveload_canvas_height = 50
        saveload_canvas = Canvas(
            saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=self.board_color_1)
        saveload_label = Label(saveload_canvas, text = "Select saved game")
        saveload_label.pack()
        saveload_canvas.pack(padx=8, pady=8)
        sg = save_load_game.SaveGame
        saved_list = sg.saved_games_list()
        self.clicked = tk.StringVar()
        self.clicked.set("Select")
        drop = tk.OptionMenu(saveload_canvas, self.clicked, *saved_list, command=self.open_saved)
        drop.pack()

    def open_saved(self, selected_game):
        sg = save_load_game.SaveGame
        if self.clicked != "Select":
            m = sg.load_game(sg, selected_game)
            self.controller.set_model(m)
            self.draw_room()
            self.controller.reset_default_characters()
            self.draw_all_sprites()
            self.on_square_clicked_manual(True)
            self.update_score_label()
            if self.vision == False:
                self.vision_button.pack_forget()

    def on_delete_games_menu_clicked(self):
        sg = save_load_game.SaveGame()
        sg.delete_all_saved_games()

    def on_preference_menu_clicked(self):
        PreferencesWindow(self)


    ##################################
    #        GUI CONSTRUCTION        #
    ##################################

    def setup_gui(self):
        """
        Builds the base elements of the GUI
        """
        self.create_canvas()
        self.draw_walls()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.create_bottom_frame()

    def create_canvas(self):
        """
        Creates the base canvas for the game.
        Parameters can be modified in configurations.py
        """
        self.canvas = Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, bg=BOARD_COLOR_1)
        self.canvas.pack(padx=8, pady=8)

    def create_bottom_frame(self):
        """
        Constructs a frame at the base of the window
        and adds the relevant widgets.
        """
        def create_frame():
            self.bottom_frame = Frame(self.root, height=64)
            self.info_label = Label(
                self.bottom_frame, text="")
            self.info_label.pack(side="left", padx=8, pady=5)
            self.bottom_frame.pack(fill="x", side="bottom")

        def create_vision_button():
            """
            Constructs the vision potion button
            and addis it to the bottom frame.
            """
            self.vision_button = Button(self.bottom_frame, text="Use Vision", command=self.use_vision)
            self.vision_button.configure(activebackground="#33B5E5")
            self.vision_button.pack(side=TOP)
            if self.vision == False:
                self.vision_button.pack_forget()

        def create_health_button():
            """
            Constructs the health potion button
            and adds it to the bottom frame.
            """
            self.health_button = Button(self.bottom_frame, text="Use Health", command=self.use_health)
            self.health_button.configure(activebackground="#33B5E5")
            self.health_button.pack(side=TOP)
            if self.show_health_button == False:
                self.health_button.pack_forget()

        create_frame()
        create_vision_button()
        create_health_button()


    ##################################
    #    GUI BUTTON FUNCTIONALITY    #
    ##################################

    def use_health(self):
        self.controller.use_health_potion()
        self.update_score_label()

    def use_vision(self):
        self.create_vision_window()
        vision_grid = self.controller.use_vision_potion(self.controller.get_room_data())
        row_min = 100
        row_max = 0
        col_min = 100
        col_max = 0
        for r in range(0, len(vision_grid[0])):
            for c in range(0, len(vision_grid[1])):
                if vision_grid[r][c]:
                    row_min = min(row_min, vision_grid[r][c].location[0])
                    row_max = max(row_max, vision_grid[r][c].location[0])
                    col_min = min(col_min, vision_grid[r][c].location[1])
                    col_max = max(col_max, vision_grid[r][c].location[1])
                    self.draw_vision_room(vision_grid[r][c], c, r, "vision")
                else:
                    pass
        self.controller.model.game_stats["Vision Potions"] = self.controller.model.player.vision_potions
        self.vision = False
        self.vision_button.pack_forget()
        self.update_score_label()

    def create_vision_window(self):
        self.vision_window = tk.Tk()
        self.vision_canvas_width = 900
        self.vision_canvas_height = 900
        self.vision_canvas = Canvas(
            self.vision_window, width=self.vision_canvas_width, height=self.vision_canvas_height, bg=self.board_color_1)
        self.vision_canvas.pack(padx=8, pady=8)

    def on_close_window(self):
        """
        Event handler for window closure..
        """
        self.music_player.stop_music()
        self.root.destroy()


    ##################################
    #     GRAPHICS FUNCTIONALITY     #
    ##################################

    def start_new_game(self):
        """
        Resets game data to a fresh start, then displays the game state.
        """
        self.controller.reset_default_characters()

        self.load_current_room()
        self.update_score_label()

    def draw_walls(self):
        """
        Draws walls on each side of the room.
        """
        up_wall = (
                0, 0,
                self.canvas_width, WALL_WIDTH)
        down_wall = (
                0, self.canvas_height - WALL_WIDTH,
                self.canvas_width, self.canvas_height)
        left_wall = (
                0, 0, 
                WALL_WIDTH, self.canvas_height)
        right_wall = (
                self.canvas_width - WALL_WIDTH, 
                0, self.canvas_height, self.canvas_height)

        for wall in [up_wall, down_wall, left_wall, right_wall]:
            self.canvas.create_rectangle(
                    wall[0], wall[1],
                    wall[2], wall[3],
                    fill="black")

    def load_current_room(self):
        """
        gets all GUI-relevant information about the current room and displays it.
        """
        self.draw_doors()
        self.draw_all_sprites()

    def draw_doors(self, fill_color=BOARD_COLOR_1):
        """
        Draws doors where appropriate given the player's current locations.
        """
        self.erase_doors()
        door_dict = self.model.get_curr_pos().door_value

        door_coords = {
            "Up" : (
                    self.canvas_width//3, 0, 
                    2 * self.canvas_width//3, WALL_WIDTH),
            "Down" : (
                    self.canvas_width//3, self.canvas_height - WALL_WIDTH,
                    2 * self.canvas_width//3, self.canvas_height),
            "Left" : (
                    0, self.canvas_height//3,
                    WALL_WIDTH, 2 * self.canvas_height//3),
            "Right" : (
                    self.canvas_width - WALL_WIDTH, self.canvas_height//3,
                    self.canvas_width, 2 * self.canvas_height//3)
        }

        for dir in ["Up", "Down", "Left", "Right"]:
            if door_dict[dir]:
                door = door_coords[dir]
                self.canvas.create_rectangle(
                        door[0], door[1],
                        door[2], door[3],
                        fill=fill_color,
                        tags="doors")

    def erase_doors(self):
        """
        removes all doors from the canvas;
        this prevents memory leaks from drawing
        the same door on top of itself in every room
        """
        self.canvas.delete("doors")

    def reload_colors(self, color):
        """
        Redraws the room wih a new color; unsure if this works
        """
        self.canvas.config(bg=color)
        self.erase_doors()
        self.draw_doors(color)

    def load_sprites(self):
        """
        Instantiates a Sprite object for each type of object in the dungeon
        """
        for position, name in START_SPRITES_POSITION.items():
            self.sprite_dict[name] = Sprite(name, self.canvas, position)

    def draw_all_sprites(self):
        """
        Draws the hero, then gets a list of all game objeects in the current room and displays the corresponding sprites.
        """
        self.canvas.delete("sprites")
        self.hero_sprite.draw()

        objects_to_display = self.model.get_current_room_contents()

        for game_object in objects_to_display:
            self.sprite_dict[game_object].draw()
            print(f"drew a {game_object}")

    def clear_all_sprites(self):
        """
        Deletes all sprites from the canvas.  Used when transitioning between rooms.
        """
        self.canvas.delete("sprites")

    def update_score_label(self):
        """
        Modifies the text in the bottom frame using information from Model.
        """

        game_stats = self.model.get_game_stats()
        exit_flag = self.model.get_curr_pos().is_exit

        info_fields = []
        for key, value in game_stats.items():
            info_fields.append(f"{key}: {value}")
        label_text = " | ".join(info_fields)

        if self.model.player_is_dead():
            label_text = "Y O U  D I E D !!!!!"
        elif exit_flag and self.model.player_has_all_pillars():
            label_text = "Y O U  W I N !!!!!"
        self.info_label["text"] = label_text


    ##################################
    # GAME CONTROLS (TODO move these to controller)
    ##################################

    def on_square_clicked(self, event):
        """
        Event handling for click event.  Resolves any object interactions in the clicked square and then moves the player to the square if no object remains there.
        """

        click_pos = self.pixels_to_alphanum(event)
        if click_pos is None:
            return

        # activate_square returns True or False depending on whether the square is empty after resolution
        item_resolved = self.controller.activate_square(click_pos)

        if item_resolved:
            # in the case of a room transition, modify player location
            if self.controller.check_for_room_transition():
                if "1" in click_pos:
                    click_pos.replace("1", "7")
                elif "7" in click_pos:
                    click_pos.replace("7", "1")
                elif "A" in click_pos:
                    click_pos.replace("A", "G")
                elif "G" in click_pos:
                    click_pos.replace("G", "A")

                # then redraw the room
                self.load_current_room()

            self.hero_sprite.redraw_at(click_pos)


    def pixels_to_alphanum(self, event):
        """
        Given a click event, returns the alphanumeric position that was clicked
        """
        col_size = row_size = SQUARE_SIZE
        clicked_column = event.x // col_size
        clicked_row = 6 - (event.y // row_size)

        if clicked_row not in range(7):
            return None
        if clicked_column not in range(7):
            return None

        return f"{X_AXIS_LABELS[clicked_column]}{Y_AXIS_LABELS[clicked_row]}"



    def on_square_clicked_manual(self, clicked):
        """
        This is to prevent an infinite loop when the user clicks near a door. The room only changes if the user
        clicked a doorway, not if the user appears in the next room in a doorway. It also redraws the room after
        every user click.
        """
        rm = self.controller.get_room_data()
        door_dict = rm.door_value
        self.hide_all_sprites()

        hero_dict = self.controller.get_hero_dict()
        model_dict = self.controller.get_model_dict()

        sprite_obj = hero_dict[self.sprite_position]

        self.ok_to_leave = False

        if rm.monster:
            if self.controller.i_fought_a_monster:
                self.ok_to_leave = True
            else:
                self.controller.model.announce(
                    "You cannot leave until you kill the monster.Click on the monster to start battle")
                self.ok_to_leave = False
        else:
            self.ok_to_leave = True

        if rm.pit:
            if self.pit_falls == 0:
                self.controller.pit_fall()
                self.pit_falls = 1

        if clicked == True and self.ok_to_leave == True:
            if self.sprite_position == "G5" or self.sprite_position == "G4" or self.sprite_position == "G3":
                if door_dict["Right"] == True:
                    self.controller.move_right()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("G", "A")
                    hero_dict[self.sprite_position] = sprite_obj
                    # self.controller.gather()
                    self.sound_effect_play_count = 0
                    self.controller.i_fought_a_monster = False
                    self.pit_falls = 0
            elif self.sprite_position == "C1" or self.sprite_position == "D1" or self.sprite_position =="E1":
                if door_dict["Down"] == True:
                    self.controller.move_down()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("1", "7")
                    hero_dict[self.sprite_position] = sprite_obj
                    # self.controller.gather()
                    self.sound_effect_play_count = 0
                    self.controller.i_fought_a_monster = False
                    self.pit_falls = 0
            elif self.sprite_position == "A5" or self.sprite_position == "A4" or self.sprite_position == "A3":
                if door_dict["Left"] == True:
                    self.controller.move_left()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("A", "G")
                    hero_dict[self.sprite_position] = sprite_obj
                    # self.controller.gather()
                    self.sound_effect_play_count = 0
                    self.controller.i_fought_a_monster = False
                    self.pit_falls = 0
            elif self.sprite_position == "C7" or self.sprite_position == "D7" or self.sprite_position == "E7":
                if door_dict["Up"] == True:
                    self.controller.move_upper()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("7", "1")
                    hero_dict[self.sprite_position] = sprite_obj
                    # self.controller.gather()
                    self.sound_effect_play_count = 0
                    self.controller.i_fought_a_monster = False
                    self.pit_falls = 0
            else:
                pass

        self.canvas.delete("all")
        self.controller.refresh_room()
        self.draw_room()
        self.draw_all_sprites()
        self.sound_effect_play_count = self.sound_effect_play_count + 1
        if self.sound_effect_play_count == 1:
            self.controller.gather_sounds()
        if clicked == True:
            self.doorway_refresh(hero_dict, clicked)
        m = self.controller.get_model()
        if rm.is_exit == True and m.pillars["E"] == True and m.pillars["E"] == True and m.pillars["A"] == True and m.pillars["I"] == True:
            self.controller.model.announce(f"{self.controller.model.player} has won the game!")
            self.controller.play("you_win")
            self.ask_new_game()



    def check_sq_for_gatherable_objects(self, position_of_click):
        model_dict = self.controller.get_model_dict()
        for position, value in model_dict.items():
            if position == position_of_click:
                s_obj = model_dict[position]
                return s_obj



    ##################################
    #           UNSORTED             #
    ##################################

    def doorway_refresh(self, hero_dict, clicked):
        sprite = hero_dict[self.sprite_position]
        doors = ["C1", "D1", "E1", "C7", "D7", "E7", "G3", "G4", "G5", "A3", "A4", "A5"]
        if sprite.name == "warrior" and self.sprite_position in doors:
            for doorway in doors:
                if self.sprite_position == doorway:
                    self.on_square_clicked_manual(False)


        self.update_score_label()

    def process_gatherable_object(self, obj, pos):
        self.controller.gather(obj, pos)





    def shift(self, start_pos, end_pos):
        self.controller.pre_move_validation(start_pos, end_pos)
 








    ##################################
    #        NEED REFACTORING
    ##################################

    def draw_vision_room(self, rm, i, j, type):
        WALL_WIDTH = 10
        door_dict = rm.door_value
        vision_square_width = self.vision_canvas_width / 3
        vision_square_height = self.vision_canvas_height / 3
        if type == "map":
            pass
            # vision_square_width = self.vision_canvas_width / 3
            # vision_square_height = self.vision_canvas_height / 3
        vi = i * vision_square_width
        vj = j * vision_square_height

        vrs = []
        VISION_SQUARE = 100
        if rm.heal == "y":
            vrs.append([sprite.create_sprite("healing_potion_y"), 0, 0])
        if rm.heal == "g":
            vrs.append([sprite.create_sprite("healing_potion_g"), 0, 2 * VISION_SQUARE])
        if rm.vision == True:
            vrs.append([sprite.create_sprite("vision_potion"), 0, 1 * VISION_SQUARE])
        if rm.pillar == "a":
            vrs.append([sprite.create_sprite("abstraction_pillar"), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "e":
            vrs.append([sprite.create_sprite("encapsulation_pillar"), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "p":
            vrs.append([sprite.create_sprite("polymorphism_pillar"), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "i":
            vrs.append([sprite.create_sprite("inheritance_pillar"), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.monster == "Gremlin":
            vrs.append([sprite.create_sprite("gremlin"), 2 * VISION_SQUARE, 0])
        if rm.monster == "Ogre":
            vrs.append([sprite.create_sprite("ogre"), 2 * VISION_SQUARE, 0])
        if rm.monster == "Skeleton":
            vrs.append([sprite.create_sprite("skeleton"), 2 * VISION_SQUARE, 0])
        if rm.pit == True:
            vrs.append([sprite.create_sprite("pit"), 2 * VISION_SQUARE, 2 * VISION_SQUARE])
        if rm.is_entrance:
            vrs.append([sprite.create_sprite("entrance"), 0 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.is_exit:
            vrs.append([sprite.create_sprite("exit"), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        orig_rm = self.controller.get_room_data()
        if rm == orig_rm:
            vrs.append([sprite.create_sprite(HERO_SPRITE), VISION_SQUARE, VISION_SQUARE])
        for i in range(0, len(vrs)):
            self.draw_vision_sprite(vrs[i][0], vrs[i][1], vrs[i][2], vi, vj)

        for key, value in door_dict.items():
            if key == "Up" and value == True:
                self.vision_canvas.create_rectangle(vi, vj, vi + (vision_square_width/3), vj + WALL_WIDTH, fill="black")
                self.vision_canvas.create_rectangle(vi + (2 * (vision_square_width/3)), vj, vi + vision_square_width,
                                                     vj + WALL_WIDTH, fill="black")
            if key == "Up" and value == False:
                self.vision_canvas.create_rectangle(vi, vj, (vi + vision_square_width), vj + WALL_WIDTH, fill="black")
            if key == "Down" and value == True:
                self.vision_canvas.create_rectangle(vi, vj + vision_square_height - WALL_WIDTH, vi + (vision_square_width/3),
                                             vj + vision_square_height, fill="black")
                self.vision_canvas.create_rectangle(vi + (2 * (vision_square_width/3)), vj + vision_square_height - WALL_WIDTH,
                                             vi + vision_square_width, vj + vision_square_height, fill="black")
            if key == "Down" and value == False:
                self.vision_canvas.create_rectangle(vi, vj + vision_square_height - WALL_WIDTH, vi + vision_square_width,
                                             vj + vision_square_height, fill="black")
            if key == "Left" and value == True:
                self.vision_canvas.create_rectangle(vi, vj, vi + WALL_WIDTH, vj + (vision_square_height/3), fill="black")
                self.vision_canvas.create_rectangle(vi, vj + (2 * (vision_square_height/3)), vi + WALL_WIDTH,
                                             vj + vision_square_height, fill="black")
            if key == "Left" and value == False:
                self.vision_canvas.create_rectangle(vi, vj, vi + WALL_WIDTH, vj + vision_square_height, fill="black")
            if key == "Right" and value == True:
                self.vision_canvas.create_rectangle(vi + vision_square_width - WALL_WIDTH, vj, vi + vision_square_width,
                                             vj + (vision_square_height/3), fill="black")
                self.vision_canvas.create_rectangle(vi + vision_square_width - WALL_WIDTH, vj + (2 * (vision_square_height/3)),
                                             vi + vision_square_width, vj + vision_square_height, fill="black")
            if key == "Right" and value == False:
                self.vision_canvas.create_rectangle(vi + vision_square_width - WALL_WIDTH, vj, vi + vision_square_height,
                                             vj + vision_square_height, fill="black")
            else:
                pass

    def draw_vision_sprite(self, sprite, x_pos, y_pos, vi, vj):
        UNDER_100 = (70, 70)

        if isinstance(sprite, Sprite):
            filename = "sprites_image/{}.png".format(
                sprite.name.lower())
            im = Image.open(filename)
            image = ImageOps.contain(im, UNDER_100)
            ph = ImageTk.PhotoImage(image, master=self.vision_canvas)
            x_pos = x_pos + 15 + vi
            y_pos = y_pos + 15 + vj
            label = tk.Label(self.vision_canvas, image=ph, bg=self.board_color_1)
            label.config(width=70, height=70)
            label.image = ph
            label.place(x=x_pos, y=y_pos)

    def ask_new_game(self):
        self.root.quit()
        res = messagebox.askyesno("Game Over!", "Would you like to play again?")
        if res == True:
            m = self.controller.get_model()
            m.pillars = {"A": "", "E": "", "P": "", "I": ""}
            self.game_stats = {"Hit Points": 0, "Pillars": "", "Healing Potions": 0, "Vision Potions": 0}
            self.update_score_label()
            self.on_new_game_menu_clicked()
            self.root.destroy()
            time.sleep(3)
            self.music_player.stop_music()
            self.root.quit()
            init_new_game()
        else:
            self.root.destroy()
            sys.exit()
