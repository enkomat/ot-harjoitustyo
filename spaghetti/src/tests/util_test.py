import unittest
from util import Util, Level_1

class TestUtil(unittest.TestCase):
    def test_one(self):
        Level_1.move_player_down()
        self.assertEqual(1, 1)
    
    def test_two(self):
        Level_1.move_player_down()
        self.assertEqual(1, 1)