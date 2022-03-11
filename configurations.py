"""
"""
from configparser import ConfigParser

NUMBER_OF_ROWS = 7
NUMBER_OF_COLUMNS = 7
DIMENSION_OF_EACH_SQUARE = 64
X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7)

HERO_SPRITE = "w"
HERO_POSITION = "D4"

START_SPRITES_POSITION = {
    "D4": "pt", "F6": "pp", "B2": "ap", "F2": "ep", "B6": "ip", "A1": "p", "G1": "t", "C3": "o", "F3": "g", "C5": "s",
    "D2": "hy", "D6": "hg", "F4": "v"
}

SHORT_NAME = {'W': 'Warrior',  'P': 'Priestess',  'T': 'Thief',  'O': 'Ogre', 'G': 'Gremlin',  'S': 'Skeleton',
              'AP': 'Abstraction_pillar', 'EP': 'Encapsulation_pillar', 'IP': 'Inheritance_pillar',
              'PP': 'Polymorphism_pillar', 'PT': 'Pit', 'HY': 'Healing_potion_y', 'HG': 'Healing_potion_g',
              'V': 'Vision_potion'}

'''
User Modifiable Options
'''
config = ConfigParser()
config.read('options.ini')
BOARD_COLOR_1 = config.get('colors', 'board_color_1', fallback="#e6a803")
