from view import View
from controller import Controller

new_game = View()
control = Controller(new_game.get_root())
new_game.set_controller(control)
new_game.start_loop()