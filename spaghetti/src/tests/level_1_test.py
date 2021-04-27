import unittest
import pygame
import time
from util import Level_1, Util_Level_1, Util

class TestLevel_1(unittest.TestCase):
    def test_move_player_down(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player_position_x
        player_start_y = util_lvl_1.player_position_y
        lvl1.move_player_down()
        lvl1.move_player_down()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player_position_x, player_start_x)
        self.assertEqual(util_lvl_1.player_position_y, player_start_y + 2)

    def test_move_player_down_up(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player_position_x
        player_start_y = util_lvl_1.player_position_y
        lvl1.move_player_down()
        lvl1.move_player_down()
        lvl1.move_player_down()
        lvl1.move_player_down()
        lvl1.move_player_up()
        lvl1.move_player_up()
        lvl1.move_player_up()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player_position_x, player_start_x)
        self.assertEqual(util_lvl_1.player_position_y, player_start_y + 1)

    def test_move_player_right(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player_position_x
        player_start_y = util_lvl_1.player_position_y
        lvl1.move_player_right()
        lvl1.move_player_right()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player_position_x, player_start_x + 2)
        self.assertEqual(util_lvl_1.player_position_y, player_start_y)

    def test_move_player_right_left(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player_position_x
        player_start_y = util_lvl_1.player_position_y
        lvl1.move_player_right()
        lvl1.move_player_right()
        lvl1.move_player_right()
        lvl1.move_player_left()
        lvl1.move_player_left()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player_position_x, player_start_x + 1)
        self.assertEqual(util_lvl_1.player_position_y, player_start_y)

    def test_solve_level(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player_position_x
        player_start_y = util_lvl_1.player_position_y
        for i in range(29):
            lvl1.move_player_down()
            lvl1.move_player_right()
        lvl1.player_interact()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player_position_x, player_start_x + 29)
        self.assertEqual(util_lvl_1.player_position_y, player_start_y + 29)