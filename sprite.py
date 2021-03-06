from configurations import *
import tkinter as tk
from PIL import Image, ImageTk, ImageOps

class Sprite():
    """
    Class that handles displaying the art asset for one game object
    params:
    :name: a string corresponding to a .png file in the images folder
    :canvas: a reference to the game canvas, used to draw the sprite
    :position: an alphanumeric code used to determine where to draw the sprite
    """
    def __init__(self, name, canvas, position=None, pos_x=0, pos_y=0):
        self.__name = name 

        # tk references
        self.canvas : tk.Canvas = canvas
        self.image : Image = None
        self.image_id = None

        # display parameters
        self.__mirror = False
        if position:
            self.__x_pos, self.__y_pos = self.parse_position_code(position)
        if pos_x:
            self.__x_pos = pos_x
        if pos_y:
            self.__y_pos = pos_y


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

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

    def parse_position_code(self, position):
        """
        Expects a board location code (e.g. "D3") and translates to coordinates tkinter can use
        """
        row, col = position

        # convert from 1-indexed to 0-indexed
        col = 7 - int(col)
        col = col * SQUARE_SIZE
        col += SQUARE_SIZE//2

        # cheap hack to convert A-G to 0-6
        row = X_AXIS_LABELS.index(row)
        row = row * SQUARE_SIZE
        row += SQUARE_SIZE//2

        return row, col

    def redraw_at(self, alphanum, invert=False):
        """
        Given an alphanumeric position code, deletes this image and redraws at the specified location
        """
        self.erase()

        # get new position
        new_x, new_y = self.parse_position_code(alphanum)

        # check if we need to flip the sprite
        self.__mirror = self.__x_pos > new_x

        # set new position and draw
        self.__x_pos = new_x
        self.__y_pos = new_y
        self.draw()

    def draw(self):
        """
        Creates a PhotoImage object at the specified location on self.canvas.
        Retains a reference for later destruction.
        """

        # create and process image object
        image_file = Image.open(f"sprites_image/{self.name}.png")

        if self.__mirror:
            image_file = image_file.transpose(Image.FLIP_LEFT_RIGHT)

        dimensions = (64, 64) if self.name != "pit" else (256, 256)
        image_obj = ImageOps.contain(image_file, dimensions)

        self.image = ImageTk.PhotoImage(image=image_obj)



        # draw sprite
        self.image_id = self.canvas.create_image(self.__x_pos, self.__y_pos, image=self.image, anchor=tk.CENTER, tags=f"sprites")

    def erase(self):
        """
        Deletes the image from the canvas
        """
        if self.image:
            self.canvas.delete(self.image_id)

