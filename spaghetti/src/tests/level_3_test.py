import unittest
import pygame
import levels
from levels.level_3 import Level_3

class TestLevel_3(unittest.TestCase):
    def test_move_players_right(self):
        lvl3 = Level_3() 
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_x = []
        for player in util_lvl_3.players:
            start_positions_x.append(player._Player__position_x)
        for player in lvl3.players:
            player.move_right()
        util_lvl_3.run(True)
        for player, start_position_x in zip(lvl3.players, start_positions_x):
            self.assertEqual(player._Player__position_x, start_position_x + 1)

    def test_move_players_left(self):
        lvl3 = Level_3()
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_x = []
        for player in util_lvl_3.players:
            start_positions_x.append(player._Player__position_x)
        for player in lvl3.players:
            player.move_left()
        util_lvl_3.run(True)
        for player, start_position_x in zip(lvl3.players, start_positions_x):
            self.assertEqual(player._Player__position_x, start_position_x - 1)
    
    def test_solve_level(self):
        lvl3 = Level_3()
        util_lvl_3 = lvl3._Level_3__util_level_3
        start_positions_y = []
        for player in util_lvl_3.players:
            start_positions_y.append(player._Player__position_y)
        for i in range(len(util_lvl_3.players)):
            for n in range(29):
                if i % 2 == 0:
                    lvl3.players[i].move_down()
                else:
                    lvl3.players[i].move_up()
            lvl3.players[i].interact()
        util_lvl_3.run(True)
        for i in range(len(util_lvl_3.players)):
            if i % 2 == 0:
                self.assertEqual(util_lvl_3.players[i]._Player__position_y, start_positions_y[i] + 29)
            else:
                self.assertEqual(util_lvl_3.players[i]._Player__position_y, start_positions_y[i] - 29)