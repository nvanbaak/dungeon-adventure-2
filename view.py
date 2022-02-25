"""

"""

from tkinter import Tk, Menu, Label, Frame, Canvas, RIGHT, PhotoImage, messagebox
import controller
import exceptions
from configurations import *
import preferenceswindow


class View():

    # print("V | class variables initialized before __init__: images, piece position, board color")
    selected_piece_position = None
    images = {}
    board_color_1 = BOARD_COLOR_1

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.create_board_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.start_new_game()

    def create_board_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()

    def create_top_menu(self):
        self.menu_bar = Menu(self.parent)
        self.create_file_menu()
        self.create_edit_menu()
        self.create_about_menu()

    def create_bottom_frame(self):
        self.bottom_frame = Frame(self.parent, height=64)
        self.info_label = Label(
            self.bottom_frame, text="   In-Game Instructions Here  ")
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")

    def on_about_menu_clicked(self):
        messagebox.showinfo("By:",
                            "Shoby, Nik, and Tos")

    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label="New Game", command=self.on_new_game_menu_clicked)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def create_edit_menu(self):
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(
            label="Preferences", command=self.on_preference_menu_clicked)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.parent.config(menu=self.menu_bar)

    def create_about_menu(self):
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(
            label="About", command=self.on_about_menu_clicked)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)

    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(
            self.parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def draw_board(self):
        current_color = BOARD_COLOR_1
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLUMNS):
                x1, y1 = self.get_x_y_coordinate(row, col)
                x2, y2 = x1 + DIMENSION_OF_EACH_SQUARE, y1 + DIMENSION_OF_EACH_SQUARE
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=current_color, outline="")

    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        position_of_click = self.controller.get_alphanumeric_position(
            (clicked_row, clicked_column))
        # print(f"V | on_square_clicked | curr pos: {self.selected_piece_position} | clicked: {position_of_click}")
        self.shift(self.selected_piece_position, position_of_click)
        self.selected_piece_position = position_of_click
        self.draw_board()
        self.draw_all_pieces()

    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = 6 - (event.y // row_size)
        return (clicked_row, clicked_column)

    def get_x_y_coordinate(self, row, col):
        x = (col * DIMENSION_OF_EACH_SQUARE)
        y = ((6 - row) * DIMENSION_OF_EACH_SQUARE)
        return (x, y)

    def calculate_piece_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        y0 = ((6 - row) * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        # print(f"V | calculate_piece_coordinates | return {x0}, {y0}")
        return (x0, y0)

    def draw_single_piece(self, position, piece):
        # print(f"V | draw_single_piece | position: {position} | piece {piece}")
        # print(f"V | call get_numeric_notation(position) via Controller")
        x, y = self.controller.get_numeric_notation(position)
        if piece:
            filename = "pieces_image/{}.png".format(
                piece.name.lower())
            if filename not in self.images:
                self.images[filename] = PhotoImage(file=filename)
                img_max = max(self.images[filename].width(), self.images[filename].height())
                img_adj = int(1/(64/img_max))
                self.images[filename] = self.images[filename].subsample(img_adj)
            x0, y0 = self.calculate_piece_coordinate(x, y)
            self.canvas.create_image(x0, y0, image=self.images[
                                     filename], tags=("occupied"), anchor="c")
            # print(f"FIX THIS")
            if piece.name == "warrior":
                self.selected_piece_position = position


    def draw_all_pieces(self):
        self.canvas.delete("occupied")
        # print("V | draw_all_pieces | gets position/pieces from controller.get_all_pieces_on_board()")
        # print("V | draw_all_pieces | then passes each position/piece to draw_single_piece()")
        for position, piece in self.controller.get_all_peices_on_board():
            self.draw_single_piece(position, piece)

    def start_new_game(self):
        # print("V | start_new_game | calls controller.reset_game_data()")
        self.controller.reset_game_data()
        # print("V | start_new_game | calls controller.reset_default_characters()()")
        self.controller.reset_default_characters()
        # print("V | start_new_game | calls draw_all_pieces()")
        self.draw_all_pieces()
        self.info_label.config(text="   In-Game status/instructions here  ")

    def reload_colors(self, color_1):
        self.board_color_1 = color_1
        self.draw_board()
        self.draw_all_pieces()

    def on_preference_menu_clicked(self):
        self.show_preferences_window()
#
    def show_preferences_window(self):
        preferenceswindow.PreferencesWindow(self)

    def on_new_game_menu_clicked(self):
        self.start_new_game()

    def shift(self, start_pos, end_pos):
        try:
            self.controller.pre_move_validation(start_pos, end_pos)
        except exceptions.ChessError as error:
            self.info_label["text"] = error.__class__.__name__

    def update_label(self, piece, start_pos, end_pos):
        pass


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
