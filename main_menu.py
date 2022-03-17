import tkinter as tk
from view import View
from controller import Controller

class MainMenu:
    """
    class representing the main menu of the game
    """
    def __init__(self, root) -> None:
        # references
        self.view = None

        # tk objects
        self.root = root
        self.canvas = None
        self.title_image = None
        self.hero_image = None
        self.hero_class = None
        self.hero_desc = None
        self.name_entry_label = None
        self.name_entry = None
        self.start_button_label = None

        # tk parameters
        self.canvas_width = 900
        self.canvas_height = 600

        # menu data
        self.char_list = ["warrior", "priestess", "thief"]
        self.current_hero = "warrior"
        self.char_title_dict = {
                "warrior" : "The Warrior",
                "priestess" : "The Priestess",
                "thief" : "The Thief"
        }
        self.char_description_dict = {
                "warrior" : "A master of arms, the Warrior attacks with a Crushing Blow to defeat his enemies.",
                "priestess" : "Wreathed in holy light, the Priestess heals from her wounds in combat.",
                "thief": "Mysterious as he is greedy, the Thief attacks multiple times in a flash of knives."
        }

        # init
        self.build_menu()

    ##################################
    #      TK WIDGET CONSTRUCTION    #
    ##################################

    def build_menu(self):
        """
        creates and diplays the start menu
        """

        # build base canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="#476E22")
        self.canvas.pack(expand=True)

        # place title graphic
        self.title_image = tk.PhotoImage(file="sprites_image/title_text.png")

        title_x = self.canvas_width // 2
        title_y = self.canvas_height // 4

        title_text = self.canvas.create_image(title_x, title_y, anchor=tk.CENTER, image=self.title_image)
            # although this reference isn't used, garbage
            # collection eats the image without it

        # create name entry field
        self.name_entry = tk.Entry(
                master=self.canvas,
                width=15,
                font="Optima 25",
                justify=tk.CENTER
                )
        self.name_entry.pack()

        name_entry_x = (self.canvas_width // 2)
        name_entry_y = (self.canvas_height // 5) * 4 - 31

        self.canvas.create_window(name_entry_x, name_entry_y, window=self.name_entry)

        # set up functional parts of menu
        self.create_start_menu_buttons()
        self.update_labels()
        self.update_hero_image()

    def create_start_menu_buttons(self):
        """
        Creates buttons and labels for start menu
        """
        def create_start_button():
            # start button
            start_button = tk.Button(
                    text="ENTER THE DUNGEON", 
                    font="Optima 10 bold", 
                    # width=7, 
                    height=2, 
                    command=self.init_new_game)

            start_x = (self.canvas_width // 5) * 4
            start_y = (self.canvas_height // 4) * 3 
            self.canvas.create_window(start_x, start_y, window=start_button)

            # label for start button
            self.start_button_label = tk.Label(
                    master=self.canvas,
                    text="Are you prepared?",
                    font="Optima 15",
                    anchor=tk.CENTER,
                    bg="#476E22",
                    fg="#F2F230"
            )

            start_label_y = (self.canvas_height // 9) * 5

            self.canvas.create_window(start_x, start_label_y, window=self.start_button_label)

        def create_hero_selection_buttons():
            # hero selection
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

            char_select_x = self.canvas_width // 4 - 20
            char_select_y = (self.canvas_height // 4) * 3 

            self.canvas.create_window(char_select_x - 25, char_select_y, window=prev_hero_btn)
            self.canvas.create_window(char_select_x + 25, char_select_y, window=next_hero_btn)

        create_start_button()
        create_hero_selection_buttons()

    def update_labels(self):
        """
        Sets the menu text according to which character is selected
        """
        def update_class_title():
            # place class title
            class_text = self.char_title_dict[self.current_hero]

            if self.hero_class:
                self.hero_class.destroy()
            self.hero_class = tk.Label(
                    master=self.root,
                    text=class_text,
                    font="Optima 20",
                    anchor=tk.CENTER,
                    bg="#476E22",
                    fg="#F2F230"
                    )
            self.hero_class.pack()

            class_x = self.canvas_width // 4 - 20
            class_y = (self.canvas_height // 2)

            self.canvas.create_window(class_x, class_y, window=self.hero_class)

        def update_class_description():
            # place class description
            class_desc = self.char_description_dict[self.current_hero]

            if self.hero_desc:
                self.hero_desc.destroy()
            self.hero_desc = tk.Label(
                master=self.root,
                text=class_desc,
                font="Optima 15",
                anchor=tk.CENTER,
                bg="#476E22",
                fg="#F2F230",
                wraplength=200
            )

            desc_x = self.canvas_width // 2 + 10
            desc_y = self.canvas_height // 2 + 20

            self.canvas.create_window(desc_x, desc_y, window=self.hero_desc)

        def update_name_entry_label():
            # label name entry field
            female = self.current_hero == "priestess"
            pronoun = "Her" if female else "His"
            entry_label = f"{pronoun} name is..."

            self.name_entry_label = tk.Label(
                master=self.root,
                text=entry_label,
                font="Optima 15",
                anchor=tk.CENTER,
                bg="#476E22",
                fg="#F2F230"
            )

            name_entry_x = self.canvas_width // 2 + 10
            name_entry_y = (self.canvas_height // 4) * 3 - 50

            self.canvas.create_window(name_entry_x, name_entry_y, window=self.name_entry_label)

        update_class_title()
        update_class_description()
        update_name_entry_label()

    def update_hero_image(self):
        """
        displays an image of the current hero on the menu
        """

        self.hero_image = tk.PhotoImage(file=f"sprites_image/{self.current_hero}.png")

        hero_x = self.canvas_width // 4 - 20
        hero_y = (self.canvas_height // 5) * 3

        self.canvas.create_image(hero_x, hero_y, anchor=tk.CENTER, image=self.hero_image)

        self.update_labels()


    ##################################
    #      BUTTON FUNCTIONALITY      #
    ##################################

    def next_hero(self):
        """
        advances char selection to the next hero and updatse the image
        """
        curr_index = self.char_list.index(self.current_hero)
        next_index = curr_index + 1
        if next_index >= 3:
            next_index = 0
        self.current_hero = self.char_list[next_index]

        self.update_hero_image()

    def prev_hero(self):
        """
        regresses char selection to the previous hero and updates the image
        """
        curr_index = self.char_list.index(self.current_hero)
        self.current_hero = self.char_list[curr_index - 1]

        self.update_hero_image()

    def init_new_game(self):
        """
        gets the selected class and user-supplied character name, then starts a new game using that information.
        If no name has been entered, the game does not start.
        """
        player_name = self.name_entry.get()
        if player_name == "":
            return

        # close the menu before opening the game window
        self.root.destroy()

        game_root = tk.Tk()
        game_root.title("Dungeon Adventure II: Dungeon Harder")
        View(self, game_root, self.current_hero, player_name)
        game_root.mainloop()