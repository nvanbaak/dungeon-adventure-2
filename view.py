import tkinter as tk

class View:
    """
    Class governing GUI behavior and function
    """
    def __init__(self) -> None:
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Dungeon Adventure")

        # self.controller = Controller()
    
    def start_loop(self):
        """
        function run at the beginning of the program to start the main loop
        """
        self.__root.mainloop()

    def get_canvas(self):
        return self.__root