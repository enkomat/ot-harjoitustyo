import random
from game_objects import *

class Util_Level_5:
    def __init__(self, util):
        self.util = util
        
        self.random_positions = []
        for i in range(16):
            x = random.choice([i for i in range(1,30) if i not in [15]])
            y = random.choice([i for i in range(1,30) if i not in [15]])
            self.random_positions.append((x, y))

        self.__p1 = Player(self, self.random_positions[0][0], self.random_positions[0][1])
        self.__p2 = Player(self, self.random_positions[1][0], self.random_positions[1][1])
        self.__p3 = Player(self, self.random_positions[2][0], self.random_positions[2][1])
        self.__p4 = Player(self, self.random_positions[3][0], self.random_positions[3][1])
        self.__p5 = Player(self, self.random_positions[4][0], self.random_positions[4][1])
        self.__p6 = Player(self, self.random_positions[5][0], self.random_positions[5][1])
        self.__p7 = Player(self, self.random_positions[6][0], self.random_positions[6][1])
        self.__p8 = Player(self, self.random_positions[7][0], self.random_positions[7][1])
        self.__p9 = Player(self, self.random_positions[8][0], self.random_positions[8][1])
        self.__p10 = Player(self, self.random_positions[9][0], self.random_positions[9][1])
        self.__p11 = Player(self, self.random_positions[10][0], self.random_positions[10][1])
        self.__p12 = Player(self, self.random_positions[11][0], self.random_positions[11][1])
        self.__p13 = Player(self, self.random_positions[12][0], self.random_positions[11][1])
        self.__p14 = Player(self, self.random_positions[13][0], self.random_positions[12][1])
        self.__p15 = Player(self, self.random_positions[14][0], self.random_positions[13][1])
        self.__p16 = Player(self, self.random_positions[15][0], self.random_positions[14][1])
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
               self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

        self.door = Door(15, 15)
        self.doors = [self.door]

        self.walls = []
        
        self.level = Level_5(self)

class Level_5:
    def __init__(self, level_util):
        self.__util_level_5 = level_util
        self.players = self.__util_level_5.players
