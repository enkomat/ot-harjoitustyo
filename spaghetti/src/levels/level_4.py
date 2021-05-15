from game_objects.player import Player
from game_objects.door import Door

class Util_Level_4:
    def __init__(self, util):
        self.util = util

        self.p1 = Player(self, 1, 5)
        self.p2 = Player(self, 3, 5)
        self.p3 = Player(self, 5, 5)
        self.p4 = Player(self, 7, 5)
        self.p5 = Player(self, 9, 5)
        self.p6 = Player(self, 11, 5)
        self.p7 = Player(self, 13, 5)
        self.p8 = Player(self, 15, 5)
        self.p9 = Player(self, 17, 5)
        self.p10 = Player(self, 19, 5)
        self.p11 = Player(self, 21, 5)
        self.p12 = Player(self, 23, 5)
        self.p13 = Player(self, 25, 5)
        self.p14 = Player(self, 27, 5)
        self.p15 = Player(self, 29, 5)
        self.p16 = Player(self, 31, 5)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, 
        self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.door = Door(15, 15)
        self.doors = [self.door]

        self.pillars = []

        self.walls = []

        self.level = Level_4(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level_4:
    def __init__(self, level_util):
        self.__util_level_4 = level_util
        self.players = self.__util_level_4.players