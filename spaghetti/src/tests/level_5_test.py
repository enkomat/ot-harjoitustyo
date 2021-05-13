import unittest
from levels.level_5 import Level_5

class TestLevel_5(unittest.TestCase):
    def test_solve_level(self):
        for i in range(2): # try twice to be sure
            lvl5 = Level_5()
            util_lvl_5 = lvl5._Level_5__util_level_5
            
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

            util_lvl_5.run(True)
            for player in lvl5.players:
                self.assertEqual(player.get_position_x(), 15)
                self.assertEqual(player.get_position_y(), 15)
        