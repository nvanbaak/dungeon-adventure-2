"""
"""
import model
import sprite


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

    def get_room_data(self):
        return self.model.get_curr_pos()

    def get_numeric_notation(self, rowcol):
        # print("C | calls get_numeric_notation via Sprite()")
        return sprite.get_numeric_notation(rowcol)

    def get_alphanumeric_position(self, rowcolumntuple):
        # print(f"C | calls get_alphanumeric_position({rowcolumntuple}) via Model")
        return self.model.get_alphanumeric_position(rowcolumntuple)

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)