from dungeon import Dungeon
from room import Room
import unittest


class MyTestCase(unittest.TestCase):
    def test__set_rowCount(self):
        dun = Dungeon(4, 4)
        self.assertEqual(4, dun.row_Count, "row count does not match")

    def test__set_colCount(self):
        dun = Dungeon(4, 4)
        self.assertEqual(4, dun.col_Count, "col count does not match")

    def test_enter_dungeon(self):
        dun = Dungeon(4, 4)
        enter = dun.enter_dungeon()
        self.assertEqual(enter.is_entrance, True, "not in the entrance room")

if __name__ == '__main__':
    unittest.main()
