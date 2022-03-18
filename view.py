import tkinter as tk
from tkinter import LEFT, N, Tk, Menu, Button, Label, Frame, Canvas, FLAT, SW, W, E, RIGHT, TOP, PhotoImage, messagebox
from PIL import Image, ImageTk, ImageOps

from configurations import *
from controller import Controller
from model import Model
from preferenceswindow import PreferencesWindow
from musicplayer import MusicPlayer
from sprite import Sprite
from save_load_game import SaveGame
import menu_factory

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
        self.main_frame = None
        self.canvas = None

        self.health_button = None
        self.vision_button = None
        self.info_label = None
        self.bottom_frame = None
        self.game_log = None
        self.game_log_contents = [
            "As you adventure, information about your progress will appear here."]

        self.root.protocol("WM_DELETE_WINDOW", self.on_close_window)

        # init
        self.create_top_menu()
        self.setup_gui()

        self.hero_sprite = Sprite(hero_class, self.canvas, HERO_POSITION)
        self.sprite_dict = {}
        self.load_sprites()
        self.secret_view = False

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
            label="New Game", command=self.ask_new_game)
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

    def on_save_game_menu_clicked(self):
        saveload_window = tk.Tk()
        saveload_canvas_width = 100
        saveload_canvas_height = 40
        saveload_canvas = Canvas(
            saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=BOARD_COLOR_1)
        saveload_label = Label(saveload_canvas)
        sg = SaveGame()
        game_name = sg.game_name_generator()
        sg.save_game(game_name, self.controller.get_model())
        lbltxt = f"{game_name} successfully saved!"
        saveload_label.config(text = lbltxt)
        saveload_label.pack()
        saveload_canvas.pack(padx=8, pady=8)

    def on_load_game_menu_clicked(self):
        self.saveload_window = tk.Tk()
        saveload_canvas_width = 50
        saveload_canvas_height = 50
        saveload_canvas = Canvas(
            self.saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=BOARD_COLOR_1)
        saveload_label = Label(saveload_canvas, text = "Select saved game")
        saveload_label.pack()
        saveload_canvas.pack(padx=8, pady=8)
        sg = SaveGame()
        saved_list = sg.saved_games_list()
        if len(saved_list) > 0:
            self.clicked = tk.StringVar()
            self.clicked.set("Select")
            drop = tk.OptionMenu(saveload_canvas, self.clicked, *saved_list, command=self.open_saved)
            drop.pack()
        else: # no games saved
            no_saved_game_label = Label(saveload_canvas, text = "No game saved to load")
            no_saved_game_label.pack()
            saveload_canvas.pack()

    def open_saved(self, selected_game):
        sg = SaveGame()
        if self.clicked != "Select":
            m = sg.load_game(selected_game)
            self.model = m 
            self.controller = Controller(self, self.model)
            self.hero_sprite.name = self.model.hero
            self.load_current_room()
            self.update_frame_info()
            self.update_game_log()
            self.saveload_window.destroy()  # destroys the saveload window after loading the game

    def on_delete_games_menu_clicked(self):
        sg = SaveGame()
        sg.delete_all_saved_games()

    def on_preference_menu_clicked(self):
        PreferencesWindow(self)

    def ask_new_game(self):
        """
        Gives the player the option of quitting or returning to the menu
        """
        play_again = messagebox.askyesno("Game Over!", "Would you like to play again?")
        if play_again:
            self.music_player.stop_music()
            self.root.destroy()
            menu_factory.MenuFactory.create_main_menu()
        else:
            self.root.destroy()
            sys.exit()


    ##################################
    #        GUI CONSTRUCTION        #
    ##################################

    def setup_gui(self):
        """
        Builds the base elements of the GUI
        """
        self.main_frame = Frame(self.root, height=self.room_size)
        self.main_frame.pack()
        self.create_canvas()
        self.draw_walls()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.root.bind("<Key>", self.on_key_pressed)
        self.create_bottom_frame()
        self.update_game_log()

    def create_canvas(self):
        """
        Creates the base canvas for the game.
        Parameters can be modified in configurations.py
        """
        self.canvas = Canvas(
            self.main_frame, width=self.canvas_width, height=self.canvas_height, bg=BOARD_COLOR_1)
        self.canvas.pack(side="left", padx=8, pady=8)

    def create_bottom_frame(self):
        """
        Constructs a frame at the base of the window
        and adds the relevant widgets.
        """
        def create_frame():
            self.bottom_frame = Frame(self.root, height=64)
            self.bottom_frame.pack(fill="x", side="bottom")
            
            self.info_label = Label(self.bottom_frame)
            self.info_label.pack(side="left", padx=8, pady=5)

        def create_vision_button():
            """
            Constructs the vision potion button
            and addis it to the bottom frame.
            """
            self.vision_button = Button(self.bottom_frame, text="Use Vision", command=self.use_vision)
            self.vision_button.configure(activebackground="#33B5E5")
            self.vision_button.pack(side=TOP)
            if self.model.player.vision_potions == 0:
                self.vision_button.pack_forget()

        def create_health_button():
            """
            Constructs the health potion button
            and adds it to the bottom frame.
            """
            self.health_button = Button(self.bottom_frame, text="Use Health", command=self.use_health)
            self.health_button.configure(activebackground="#33B5E5")
            self.health_button.pack(side=TOP)
            if self.model.player.health_potions == 0:
                self.health_button.pack_forget()

        create_frame()
        create_vision_button()
        create_health_button()

    def update_game_log(self):
        """
        Constructs a frame on the side of the screen, used for combat logs
        """
        if self.game_log:
            self.game_log.destroy()

        self.get_announcements()

        while( len(self.game_log_contents) > 13 ):
            self.game_log_contents.pop(0)

        log_text = "\n\n".join(self.game_log_contents)

        self.game_log = Label(self.main_frame, width=20, height=10, text=log_text, wraplength=150, anchor=N)
        self.game_log.pack(fill="y", side="right", padx=8, pady=8)

    def get_announcements(self):
        """
        Retrieves announcements from controller
        """
        while self.controller.announcements:
            announce = self.controller.announcements.pop(0)
            self.game_log_contents.append(announce)


    ##################################
    #    GUI BUTTON FUNCTIONALITY    #
    ##################################

    def use_health(self):
        self.controller.use_health_potion()
        self.update_frame_info()

    def use_vision(self):
        self.create_vision_window()
        rm = self.model.get_curr_pos()
        vision_grid = self.controller.use_vision_potion(rm)
        for r in range(0, len(vision_grid[0])):
            for c in range(0, len(vision_grid[1])):
                if vision_grid[r][c]:
                    self.draw_vision_room(vision_grid[r][c], c, r, "vision")
                else:
                    pass
        self.controller.model.game_stats["Vision Potions"] = self.controller.model.player.vision_potions
        self.vision = False
        self.vision_button.pack_forget()
        self.update_frame_info()

    def create_vision_window(self):
        self.vision_window = tk.Tk()
        self.vision_canvas_width = 900
        self.vision_canvas_height = 900
        self.vision_canvas = Canvas(
            self.vision_window, width=self.vision_canvas_width, height=self.vision_canvas_height, bg=BOARD_COLOR_1)
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
        self.update_frame_info()

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

        self.model.visited[self.model.get_curr_pos().location[0]][self.model.get_curr_pos().location[1]] = True

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

    def clear_all_sprites(self):
        """
        Deletes all sprites from the canvas.  Used when transitioning between rooms.
        """
        self.canvas.delete("sprites")

    def update_frame_info(self):
        """
        Modifies the text in the bottom frame using information from Model.  Also updates game log.
        """
        exit_flag = self.model.get_curr_pos().is_exit

        pillar_str = ""
        # collate pillar information
        for pillar in self.model.pillars:
            if self.model.pillars[pillar]:
                pillar_str += f"{pillar} "
  
        # if none, say none.  Otherwise remove trailing space
        if pillar_str == "": pillar_str = "None"
        else: pillar_str = pillar_str[:-1]

        hud_data = {
            "Hit Points:" : self.model.player.hp,
            "Pillars" : pillar_str,
            "Health Potions" : self.model.player.health_potions,
            "Vision Potions" : self.model.player.vision_potions
        }

        info_fields = []
        for key, value in hud_data.items():
            if value == "":
                value = "None"
            info_fields.append(f"{key}: {value}")
        label_text = " | ".join(info_fields)

        if self.model.player_is_dead():
            label_text = "Y O U  D I E D !!!!!"
        elif exit_flag and self.model.player_has_all_pillars():
            label_text = "Y O U  W I N !!!!!"
            self.show_entire_map()

        self.info_label.destroy()
        self.info_label = Label(self.bottom_frame, text=label_text)
        self.info_label.pack(side=LEFT, padx=8, pady=5)

        # while we have the potion counts handy, let's check if the relevant buttons should be visible
        if hud_data["Health Potions"]:
            self.health_button.pack(side=RIGHT, padx=10)
        else:
            self.health_button.pack_forget()
        
        if hud_data["Vision Potions"]:
            self.vision_button.pack(side=RIGHT, padx=10)
        else:
            self.vision_button.pack_forget()


    ##################################
    #        CONTROL HANDLING        #
    ##################################

    def on_square_clicked(self, event):
        """
        Event handling for click event.  Resolves any object interactions in the clicked square and then moves the player to the square if no object remains there.
        """
        click_pos = self.click_event_to_alphanum(event)
        if click_pos is None:
            return

        # activate_square returns True or False depending on whether the square is empty after resolution
        item_resolved = self.controller.activate_square(click_pos)

        if item_resolved:
            # in the case of a room transition, modify player location
            if self.controller.check_for_room_transition():
                if "1" in click_pos:
                    click_pos = click_pos.replace("1", "7")
                elif "7" in click_pos:
                    click_pos = click_pos.replace("7", "1")
                elif "A" in click_pos:
                    click_pos = click_pos.replace("A", "G")
                elif "G" in click_pos:
                    click_pos = click_pos.replace("G", "A")

            # then redraw the room
            self.hero_sprite.redraw_at(click_pos)
            self.load_current_room()

        # finally, update frames
        self.update_frame_info()
        self.update_game_log()

    def click_event_to_alphanum(self, event):
        """
        Given a click event, returns the alphanumeric position that was clicked.  Returns None if the player clicked out of bounds.
        """
        col_size = row_size = SQUARE_SIZE
        clicked_column = event.x // col_size
        clicked_row = 6 - (event.y // row_size)

        if clicked_row not in range(7):
            return None
        if clicked_column not in range(7):
            return None

        return f"{X_AXIS_LABELS[clicked_column]}{Y_AXIS_LABELS[clicked_row]}"

    ##################################
    #        NEED REFACTORING
    ##################################

    def draw_vision_room(self, rm, col, row, type):
        vision_room_width = 0
        vision_room_height = 0
        canvas = ""
        grid_h = 0
        grid_w = 0
        vision_sq_dim = 100
        size = 0
        ROWS = 3
        COLS = 3
        WALL_WIDTH = 10
        door_dict = rm.door_value

        if type == "vision":
            vision_room_width = self.vision_canvas_width / 3
            vision_room_height = self.vision_canvas_height / 3
            canvas = self.vision_canvas
            size = 300

        if type == "map":
            entire_grid = self.model.dungeon.dungeon.maze
            grid_h = entire_grid.shape[0]
            grid_w = entire_grid.shape[1]
            size = int(.92 * (min(self.map_canvas_width/grid_w, self.map_canvas_height/grid_h)))
            vision_room_width = size
            vision_room_height = size
            canvas = self.map_canvas
            ROWS = grid_h
            COLS = grid_w
            vision_sq_dim = int(vision_room_width / 3)
            WALL_WIDTH = int(vision_sq_dim/10)

        vx = col * vision_room_width
        vy = row * vision_room_height

        vrs = []
        VISION_SQUARE = vision_sq_dim
        if rm.heal == "y":
            vrs.append([Sprite("healing_potion_y", canvas), 0, 0])
        if rm.heal == "g":
            vrs.append([Sprite("healing_potion_g", canvas), 0, 2 * VISION_SQUARE])
        if rm.vision == True:
            vrs.append([Sprite("vision_potion", canvas), 0, 1 * VISION_SQUARE])
        if rm.pillar == "a":
            vrs.append([Sprite("abstraction_pillar", canvas), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "e":
            vrs.append([Sprite("encapsulation_pillar", canvas), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "p":
            vrs.append([Sprite("polymorphism_pillar", canvas), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.pillar == "i":
            vrs.append([Sprite("inheritance_pillar", canvas), 2 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.monster == "Gremlin":
            vrs.append([Sprite("gremlin", canvas), 2 * VISION_SQUARE, 0])
        if rm.monster == "Ogre":
            vrs.append([Sprite("ogre", canvas), 2 * VISION_SQUARE, 0])
        if rm.monster == "Skeleton":
            vrs.append([Sprite("skeleton", canvas), 2 * VISION_SQUARE, 0])
        if rm.pit == True:
            vrs.append([Sprite("pit", canvas), 2 * VISION_SQUARE, 2 * VISION_SQUARE])
        if rm.is_entrance:
            vrs.append([Sprite("entrance", canvas), 0 * VISION_SQUARE, 1 * VISION_SQUARE])
        if rm.is_exit:
            vrs.append([Sprite("exit", canvas), 2 * VISION_SQUARE, 1 * VISION_SQUARE])

        orig_rm = self.model.get_curr_pos()

        vis = self.model.visited
        visited = False
        if vis[rm.location[0]][rm.location[1]]:
            visited = True

        if type == "map" and self.secret_view == True:
            # secret view, want to show location in maze so only show player sprite in current room
            if rm == orig_rm:
                vrs.append([self.hero_sprite, VISION_SQUARE, VISION_SQUARE])
        elif type == "map" and self.secret_view == False:
            # end of game view: want to show player sprite in all rooms visited
            if rm == orig_rm or visited == True:
                vrs.append([self.hero_sprite, VISION_SQUARE, VISION_SQUARE])
        else:
            # vision potion room, so only want to show player sprite in current location
            if rm == orig_rm:
                vrs.append([self.hero_sprite, VISION_SQUARE, VISION_SQUARE])

        for i in range(0, len(vrs)):
            # print(vrs[i][0], vrs[i][1], vrs[i][2], vx, vy, canvas)
            self.draw_vision_sprite(vrs[i][0], vrs[i][1], vrs[i][2], vx, vy, canvas, VISION_SQUARE)

        for key, value in door_dict.items():
            if key == "Up" and value == True:
                canvas.create_rectangle(vx, vy, vx + (vision_room_width/3), vy + WALL_WIDTH, fill="black")
                canvas.create_rectangle(vx + (2 * (vision_room_width/3)), vy, vx + vision_room_width,
                                                     vy + WALL_WIDTH, fill="black")
            if key == "Up" and value == False:
                canvas.create_rectangle(vx, vy, (vx + vision_room_width), vy + WALL_WIDTH, fill="black")
            if key == "Down" and value == True:
                canvas.create_rectangle(vx, vy + vision_room_height - WALL_WIDTH, vx + (vision_room_width/3),
                                             vy + vision_room_height, fill="black")
                canvas.create_rectangle(vx + (2 * (vision_room_width/3)), vy + vision_room_height - WALL_WIDTH,
                                             vx + vision_room_width, vy + vision_room_height, fill="black")
            if key == "Down" and value == False:
                canvas.create_rectangle(vx, vy + vision_room_height - WALL_WIDTH, vx + vision_room_width,
                                             vy + vision_room_height, fill="black")
            if key == "Left" and value == True:
                canvas.create_rectangle(vx, vy, vx + WALL_WIDTH, vy + (vision_room_height/3), fill="black")
                canvas.create_rectangle(vx, vy + (2 * (vision_room_height/3)), vx + WALL_WIDTH,
                                             vy + vision_room_height, fill="black")
            if key == "Left" and value == False:
                canvas.create_rectangle(vx, vy, vx + WALL_WIDTH, vy + vision_room_height, fill="black")
            if key == "Right" and value == True:
                canvas.create_rectangle(vx + vision_room_width - WALL_WIDTH, vy, vx + vision_room_width,
                                             vy + (vision_room_height/3), fill="black")
                canvas.create_rectangle(vx + vision_room_width - WALL_WIDTH, vy + (2 * (vision_room_height/3)),
                                             vx + vision_room_width, vy + vision_room_height, fill="black")
            if key == "Right" and value == False:
                canvas.create_rectangle(vx + vision_room_width - WALL_WIDTH, vy, vx + vision_room_height,
                                             vy + vision_room_height, fill="black")
            else:
                pass
            canvas.pack()

    def draw_vision_sprite(self, sprite, spr_start_x, spr_start_y, rm_start_x, rm_start_y, canvas, VISION_SQUARE):
        SPRITE_SIZE = (int(.9 * VISION_SQUARE), int(.9 * VISION_SQUARE))

        if isinstance(sprite, Sprite):
            WALL_CLEARANCE = int(VISION_SQUARE/10)
            filename = "sprites_image/{}.png".format(
                sprite.name)
            im = Image.open(filename)
            image = ImageOps.contain(im, SPRITE_SIZE)
            ph = ImageTk.PhotoImage(image, master=canvas)
            if spr_start_x == 0 or spr_start_y == 0:
                if spr_start_x == 0:
                    spr_start_x = spr_start_x + WALL_CLEARANCE
                if spr_start_y == 0:
                    # bordering top wall
                    spr_start_y = spr_start_y + WALL_CLEARANCE
            else:
                spr_start_x = spr_start_x - WALL_CLEARANCE
                spr_start_y = spr_start_y - WALL_CLEARANCE
            spr_start_x = spr_start_x + rm_start_x
            spr_start_y = spr_start_y + rm_start_y
            label = tk.Label(canvas, image=ph, bg=BOARD_COLOR_1)
            label.config(width=SPRITE_SIZE[0], height=SPRITE_SIZE[1])
            label.image = ph
            label.place(x=spr_start_x, y=spr_start_y)
            canvas.pack()

    def on_key_pressed(self, event):
        if event.char == "x":
            self.secret_view = True
            self.show_entire_map()
        else:
            self.secret_view = False

    def show_entire_map(self):
        self.create_map_window()
        entire_grid = self.controller.model.dungeon.dungeon.maze
        grid_h = entire_grid.shape[0]
        grid_w = entire_grid.shape[1]
        for r in range(0, grid_h):
            for c in range(0, grid_w):
                if entire_grid[r][c]:
                    self.draw_vision_room(entire_grid[r][c], c, r, "map")
                else:
                    pass

    def create_map_window(self):
        self.map_window = tk.Tk()
        self.map_canvas_width = self.map_window.winfo_screenwidth()
        self.map_canvas_height = self.map_window.winfo_screenheight()
        self.map_canvas = Canvas(
            self.map_window, width=self.map_canvas_width, height=self.map_canvas_height, bg=BOARD_COLOR_1)
        self.map_canvas.pack(padx=8, pady=8)
