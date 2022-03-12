"""
Name: Tos Fackenthall
Net ID: tos
"""
from player import Player
from dungeon import Dungeon
import sys


class DungeonAdventure:
    """
    A class to run the Dungeon Adventure game.
    """
    def __init__(self, name):
        """
        Text to introduce the game, describing what the game is about and how to play
        """
        self.__name = name
        print(f"Welcome to Dungeon Adventure, {name}!")
        print("Your task is to find each of the four pillars of OO, and the exit!")
        print("Along the way you will find potions to help you and pits to hurt you. Good luck!")
        print()
        # additionally, (X) key can be used to view entire maze (for testing purposes)
        hlp = ("-------------------Help Menu-------------------\n"
               "Navigation: (U) up, (D) down, (L) left, (R) right ||| Menu: (H) Help, (Q) quit\n"
               "Special: (V) use vision potion, which shows contents of surrounding rooms in the maze\n"
               "Passable U/D door: -----::-----   Impassable: -----==-----\n"
               "Passable L/R door: ::        ::   Impassable: |          |\n"
               "Room contents: X = pit, I = pillar, U = healing potion, oo = vision potion")
        print(hlp)
        print()

    def get_name(self):
        return self.__name

    def is_he_dead(self, a, da):
        """
        Checks hit points to see if player has died. If so, asks if they want to play again.
        :param a: Player object
        :param da: DungeonAdventure object
        :return: Boolean
        """
        hp = a.hit_points()
        if hp < 50:
            print("!!!!!!!!!!!!!!!!!!!!!!!! You died !!!!!!!!!!!!!!!!!!!!!!!! ")
            print()
            da.ask_play_again()
        else:
            return False

    def ask_play_again(self):
        print()
        p = input("Play again? (y/n)")
        if p == "y":
            a = Player(self.__name)
            dun = Dungeon(4, 4)
            curr = dun.enter_dungeon()
            print(curr)
            da.get_user_move(a, dun, curr)
        elif p == "n":
            sys.exit("Game over.")
            quit()

    def get_user_move(self, a, dun, cur):
        """
        Asks user for next move and passes that info to move().
        :param a: Player object
        :param dun: Dungeon object
        :param cur: Room object
        :return:
        """
        m = ""
        print()
        if da.is_he_dead(a, da) == False:
            while m == "":
                m = input("Next move? (U, D, R, L, V, H, Q): >>> ").lower()
                self.move(a, dun, cur, m)
        else:
            # shouldn't ever get here since is_he_dead will kill program
            print("You're dead. Game over.")

    def move(self, a, dun, cur, mv):
        """
        Takes input from get_user_move() and navigates player to the corresponding room in the dungeon,
        providing the room is not impassable.

        :param a: Player object
        :param dun: Dungeon object
        :param cur: Room object
        :param mv: String (navigation input from user)
        """

        if mv == "u":
            print("moving UP")
            if cur.upper_room.is_impassable == False:
                cur = cur.upper_room
            else:
                print("You can't go that way! Try again!")
                self.get_user_move(a, dun, cur)
                return
            print(cur)
        elif mv == "d":
            print("moving DOWN")
            if cur.down_room.is_impassable == False:
                cur = cur.down_room
            else:
                print("You can't go that way! Try again!")
                self.get_user_move(a, dun, cur)
                return
            print(cur)
        elif mv == "l":
            print("moving LEFT")
            if cur.left_room.is_impassable == False:
                cur = cur.left_room
            else:
                print("You can't go that way! Try again!")
                self.get_user_move(a, dun, cur)
                return
            print(cur)
        elif mv == "r":
            print("moving RIGHT")
            if cur.right_room.is_impassable == False:
                cur = cur.right_room
            else:
                print("You can't go that way! Try again!")
                self.get_user_move(a, dun, cur)
                return
            print(cur)
        elif mv == "v":
            if a.vision_potions() > 0:
                print("Using vision potion!")
                print(dun.use_vision_potion(cur))
                a.decrease_vision_potion()
            else:
                print("Sorry, you don't have any vision potions!")
            self.get_user_move(a, dun, cur)
        elif mv == "x":
            # (X) key used to view entire maze (for testing purposes)
            print(dun.print_dungeon_live_location(cur))
        elif mv == "h":
            hlp = ("-------------------Help Menu-------------------\n"
                   "Navigation: (U) up, (D) down, (L) left, (R) right ||| Menu: (H) Help, (Q) quit\n"
                   "Special: (V) use vision potion, which shows contents of surrounding rooms in the maze\n"
                   "Passable U/D door: -----::-----   Impassable: -----==-----\n"
                   "Passable L/R door: ::        ::   Impassable: |          |\n"
                   "Room contents: X = pit, I = pillar, U = healing potion, oo = vision potion")
            print(hlp)
            print()
            print(cur)
            self.get_user_move(a, dun, cur)
            return
        elif mv == "q":
            sys.exit("Game over.")
            quit()
        else:
            print("invalid key! please try again")
            self.get_user_move(a, dun, cur)
            return
        da.move_results(a, dun, cur, mv)

    def move_results(self, a, dun, cur, mv):
        """
        Displays the contents of the current room in a slightly more verbose manner than how the information is stored
        in the Dungeon and Room classes.

        :param a: Player object
        :param dun: Dungeon object
        :param cur: Room object
        """

        p = ""
        if cur.pillar == None:
            pass
        else:
            if str(cur.pillar) == "a":
                p = "Abstraction"
            if str(cur.pillar) == "e":
                p = "Encapsulation"
            if str(cur.pillar) == "i":
                p = "Inheritance"
            if str(cur.pillar) == "p":
                p = "Polymorphism"
            print(f"You've found the {p} pillar!")
            a.add_pillar(cur.pillar)
            a.pillar_count()

        if mv == "v" or mv == "x":
            pass
        else:
            if cur.pit == True:
                print(f"You've fallen into a pit!")
                a.fall_into_pit()

        p = ""
        if cur.heal == None:
            pass
        else:
            if str(cur.heal) == "g":
                p = "green"
            if str(cur.heal) == "y":
                p = "yellow"
            print(f"You've found a {p} healing potion!")
            a.add_healing_potion(str(cur.heal))

        if cur.vision == True:
            print("You've found a vision potion!")
            a.add_vision_potion(1)

        print(a)
        pillars = a.pillar_count()

        if cur.is_exit == False:
            dun.clear_healing_pillar_vision(cur)
            da.get_user_move(a, dun, cur)
        elif cur.is_exit == True and pillars < 4:
            print(f"You've found the exit but you're missing {4 - pillars} pillars! Go find them!")
            da.get_user_move(a, dun, cur)
            return
        else:
            print()
            print("You've found the exit and all the pillars! YOU WIN!!")
            print(dun)
            print()
            da.ask_play_again()
            sys.exit()
            quit()

if __name__ == '__main__':

    p_name = input("What is your name? >>> ")
    da = DungeonAdventure(p_name)
    dun = Dungeon(4, 4)
    curr = dun.enter_dungeon()
    print(curr)
    n = da.get_name()

    a = Player(n)

    da.get_user_move(a, dun, curr)
