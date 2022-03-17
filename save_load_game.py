# name  : Shoby Gnanasekaran
# net id: shoby

import pickle
from dungeonchar_db_access import DungeonCharDb
import os

class SaveGame:

    def save_game(self,name, model):
        """ validates if another game is saved with the same name,
        if not makes a temp pickle file of the model, converts it to binary and saves the name and game_file to
        save_game table of dungeondb.db. Deletes the temp pickle file
        :param name string
        :param model Model"""

        db = DungeonCharDb()
        validate = db.load_game(name)
        if validate is None:
            to_pickle = model
            with open(f'{name}.pkl', 'wb') as file:
                pickle.dump(to_pickle, file)
            pickle_binary_file = self.__convert_to_binary_data(f'{name}.pkl')
            os.remove(f'{name}.pkl')
            db.save_game(name,pickle_binary_file)

        else:
            raise ValueError(f"{name} already exist")

    @staticmethod
    def __convert_to_binary_data(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    @staticmethod
    def __write_to_file(blob_data, name):
        # Convert binary data to proper format and write it the pickle file
        with open(f'{name}.pkl', 'wb') as file:
            file.write(blob_data[0])

    def load_game(self, name):
        """ Loads the binary file saved in name. Converts to temp pickle file, loads the model object,
        deletes the pickle file, returns the model object"""

        db = DungeonCharDb()
        binary_pickle_file = db.load_game(name)
        if binary_pickle_file is not None:
            self.__write_to_file(binary_pickle_file, name)
            with open(f'{name}.pkl', 'rb') as file:
                model = pickle.load(file)
            os.remove(f'{name}.pkl')
            return model

        else:
            raise ValueError(f"{name} not found")

    @staticmethod
    def delete_single_game(name):
        db = DungeonCharDb()
        db.delete_single_game(name)

    @staticmethod
    def delete_all_saved_games():
        db = DungeonCharDb()
        db.delete_all_saved_games()

    @staticmethod
    def game_name_generator():
        """generates a name for saving a game"""
        db = DungeonCharDb()
        existing_saved_games = db.select_column_from_table("saved_games", "name")
        count = 1
        for i in existing_saved_games:
            value = int(i[0][-1])
            if count == value:
                count +=1
            else:
                return f"Game{count}"

        return f"Game{count}"

    @staticmethod

    def saved_games_list():
        """ returns the list of saved games list"""
        db = DungeonCharDb()
        saved_games =[]
        existing_saved_games = db.select_column_from_table("saved_games", "name")
        for i in existing_saved_games:
            saved_games.append(i[0])

        return saved_games




