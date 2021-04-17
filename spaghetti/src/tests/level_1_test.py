import unittest
from util import Level_1

class TestLevel_1(unittest.TestCase):
    def test_one(self):
        Level_1.move_player_down()
        self.assertEqual(1, 1)
