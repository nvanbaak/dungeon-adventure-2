
# name  : Shoby Gnanasekaran
# net id: shoby

from maze_generator import Maze
from room import Room


class Dungeon:
    """
    The Dungeon is built on an array of rooms that has reference to other rooms.
    The enter_dungeon() takes the player to the entrance of the Dungeon.
    We can see the live location of the player in the Dungeon using print_dungeon_live_location() method.
    The __str__ gives the string representation of the whole Dungeon

    Each room is connected to 4 adjacent rooms through pointers
     The down_room of a room on the last row is linked to the room on the first row on the same column
     The upper_room of a room on the first row is linked to the room on the last row on the same column
     The left_room of a room on the first column is linked to the room on the last column on the same row
     The right_room of a room on the last column is linked to the room on the first column on the same row

    """

    def __init__(self, row_count=-1, col_count=-1):
        self.__set_rowCount(row_count)  # sets the number of rows of rooms of Dungeon
        self.__set_colCount(col_count)  # sets the number of columns of rooms of Dungeon
        self.__maze = Maze(self.__rowCount, self.__colCount)  # creates a maze object
        self.__create_maze()
        # self.__create_room_links()  # creates pointers between each rooms
        self._setting_doors()  # updates the __door dictionary of Room
        self.__dungeon_str = ""
        self.__set_dungeon_str()  # creates the string representation of the Dungeon

    def __str__(self):
        """
        returns the the string representation of the Dungeon
        :return: string
        """
        return str(self.__dungeon_str)

    def __create_maze(self):
        try:
            self.__maze.create_maze()  # creates a playable maze(array) of Rooms
        except RecursionError:
            self.__maze.create_maze()
            # raise ValueError("maze is not traversable, try again")

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

    # def __create_room_links(self):
    #     """creates pointers between each rooms"""
    #     for row in range(0, self.__rowCount):
    #         for col in range(0, self.__colCount):
    #             self._valid_movements(row, col)

    # def _valid_movements(self, row, col):
    #     # method is made protected(not private) to create mock dungeon for testing purposes
    #     """ validates and assigns links to down_room,upper_room,right_room and left_room
    #     the down_room of a room on the last row is linked to the room on the first row on the same column
    #     the upper_room of a room on the first row is linked to the room on the last row on the same column
    #     the left_room of a room on the first column is linked to the room on the last column on the same row
    #     the right_room of a room on the last column is linked to the room on the first column on the same row
    #     """
    #
    #     if 0 <= row + 1 < self.__rowCount and 0 <= col < self.__colCount:  # link to the down_room
    #         self.__maze.maze[row, col].down_room = self.__maze.maze[row + 1, col]
    #     else:  # the down_room of a room on the last row is linked to the room on the first row on the same column
    #         self.__maze.maze[row, col].down_room = self.__maze.maze[0, col]
    #     if 0 <= row - 1 < self.__rowCount and 0 <= col < self.__colCount:  # link to the upper_room
    #         self.__maze.maze[row, col].upper_room = self.__maze.maze[row - 1, col]
    #     else:  # the upper_room of a room on the first row is linked to the room on the last row on the same column
    #         self.__maze.maze[row, col].upper_room = self.__maze.maze[self.__rowCount - 1, col]
    #     if 0 <= row < self.__rowCount and 0 <= col - 1 < self.__colCount:  # link to the left_room
    #         self.__maze.maze[row, col].left_room = self.__maze.maze[row, col - 1]
    #     else:  # the left_room of a room on the first column is linked to the room on the last column on the same row
    #         self.__maze.maze[row, col].left_room = self.__maze.maze[row, self.__colCount - 1]
    #     if 0 <= row < self.__rowCount and 0 <= col + 1 < self.__colCount:  # link to the right_room
    #         self.__maze.maze[row, col].right_room = self.__maze.maze[row, col + 1]
    #     else:  # the right_room of a room on the last column is linked to the room on the first column on the same row
    #         self.__maze.maze[row, col].right_room = self.__maze.maze[row, 0]

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

    def __set_dungeon_str(self):
        """creates a string representation of the Dungeon  """
        for i in range(0, self.__rowCount):
            self.__dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the up door representation of each room in the ith row is appended to the self.__dungeon_str
                self.__dungeon_str += self.__maze.maze[i, j].print_up()

            self.__dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the room contents of each room in the ith row is appended to the self.__dungeon_str
                self.__dungeon_str += self.__maze.maze[i, j].print_room_contents()
            self.__dungeon_str += "\n"
            for j in range(0, self.__colCount):
                # the down door representation of each room in the ith row is appended to the self.__dungeon_str
                self.__dungeon_str += self.__maze.maze[i, j].print_down()

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

#
# dun = Dungeon(4, 4)
# print(dun)
# curr = dun.enter_dungeon()
# print(dun.print_dungeon_live_location(curr))
# print(dun.use_vision_potion(curr))