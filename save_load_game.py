# name  : Shoby Gnanasekaran
# net id: shoby


from dungeon import Dungeon
from hero import Hero
import pickle

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

    save_game_name = property(fset = __add_to_saved_games)

    def check_in_saved_games(self,name):
        if name in self.__saved_games:
            return True
        else:
            return False

    def __get_saved_games(self):
        return self.__saved_games

    def save_game(self, name , dungeon_list, floor_num, location, hero):
        """ creates the pickle files for the list of game objects passed"""
        to_pickle_object_list = self.__create_objects_list(name , dungeon_list, floor_num, location, hero)
        with open(f'{name}.pkl', 'wb') as file:
            pickle.dump(to_pickle_object_list, file)

    def __create_objects_list(self,name , dungeon_list, floor_num, location, hero):
        """ validates the input parameters, adds it to the game_objects list and returns the game_objects list
        :param name str
        :param dungeon_list list of Dungeon objects
        :param floor_num int
        :param location list
        :param hero Hero
        :return list of game_objects
        """

        if not self.check_in_saved_games(name): # name should not be an already saved games' name
            self.__add_to_saved_games = name

        game_objects = []
        i = 0
        while i < len(dungeon_list):
            if isinstance(dungeon_list[i], Dungeon):
                continue
            else:
                raise TypeError("should be a Dungeon object")
        game_objects.append(dungeon_list)
        if isinstance(floor_num, int) and floor_num < len(dungeon_list):
            game_objects.append(floor_num)

        if 0 <= location[0] < dungeon_list[floor_num].row_Count and 0 <= location[1] < dungeon_list[
            floor_num].col_Count:
            game_objects.append(location)

        if isinstance(hero, Hero):
            game_objects.append(hero)

        return game_objects

    def load_game(self,name):
        """ return the de-serialised list of game objects"""
        if self.check_in_saved_games(name):
            file = open(f'{name}.pkl', 'rb')
            return pickle.load(file)


