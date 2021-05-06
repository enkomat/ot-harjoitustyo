import unittest
import pygame
from util import Level_4, Util_Level_4, Util

class TestLevel_4(unittest.TestCase):
    def test_move_players_right(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_x = []
        for player in util_lvl_4.players:
            start_positions_x.append(player._Player__position_x)
        for player in lvl4.players:
            player.move_right()
        util_lvl_4.run(True)
        for player, start_position_x in zip(lvl4.players, start_positions_x):
            self.assertEqual(player._Player__position_x, start_position_x + 1)

    def test_move_players_left(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_x = []
        for player in util_lvl_4.players:
            start_positions_x.append(player._Player__position_x)
        for player in lvl4.players:
            player.move_left()
        util_lvl_4.run(True)
        for player, start_position_x in zip(lvl4.players, start_positions_x):
            self.assertEqual(player._Player__position_x, start_position_x - 1)
    
    def test_solve_level(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_y = []
        for player in util_lvl_4.players:
            start_positions_y.append(player._Player__position_y)
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