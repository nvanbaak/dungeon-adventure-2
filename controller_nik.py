from dungeon import Dungeon

class Controller:
    """
    Class that governs player controls
    """
    def __init__(self, root):
        self.__root = root
        self.__model = None

    def get_model(self, model):
        self.__model = model

    def bind_keys(self):
        # self.__canvas.keybind(whatever)

        # if they press g they instantly die
        # self.__root.bind("<g>", self.__model.dungeon.kill_player)
        pass

    def start_game(self):
        """
        Initializes a dungeon and player character
        """
        # self__model = Dungeon(3, 3)
        print("HEY LOOK A DUNGEON")