import unittest
import pygame
from util import Level_2, Util_Level_2, Util

class TestLevel_2(unittest.TestCase):
    def test_move_players_down(self):
        lvl2 = Level_2()
        util_lvl_2 = lvl2._Level_2__util_level_2
        start_positions_y = []
        for player in util_lvl_2.players:
            start_positions_y.append(player._Player__position_y)
        for player in lvl2.players:
                player.move_down()
        util_lvl_2.run(True)
        for i in range(len(util_lvl_2.players)):
            self.assertEqual(util_lvl_2.players[i]._Player__position_y, start_positions_y[i] + 1)
    
    def test_solve_level(self):
        lvl2 = Level_2()
        util_lvl_2 = lvl2._Level_2__util_level_2
        start_positions_y = []
        for player in lvl2.players:
            start_positions_y.append(player._Player__position_y)
        for player in lvl2.players:
            for i in range(29):
                player.move_down()
            player.interact()
        util_lvl_2.run(True)
        for i in range(len(lvl2.players)):
            self.assertEqual(lvl2.players[i]._Player__position_y, start_positions_y[i] + 29)