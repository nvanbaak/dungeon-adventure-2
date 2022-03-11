# name  : Shoby Gnanasekaran
# net id: shoby

from model import Model
import pickle
import os

class SaveGame:
    def __init__(self):
        self.__saved_games = []

    def __add_to_saved_games(self, name):
        try:
            name = str(name)
            if not self.check_in_saved_games(name):
                self.__saved_games.append(name)
            else:
                raise ValueError("Game name already exist")
        except TypeError:
            raise TypeError(f"cannot save the game with {name} name")

    def __remove_from_saved_games(self, name):
        if self.check_in_saved_games(name):
            self.__saved_games.remove(name)

    save_game_name = property(fset = __add_to_saved_games)

    def check_in_saved_games(self,name):
        if name in self.__saved_games:
            return True
        else:
            return False

    def __get_saved_games(self):
        return self.__saved_games

    saved_games = property(__get_saved_games)

    def save_game(self, name , model):
        """ creates the pickle files for the list of game objects passed"""
        if not self.check_in_saved_games(name) and isinstance(model, Model):
            self.save_game_name = str(name)
            to_pickle = model
            with open(f'{name}.pkl', 'wb') as file:
                pickle.dump(to_pickle, file)

        else:
            raise ValueError(f"{name} already in use, please try a different name")

    def load_game(self,name):
        """ return the de-serialised list of game objects"""
        if self.check_in_saved_games(name):
            with open(f'{name}.pkl', 'rb') as file:
                return pickle.load(file)

        else:
            raise ValueError(f"{name} not saved to load")

    def delete_saved_game(self, name):
        if self.check_in_saved_games(name):
            os.remove(f'{name}.pkl')
            self.__remove_from_saved_games(name)

        else:
            raise ValueError(f"{name} not saved to delete")
