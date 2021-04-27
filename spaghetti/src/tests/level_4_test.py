import unittest
import pygame
import time
from util import Level_4, Util_Level_4, Util

class TestLevel_4(unittest.TestCase):
    def test_move_players_right(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_x = []
        for player in util_lvl_4.players:
            start_positions_x.append(player.position_x)
        for player in lvl4.players:
            player.move_player_right()
        util_lvl_4.run(True)
        for i in range(len(util_lvl_4.players)):
            self.assertEqual(util_lvl_4.players[i].position_x, start_positions_x[i] + 1)

    def test_move_players_left(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_x = []
        for player in util_lvl_4.players:
            start_positions_x.append(player.position_x)
        for player in lvl4.players:
            player.move_player_left()
        util_lvl_4.run(True)
        for i in range(len(util_lvl_4.players)):
            self.assertEqual(util_lvl_4.players[i].position_x, start_positions_x[i] - 1)
    
    def test_solve_level(self):
        lvl4 = Level_4()
        util_lvl_4 = lvl4._Level_4__util_level_4
        start_positions_y = []
        for player in util_lvl_4.players:
            start_positions_y.append(player.position_y)
        n = 14
        go_right = True
        for i in range(len(util_lvl_4.players)):
            for y in range(14):
                lvl4.players[i].move_player_down()
            for x in range(n):
                if go_right:
                    lvl4.players[i].move_player_right()
                else:
                    lvl4.players[i].move_player_left()
            if go_right:
                n -= 2
            else:
                n += 2
            if n == 0:
                go_right = False
            lvl4.players[i].interact()
        util_lvl_4.run(True)
        for i in range(len(util_lvl_4.players)):
            self.assertEqual(util_lvl_4.players[i].position_x, 15)
            self.assertEqual(util_lvl_4.players[i].position_y, 15)