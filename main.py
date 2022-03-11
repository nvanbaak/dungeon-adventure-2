from view import View
from controller import Controller
import tkinter as Tk


root = Tk()
root.title("Dungeon Adventure II: Dungeon Harder")
View(root, Controller())
root.mainloop()