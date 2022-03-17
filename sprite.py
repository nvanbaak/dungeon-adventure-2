from configurations import *
import tkinter as tk
from PIL import Image, ImageTk


def create_sprite(sprite):
    # print(f"P | create_sprite | {sprite}")
    if isinstance(sprite, str):
        if sprite.upper() in SHORT_NAME.keys():
            sprite = SHORT_NAME[sprite.upper()]
        sprite = sprite.capitalize()
        if sprite in SHORT_NAME.values():
            # returns an object of type specified in variable 'sprite'
            return eval("{classname}()".format(classname=sprite))
    raise ValueError("invalid sprite name: '{}'".format(sprite))

def get_numeric_notation(rowcol):
    row, col = rowcol
    return int(col) - 1, X_AXIS_LABELS.index(row)


class Sprite():
    """
    Class that handles displaying the art asset for one game object
    """
    def __init__(self, name, canvas, position):
        self.name = name # should be identical to a filename in the images folder
        self.canvas : tk.Canvas = canvas
        self.visible = False
        self.image : tk.Image = None
        self.__mirror = False
        self.__x_pos, self.__y_pos = position

    @property
    def position(self):
        return (self.__x_pos, self.__y_pos)
    @position.setter
    def position(self, xy):
        self.__x_pos, self.__y_pos = xy

    @property
    def mirror(self):
        return self.__mirror
    @mirror.setter
    def mirror(self, value):
        if isinstance(value, bool):
            self.__mirror = value


    def draw(self):
        """
        Creates a PhotoImage object at the specified location on self.canvas.
        Retains a reference for later destruction.
        """
        image_file = Image.open(file=f"sprites_image/{self.name}.png")

        self.image = ImageTk.PhotoImage(file=image_file)

        if self.__mirror:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)

        self.canvas.create_image(self.__x_pos, self.__y_pos, image=self.image, anchor=tk.NW)

    def erase(self):
        """
        Destroys the image reference, removing it from the screen.
        """
        if self.image:
            self.image.destroy()

