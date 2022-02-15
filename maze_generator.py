import numpy as np
from numpy import random
from room import Room


class Maze:
    def __init__(self, row_count=-1, col_count=-1):
        self.__set_rowCount(row_count)
        self.__set_colCount(col_count)
        # array unique elements to help in random selections
        self.__x = np.random.rand(self.__rowCount, self.__colCount)
        # initializing our maze array of type Room
        self.__map = np.empty((self.__rowCount, self.__colCount), Room)
        self.__i_entry = -1
        self.__j_entry = -1
        self.__i_exit = -1
        self.__j_exit = -1
        self.__path_taken = []
        self.__pillar_position =[]

    # def __str__(self):
    #     return self.__dungeon_str
    #
    # def __set_dungeon_str(self):
    #     """creates a string representation of the Dungeon  """
    #     for i in range(0, self.__rowCount):
    #         self.__dungeon_str += "\n"
    #         for j in range(0, self.__colCount):
    #             # the up door representation of each room in the ith row is appended to the self.__dungeon_str
    #             self.__dungeon_str += self.__map[i, j].print_up()
    #
    #         self.__dungeon_str += "\n"
    #         for j in range(0, self.__colCount):
    #             # the room contents of each room in the ith row is appended to the self.__dungeon_str
    #             self.__dungeon_str += self.__map[i, j].print_room_contents()
    #         self.__dungeon_str += "\n"
    #         for j in range(0, self.__colCount):
    #             # the down door representation of each room in the ith row is appended to the self.__dungeon_str
    #             self.__dungeon_str += self.__map[i, j].print_down()
    #
    def __set_rowCount(self, row_count):
        """
        validates if the row_count passed is an integer and assigns it to __rowcount
        :param row_count:
        """
        if isinstance(row_count, int) and row_count > 0:
            self.__rowCount = row_count
        else:
            raise ValueError("number of rows:" + row_count + "is not an integer greater than 0")

    def __get_rowCount(self):
        return self.__rowCount

    rowCount = property(__get_rowCount)

    def __set_colCount(self, col_count):
        """
        validates if the col_count passed is an integer and assigns it to __col_count
        :param col_count:
        """
        if isinstance(col_count, int) and col_count > 0:
            self.__colCount = col_count
        else:
            raise ValueError("number of rows:" + col_count + "is not an integer greater than 0")

    def __get_colCount(self):
        return self.__colCount

    colCount = property(__get_colCount)

    def __create_maze_of_empty_rooms(self):
        """the method that creates empty of room objects on the __map elements """
        for r in range(0, self.__rowCount):
            for c in range(0, self.__colCount):
                self.__map[r, c] = Room()
                self.__map[r, c].location = [r, c]

    def create_maze(self):
        """the method that creates the maze of room objects """
        self.__set_entrance_room()  # sets the entrance room
        self.__set_exit_room()  # sets the exit room
        self._create_room_links()
        # traverses through the __map array and checks if we can reach the exit from entrance
        # and save the successful path
        self.__set_path()
        self.__set_impassable()  # sets the rooms impassable (dead_ends)
        self.__set_pillars()  # places the pillars in the rooms
        self.__set_monsters() # place monsters in all the rooms with pillars
        self.__set_healing_vision_pit()  # sets the healing potion, vision potion and pits in each room randomly

    def __set_entrance_room(self):
        """ chooses an entrance randomly from sides of the __map_blueprint"""
        self.__create_maze_of_empty_rooms()
        corners = [self.__x[-1, :], self.__x[0, :], self.__x[:, 0], self.__x[:, -1]]
        entry_corner = np.random.choice(len(corners))  # selects the entry corner
        i, j = np.where(self.__x == np.random.choice(corners[entry_corner]))
        self.__i_entry, self.__j_entry = int(i), int(j)
        self.__map[self.__i_entry, self.__j_entry].is_entrance = True

    def __set_exit_room(self):
        """ chooses an entrance randomly from the __map_blueprint given the minimum distance from the entrance is >= 5
               """
        exit_choices = []
        for i in range(0, self.__rowCount):
            for j in range(0, self.__colCount):
                if abs((self.__i_entry - i) + (self.__j_entry - j)) >= 5:
                    exit_choices.append(self.__x[i, j])
        if len(exit_choices) == 0:
            self.__set_entrance_room()
            self.__set_exit_room()
        else:
            i, j = np.where(self.__x == np.random.choice(exit_choices))
            self.__i_exit, self.__j_exit = int(i), int(j)
            self.distance = abs((self.__i_entry - self.__i_exit) + (self.__j_entry - self.__j_exit))
            self.__map[self.__i_exit, self.__j_exit].is_exit = True

    def _create_room_links(self):
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                if 0 <= row + 1 < self.__rowCount and 0 <= col < self.__colCount:  # link to the down_room
                    self.__map[row, col].down_room = self.__map[row + 1, col]
                if 0 <= row - 1 < self.__rowCount and 0 <= col < self.__colCount:  # link to the upper_room
                    self.__map[row, col].upper_room = self.__map[row - 1, col]
                if 0 <= row < self.__rowCount and 0 <= col - 1 < self.__colCount:  # link to the left_room
                    self.__map[row, col].left_room = self.__map[row, col - 1]
                if 0 <= row < self.__rowCount and 0 <= col + 1 < self.__colCount:  # link to the right_room
                    self.__map[row, col].right_room = self.__map[row, col + 1]

    def __set_path(self):
        """ with entrance, exit and dead-ends randomly set finds one random winning path from entrance to exit"""
        self.__path_taken = self.__depth_first_search_traversal()
        # print(self.__path_taken)
        # print(self.__path_taken[0])
        # print(self.__path_taken[-1])

    def __depth_first_search_traversal(self):
        stack = []
        p = []
        visited = []
        stack.append(self.__map[self.__i_entry, self.__j_entry].location)
        while len(stack) > 0:
            possible_neighbor = []
            node = stack.pop()
            p.append(node)
            visited.append(node)
            row, col = node[0], node[1]

            if self.__map[row, col].down_room:
                if self.__map[row, col].down_room.is_exit and len(p) >= 4:
                    p.append(self.__map[row, col].down_room.location)
                    return p
                elif not self.__map[row, col].down_room.is_exit and self.__map[row, col].down_room.location not in visited and self.__map[row, col].down_room.location not in stack:
                    possible_neighbor.append(self.__map[row, col].down_room.location)
                elif self.__map[row, col].down_room.is_exit:
                    del p[-1]

            if self.__map[row, col].upper_room:
                if self.__map[row, col].upper_room.is_exit and len(p) >= 4:
                    p.append(self.__map[row, col].upper_room.location)
                    return p
                elif not self.__map[row, col].upper_room.is_exit and self.__map[row, col].upper_room.location not in visited and self.__map[row, col].upper_room.location not in stack:
                    possible_neighbor.append(self.__map[row, col].upper_room.location)
                elif self.__map[row, col].upper_room.is_exit:
                    del p[-1]

            if self.__map[row, col].left_room:
                if self.__map[row, col].left_room.is_exit and len(p) >= 4:
                    p.append(self.__map[row, col].left_room.location)
                    return p
                elif not self.__map[row, col].left_room.is_exit and self.__map[row, col].left_room.location not in visited and self.__map[row, col].left_room.location not in stack:
                    possible_neighbor.append(self.__map[row, col].left_room.location)
                elif self.__map[row, col].left_room.is_exit:
                    del p[-1]

            if self.__map[row, col].right_room:
                if self.__map[row, col].right_room.is_exit and len(p) >= 4:
                    p.append(self.__map[row, col].right_room.location)
                    return p
                elif not self.__map[row, col].right_room.is_exit and self.__map[row, col].right_room.location not in visited and self.__map[row, col].right_room.location not in stack:
                    possible_neighbor.append(self.__map[row, col].right_room.location)
                elif self.__map[row, col].right_room.is_exit:
                    del p[-1]

            if not self.__map[row, col].down_room and not self.__map[row, col].upper_room and \
                    not self.__map[row, col].left_room and not self.__map[row, col].right_room:
                    del p[-1]
            else:
                count = len(possible_neighbor)
                for i in range(count):
                    choice = random.choice(len(possible_neighbor))
                    stack.append(possible_neighbor[choice])
                    possible_neighbor.remove(possible_neighbor[choice])

    def __set_impassable(self):
        """
        Ensures that a  room is not an entrance/exit and randomly sets some rooms impassable (dead_ends).
        """
        self.__impassable_rooms = []  # only to test and validate the impassable rooms
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                number = random.randint(1, 10)
                if number >= 6 and [row, col] not in self.__path_taken:
                    self.__map[row, col].is_impassable = True
                    self.__impassable_rooms.append([row, col])

    def _get_impassable_rooms(self):
        return self.__impassable_rooms

    impassable_rooms = property(_get_impassable_rooms)

    def __set_pillars(self):
        """ sets the pillars along the found winning path """
        pillars = ['a', 'e', 'i', 'p']
        pillar_choices = self.__path_taken.copy()  # copy of the winning path is made
        del pillar_choices[0]  # deletes the entrance from the list of pillar choices
        del pillar_choices[-1]  # deletes the exit from the list of pillar choices
        for i in range(0, 4):
            j = np.random.choice(len(pillar_choices))
            row, col = pillar_choices[j]
            self.__pillar_position.append(pillar_choices[j])
            del pillar_choices[j]
            self.__map[row, col].pillar = str(pillars[i])  # sets a pillar in the room

    def __set_monsters(self):
        monster_positions = self.__pillar_position.copy()
        monster_choices = ["Ogre", "Gremlin", "Skeleton"]
        for i in monster_positions:
            chosen = random.choice(monster_choices)
            row, col = i[0], i[1]
            self.__map[row, col].monster = str(chosen)

    def __set_healing_vision_pit(self):
        """
        Healing potion is randomly placed in the rooms other than entrance, exit and impassible
        with the probability of 0.2
        vision potion is randomly placed in the rooms other than entrance, exit and impassible
        with the probability of 0.1
        Pit is randomly placed in the rooms other than entrance, exit,impassible and
        pillar (don't have to fall into a pit to collect a pillar) with the probability of 0.4
        More than one potion can be found in a room (randomly placed)
        """
        self.__healing_potion_rooms = []
        self.__vision_potion_rooms = []
        self.__pit_rooms = []
        # loops through each room of the array
        for row in range(0, self.__rowCount):
            for col in range(0, self.__colCount):
                if not self.__map[row, col].is_impassable and not self.__map[row, col].is_entrance and \
                        not self.__map[row, col].is_exit:  # not an entrance/exit/impassible room
                    healing_chance = random.choice([0, 1], p=[0.8, 0.2])
                    if healing_chance == 1:
                        # randomly chooses how powerful the healing potion will be
                        heal_type = random.choice(("y", "g"))
                        self.__map[row, col].heal = str(heal_type)
                        self.__healing_potion_rooms.append(self.__map[row, col])  # for testing
                    vision_chance = random.choice([0, 1], p=[0.9, 0.1])
                    if vision_chance == 1:
                        self.__map[row, col].vision = True
                        self.__vision_potion_rooms.append(self.__map[row, col])  # for testing
                    if self.__map[row, col].pillar is None:  # to ensure that a room does not have a pillar and a pit
                        pit_chance = random.choice([0, 1], p=[0.6, 0.4])
                        if pit_chance == 1:
                            self.__map[row, col].pit = True
                            self.__pit_rooms.append(self.__map[row, col])  # for testing

    def _get_healing_potion_rooms(self):
        return self.__healing_potion_rooms

    def _get_vision_potion_rooms(self):
        return self.__vision_potion_rooms

    def _get_pit_rooms(self):
        return self.__pit_rooms

    healing_potion_rooms = property(_get_healing_potion_rooms)  # for testing
    vision_potion_rooms = property(_get_vision_potion_rooms)  # for testing
    pit_rooms = property(_get_pit_rooms)  # for testing

    def _get_map(self):
        return self.__map

    def _get_winning_path(self):
        return self.__path_taken

    def _get_pillar_positions(self):
        return self.__pillar_position

    maze = property(_get_map)  # property to access the maze
    winning_path = property(_get_winning_path)  # property to access the winning_path
    pillar_position = property(_get_pillar_positions)

# maze = Maze(4,4)
# maze.create_maze()
# print(maze)