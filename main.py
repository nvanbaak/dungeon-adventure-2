from view import View
from controller import Controller

new_game = View()
new_game.start_loop()
control = Controller(new_game.get_root())