# name  : Shoby Gnanasekaran
# net id: shoby


class Room:
    """represents a room inside a rectangular dungeon/maze. If the room is an entrance or an exit, it should be an empty
         room. If the room is impassable that means that it's a dead-end and all doors of that room are closed. As the
         player walks through the maze, there is a 10% chance of him/her finding each of these objects inside each room:
         pillar, healing potion, vision potion and pit."""

    def __init__(self):
        self.__location = None
        self.__stairs = None
        self.__left_room = None
        self.__right_room = None
        self.__upper_room = None
        self.__down_room = None
        self.__room_contents = {
            "pillar": None,  # 10% chance of spotting, if all 4 pillars are spotted, the player wins the game
            "healing_potion": None,  # 10% chance of spotting, green: 5-10, yellow: 11-15 hit points generated randomly
            "vision_potion": False,  # 10% chance of spotting, allows the player to see up to 8 surrounding rooms
            "pit": False,  # 10% chance of spotting, , causes a damage of 1-20 hit points generated randomly
            "monster": None
        }
        self.__is_entrance = False
        self.__is_exit = False
        self.__door = {  # if all 4 doors are set to False, it is an impassable room
            "Up": True,
            "Down": True,
            "Left": True,
            "Right": True
        }
        self.__visited = False

    def __set_stairs(self,room):
        if isinstance(room, Room):
            self.__stairs = room
        else:
            self.__stairs = None

    def __get_stairs(self):
        return self.__stairs

    stairs = property(__get_stairs, __set_stairs)

    def __set_upper_room(self, room):
        if isinstance(room, Room):
            self.__upper_room = room
        else:
            self.__upper_room = None

    def __get_upper_room(self):
        return self.__upper_room

    upper_room = property(__get_upper_room,__set_upper_room)

    def __set_down_room(self, room):
        if isinstance(room, Room):
            self.__down_room = room
        else:
            self.__down_room = None

    def __get_down_room(self):
        return self.__down_room

    down_room = property(__get_down_room,__set_down_room)

    def __set_left_room(self, room):
        if isinstance(room, Room):
            self.__left_room = room
        else:
            self.__left_room = None

    def __get_left_room(self):
        return self.__left_room

    left_room = property(__get_left_room,__set_left_room)

    def __set_right_room(self, room):
        if isinstance(room, Room):
            self.__right_room = room
        else:
            self.__right_room = None

    def __get_right_room(self):
        return self.__right_room

    right_room = property(__get_right_room,__set_right_room)

    def __set_location(self, nums):
        """sets the current room's location (matrix coordinates)."""
        if len(nums) == 2:
            if isinstance(nums[0], int) and isinstance(nums[1], int) and nums[0] >= 0 and nums[1] >= 0:
                self.__location = [int(nums[0]), int(nums[1])]
            else:
                raise ValueError("Please enter a list of two int values greater than or equal to zero.")
        else:
            raise TypeError("Please enter a list of two int values greater than or equal to zero.")

    def __get_location(self):
        return self.__location

    location = property(__get_location, __set_location)

    def __set_monster(self,monster):
        if monster in ["Ogre", "Gremlin", "Skeleton"]:
            self.__room_contents["monster"] = monster
        else:
            self.__room_contents["monster"] = None

    def __get_monster(self):
        return self.__room_contents["monster"]

    monster = property(__get_monster, __set_monster)

    def __set_pillar(self, pillar):
        if pillar in ['a', 'e', 'i', 'p']:
            self.__room_contents["pillar"] = pillar
        else:
            self.__room_contents["pillar"] = None

    def __get_pillar(self):
        """getter method to return the name of pillar that exists, None otherwise"""
        return self.__room_contents["pillar"]

    pillar = property(__get_pillar, __set_pillar)

    def __set_healing_potion(self, name):
        """sets whether a healing potion exists inside the room and if yes, which type
        :param name: name of the healing potion if it exists, otherwise None"""
        if name is None:
            self.__room_contents["healing_potion"] = None
        else:
            if name in ["y", "Y"]:
                self.__room_contents["healing_potion"] = name.lower()
            elif name in ["g", "G"]:
                self.__room_contents["healing_potion"] = name.lower()
            else:
                raise ValueError("incorrect value of healing potion.")

    def __get_healing_potion(self):
        """getter method to return the name of healing potion that exists inside the room, returns None otherwise."""
        return self.__room_contents["healing_potion"]

    heal = property(__get_healing_potion, __set_healing_potion)

    def __set_vision_potion(self, tf):
        """sets whether a vision potion exists inside the room.
        :param tf: Boolean True or False for whether a vision potion exists."""
        if str(tf) in ["True", "False"]:
            self.__room_contents["vision_potion"] = bool(tf)
        else:
            raise TypeError("Please enter boolean: True or False.")

    def __get_vision_potion(self):
        """getter method to return if vision potion exists inside the room."""
        return self.__room_contents["vision_potion"]

    vision = property(__get_vision_potion, __set_vision_potion)

    def __set_pit(self, tf):
        """sets whether a pit exists inside the room.
        :param tf: Boolean True or False for whether a pit exists."""
        if str(tf) in ["True", "False"]:
            self.__room_contents["pit"] = bool(tf)
        else:
            raise TypeError("Please enter boolean: True or False.")

    def __get_pit(self):
        """getter method that returns whether or not a pit exists inside the room."""
        return self.__room_contents["pit"]

    pit = property(__get_pit, __set_pit)

    def __set_is_entrance(self, tf):
        """helper method that sets the value of whether the room is an entrance.
        :param tf: boolean True or False"""
        if str(tf) in ["True", "False"]:
            self.__is_entrance = bool(tf)
        else:
            raise TypeError("Please enter boolean: True or False.")

    def __get_is_entrance(self):
        """returns if the room is the entrance.
        :returns True or False"""
        return self.__is_entrance

    is_entrance = property(__get_is_entrance, __set_is_entrance)

    def __set_visited(self, tf):
        """helper method that sets the value of whether the room has been visited before.
        :param tf: boolean True or False"""
        if str(tf) in ["True", "False"]:
            self.__visited = bool(tf)
        else:
            raise TypeError("Please enter boolean: True or False.")

    def __get_is_visited(self):
        """returns if the room has been visited
        :returns True or False"""
        return self.__visited

    is_visited = property(__get_is_visited, __set_visited)

    def __set_is_exit(self, tf):
        """helper method that sets the value of whether the room is an exit.
        :param tf: boolean True or False"""
        if str(tf) in ["True", "False"]:
            self.__is_exit = bool(tf)
        else:
            raise TypeError("Please enter boolean: True or False.")

    def __get_is_exit(self):
        """returns if the room is an exit
        :returns True or False"""
        return self.__is_exit

    is_exit = property(__get_is_exit, __set_is_exit)

    def __get_is_impassable(self):
        """returns whether a room is impassable i.e. there is no door
        :returns True or False"""
        for key in self.__door:
            if self.__door[key] == bool(True):
                return False
        return True

    def __set_impassable(self, tf):
        """sets a room impassable by removing all doors and room contents"""
        if str(tf) == "True":
            for key in self.__door:
                if self.__door[key] == bool(True):
                    self.__door[key] = bool(False)

    is_impassable = property(__get_is_impassable, __set_impassable)

    def set_door(self, up_tf, down_tf, left_tf, right_tf):
        """helper method to set the values of doors in each direction
        :param up_tf: Boolean True or False for 'up' direction
        :param down_tf: Boolean True or False for 'down' direction
        :param left_tf: Boolean True or False for 'left' direction
        :param right_tf: Boolean True or False for 'right' direction"""
        if str(up_tf) in ["True", "False"]:
            self.__door["Up"] = bool(up_tf)
        else:
            raise TypeError("Please enter True or False for up_tf.")

        if str(down_tf) in ["True", "False"]:
            self.__door["Down"] = bool(down_tf)
        else:
            raise TypeError("Please enter True or False for down_tf.")

        if str(left_tf) in ["True", "False"]:
            self.__door["Left"] = bool(left_tf)
        else:
            raise TypeError("Please enter True or False for left_tf.")

        if str(right_tf) in ["True", "False"]:
            self.__door["Right"] = bool(right_tf)
        else:
            raise TypeError("Please enter True or False for right_tf.")

    def __str__(self):
        return self.print_room()

    def print_room(self):
        ret = ""
        ret += self.print_up() + "\n"
        ret += self.print_room_contents() + "\n"
        ret += self.print_down() + "\n"
        return ret
    #     if self.__door["Up"] is True and self.__door["Down"] is True:
    #         ret += self.print_up_down(True) + "\n"
    #         ret += self.print_room_contents() + "\n"
    #         ret += self.print_up_down(True)
    #     if self.__door["Up"] is True and self.__door["Down"] is False:
    #         ret += self.print_up_down(True) + "\n"
    #         ret += self.print_room_contents() + "\n"
    #         ret += self.print_up_down(False)
    #     if self.__door["Up"] is False and self.__door["Down"] is True:
    #         ret += self.print_up_down(False) + "\n"
    #         ret += self.print_room_contents() + "\n"
    #         ret += self.print_up_down(True)
    #     if self.__door["Up"] is False and self.__door["Down"] is False:
    #         ret += self.print_up_down(False) + "\n"
    #         ret += self.print_room_contents() + "\n"
    #         ret += self.print_up_down(False)
    #     return ret

    def print_up(self):
        up_str = ""
        if self.__door["Up"] is True:
            up_str += "|------::------|" + "\t"
        else:
            up_str += "|------==------|" + "\t"
        return up_str

    def print_down(self):
        up_str = ""
        if self.__door["Down"] is True:
            up_str += "|------::------|" + "\t"
        else:
            up_str += "|------==------|" + "\t"
        return up_str

    def print_room_contents(self):
        if self.__is_entrance:
            if self.__door["Left"] is False and self.__door["Right"] is False:
                return "|     Enter    |" + "\t"
            elif self.__door["Left"] is False and self.__door["Right"] is True:
                return "|     Enter   ::" + "\t"
            elif self.__door["Left"] is True and self.__door["Right"] is True:
                return "::    Enter   ::" + "\t"
            else:
                return "::    Enter    |" + "\t"
        elif self.__is_exit:
            if self.__door["Left"] is False and self.__door["Right"] is False:
                return "|     Exit     |" + "\t"
            elif self.__door["Left"] is False and self.__door["Right"] is True:
                return "|     Exit    ::" + "\t"
            elif self.__door["Left"] is True and self.__door["Right"] is True:
                return "::    Exit    ::" + "\t"
            else:
                return "::    Exit     |" + "\t"
        elif self.is_impassable is True:
            return "|  Impassable  |" + "\t"
        else:
            pillar = "I"
            pit = " X"
            healing_potion = " U"
            vision_potion = " oo"
            monster ="m"
            if self.__room_contents["monster"] is None:
                monster = " "
            if self.__room_contents["pillar"] is None:
                pillar = " "
            if self.__room_contents["pit"] is False:
                pit = "  "
            if self.__room_contents["healing_potion"] is None:
                healing_potion = "  "
            if self.__room_contents["vision_potion"] is False:
                vision_potion = "   "
            if self.__door["Left"] is True and self.__door["Right"] is True:
                return f":: {pillar}{monster}{pit}{healing_potion}{vision_potion}  ::" + "\t"
            elif self.__door["Left"] is True and self.__door["Right"] is False:
                return f":: {pillar}{monster}{pit}{healing_potion}{vision_potion}   |" + "\t"
            elif self.__door["Left"] is False and self.__door["Right"] is False:
                return f"|   {pillar}{monster}{pit}{healing_potion}{vision_potion}  |" + "\t"
            else:
                return f"|  {pillar}{monster}{pit}{healing_potion}{vision_potion}  ::" + "\t"

    def vision_current_room(self):

        if self.__door["Left"] is True and self.__door["Right"] is True:
            return "::  +here+    ::" + "\t"
        elif self.__door["Left"] is False and self.__door["Right"] is True:
            return "|   +here+    ::" + "\t"
        elif self.__door["Left"] is False and self.__door["Right"] is False:
            return "|   +here+     |" + "\t"
        else:
            return "|   +here+    ::" + "\t"


# class Main:
#     r = Room()
#     print(r)
#     r.pillar = 'a'
#     r.pit = True
#     r.heal = "g"
#     r.vision = True
#     r.set_door(False, True, False, True)
#     print(r)
    # s = Room()
    # s.set_pillar(None)
    # s.set_pit(True)
    # s.set_vision_potion(False)
    # s.set_healing_potion("y")
    # t = Room()
    # print(r)
    #
    # print(s)
    # t.set_impassable()
    # print(t)
    # r.set_exit(True)
    # print(r)
