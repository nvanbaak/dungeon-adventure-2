import model
import sprite


class Controller:

    def __init__(self):
        # print("C | __init__ | Controller init calls init of Model")
        self.model = model.Model()

    def get_room_data(self):
        return self.model.get_curr_pos()

    def get_left_room(self):
        return self.model.move_left()

    def get_right_room(self):
        return self.model.move_right()

    def get_upper_room(self):
        return self.model.move_up()

    def get_down_room(self):
        return self.model.move_down()

    def reset_default_characters(self):
        # print("C | calls model.reset_default_characters() via Controller")
        self.model.reset_default_characters()

    def get_all_peices_on_board(self):
        return self.model.dict.items()

    def get_alphanumeric_position(self, rowcolumntuple):
        # print(f"C | calls get_alphanumeric_position({rowcolumntuple}) via Model")
        return self.model.get_alphanumeric_position(rowcolumntuple)

    def get_numeric_notation(self, rowcol):
        # print("C | calls get_numeric_notation via Sprite()")
        return sprite.get_numeric_notation(rowcol)

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)

    def update_dict(self, dict):
        self.model.update_dict(dict)

    def get_dict(self):
        return self.model.get_dict()