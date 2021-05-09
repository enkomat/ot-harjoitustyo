import unittest
from levels.level_1 import Level_1

class TestLevel_1(unittest.TestCase):
    def test_solve_level(self):
        lvl1 = Level_1()
        util_lvl_1 = lvl1._Level_1__util_level_1
        player_start_x = util_lvl_1.player._Player__position_x
        player_start_y = util_lvl_1.player._Player__position_x
        for i in range(4):
            lvl1.player.move_left()
            lvl1.player.build_wall()
        for i in range(4):
            lvl1.player.move_up()
            lvl1.player.build_wall()
        for i in range(3):
            lvl1.player.move_right()
            lvl1.player.build_wall()
        for i in range(3):
            lvl1.player.move_left()
        for i in range(6):
            lvl1.player.move_left()
            lvl1.player.build_wall()
        for i in range(6):
            lvl1.player.move_up()
            lvl1.player.build_wall()
        for i in range(10):
            lvl1.player.move_right()
            lvl1.player.build_wall()
        for i in range(10):
            lvl1.player.move_down()
            lvl1.player.build_wall()
        
        lvl1.player.move_down()
        util_lvl_1.run()