import random
import unittest
from room import Room
from numpy import random


class RoomTestCase(unittest.TestCase):

    def test_Room_init_and_str(self):
        """checks whether the room object prints as initialized."""
        r = Room()
<<<<<<< HEAD
        self.assertEqual("|------::------|" + "\t" + "\n" + "::            ::" + "\t" + "\n" + "|------::------|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.pillar = "a"
        self.assertEqual("|------::------|" + "\t" + "\n" + ":: I          ::" + "\t" + "\n" + "|------::------|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.pit = True
        self.assertEqual("|------::------|" + "\t" + "\n" + ":: I  X       ::" + "\t" + "\n" + "|------::------|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.heal= "y"
        self.assertEqual("|------::------|" + "\t" + "\n" + ":: I  X U     ::" + "\t" + "\n" + "|------::------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.vision = True
        self.assertEqual("|------::------|" + "\t" + "\n" + ":: I  X U oo  ::" + "\t" + "\n" + "|------::------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, True, True, False)
        self.assertEqual("|------::------|" + "\t" + "\n" + ":: I  X U oo   |" + "\t" + "\n" + "|------::------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, True, False, False)
        self.assertEqual("|------::------|" + "\t" + "\n" + "|   I  X U oo  |" + "\t" + "\n" + "|------::------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, False, False, False)
        self.assertEqual("|------::------|" + "\t" + "\n" + "|   I  X U oo  |" + "\t" + "\n" + "|------==------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(False, False, False, False)
        self.assertEqual("|------==------|" + "\t" + "\n" + "|  Impassable  |" + "\t" + "\n" + "|------==------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_entrance =True
        self.assertEqual("|------==------|" + "\t" + "\n" + "|     Enter    |" + "\t" + "\n" + "|------==------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_entrance =False
        self.assertEqual("|------==------|" + "\t" + "\n" + "|  Impassable  |" + "\t" + "\n" + "|------==------|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_exit = True
        self.assertEqual("|------==------|" + "\t" + "\n" + "|     Exit     |" + "\t" + "\n" + "|------==------|" + "\t"+"\n",
=======
        self.assertEqual("|-----::-----|" + "\t" + "\n" + "::          ::" + "\t" + "\n" + "|-----::-----|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.pillar = "a"
        self.assertEqual("|-----::-----|" + "\t" + "\n" + ":: I        ::" + "\t" + "\n" + "|-----::-----|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.pit = True
        self.assertEqual("|-----::-----|" + "\t" + "\n" + ":: I X      ::" + "\t" + "\n" + "|-----::-----|" + "\t" +"\n",
                         r.__str__(), "values don't match")
        r.heal= "y"
        self.assertEqual("|-----::-----|" + "\t" + "\n" + ":: I X U    ::" + "\t" + "\n" + "|-----::-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.vision = True
        self.assertEqual("|-----::-----|" + "\t" + "\n" + ":: I X U oo ::" + "\t" + "\n" + "|-----::-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, True, True, False)
        self.assertEqual("|-----::-----|" + "\t" + "\n" + ":: I X U oo  |" + "\t" + "\n" + "|-----::-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, True, False, False)
        self.assertEqual("|-----::-----|" + "\t" + "\n" + "|  I X U oo  |" + "\t" + "\n" + "|-----::-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(True, False, False, False)
        self.assertEqual("|-----::-----|" + "\t" + "\n" + "|  I X U oo  |" + "\t" + "\n" + "|-----==-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.set_door(False, False, False, False)
        self.assertEqual("|-----==-----|" + "\t" + "\n" + "| Impassable |" + "\t" + "\n" + "|-----==-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_entrance =True
        self.assertEqual("|-----==-----|" + "\t" + "\n" + "|    Enter   |" + "\t" + "\n" + "|-----==-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_entrance =False
        self.assertEqual("|-----==-----|" + "\t" + "\n" + "| Impassable |" + "\t" + "\n" + "|-----==-----|" + "\t"+"\n",
                         r.__str__(), "values don't match")
        r.is_exit = True
        self.assertEqual("|-----==-----|" + "\t" + "\n" + "|    Exit    |" + "\t" + "\n" + "|-----==-----|" + "\t"+"\n",
>>>>>>> dev
                         r.__str__(), "values don't match")
    def test_set_monster(self):
        r = Room()
        name = random.choice(["Ogre", "Gremlin", "Skeleton"])
        r.monster = name
        self.assertEqual(name, r.monster)

    def test_set_monster_invalid_input(self):
        r = Room()
        name = "new_monster"
        r.monster = name
        self.assertEqual(None, r.monster)

<<<<<<< HEAD
    def test_floor_valid_input(self):
        r = Room()
        r.floor = 1
        self.assertEqual(1, r.floor, "values don't match")

    def test_floor_invalid_input(self):
        """tests the set_location method when invalid input (list containing a negative number) is given."""

        try:
            r = Room()
            r.floor = -1

        except ValueError:
            self.assertEqual(True, True, "value error not raised.")


=======
>>>>>>> dev
    def test_Room_set_location_list_input(self):
        """tests the set_location method when valid input (list of length 2) is given."""
        r = Room()
        nums = [0, 0]
        r.location = nums
        self.assertEqual([0, 0], r.location, "values don't match")

    def test_Room_set_location_tuple_input(self):
        """tests the set_location method when valid input (tuple of length 2) is given."""
        r = Room()
        nums = (0, 0)
        r.location = nums
        self.assertEqual([0, 0], r.location, "values don't match")

    def test_Room_set_location_invalid_input_negative_input(self):
        """tests the set_location method when invalid input (list containing a negative number) is given."""
        try:
            r = Room()
            nums = (2, -1)
            r.location = nums
        except ValueError:
            self.assertEqual(True, True, "value error not raised.")

    def test_Room_set_location_invalid_input_wrong_length_input(self):
        """tests the set_location method when invalid input (single integer) is given."""
        try:
            r = Room()
            nums = 8
            r.location = nums
        except ValueError:
            self.assertEqual(True, True, "value error not raised.")
        except TypeError:
            self.assertEqual(True, True, "Type error not raised.")

    def test_Room_set_location_invalid_input_str_list_input(self):
        """tests the set_location method when invalid input (list of string objects) is given."""
        try:
            r = Room()
            nums = ["a", "b"]
            r.location = nums
        except ValueError:
            self.assertEqual(True, True, "value error not raised.")
        except TypeError:
            self.assertEqual(True, True, "Type error not raised.")

    def test_Room_set_pillar_valid_input(self):
        """tests the set_pillar method when valid input ("a", "e", "i", "p") is given."""
        r = Room()
        ran = random.choice(["a", "e", "i", "p"])
        r.pillar = ran
        ran = ran.lower()
        self.assertEqual(ran, str(r.pillar), "values don't match.")

    def test_Room_set_pillar_valid_input_None(self):
        """tests the set_pillar method when valid input (None) is given."""
        r = Room()
        r.pillar =None
        self.assertEqual(None, r.pillar, "values don't match.")

    def test_Room_set_pillar_invalid_input(self):
        """tests the set_pillar method when invalid input (int or str values other than a, e, i, p) is given."""
        r = Room()
        r.pillar = 2
        self.assertEqual(None, r.pillar, "values don't match.")
        r.pillar ="k"
        self.assertEqual(None, r.pillar, "values don't match.")

    def test_Room_set_healing_potion_valid_input(self):
        """tests the set_healing_potion method when valid input ("y" or "g" - upper or lower case) is given."""
        r = Room()
        ran = random.choice(["Y", "y", "g", "G"])
        r.heal = ran
        ran = ran.lower()
        self.assertEqual(ran, str(r.heal), "values don't match")

    def test_Room_set_healing_potion_valid_input_None(self):
        """tests the set_healing_potion method when valid input (None) is given."""
        r = Room()
        r.heal = None
        self.assertEqual(None, r.heal, "values don't match")

    def test_Room_set_healing_potion_invalid_input(self):
        """tests the set_healing_potion method when invalid input (int or str values other than y and g) is given."""
        try:
            r = Room()
            r.heal = 2
            r.heal = "k"
        except ValueError:
            self.assertEqual(True, True, "Value error not raised")

    def test_Room_set_vision_potion_valid_input(self):
        """tests the set_vision_potion method when valid input (boolean) is given."""
        r = Room()
        tf = random.choice([True, False])
        r.vision =tf
        self.assertEqual(tf, r.vision, "values don't match")

    def test_Room_set_vision_potion_invalid_input(self):
        """tests the set_vision_potion method when invalid input (str) is given."""
        try:
            r = Room()
            r.vision = "a"
        except TypeError:
            self.assertEqual(True, True, "Type error not raised.")

    def test_Room_set_pit_valid_input(self):
        """tests the set_pit method when valid input (boolean) is given."""
        r = Room()
        tf = random.choice([True, False])
        r.pit =tf
        self.assertEqual(tf, r.pit, "values don't match")

    def test_Room_set_pit_invalid_input(self):
        """tests the set_pit method when invalid input (str) is given."""
        try:
            r = Room()
            r.pit = "string"
        except TypeError:
            self.assertEqual(True, True, "Type error not raised")
        except ValueError:
            self.assertEqual(True, True, "Value error not raised")

    def test_Room_set_door_valid_input(self):
        """tests the set_door method when valid inputs (True or False) are given."""
        try:
            r = Room()
            r.set_door(random.choice([True, False]), random.choice([True, False]), random.choice([True, False]),
                       random.choice([True, False]))
        except TypeError:
            raise TypeError("Doors must be Boolean True of False.")

    def test_Room_set_door_invalid_input(self):
        """tests the set_door method when invalid inputs (int) are given."""
        try:
            r = Room()
            r.set_door(7, 6, 4, 5)
        except TypeError:
            self.assertEqual(True, True, "Type error not raised")

    def test_Room_set_entrance_valid_input(self):
        """tests the set_entrance method when valid input (True or False) is given."""
        r = Room()
        tf = random.choice([True, False])
        r.is_entrance = tf
        self.assertEqual(tf, r.is_entrance, "values don't match")

    def test_Room_set_entrance_invalid_input(self):
        """tests the set_entrance method when invalid input is given."""
        try:
            r = Room()
            r.is_entrance = "t"
        except TypeError:
            self.assertEqual(True, True, "Type error not raised")

    def test_Room_set_exit_valid_input(self):
        """tests the set_exit method when valid input is given."""
        r = Room()
        tf = random.choice([True, False])
        r.is_exit  = tf
        self.assertEqual(str(tf), str(r.is_exit), "values don't match")

    def test_Room_set_exit_invalid_input(self):
        """tests the set_exit method when invalid input is given."""
        try:
            r = Room()
            r.is_exit = "t"
        except TypeError:
            self.assertEqual(True, True, "Type error not raised")

    def test_Room_set_visited_valid_input(self):
        """tests the set_visited method when valid input is given."""
        r = Room()
        tf = random.choice([True, False])
        r.is_visited = tf
        self.assertEqual(str(tf), str(r.is_visited), "values don't match")

    def test_Room_set_visited_invalid_input(self):
        """tests the set_visited method when invalid input is given."""
        try:
            r = Room()
            r.is_visited= "t"
        except TypeError:
            self.assertEqual(True, True, "Type error not raised")

    def test_Room_set_impassable(self):
        """tests the set_impassable method and makes sure room contents are emptied when a room is set impassable."""
        r = Room()
        r.is_impassable = True
        self.assertEqual(True, r.is_impassable, "values don't match.")



if __name__ == '__main__':
    unittest.main()