from tkinter import Menu
import tkinter as tk
import save_load_game
from configurations import BOARD_COLOR
from preferenceswindow import PreferencesWindow

class TopMenu:
    """
    class that handles the top menu functionality for the GUI
    """
    def __init__(self, view, root) -> None:
        self.root = root
        self.view = view
        self.menu_bar = Menu(self.root)
        self.create_file_menu()
        self.create_edit_menu()

    ##################################
    #     FILE MENU FUNCTIONALITY    #
    ##################################

    def create_file_menu(self):
        """
        Creates and assigns buttons for File menu
        """
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(
            label="New Game", command=self.on_new_game_menu_clicked)
        file_menu.add_command(
            label="Save Game", command=self.on_save_game_menu_clicked)
        file_menu.add_command(
            label="Load Game", command=self.on_load_game_menu_clicked)
        file_menu.add_command(
            label="Delete All Saved Games", command=self.on_delete_games_menu_clicked)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=self.menu_bar)

    def on_new_game_menu_clicked(self):
        """
        Destroys the entire window for some reason and then starts a new instance of the application
        """
        self.view.start_new_game()

    def on_save_game_menu_clicked(self):
        """
        Creates a window with save options
        """
        saveload_window = tk.Tk()
        saveload_canvas_width = 100
        saveload_canvas_height = 40
        saveload_canvas = tk.Canvas(
            saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=BOARD_COLOR)
        saveload_label = tk.Label(saveload_canvas)
        sg = save_load_game.SaveGame()
        game_name = sg.game_name_generator()
        sg.save_game(game_name, self.view.controller.get_model())
        lbltxt = f"{game_name} successfully saved!"
        saveload_label.config(text = lbltxt)
        saveload_label.pack()
        saveload_canvas.pack(padx=8, pady=8)

    def on_load_game_menu_clicked(self):
        """
        creates a window with the option to load a game
        """
        saveload_window = tk.Tk()
        saveload_canvas_width = 50
        saveload_canvas_height = 50
        saveload_canvas = tk.Canvas(
            saveload_window, width=saveload_canvas_width, height=saveload_canvas_height, bg=BOARD_COLOR)
        saveload_label = tk.Label(saveload_canvas, text= "Select saved game")
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
            game_data = sg.load_game(sg, selected_game)
            self.view.load_from_saved_game(game_data)

    def on_delete_games_menu_clicked(self):
        sg = save_load_game.SaveGame()
        sg.delete_all_saved_games()

    ##################################
    #     EDIT MENU FUNCTIONALITY    #
    ##################################

    def create_edit_menu(self):
        """
        Creates and assigns options for Edit menu
        """
        edit_menu = Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(
            label="Preferences", command=self.on_preference_menu_clicked)
        edit_menu.add_command(
            label="Sound", command=self.view.music_player.toggle_music)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=self.menu_bar)

    def on_preference_menu_clicked(self):
        """
        Launches a window to change game preferences
        """
        PreferencesWindow(self)