"""
"""
from configparser import ConfigParser

NUMBER_OF_ROWS = 7
NUMBER_OF_COLUMNS = 7
DIMENSION_OF_EACH_SQUARE = 64
X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7)

START_SPRITES_POSITION = {
    "D4": "w", "A1": "p", "A7": "t", "G1": "o", "G4": "g", "G7": "s"
}

# START_SPRITES_POSITION = {
#     "w": "D4", "p": "A1", "t": "A7", "o": "G1", "g": "G4", "s": "G7"
# }


SHORT_NAME = {'W': 'Warrior',  'P': 'Priestess',  'T': 'Thief',  'O': 'Ogre',
              'G': 'Gremlin',  'S': 'Skeleton'}

'''
User Modifiable Options
'''
config = ConfigParser()
config.read('options.ini')
BOARD_COLOR_1 = config.get('colors', 'board_color_1', fallback="#e6a803")
