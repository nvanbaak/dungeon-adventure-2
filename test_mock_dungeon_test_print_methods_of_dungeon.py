import unittest
from room import Room
from dungeon import Dungeon


class Mock_dungeon:
    """
    creates a mock dungeon of size 4*4, with pre-fixed entrance, exit, impassable room,pillars, healing_potion,
    pit and vision to test the use_vision_potion and print_dungeon_live_location methods of the Dungeon
    """

    def __init__(self):
        self.dun = Dungeon(4, 4)  # creating a dungeon object
        self.__create_maze_of_empty_rooms()  # resetting the rooms to empty
        self.__create_mock_dungeon()
        self.__create_room_links()

    def __create_maze_of_empty_rooms(self):
        """the method resets the dungeon rooms to empty """
        for r in range(0, 4):
            for c in range(0, 4):
                self.dun.dungeon.maze[r, c] = Room()
                self.dun.dungeon.maze[r, c].location = [r, c]

    def __create_mock_dungeon(self):

        self.dun.dungeon.maze[0, 0].is_entrance = True  # setting entrance at (0,0)
        self.dun.dungeon.maze[3, 3].is_exit = True  # setting exit at (3,3)
        # placing the pillars
        self.dun.dungeon.maze[0, 1].pillar = 'a'
        self.dun.dungeon.maze[0, 2].pillar = 'e'
        self.dun.dungeon.maze[0, 3].pillar = 'i'
        self.dun.dungeon.maze[1, 3].pillar = 'p'
        # placing impassable rooms
        self.dun.dungeon.maze[1, 0].is_impassable = True
        self.dun.dungeon.maze[2, 0].is_impassable = True
        # placing healing_potion
        self.dun.dungeon.maze[1, 1].heal = 'y'
        # placing pit
        self.dun.dungeon.maze[1, 2].pit = True
        # placing vision
        self.dun.dungeon.maze[1, 3].vision = True

    def __create_room_links(self):
        """creates pointers between each rooms"""
        self.dun.dungeon._create_room_links()
        self.dun._setting_doors()


class MyTestCase(unittest.TestCase):

    def test_print_dungeon_live_location(self):
        mock_dun = Mock_dungeon()
        curr = mock_dun.dun.dungeon.maze[0, 0]
        mock_dun.dun.print_dungeon_live_location(curr)
        print_str = "\n"
        print_str += "|------==------|"+"\t"+"|------==------|"+"\t"+"|------==------|"+"\t"+"|------==------|"+"\t"+"\n"
        print_str += "|   +here+    ::"+"\t"+":: I          ::"+"\t"+":: I          ::"+"\t"+":: I           |"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|  Impassable  |"+"\t"+"|       U     ::"+"\t"+"::    X       ::"+"\t"+":: I      oo   |"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|  Impassable  |"+"\t"+"|             ::"+"\t"+"::            ::"+"\t"+"::             |"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"|------::------|"+"\t"+"\n"
        print_str += "|             ::"+"\t"+"::            ::"+"\t"+"::            ::"+"\t"+"::    Exit     |"+"\t"+"\n"
        print_str += "|------==------|"+"\t"+"|------==------|"+"\t"+"|------==------|"+"\t"+"|------==------|"+"\t"
        print_str += "\n+here+ is your current room"
        self.assertEqual(print_str, mock_dun.dun.print_dungeon_live_location(curr))

    # def test_use_vision_potion(self):
    #     mock_dun = Mock_dungeon()
    #     curr = mock_dun.dun.dungeon.maze[0, 0]
    #     print_str = "\n"
    #     print_str += "               "+"               "+"               "+"\n"
    #     print_str += "               "+"               "+"               "+"\n"
    #     print_str += "               "+"               "+"               "+"\n"
    #     print_str += "               "+"|-----::-----|"+"\t"+"|-----::-----|"+"\t"+"\n"
    #     print_str += "               "+"::  +here+  ::"+"\t"+":: I        ::"+"\t"+"\n"
    #     print_str += "               "+"|-----==-----|"+"\t"+"|-----::-----|"+"\t"+"\n"
    #     print_str += "               "+"|-----==-----|"+"\t"+"|-----::-----|"+"\t"+"\n"
    #     print_str += "               "+"| Impassable |"+"\t"+"|      U    ::"+"\t"+"\n"
    #     print_str += "               "+"|-----==-----|"+"\t"+"|-----::-----|"+"\t"
    #     self.assertEqual(print_str, mock_dun.dun.use_vision_potion(curr))

if __name__ == '__main__':
    unittest.main()


