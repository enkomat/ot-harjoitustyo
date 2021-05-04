import unittest
import math
import pygame
from util import Level_5, Util_Level_5, Util

class TestLevel_5(unittest.TestCase):
    def test_solve_level(self):
        for i in range(2): # try twice to be sure
            lvl5 = Level_5()
            util_lvl_5 = lvl5._Level_5__util_level_5
            self.solve_level(lvl5)
            util_lvl_5.run(True)
            for i in range(len(util_lvl_5.players)):
                self.assertEqual(util_lvl_5.players[i].position_x, 15)
                self.assertEqual(util_lvl_5.players[i].position_y, 15)

    def solve_level(lvl5):
        for player in lvl5.players:
            dist_x = abs(player.get_position_x() - 15)
            dist_y = abs(player.get_position_y() - 15)
            
            for i in range(dist_x):
                if player.get_position_x() > 15:        
                    player.move_left()
                else:
                    player.move_right()
            
            for i in range(dist_y):
                if player.get_position_y() > 15:        
                    player.move_up()
                else:
                    player.move_down()

            player.interact()