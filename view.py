from tkinter import Tk, Menu, Label, Frame, Canvas, RIGHT, PhotoImage, messagebox
from PIL import Image, ImageTk, ImageOps
import controller
from configurations import *
import exceptions
import random

class View():

    sprite_position = None
    images = {}
    board_color_1 = BOARD_COLOR_1
    sprite_xy = (0, 0)
    sprite_mirror = False

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.canvas_width = 0
        self.canvas_height = 0
        self.create_board_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.start_new_game()

    def create_board_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_room()
        self.create_bottom_frame()

    def create_top_menu(self):
        self.menu_bar = Menu(self.parent)

    def create_canvas(self):
        self.canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        self.canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(
            self.parent, width=self.canvas_width, height=self.canvas_height, bg="#800040")
        self.canvas.pack(padx=8, pady=8)

    def create_bottom_frame(self):
        self.bottom_frame = Frame(self.parent, height=64)
        self.info_label = Label(
            self.bottom_frame, text="   In-Game Instructions Here  ")
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")

    def draw_room(self):
        WALL_WIDTH = 25
        rm = self.controller.get_room_data()
        door_dict = rm.get_doors()
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
        rm_contents = rm.get_contents()
        rm_loc = rm.get_location()
        print(f"{rm_loc} {rm_contents}")

    def start_new_game(self):
        # print("V | start_new_game | calls controller.reset_default_characters()()")
        self.controller.reset_default_characters()
        # print("V | start_new_game | calls draw_all_sprites()")
        self.draw_all_sprites()
        self.info_label.config(text="   In-Game status/instructions here  ")

    def doorway_refresh(self, model_dict, clicked):
        sprite = model_dict[self.sprite_position]
        doors = ["C1", "D1", "E1", "C7", "D7", "E7", "G3", "G4", "G5", "A3", "A4", "A5"]
        new = ""
        if sprite.name == "warrior" and self.sprite_position in doors:
            for al_nu in doors:
                if self.sprite_position == al_nu:
                    # if al_nu[1] == "1":
                    #     new = al_nu[0] + "2"
                    # if al_nu[1] == "7":
                    #     new = al_nu[0] + "6"
                    # if al_nu[0] == "G":
                    #     new = "F" + al_nu[1]
                    # if al_nu[0] == "A":
                    #     new = "B" + al_nu[1]
                    # del model_dict[self.sprite_position]
                    # self.sprite_position = new
                    # model_dict[self.sprite_position] = sprite
                    self.on_square_clicked_manual(self.sprite_position, False)

    def draw_all_sprites(self):
        for position, sprite in self.controller.get_all_peices_on_board():
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

    def calculate_sprite_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        y0 = ((6 - row) * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        # print(f"V | calculate_sprite_coordinates | return {x0}, {y0}")
        return (x0, y0)

    # def Convert(self, a):
    #     it = iter(a)
    #     res_dct = dict(zip(it, it))
    #     return res_dct

    def on_square_clicked_manual(self, position, clicked):
        rm = self.controller.get_room_data()
        door_dict = rm.get_doors()
        str = ""
        self.update_label("")
        rm_contents = rm.get_contents()
        items = rm_contents.items()
        self.hide_all_sprites()
        for k, v in items:
            if k == "pit" and v == True:
                self.draw_pit()
                str += " PIT "
            elif k == "pillar":
                if v == "p":
                    self.draw_pillar("polymorphism_pillar")
                    str += " POLYMORPHISM_PILLAR "
                if v == "e":
                    self.draw_pillar("encapsulation_pillar")
                    str += " ENCAPSULATION_PILLAR "
                if v == "a":
                    self.draw_pillar("abstraction_pillar")
                    str += " ABSTRACTION_PILLAR "
                if v == "i":
                    self.draw_pillar("inheritance_pillar")
                    str += " INHERITANCE_PILLAR "
            elif k == "monster" and v == "Gremlin":
                str += " MONSTER "
            elif k == "vision_potion" and v == True:
                str += " VISION_POTION "
            elif k == "healing_potion" and v == "g" or k == "healing_potion" and v == "y":
                str += " HEALING_POTION "
            else:
                pass

        self.update_label(str)

        self.canvas.pack()

        model_dict = self.controller.get_dict()

        sprite_obj = model_dict[self.sprite_position]

        if clicked == True:
            if self.sprite_position == "G5" or self.sprite_position == "G4" or self.sprite_position == "G3":
                if door_dict["Right"] == True:
                    self.controller.move_right()
                    del model_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("G", "A")
                    model_dict[self.sprite_position] = sprite_obj
            elif self.sprite_position == "C1" or self.sprite_position == "D1" or self.sprite_position =="E1":
                if door_dict["Down"] == True:
                    self.controller.move_down()
                    del model_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("1", "7")
                    model_dict[self.sprite_position] = sprite_obj
            elif self.sprite_position == "A5" or self.sprite_position == "A4" or self.sprite_position == "A3":
                if door_dict["Left"] == True:
                    self.controller.move_left()
                    del model_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("A", "G")
                    model_dict[self.sprite_position] = sprite_obj
            elif self.sprite_position == "C7" or self.sprite_position == "D7" or self.sprite_position == "E7":
                if door_dict["Up"] == True:
                    self.controller.move_upper()
                    del model_dict[self.sprite_position]
                    self.sprite_position = self.sprite_position.replace("7", "1")
                    model_dict[self.sprite_position] = sprite_obj
            else:
                pass

        self.canvas.delete("all")
        self.draw_room()
        self.draw_all_sprites()
        if clicked == True:
            self.doorway_refresh(model_dict, clicked)

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

        self.on_square_clicked_manual(self.sprite_position, clicked)

    def hide_all_sprites(self):

        model_dict = self.controller.get_dict()

        for position, value in model_dict.items():
            if value.name == "warrior":
                pass
            else:
                s_obj = model_dict[position]
                s_obj.visible = False


    def draw_pillar(self, pillr):

        model_dict = self.controller.get_dict()

        for position, value in model_dict.items():
            s_obj = model_dict[position]
            if s_obj.name == pillr:
                s_obj.visible = True

    def draw_pit(self):

        model_dict = self.controller.get_dict()

        for position, value in model_dict.items():
            s_obj = model_dict[position]
            if s_obj.name == "pit":
                s_obj.visible = True

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

    def update_label(self, txt):
        self.info_label["text"] = txt

def main(ctl):
    # print("V | main(ctl) | passed Controller object")
    # print("V | main(ctl) | create new Tk object as root")
    root = Tk()
    root.title("Dungeon Adventure II")
    # print("V | main(ctl) | create new View object with root & model as parameters")
    View(root, ctl)
    # print("V | main(ctl) | last step of View init is start_game() | last step of main is root.mainloop()")
    root.mainloop()

def init_new_game():
    # print("V | init_new_game() | call init of controller object from View, save as initial_game_data")
    initial_game_data = controller.Controller()
    # print("V | init new_game() | pass initial_game_data to main()")
    # print("V _ View now has enough initial game data to draw game screen")
    # print("V _ though View object has still not been initialized. need tk root created first")
    main(initial_game_data)


if __name__ == "__main__":
    init_new_game()
