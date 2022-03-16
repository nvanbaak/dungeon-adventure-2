import tkinter as tk
from view import View
from controller import Controller

class MainMenu:
    """
    class representing the main menu of the game
    """
    def __init__(self, root) -> None:
        self.view = None
        self.canvas = None
        self.current_hero = "warrior"
        self.char_list = ["warrior", "priestess", "thief"]

        # tk variables
        self.root = root
        self.canvas = None
        self.title_image = None
        self.hero_image = None

        self.canvas_width = 900
        self.canvas_height = 600

        self.start_menu()

    def start_menu(self):
        """
        creates and diplays the start menu
        """
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="#476E22")
        self.canvas.pack(expand=True)

        self.title_image = tk.PhotoImage(file="sprites_image/title_text.png")

        title_x = self.canvas_width // 2
        title_y = self.canvas_height // 4

        title_text = self.canvas.create_image(title_x, title_y, anchor=tk.CENTER, image=self.title_image)

        self.create_start_menu_buttons()
        self.update_hero_image()


    def update_hero_image(self):
        """
        displays an image of the current hero on the menu
        """

        if self.hero_image:
            self.hero_image.destroy()
        self.hero_image = tk.PhotoImage(file=f"sprites_image/{self.current_hero}.png")

        hero_x = self.canvas_width // 4
        hero_y = (self.canvas_height // 5) * 3

        self.canvas.create_image(hero_x, hero_y, anchor=tk.CENTER, image=self.hero_image)

    def create_start_menu_buttons(self):
        """
        Creates buttons and labels for start menu
        """
        start_button = tk.Button(
                text="ENTER", 
                font="Optima 10 bold", 
                width=7, 
                height=2, 
                command=self.click_button)
        
        start_x = (self.canvas_width // 5) * 4
        start_y = (self.canvas_height // 4) * 3 
        self.canvas.create_window(start_x, start_y, window=start_button)

        next_hero_btn = tk.Button(
                text="►",
                font="Optima 10 bold",
                width=4,
                height=2,
                command=self.next_hero
        )

        prev_hero_btn = tk.Button(
                text="◄",
                font="Optima 10 bold",
                width=4,
                height=2,
                command=self.prev_hero
        )

        char_select_x = self.canvas_width // 4
        char_select_y = (self.canvas_height // 4) * 3 

        self.canvas.create_window(char_select_x - 25, char_select_y, window=prev_hero_btn)
        self.canvas.create_window(char_select_x + 25, char_select_y, window=next_hero_btn)


    def next_hero(self):
        """
        advances char selection to the next hero and updatse the image
        """
        pass

    def prev_hero(self):
        """
        regresses char selection to the previous hero and updates the image
        """
        pass


    def click_button(self):
        """
        dummy method
        """
        print("YOU DID IT!  YOU CLICKED THE BUTTON!")

    def init_new_game(self):
        root = tk.Tk()
        root.title("Dungeon Adventure II: Dungeon Harder")
        View(root, Controller())
        root.mainloop()