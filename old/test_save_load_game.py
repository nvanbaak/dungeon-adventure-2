import unittest
from dungeon_builder import DungeonBuilder
from hero import Hero
from save_load_game import SaveGame


class MockHero(Hero):
    """mock hero class to check the save and load of hero objects """
    def __init__(self, name, model):
        super().__init__(name, model)

    def attack_target(self, target):
        pass

    def combat(self, target):
        pass

    def take_damage(self, dmg, source):
        pass

    def use_health_potion(self):
        pass

    def use_vision_potion(self):
        pass

class MyTestCase(unittest.TestCase):


    def test_save_and_load_game(self):

        game = DungeonBuilder.build_easy_dungeon()
        row1, col1 = game[0].dungeon.winning_path[2][0], game[0].dungeon.winning_path[2][1]
        curr1 = game[0].dungeon.maze[row1, col1]
        curr1_map = game[0].print_dungeon_live_location(curr1)

        hero = MockHero("hero", "model")
        hero_hp = hero.hp

        sg = SaveGame()
        sg.save_game("game1",game,curr1.floor,curr1.location,hero)
        game_objects = sg.load_game("game1")

        # test if hero hp is same as before

        self.assertEqual(hero_hp, game_objects[-1].hp, "values don't match.")

        # test if the player is in the same position as before
        floor = game_objects[1]

        row, col = game_objects[2][0], game_objects[2][1]
        curr = game_objects[0][floor].dungeon.maze[row, col]
        self.assertEqual(game_objects[0][floor].print_dungeon_live_location(curr), curr1_map, "values dont match")



    def test_single_dungeon_save_and_load(self):
        game = DungeonBuilder.build_single_dungeon()
        row1, col1 = game[0].dungeon.winning_path[2][0], game[0].dungeon.winning_path[2][1]
        curr1 = game[0].dungeon.maze[row1, col1]
        curr1_map = game[0].print_dungeon_live_location(curr1)

        hero = MockHero("hero", "model")
        hero_hp = hero.hp

        sg = SaveGame()
        sg.save_game("game1", game, curr1.floor, curr1.location, hero)
        game_objects = sg.load_game("game1")

        # test if hero hp is same as before

        self.assertEqual(hero_hp, game_objects[-1].hp, "values don't match.")

        # test if the player is in the same position as before
        floor = game_objects[1]
        row, col = game_objects[2][0], game_objects[2][1]
        curr = game_objects[0][floor].dungeon.maze[row, col]
        self.assertEqual(game_objects[0][floor].print_dungeon_live_location(curr), curr1_map, "values dont match")

    def test_del_game_load_deleted_game(self):
        game = DungeonBuilder.build_single_dungeon()
        row1, col1 = game[0].dungeon.winning_path[2][0], game[0].dungeon.winning_path[2][1]
        curr1 = game[0].dungeon.maze[row1, col1]
        curr1_map = game[0].print_dungeon_live_location(curr1)

        hero = MockHero("hero", "model")
        hero_hp = hero.hp

        sg = SaveGame()
        sg.save_game("game1", game, curr1.floor, curr1.location, hero)
        game_objects = sg.load_game("game1")

        # test if hero hp is same as before

        self.assertEqual(hero_hp, game_objects[-1].hp, "values don't match.")

        # test if the player is in the same position as before
        floor = game_objects[1]
        row, col = game_objects[2][0], game_objects[2][1]
        curr = game_objects[0][floor].dungeon.maze[row, col]
        self.assertEqual(game_objects[0][floor].print_dungeon_live_location(curr), curr1_map, "values dont match")

        sg.delete_saved_game("game1")
        exception_raised = False
        try:
            game_objects = sg.load_game("game1")

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised, "exception not raised")

    def test_delete_invalid_game_name(self):
        sg = SaveGame()
        exception_raised = False
        try:
            sg.delete_saved_game("game1")

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised, "exception not raised")


    def test_save_duplicate_name(self):

        game = DungeonBuilder.build_single_dungeon()
        row1, col1 = game[0].dungeon.winning_path[2][0], game[0].dungeon.winning_path[2][1]
        curr1 = game[0].dungeon.maze[row1, col1]

        hero = MockHero("hero", "model")
        sg = SaveGame()
        sg.save_game("game1", game, curr1.floor, curr1.location, hero)

        game2 = DungeonBuilder.build_single_dungeon()
        row1, col1 = game2[0].dungeon.winning_path[2][0], game2[0].dungeon.winning_path[2][1]
        curr1 = game[0].dungeon.maze[row1, col1]

        hero1 = MockHero("hero", "model")
        exception_raised = False
        try:
            # save a different game with same name "game1" as earlier
            sg.save_game("game1", game2, curr1.floor, curr1.location, hero1)

        except ValueError:
            exception_raised = True

        self.assertEqual(True, exception_raised, "exception not raised")