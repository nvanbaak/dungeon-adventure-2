import tkinter as tk
from controller import Controller

class View:
    """
    Class governing GUI behavior and function
    """
    def __init__(self) -> None:
        self.__controller = None

        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__x_midpoint = self.__window_size[0]//2
        self.__y_midpoint = self.__window_size[1]//2
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Dungeon Adventure")

    def display_main_menu(self):
        """
        Constructs the main menu on a canvas
        """
        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.configure(bg="#476E23")

        start_button = tk.Button(text='ENTER AT YOUR OWN RISK', font="Georgia 10 bold", width=20, height=4)
        self.__canvas.create_window(self.__x_midpoint, self.__y_midpoint, window=start_button)
        start_button.config(command=self.__controller.start_game)

        self.__canvas.pack()

    def start_loop(self):
        """
        function run at the beginning of the program to start the main loop
        """
        self.display_main_menu()
        self.__root.mainloop()

    ##################################
    #       Getters / Setters
    ##################################

    def get_root(self):
        return self.__root

    def set_controller(self, controller):
        """
        stores a reference to a Controller object
        """
        self.__controller = controller

    def update_dungeon_state(self, dungeon_state):
        """
        Passed a string representing the state of the dungeon, updates the GUI accordingly
        """
        self.__dungeon_state = dungeon_state
        self.dungeon_canvas.change_text(dungeon_state)
