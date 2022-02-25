"""
Code illustration: 4.07

@ Tkinter GUI Application Development Blueprints
"""
import model
import piece


class Controller():

    def __init__(self):
        # print("C | __init__ | Controller init calls init of Model")
        self.init_model()

    def init_model(self):
        self.model = model.Model()
        # print("C | init_model() | Controller stores reference to Model as self.model")

    def get_all_peices_on_board(self):
        return self.model.dict.items()

    def reset_game_data(self):
        # print("C | calls model.reset_game_data() via Controller")
        self.model.reset_game_data()

    def reset_default_characters(self):
        # print("C | calls model.reset_default_characters() via Controller")
        self.model.reset_default_characters()

    def get_numeric_notation(self, rowcol):
        # print("C | calls get_numeric_notation via Piece()")
        return piece.get_numeric_notation(rowcol)

    def get_alphanumeric_position(self, rowcolumntuple):
        # print(f"C | calls get_alphanumeric_position({rowcolumntuple}) via Model")
        return self.model.get_alphanumeric_position(rowcolumntuple)

    # def get_piece_at(self, position_of_click):
    #     # print("C | calls get_piece_at() via Model")
    #     return self.model.get_piece_at(position_of_click)

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)
