import tkinter as tk
from view import View
from controller import Controller

class MainMenu:
    """
    class representing the main menu of the game
    """
    def __init__(self) -> None:
        self.view = None
        self.canvas = None
        self.char_select = "warrior"
        self.char_list = ["warrior", "priestess", "thief"]
        
        # tk variables
        self.root = None
        self.canvas = None
        self.title_image = None

        self.canvas_width = 900
        self.canvas_height = 600

    def init_tk(self):
        """
        Sets up the basic tk window and launches it with main menu
        """
        self.root = tk.Tk()
        self.root.title("Dungeon Adventure II: Dungeon Harder")
        self.root.mainloop()
        self.start_menu()

    def start_menu(self):
        """
        creates and diplays the start menu
        """
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="#476E22")
        self.canvas.pack(expand=True)

        self.title_image = tk.PhotoImage(file="title_text.png")

        title_x = self.canvas_width // 2
        title_y = self.canvas_height // 4

        title_text = self.canvas.create_image(title_x, title_y, anchor=tk.CENTER, image=self.title_image)

    def init_new_game(self):
        root = tk.Tk()
        root.title("Dungeon Adventure II: Dungeon Harder")
        View(root, Controller())
        root.mainloop()