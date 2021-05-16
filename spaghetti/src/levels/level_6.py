import random
from game_objects.player import Player
from game_objects.pillar import Pillar

class UtilLevel6:
    def __init__(self, util):
        self.util = util
        self.level_solved = False
        
        self.player = Player(self, 27, 27)
        self.players = [self.player]
        
        self.doors = []

        self.walls = []

        self.pillars = []
        self.randomize_pillars()

        self.level = Level6(self)

    def randomize_pillars(self):
        self.pillars.clear()
        random_x_left = random.randint(10, 15)
        random_x_right = random.randint(17, 25)
        random_y_top = random.randint(10, 15)
        random_y_bottom = random.randint(17, 25)

        self.p_0 = Pillar(random_x_right, random_y_bottom)
        self.p_1 = Pillar(random_x_left, random_y_bottom)
        self.p_2 = Pillar(random_x_left, random_y_top)
        self.p_3 = Pillar(random_x_right, random_y_top)
        self.pillars = [self.p_0, self.p_1, self.p_2, self.p_3]

    def level_win_condition_satisfied(self):
        return False

class Level6:
    def __init__(self, level_util):
        self.__util_level_6 = level_util
        self.player = self.__util_level_6.player
        self.pillars = self.__util_level_6.pillars