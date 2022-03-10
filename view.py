from tkinter import Tk, Menu, Button, Label, Frame, Canvas, FLAT, SW, W, E, RIGHT, PhotoImage, messagebox
import simpleaudio
from PIL import Image, ImageTk, ImageOps
import controller
from configurations import *
import exceptions
from pydub import AudioSegment
from pydub.playback import play
from pydub.playback import _play_with_simpleaudio
import threading
from tkinter import messagebox
import sys
import time
import preferenceswindow
# from game_observer import Publisher, Subscriber

class View():

    sprite_position = None
    images = {}
    board_color_1 = BOARD_COLOR_1
    sprite_xy = (0, 0)
    sprite_mirror = False
    sound_effect_play_count = 0
    vision = False
    music_on = True
    play_obj = ""

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.canvas_width = 0
        self.canvas_height = 0
        self.create_board_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        # self.subscriber_v = Subscriber(self)
        self.start_new_game()

    def create_board_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_room()
        self.create_bottom_frame()
        self.create_vision_button()

    def create_top_menu(self):
        self.menu_bar = Menu(self.parent)
        self.create_file_menu()
        self.create_edit_menu()


    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label="New Game", command=self.on_new_game_menu_clicked)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def create_edit_menu(self):
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(
            label="Background Color", command=self.on_preference_menu_clicked)
        self.edit_menu.add_command(
            label="Sound", command=self.toggle_bkg_music)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.parent.config(menu=self.menu_bar)

    def toggle_bkg_music(self):
        if self.music_on == False:
            self.music_on = True
            start_music_2(True)
        else:
            self.music_on = False
            start_music_2(False)

    def on_preference_menu_clicked(self):
        self.show_preferences_window()

    def show_preferences_window(self):
        preferenceswindow.PreferencesWindow(self)

    def on_new_game_menu_clicked(self):
        self.parent.destroy()
        init_new_game()

    def reload_colors(self, color_1):
        self.board_color_1 = color_1
        self.draw_room()
        self.canvas.config(bg=self.board_color_1)
        self.canvas.pack()
        self.draw_all_sprites()

    def create_canvas(self):
        self.canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        self.canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(
            self.parent, width=self.canvas_width, height=self.canvas_height, bg=self.board_color_1)
        self.canvas.pack(padx=8, pady=8)

    def create_vision_window(self):
        self.vision_window = Tk()
        self.vision_canvas_width = 1.5 * self.canvas_width
        self.vision_canvas_height = 1.5 * self.canvas_height
        self.vision_canvas = Canvas(
            self.vision_window, width=self.vision_canvas_width, height=self.vision_canvas_height, bg=self.board_color_1)
        self.vision_canvas.pack(padx=8, pady=8)

    def create_bottom_frame(self):
        self.bottom_frame = Frame(self.parent, height=64)
        self.info_label = Label(
            self.bottom_frame, text="")
        self.info_label.pack(side="left", padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")

    def create_vision_button(self):
        self.vision_button = Button(self.bottom_frame, text="Use Vision", command=self.use_vision)
        self.vision_button.configure(activebackground="#33B5E5")
        self.vision_button.pack()
        if self.vision == False:
            self.vision_button.pack_forget()

    def draw_room(self):
        WALL_WIDTH = 25
        rm = self.controller.get_room_data()
        door_dict = rm.door_value
        for key, value in door_dict.items():
            if key == "Up" and value == True:
                self.canvas.create_rectangle(0, 0, self.canvas_width/3, WALL_WIDTH, fill="black")
                self.canvas.create_rectangle((2 * self.canvas_width)/3, 0, self.canvas_width, WALL_WIDTH, fill="black")
            elif key == "Up" and value == False:
                self.canvas.create_rectangle(0, 0, self.canvas_width, 25, fill="black")
            if key == "Down" and value == True:
                self.canvas.create_rectangle(0, self.canvas_height - WALL_WIDTH, self.canvas_width/3, self.canvas_height, fill="black")
                self.canvas.create_rectangle((2 * self.canvas_width)/3, self.canvas_height - WALL_WIDTH, self.canvas_width, self.canvas_height, fill="black")
            elif key == "Down" and value == False:
                self.canvas.create_rectangle(0, self.canvas_height - WALL_WIDTH, self.canvas_width, self.canvas_height, fill="black")
            if key == "Left" and value == True:
                self.canvas.create_rectangle(0, 0, WALL_WIDTH, self.canvas_height/3, fill="black")
                self.canvas.create_rectangle(0, (2 * self.canvas_height)/3, WALL_WIDTH, self.canvas_height, fill="black")
            elif key == "Left" and value == False:
                self.canvas.create_rectangle(0, 0, WALL_WIDTH, self.canvas_height, fill="black")
            if key == "Right" and value == True:
                self.canvas.create_rectangle(self.canvas_width - WALL_WIDTH, 0, self.canvas_width, self.canvas_height/3, fill="black")
                self.canvas.create_rectangle(self.canvas_width - WALL_WIDTH, (2 * self.canvas_height)/3, self.canvas_width, self.canvas_height, fill="black")
            elif key == "Right" and value == False:
                self.canvas.create_rectangle(self.canvas_width - WALL_WIDTH, 0, self.canvas_height, self.canvas_height, fill="black")
            else:
                pass
            self.canvas.pack()
        self.controller.load_initial_points()
        rm_contents = rm.room_contents
        rm_loc = rm.location
        # print(f"{rm_loc} {rm_contents}")

    def start_new_game(self):
        # print("V | start_new_game | calls controller.reset_default_characters()()")
        self.controller.reset_default_characters()
        self.send_view_reference_to_controller()
        # print("V | start_new_game | calls draw_all_sprites()")
        self.draw_all_sprites()
        self.update_score_label()
        # self.info_label.config(text="")

    def send_view_reference_to_controller(self):
        self.controller.accept_view_reference(self)

    def doorway_refresh(self, hero_dict, clicked):
        sprite = hero_dict[self.sprite_position]
        doors = ["C1", "D1", "E1", "C7", "D7", "E7", "G3", "G4", "G5", "A3", "A4", "A5"]
        if sprite.name == "warrior" and self.sprite_position in doors:
            for al_nu in doors:
                if self.sprite_position == al_nu:
                    self.on_square_clicked_manual(False)

    def draw_all_sprites(self):
        for position, sprite in self.controller.get_all_peices_on_board():
            self.draw_single_sprite(position, sprite)
        for position, sprite in self.controller.get_hero_dict():
            self.draw_single_sprite(position, sprite)

    def draw_single_sprite(self, position, sprite):
        # print(f"V | draw_single_sprite | position: {position} | sprite {sprite}")
        # print(f"V | call get_numeric_notation(position) via Controller")
        UNDER_64 = (64, 64)
        EXTRA_LARGE = (256, 256)
        x, y = self.controller.get_numeric_notation(position)
        if sprite:
            filename = "sprites_image/{}.png".format(
                sprite.name.lower())
            image = Image.open(filename)
            w, h = image.size
            if sprite.name == "pit":
                image = ImageOps.contain(image, EXTRA_LARGE)
            else:
                image = ImageOps.contain(image, UNDER_64)

            if self.sprite_mirror == True and sprite.name == "warrior":
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            self.images[filename] = ImageTk.PhotoImage(image)

            x0, y0 = self.calculate_sprite_coordinate(x, y)
            ci = self.canvas.create_image(x0, y0, image=self.images[
                                     filename], anchor="c")
            if sprite.name == "warrior":
                sprite.visible = True
            if sprite.visible == False:
                self.canvas.itemconfig(ci, state="hidden")
            else:
                self.canvas.itemconfig(ci, state="normal")
            # print(f"ADD OTHER HERO TYPES")
            if sprite.name == "warrior":
                self.sprite_position = position
                self.sprite_xy = (x0, y0)
        self.update_score_label()

    def calculate_sprite_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        y0 = ((6 - row) * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        # print(f"V | calculate_sprite_coordinates | return {x0}, {y0}")
        return (x0, y0)

    def on_square_clicked_manual(self, clicked):
        rm = self.controller.get_room_data()
        door_dict = rm.door_value
        str = ""
        # self.update_label("")
        rm_contents = rm.room_contents
        items = rm_contents.items()
        self.hide_all_sprites()

        model_dict = self.controller.get_dict()
        hero_dict = self.controller.get_hero()

        sprite_obj = hero_dict[self.sprite_position]

        if clicked == True:
            if self.sprite_position == "G5" or self.sprite_position == "G4" or self.sprite_position == "G3":
                if door_dict["Right"] == True:
                    self.controller.move_right()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("G", "A")
                    hero_dict[self.sprite_position] = sprite_obj
                    self.controller.gather()
                    self.sound_effect_play_count = 0
            elif self.sprite_position == "C1" or self.sprite_position == "D1" or self.sprite_position =="E1":
                if door_dict["Down"] == True:
                    self.controller.move_down()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("1", "7")
                    hero_dict[self.sprite_position] = sprite_obj
                    self.controller.gather()
                    self.sound_effect_play_count = 0
            elif self.sprite_position == "A5" or self.sprite_position == "A4" or self.sprite_position == "A3":
                if door_dict["Left"] == True:
                    self.controller.move_left()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("A", "G")
                    hero_dict[self.sprite_position] = sprite_obj
                    self.controller.gather()
                    self.sound_effect_play_count = 0
            elif self.sprite_position == "C7" or self.sprite_position == "D7" or self.sprite_position == "E7":
                if door_dict["Up"] == True:
                    self.controller.move_upper()
                    del hero_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("7", "1")
                    hero_dict[self.sprite_position] = sprite_obj
                    self.controller.gather()
                    self.sound_effect_play_count = 0
            else:
                pass

        self.canvas.delete("all")
        self.controller.refresh_room()
        self.draw_room()
        self.draw_all_sprites()
        self.sound_effect_play_count = self.sound_effect_play_count + 1
        if self.sound_effect_play_count == 1:
            self.controller.gather_sounds()
        # self.controller.dispatch()
        if clicked == True:
            self.doorway_refresh(hero_dict, clicked)

    def on_square_clicked(self, event):
        clicked = True
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        xy = self.get_clicked_xy(event)
        position_of_click = self.controller.get_alphanumeric_position(
            (clicked_row, clicked_column))
        self.shift(self.sprite_position, position_of_click)
        self.sprite_position = position_of_click
        if self.sprite_xy[0] < xy[0]:
            self.sprite_mirror = False
        else:
            self.sprite_mirror = True

        self.on_square_clicked_manual(clicked)

    def hide_all_sprites(self):

        model_dict = self.controller.get_dict()

        for position, value in model_dict.items():
            if value.name == "warrior":
                pass
            else:
                s_obj = model_dict[position]
                s_obj.visible = False

    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = 6 - (event.y // row_size)
        return (clicked_row, clicked_column)

    def get_row_column(self, x, y):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        xcol = x // col_size
        xrow = y // row_size
        return (xrow, xcol)

    def get_clicked_xy(self, event):
        x = event.x
        y = event.y
        return (x, y)

    def shift(self, start_pos, end_pos):
        try:
            self.controller.pre_move_validation(start_pos, end_pos)
        except exceptions.NameError as error:
            self.info_label["text"] = error.__class__.__name__

    def update_score_label(self):
        stat_dict = self.controller.get_game_stats()
        lbl_txt = ""
        for key, value in stat_dict.items():
            lbl_txt = lbl_txt + str(key) + ": " + str(value) + " | "
        self.info_label["text"] = lbl_txt

    def use_vision(self):
        self.controller.use_vision()
        self.create_vision_window()

    def ask_new_game(self):
        self.parent.quit()
        res = messagebox.askyesno("Yes|No", "Would you like to play again?")
        if res == True:
            self.parent.destroy()
            time.sleep(5)
            init_new_game()
        else:
            self.parent.destroy()
            sys.exit()


def main(ctl):
    # print("V | main(ctl) | passed Controller object")
    # print("V | main(ctl) | create new Tk object as root")
    root = Tk()
    root.title("Dungeon Adventure II")
    # print("V | main(ctl) | create new View object with root & ctl as parameters")
    View(root, ctl)
    # print("V | main(ctl) | last step of View init is start_game() | last step of main is root.mainloop()")
    # ctl.setup_observer()
    root.mainloop()

def init_new_game():
    # print("V | init_new_game() | call init of controller object from View, save as initial_game_data")
    initial_game_data = controller.Controller()
    # print("V | init new_game() | pass initial_game_data to main()")
    # print("V _ View now has enough initial game data to draw game screen")
    # print("V _ though View object has still not been initialized. need tk root created first")
    # start_music(initial_game_data, True)
    start_music_2(True)
    main(initial_game_data)

def start_music(ctrl, tf):
    sound = AudioSegment.from_wav('audio/cyberpunk.wav')
    quieter_song = sound - 4
    ctrl.thread = threading.Thread(target=play, args=(quieter_song,))
    ctrl.thread.daemon = tf
    ctrl.thread.start()

def start_music_2(tf):
    # song = AudioSegment.from_wav('audio/cyberpunk.wav')
    # playback = _play_with_simpleaudio(song)
    # if tf == False:
    #     playback.stop()
    wav_obj = simpleaudio.WaveObject.from_wave_file('audio/cyberpunk.wav')
    play_obj = wav_obj.play()

    if tf == False:
        play_obj.stop()

if __name__ == "__main__":
    init_new_game()
