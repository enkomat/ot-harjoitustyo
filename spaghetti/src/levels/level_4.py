from game_objects.player import Player
from game_objects.door import Door

class Util_Level_4:
    def __init__(self, util):
        self.util = util

        self.p1 = Player(self, 1, 1)
        self.p2 = Player(self, 3, 1)
        self.p3 = Player(self, 5, 1)
        self.p4 = Player(self, 7, 1)
        self.p5 = Player(self, 9, 1)
        self.p6 = Player(self, 11, 1)
        self.p7 = Player(self, 13, 1)
        self.p8 = Player(self, 15, 1)
        self.p9 = Player(self, 17, 1)
        self.p10 = Player(self, 19, 1)
        self.p11 = Player(self, 21, 1)
        self.p12 = Player(self, 23, 1)
        self.p13 = Player(self, 25, 1)
        self.p14 = Player(self, 27, 1)
        self.p15 = Player(self, 29, 1)
        self.p16 = Player(self, 31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, 
        self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.door = Door(15, 15)
        self.doors = [self.door]

        self.pillars = []

        self.walls = []

        self.level = Level_4(self)

class Level_4:
    def __init__(self, level_util):
        self.__util_level_4 = level_util
        self.players = self.__util_level_4.players