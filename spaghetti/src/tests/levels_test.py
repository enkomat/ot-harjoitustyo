import unittest
from utilities.util import Util

class TestLevels(unittest.TestCase):
    def test_solve_level_1(self):
        self.util = Util(True)
        self.util.event_handler.event_execution_speed = 1
        self.util.game_paused = False
        self.load_test_events(self.util.level_index)
        self.run_test()
        
    def run_test(self):
        while self.util.run_game:
            self.util.execute_gameplay()
            if self.util.event_handler.all_events_have_been_executed():
                if self.util.level_index < 10:
                    self.util.level_index += 1
                    self.util.event_handler.event_index = 0
                    self.load_test_events(self.util.level_index)
                    self.util.game_paused = False
                    self.util.level_util.level_solved = False
                else:
                    self.assertFalse(self.util.level_util.level_solved)
                    break

    def load_test_events(self, level_index):
        self.util.event_handler.event_list.clear()
        self.util.event_handler.event_parameter_list.clear()

        if level_index == 0:
            self.load_level_1_test_events()
        elif level_index == 1:
            self.assertTrue(self.util.level_util.level_solved)
            self.load_level_2_test_events()
        elif level_index == 2:
            self.assertTrue(self.util.level_util.level_solved)
            self.load_level_3_test_events()
        elif level_index == 3:
            self.assertTrue(self.util.level_util.level_solved)
            self.load_level_4_test_events()
        elif level_index == 4:
            self.assertTrue(self.util.level_util.level_solved)
            self.load_level_5_test_events()
        elif level_index == 5:
            self.assertTrue(self.util.level_util.level_solved)
            self.load_level_1_test_events_2()
        elif level_index == 6:
            self.assertFalse(self.util.level_util.level_solved)
            self.load_level_2_test_events_2()
        elif level_index == 7:
            self.assertFalse(self.util.level_util.level_solved)
            self.load_level_3_test_events_2()
        elif level_index == 8:
            self.assertFalse(self.util.level_util.level_solved)
            self.load_level_4_test_events_2()
        elif level_index == 9:
            self.assertFalse(self.util.level_util.level_solved)
            self.load_level_5_test_events_2()

        self.util.reset_level()

    def load_level_1_test_events(self):
        self.util.level_util = self.util.levels[0]
        self.util.logic.level_util = self.util.levels[0]
        from tests.level_1_test_solution import Level1TestSolution
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level1TestSolution(self.util.level_util.level)

    def load_level_1_test_events_2(self):
        self.util.level_util = self.util.levels[0]
        self.util.logic.level_util = self.util.levels[0]
        from tests.level_1_test_solution_2 import Level1TestSolution2
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level1TestSolution2(self.util.level_util.level)
    
    def load_level_2_test_events(self):
        self.util.level_util = self.util.levels[1]
        self.util.logic.level_util = self.util.levels[1]
        from tests.level_2_test_solution import Level2TestSolution
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level2TestSolution(self.util.level_util.level)

    def load_level_2_test_events_2(self):
        self.util.level_util = self.util.levels[1]
        self.util.logic.level_util = self.util.levels[1]
        from tests.level_2_test_solution_2 import Level2TestSolution2
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level2TestSolution2(self.util.level_util.level)

    def load_level_3_test_events(self):
        self.util.level_util = self.util.levels[2]
        self.util.logic.level_util = self.util.levels[2]
        from tests.level_3_test_solution import Level3TestSolution
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level3TestSolution(self.util.level_util.level)

    def load_level_3_test_events_2(self):
        self.util.level_util = self.util.levels[2]
        self.util.logic.level_util = self.util.levels[2]
        from tests.level_3_test_solution_2 import Level3TestSolution2
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level3TestSolution2(self.util.level_util.level)
    
    def load_level_4_test_events(self):
        self.util.level_util = self.util.levels[3]
        self.util.logic.level_util = self.util.levels[3]
        from tests.level_4_test_solution import Level4TestSolution
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level4TestSolution(self.util.level_util.level)

    def load_level_4_test_events_2(self):
        self.util.level_util = self.util.levels[3]
        self.util.logic.level_util = self.util.levels[3]
        from tests.level_4_test_solution_2 import Level4TestSolution2
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[1]
        self.util.solution = Level4TestSolution2(self.util.level_util.level)
    
    def load_level_5_test_events(self):
        self.util.level_util = self.util.levels[4]
        self.util.logic.level_util = self.util.levels[4]
        from tests.level_5_test_solution import Level5TestSolution
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[0]
        self.util.solution = Level5TestSolution(self.util.level_util.level)

    def load_level_5_test_events_2(self):
        self.util.level_util = self.util.levels[4]
        self.util.logic.level_util = self.util.levels[4]
        from tests.level_5_test_solution_2 import Level5TestSolution2
        self.util.gui.level_background = self.util.gui.tiles.level_backgrounds[0]
        self.util.solution = Level5TestSolution2(self.util.level_util.level)
        