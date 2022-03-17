from configurations import *
import tkinter as tk
import exceptions


def create_sprite(sprite):
    # print(f"P | create_sprite | {sprite}")
    if isinstance(sprite, str):
        if sprite.upper() in SHORT_NAME.keys():
            sprite = SHORT_NAME[sprite.upper()]
        sprite = sprite.capitalize()
        if sprite in SHORT_NAME.values():
            # returns an object of type specified in variable 'sprite'
            return eval("{classname}()".format(classname=sprite))
    raise exceptions.NameError("invalid sprite name: '{}'".format(sprite))

def get_numeric_notation(rowcol):
    row, col = rowcol
    return int(col) - 1, X_AXIS_LABELS.index(row)


class Sprite():
    """
    Class that handles displaying the art asset for one game object
    """
    def __init__(self, name, canvas):
        self.name = name # should be identical to a filename in the images folder
        self.canvas : tk.Canvas = canvas
        self.visible = False
        self.image = None

    def draw(self, x_pos, y_pos):
        """
        Creates a PhotoImage object at the specified location on self.canvas.
        Retains a reference for later destruction.
        """
        self.image = tk.PhotoImage(file=f"sprites_image/{self.name}.png")
        self.canvas.create_image(x_pos, y_pos, image=self.image, anchor=tk.NW)

    def erase(self):
        """
        Destroys the image reference, removing it from the screen.
        """
        if self.image:
            self.image.destroy()

