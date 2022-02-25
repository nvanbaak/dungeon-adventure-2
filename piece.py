"""
"""

from configurations import *
import sys
import exceptions


def create_piece(piece, visible=False):
    # print(f"P | create_piece | {piece}")
    if isinstance(piece, str):
        if piece.upper() in SHORT_NAME.keys():
            color = ""
            piece = SHORT_NAME[piece.upper()]
        piece = piece.capitalize()
        if piece in SHORT_NAME.values():
            return eval("{classname}(color)".format(classname=piece))
    raise exceptions.ChessError("invalid piece name: '{}'".format(piece))

def get_numeric_notation(rowcol):
    row, col = rowcol
    return int(col) - 1, X_AXIS_LABELS.index(row)


class Piece():

    def __init__(self, visible):
        self.name = self.__class__.__name__.lower()
        self.visible = visible

    def keep_reference(self, model):
        self.model = model

    def moves_available(self, current_position, directions, distance):
        pass
        model = self.model
        allowed_moves = []
        piece = self
        start_row, start_column = get_numeric_notation(current_position)
        for x, y in directions:
            collision = False
            for step in range(1, distance + 1):
                if collision:
                    break
                destination = start_row + step * x, start_column + step * y
                if self.possible_position(destination) not in model.all_occupied_positions():
                    allowed_moves.append(destination)
                else:
                    allowed_moves.append(destination)
                    collision = True
        allowed_moves = filter(model.is_on_board, allowed_moves)
        return map(model.get_alphanumeric_position, allowed_moves)

    def possible_position(self, destination):
        return self.model.get_alphanumeric_position(destination)


class Priestess(Piece):

    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 1

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Thief(Piece):

    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Warrior(Piece):

    directions = ORTHOGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Ogre(Piece):

    directions = DIAGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Gremlin(Piece):

    def moves_available(self, current_position):
        model = self.model
        allowed_moves = []
        start_col, start_row = get_numeric_notation(current_position)
        piece = model.get(current_position.upper())
        for x, y in KNIGHT_POSITIONS:
            destination = start_col + x, start_row + y
            if model.get_alphanumeric_position(destination) not in model.all_positions_occupied_by_color(piece.color):
                allowed_moves.append(destination)
        allowed_moves = filter(model.is_on_board, allowed_moves)
        return map(model.get_alphanumeric_position, allowed_moves)


class Skeleton(Piece):

    directions = DIAGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)
