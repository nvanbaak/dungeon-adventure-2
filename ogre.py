# name  : Shoby Gnanasekaran
# net id: shoby

from monster import Monster


class Ogre(Monster):
    """ Ogre is a monster with it own statistics. The behaviour is same as the monsters"""
    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)




