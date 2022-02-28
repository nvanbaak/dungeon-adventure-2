"""
"""

from configurations import *
import sys
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

    def __init__(self, visible=False):
        self.name = self.__class__.__name__.lower()
        self.visible = False

    def keep_reference(self, model):
        self.model = model


class Priestess(Sprite):
    pass

class Thief(Sprite):
    pass


class Warrior(Sprite):
    pass


class Ogre(Sprite):
    pass


class Gremlin(Sprite):
    pass


class Skeleton(Sprite):
    pass