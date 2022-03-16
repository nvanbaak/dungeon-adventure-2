"""
re-added
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import *
from configparser import ConfigParser
import configurations


class PreferencesWindow():

    def __init__(self, view):
        self.root = view.root
        self.fill_preference_colors()
        self.view = view
        self.create_preferences_window()

    def fill_preference_colors(self):
        self.board_color_1 = configurations.BOARD_COLOR

    def set_color_1(self):
        self.board_color_1 = askcolor(initialcolor=self.board_color_1)[-1]

    def create_preferences_window(self):
        self.pref_window = Toplevel(self.root)
        self.pref_window.title("set preferences")
        self.create_preferences_list()
        self.pref_window.transient(self.root)

    def create_preferences_list(self):
        Label(self.pref_window, text="Board Color 1").grid(
            row=1, sticky=W, padx=5, pady=5)
        self.board_color_1_button = Button(
            self.pref_window, text='Select Board Color 1', command=self.set_color_1)
        self.board_color_1_button.grid(
            row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)
        Button(self.pref_window, text="Save", command=self.on_save_button_clicked).grid(
            row=4, column=2, sticky=E, padx=5, pady=5)
        Button(self.pref_window, text="Cancel", command=self.on_cancel_button_clicked).grid(
            row=4, column=1, sticky=E, padx=5, pady=5)

    def on_save_button_clicked(self):
        self.set_new_values()
        self.pref_window.destroy()
        self.view.reload_colors(
            self.board_color_1)

    def set_new_values(self):
        config = ConfigParser()
        config.read('options.ini')
        config.set('colors', 'board_color_1', self.board_color_1)
        configurations.BOARD_COLOR_1 = self.board_color_1
        with open('options.ini', 'w') as config_file:
            config.write(config_file)

    def on_cancel_button_clicked(self):
        self.pref_window.destroy()
