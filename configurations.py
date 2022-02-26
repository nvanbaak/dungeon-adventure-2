"""
Code illustration: 4.07
    
@ Tkinter GUI Application Development Blueprints
"""
from configparser import ConfigParser

NUMBER_OF_ROWS = 7
NUMBER_OF_COLUMNS = 7
DIMENSION_OF_EACH_SQUARE = 64
X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7)

START_PIECES_POSITION = {
    "D4": "w", "A1": "p", "A7": "t", "G1": "o", "G4": "g", "G7": "s"
}


SHORT_NAME = {'W': 'Warrior',  'P': 'Priestess',  'T': 'Thief',  'O': 'Ogre',
              'G': 'Gremlin',  'S': 'Skeleton'}


ORTHOGONAL_POSITIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIAGONAL_POSITIONS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
KNIGHT_POSITIONS = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                    (1, -2), (1, 2), (2, -1), (2, 1))


'''
User Modifiable Options
'''
config = ConfigParser()
config.read('options.ini')
BOARD_COLOR_1 = config.get('colors', 'board_color_1', fallback="#e6a803")
# BOARD_COLOR_2 = config.get('chess_colors', 'board_color_2', fallback="#8b8350")
# HIGHLIGHT_COLOR = config.get(
#     'chess_colors', 'highlight_color', fallback="#2EF70D")
