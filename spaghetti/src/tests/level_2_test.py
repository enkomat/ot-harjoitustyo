import unittest
from levels.level_2 import Level_2

class TestLevel_2(unittest.TestCase):
    def test_solve_level(self):
        lvl2 = Level_2()
        util_lvl_2 = lvl2._Level_2__util_level_2
        
        util_lvl_2.run()
        self.assertEqual(True, False)