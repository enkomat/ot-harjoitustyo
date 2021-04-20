import unittest
import pygame
import time
from util import Level_1, Util_Level_1, Util


class TestLevel_1(unittest.TestCase):
    util_lvl_1 = Util_Level_1()
    lvl1 = Level_1()

    def test_move_player_down(self):
        player_start_x = self.util_lvl_1.player_position_x
        player_start_y = self.util_lvl_1.player_position_y
        self.lvl1.move_player_down()
        self.lvl1.move_player_down()
        self.lvl1.move_player_down()
        self.lvl1.move_player_down()
        self.lvl1.run(True)
        print(self.util_lvl_1.player_position_x)
        print(self.util_lvl_1.player_position_y)
        self.assertEqual(self.util_lvl_1.player_position_x, player_start_x)
        self.assertEqual(self.util_lvl_1.player_position_y, player_start_y + 4)

    def test_move_player_up(self):
        player_start_x = self.util_lvl_1.player_position_x
        player_start_y = self.util_lvl_1.player_position_y
        self.lvl1.move_player_up()
        self.lvl1.move_player_up()
        self.lvl1.run(True)
        print(self.util_lvl_1.player_position_x)
        print(self.util_lvl_1.player_position_y)
        self.assertEqual(self.util_lvl_1.player_position_x, player_start_x)
        self.assertEqual(self.util_lvl_1.player_position_y, player_start_y - 2)

    def test_move_player_right(self):
        player_start_x = self.util_lvl_1.player_position_x
        player_start_y = self.util_lvl_1.player_position_y
        self.lvl1.move_player_right()
        self.lvl1.move_player_right()
        self.lvl1.move_player_right()
        self.lvl1.move_player_right()
        self.lvl1.run(True)
        print(self.util_lvl_1.player_position_x)
        print(self.util_lvl_1.player_position_y)
        self.assertEqual(self.util_lvl_1.player_position_x, player_start_x + 4)
        self.assertEqual(self.util_lvl_1.player_position_y, player_start_y)

    def test_move_player_left(self):
        player_start_x = self.util_lvl_1.player_position_x
        player_start_y = self.util_lvl_1.player_position_y
        self.lvl1.move_player_left()
        self.lvl1.move_player_left()
        self.lvl1.move_player_left()
        self.lvl1.move_player_left()
        self.lvl1.run(True)
        self.assertEqual(self.util_lvl_1.player_position_x, player_start_x - 4)
        self.assertEqual(self.util_lvl_1.player_position_y, player_start_y)
