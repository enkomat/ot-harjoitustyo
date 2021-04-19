import unittest
import pygame
from util import Level_1, Util_Level_1, Util

class TestLevel_1(unittest.TestCase):
    def test_move_player_down(self):
        player_start_x = Util_Level_1.player_position_x
        player_start_y = Util_Level_1.player_position_y
        Level_1.move_player_down()
        Level_1.move_player_down()
        Level_1.move_player_down()
        Level_1.move_player_down()
        print(Util_Level_1.player_position_x)
        print(Util_Level_1.player_position_y)
        self.assertEqual(player_start_x, player_start_x)
        self.assertEqual(player_start_y, player_start_y + 4)

    def test_move_player_up(self):
        player_start_x = Util_Level_1.player_position_x
        player_start_y = Util_Level_1.player_position_y
        Level_1.move_player_up()
        Level_1.move_player_up()
        print(Util_Level_1.player_position_x)
        print(Util_Level_1.player_position_y)
        self.assertEqual(player_start_x, player_start_x)
        self.assertEqual(player_start_y, player_start_y - 2)

    def test_move_player_right(self):
        player_start_x = Util_Level_1.player_position_x
        player_start_y = Util_Level_1.player_position_y
        Level_1.move_player_right()
        Level_1.move_player_right()
        Level_1.move_player_right()
        Level_1.move_player_right()
        print(Util_Level_1.player_position_x)
        print(Util_Level_1.player_position_y)
        self.assertEqual(player_start_x, player_start_x + 4)
        self.assertEqual(player_start_y, player_start_y)

    def test_move_player_left(self):
        player_start_x = Util_Level_1.player_position_x
        player_start_y = Util_Level_1.player_position_y
        Level_1.move_player_left()
        Level_1.move_player_left()
        Level_1.move_player_left()
        Level_1.move_player_left()
        self.assertEqual(player_start_x, player_start_x - 4)
        self.assertEqual(player_start_y, player_start_y)

    # This method should come last
    def test_run_level(self):
        Util_Level_1.run(True)
