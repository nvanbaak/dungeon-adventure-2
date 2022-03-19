"""
"""
from configparser import ConfigParser

ROW_COUNT = 7
COL_COUNT = 7
SQUARE_SIZE = 64
X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7)

WALL_WIDTH = 25

HERO_POSITION = "D4"

START_SPRITES_POSITION = {
    "D4": "pit",
    "F6": "polymorphism_pillar",
    "B2": "abstraction_pillar",
    "F2": "encapsulation_pillar",
    "B6": "inheritance_pillar",
    "C3": "ogre",
    "F3": "gremlin",
    "C5": "skeleton",
    "D2": "healing_potion_y",
    "D6": "healing_potion_g",
    "F4": "vision_potion",
    "A1": "entrance",
    "A6": "exit"
}

SHORT_NAME = {'W': 'Warrior',  'P': 'Priestess',  'T': 'Thief',  'O': 'Ogre', 'G': 'Gremlin',  'S': 'Skeleton',
              'AP': 'Abstraction_pillar', 'EP': 'Encapsulation_pillar', 'IP': 'Inheritance_pillar',
              'PP': 'Polymorphism_pillar', 'PT': 'Pit', 'HY': 'Healing_potion_y', 'HG': 'Healing_potion_g',
              'V': 'Vision_potion', 'E': 'Entrance', 'EX': 'Exit'}




'''
User Modifiable Options
'''
config = ConfigParser()
config.read('options.ini')
BOARD_COLOR_1 = config.get('colors', 'board_color_1', fallback="#476E22")