import unittest
import pygame
import time
from util import Level_3, Util_Level_3, Util

class TestLevel_3(unittest.TestCase):
    def test_move_players_right(self):
        lvl3 = Level_3()
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_x = []
        for player in util_lvl_3.players:
            start_positions_x.append(player.position_x)
        for player in lvl3.players:
            player.move_player_right()
        util_lvl_3.run(True)
        for i in range(len(util_lvl_3.players)):
            self.assertEqual(util_lvl_3.players[i].position_x, start_positions_x[i] + 1)

    def test_move_players_left(self):
        lvl3 = Level_3()
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_x = []
        for player in util_lvl_3.players:
            start_positions_x.append(player.position_x)
        for player in lvl3.players:
            player.move_player_left()
        util_lvl_3.run(True)
        for i in range(len(util_lvl_3.players)):
            self.assertEqual(util_lvl_3.players[i].position_x, start_positions_x[i] - 1)
    
    def test_solve_level(self):
        lvl3 = Level_3()
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_y = []
        for player in util_lvl_3.players:
            start_positions_y.append(player.position_y)
        for i in range(len(util_lvl_3.players)):
            for n in range(29):
                if i % 2 == 0:
                    lvl3.players[i].move_player_down()
                else:
                    lvl3.players[i].move_player_up()
            lvl3.players[i].interact()
        util_lvl_3.run(True)
        for i in range(len(util_lvl_3.players)):
            if i % 2 == 0:
                self.assertEqual(util_lvl_3.players[i].position_y, start_positions_y[i] + 29)
            else:
                self.assertEqual(util_lvl_3.players[i].position_y, start_positions_y[i] - 29)