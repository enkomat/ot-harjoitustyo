import unittest
import pygame
import time
from util import Level_1, Util_Level_1, Util

class TestLevel_1(unittest.TestCase):
    def test_solve_level(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player._Player__position_x
        player_start_y = util_lvl_1.player._Player__position_x
        for i in range(29):
            lvl1.player.move_down()
            lvl1.player.move_right()
        lvl1.player.interact()
        util_lvl_1.run(True)
        self.assertEqual(util_lvl_1.player._Player__position_y, player_start_y + 29)
        self.assertEqual(util_lvl_1.player._Player__position_x, player_start_x + 29)