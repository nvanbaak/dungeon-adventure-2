
# name  : Shoby Gnanasekaran
# net id: shoby

import numpy as np
from maze_generator import Maze
from room import Room
from monster_factory import MonsterFactory

class Dungeon:
    """
    The Dungeon is built on an array of rooms that has reference to other rooms.
    The enter_dungeon() takes the player to the entrance of the Dungeon.
    We can see the live location of the player in the Dungeon using print_dungeon_live_location() method.
    The __str__ gives the string representation of the whole Dungeon

    Each room is connected to 4 adjacent rooms through pointers
    """

    def __init__(self, row_count=-1, col_count=-1, entrance =False, entrance_row_value = -1, entrance_col_value = -1 ):
        self.__set_rowCount(row_count)  # sets the number of rows of rooms of Dungeon
        self.__set_colCount(col_count)  # sets the number of columns of rooms of Dungeon
        self.__maze = Maze(self.__rowCount, self.__colCount)  # creates a maze object
        if not entrance:
            self.__create_maze_random_entrance()
        else:
            self.__create_maze_specified_entrance(entrance_row_value, entrance_col_value)
        self._setting_doors()  # updates the __door dictionary of Room
        self.__dungeon_str = ""
        self.__dungeon_str = self.__set_dungeon_str()  # creates the string representation of the Dungeon

    def print_initial_map(self):
        """ string representation of the initial dungeon, when the player starts a new game
        :return string"""
        return str(self.__dungeon_str)

    def __str__(self):
        """
        returns the string representation of the Dungeon
        :return: string
        """
        return str(self.__set_dungeon_str())

    def __create_maze_specified_entrance(self,entrance_row_value, entrance_col_value):
        """generates random maze with the specified entrance room"""
        if 0 <= entrance_row_value < self.__rowCount and 0<= entrance_col_value < self.__colCount:
            try:
                self.__maze.create_maze_specified_entrance(entrance_row_value, entrance_col_value)

            except RecursionError:
                self.__maze.create_maze_specified_entrance(entrance_row_value, entrance_col_value)

    def __create_maze_random_entrance(self):
        """generates random maze with random entrance room"""
        try:
            self.__maze.create_maze_random_entrance()  # creates a playable maze(array) of Rooms
        except RecursionError:
            self.__maze.create_maze_random_entrance()

    def __set_rowCount(self, row_count):
        """
        validates if the row_count passed is an integer and assigns it to __rowcount
        :param row_count:
        """
        if isinstance(row_count, int) and row_count > 0:
            self.__rowCount = row_count
        else:
            raise ValueError("number of rows:" + row_count + "is not an integer greater than 0")

    def _get_rowCount(self):
        return self.__rowCount

    row_Count = property(_get_rowCount)  # used for test purposes

    def __set_colCount(self, col_count):
        """
        validates if the col_count passed is an integer and assigns it to __col_count
        :param col_count:
        """
        if isinstance(col_count, int) and col_count > 0:
            self.__colCount = col_count
        else:
            raise ValueError("number of rows:" + col_count + "is not an integer greater than 0")

    def _get_colCount(self):
        return self.__colCount

    col_Count = property(_get_colCount)  # used for test purposes

    def _get_maze(self):
        """ Returns the entire dungeon"""
        return self.__maze

    dungeon = property(_get_maze)  # Property to get maze

    def _setting_doors(self):
        # method is made protected(not private) to create mock dungeon for testing purposes
        """" updates the __door dictionary of the Room
        all door are marked false for an impassable room
        for any other room, if it has an impassable room adjacent to it, the corresponding door is marked false"""
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                # the doors of an impassable room are already set to False by the maze generator
                # setting the doors only for the non impassable rooms
                if not self.__maze.maze[row, col].is_impassable:
                    if self.__maze.maze[row, col].upper_room is not None and not self.__maze.maze[row, col].upper_room.is_impassable :  # upper room is not impassable
                        upper_room = True
                    else:  # upper room is impassable
                        upper_room = False
                    if self.__maze.maze[row, col].down_room is not None and not self.__maze.maze[row, col].down_room.is_impassable:  # down room is not impassable
                        down_room = True
                    else:  # down room is impassable
                        down_room = False
                    if self.__maze.maze[row, col].right_room is not None and not self.__maze.maze[row, col].right_room.is_impassable:  # right room is not impassable
                        right_room = True
                    else:  # right room is impassable
                        right_room = False
                    if self.__maze.maze[row, col].left_room is not None and not self.__maze.maze[row, col].left_room.is_impassable:  # left room is not impassable
                        left_room = True
                    else:  # left room is impassable
                        left_room = False
                    # setting the __door dictionary of the Room object
                    self.__maze.maze[row, col].set_door(upper_room, down_room, left_room, right_room)

    def enter_dungeon(self):
        """Takes to entrance room of the dungeon"""
        row, col = self.__maze.winning_path[0]
        return self.__maze.maze[row, col]

    def re_enter_dungeon(self, room_obj):
        """ Takes to the room in the specified location
        :param room_obj Room
        :return Room object """
        if isinstance(room_obj, Room):
            current_location = room_obj.location
            row, col = current_location[0], current_location[1]
            return self.__maze.maze[row, col]

    def update_monsters_to_room(self, model):
        """ if the monster string is placed during maze_generation, creates respective monster objects to the room """
        for i in range (self.row_Count):
            for j in range (self.col_Count):
                if self.dungeon.maze[i, j].monster == "Ogre":
                    self.dungeon.maze[i, j].monster_obj = MonsterFactory.create_ogre("ogre", model)
                if self.dungeon.maze[i, j].monster == "Gremlin":
                    self.dungeon.maze[i, j].monster_obj = MonsterFactory.create_gremlin("gremlin", model)
                if self.dungeon.maze[i, j].monster == "Skeleton":
                    self.dungeon.maze[i, j].monster_obj = MonsterFactory.create_skeleton("skeleton", model)

    def __set_dungeon_str(self):
        """creates a string representation of the Dungeon  """
        dungeon_str =""
        for i in range(0, self.__rowCount):
            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the up door representation of each room in the ith row is appended to the self.__dungeon_str
                dungeon_str += self.__maze.maze[i, j].print_up()

            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the room contents of each room in the ith row is appended to the self.__dungeon_str
                dungeon_str += self.__maze.maze[i, j].print_room_contents()
            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the down door representation of each room in the ith row is appended to the self.__dungeon_str
                dungeon_str += self.__maze.maze[i, j].print_down()
        return dungeon_str

    def print_dungeon_live_location(self, room_obj):
        """creates a string representation of the Dungeon with the current room marked as +here+  """
        dungeon_str = ""  # self.dungeon_str is used for testing
        current_location = room_obj.location
        for i in range(0, self.__rowCount):
            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                dungeon_str += self.__maze.maze[i, j].print_up()
            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                if i == current_location[0] and j == current_location[1]:  # current room
                    dungeon_str += str(self.__maze.maze[i, j].vision_current_room())
                else:
                    # the room contents of each room in the ith row is appended to the dungeon_str
                    dungeon_str += self.__maze.maze[i, j].print_room_contents()
            dungeon_str += "\n"
            for j in range(0, self.__colCount):
                dungeon_str += self.__maze.maze[i, j].print_down()
        dungeon_str += "\n"+"+here+ is your current room"
        return dungeon_str

    def vision_potion_rooms(self, room_obj):
        """return the adjacent rooms of the input room_obj
        :param room_obj type Room
        :return 3*3 array of Rooms """

        vision_rooms = np.zeros((3,3), Room)
        room_location = room_obj.location
        x, y = room_location[0], room_location[1]
        row = 0
        for i in [x - 1, x, x + 1]:
            col = 0

            for j in [y - 1, y, y + 1]:
                if 0 <= i < self.__rowCount and 0 <= j < self.__colCount:
                    vision_rooms[row, col] = self.__maze.maze[i, j]
                    col +=1
                else:
                    vision_rooms[row, col] = None
                    col += 1
            row +=1
        return vision_rooms

    def use_vision_potion(self, room_obj):
        """
        prints 8 adjacent rooms of the room_obj passed with the room_obj room in the middle
        when for_test is passed True, vision_str is returned.
        :param room_obj: Room
        """
        vision_str = ""
        room_location = room_obj.location
        x , y = room_location[0], room_location[1]
        for i in [x-1, x, x+1]:
            vision_str += "\n"
            if 0 <= i < self.__rowCount:
                for j in [y-1, y, y+1]:
                    if 0 <= j < self.__colCount:
                        # the up door representation of each room in the ith row is appended to the vision_str
                        vision_str += str(self.__maze.maze[i, j].print_up())
                    else:
                        vision_str += "               "

                vision_str += "\n"
                for j in [y-1, y, y+1]:
                    # the room contents of each room in the ith row is appended to the vision_str
                    if 0 <= j < self.__colCount:
                        if i == x and j == y:
                            vision_str += str(self.__maze.maze[i, j].vision_current_room())
                        else:
                            vision_str += str(self.__maze.maze[i, j].print_room_contents())
                    else:
                        vision_str += "               "
                vision_str += "\n"
                for j in [y-1, y, y+1]:
                    if 0 <= j < self.__colCount:
                        vision_str += str(self.__maze.maze[i, j].print_down())
                    else:
                        vision_str += "               "
        return vision_str

    @staticmethod
    def clear_healing_pillar_vision(room_obj):
        """
        clears the healing potion, vision potion and pillars of the Room
        :param room_obj: type - Room

        """
        if isinstance(room_obj, Room):
            if room_obj.vision:
                room_obj.vision = False  # sets the vision_potion to False in the room_content dictionary of the Room
            if room_obj.pillar is not None:
                room_obj.pillar = None  # sets the pillar to None in the room_content dictionary of the Room
            if room_obj.heal is not None:
                room_obj.heal = None   # sets the healing_potion to None in the room_content dictionary of the Room

