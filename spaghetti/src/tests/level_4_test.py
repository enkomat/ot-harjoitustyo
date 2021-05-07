import unittest
import pygame
import levels
from levels.level_4 import Level_4

class TestLevel_4(unittest.TestCase):
    
    def test_solve_level(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        n = 14
        go_right = True
        
        for player in lvl4.players:
            for y in range(14):
                player.move_down()
            for x in range(n):
                if go_right:
                    player.move_right()
                else:
                    player.move_left()
            if go_right:
                n -= 2
            else:
                n += 2
            if n == 0:
                go_right = False
            player.interact()
        
        util_lvl_4.run(True)
        for player in lvl4.players:
            self.assertEqual(player._Player__position_x, 15)
            self.assertEqual(player._Player__position_y, 15)