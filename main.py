import tkinter as tk
from main_menu import MainMenu
from view import View
from controller import Controller


root = tk.Tk()
root.title("Dungeon Adventure II: Dungeon Harder")
menu = MainMenu(root)
root.mainloop()

# game_root = tk.Tk()
# game_root.title("Dungeon Adventure II: Dungeon Harder")
# View("self", game_root, Controller("priestess"))
# game_root.mainloop()