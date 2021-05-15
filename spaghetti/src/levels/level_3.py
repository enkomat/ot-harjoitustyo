from game_objects.player import Player
from game_objects.door import Door

class Util_Level_3:
    def __init__(self, util):
        self.util = util
        
        self.p1 = Player(self, 1, 5)
        self.p2 = Player(self, 3, 25)
        self.p3 = Player(self, 5, 5)
        self.p4 = Player(self, 7, 25)
        self.p5 = Player(self, 9, 5)
        self.p6 = Player(self, 11, 25)
        self.p7 = Player(self, 13, 5)
        self.p8 = Player(self, 15, 25)
        self.p9 = Player(self, 17, 5)
        self.p10 = Player(self, 19, 25)
        self.p11 = Player(self, 21, 5)
        self.p12 = Player(self, 23, 25)
        self.p13 = Player(self, 25, 5)
        self.p14 = Player(self, 27, 25)
        self.p15 = Player(self, 29, 5)
        self.p16 = Player(self, 31, 25)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = Door(1, 25)
        self.g2 = Door(3, 5)
        self.g3 = Door(5, 25)
        self.g4 = Door(7, 5)
        self.g5 = Door(9, 25)
        self.g6 = Door(11, 5)
        self.g7 = Door(13, 25)
        self.g8 = Door(15, 5)
        self.g9 = Door(17, 25)
        self.g10 = Door(19, 5)
        self.g11 = Door(21, 25)
        self.g12 = Door(23, 5)
        self.g13 = Door(25, 25)
        self.g14 = Door(27, 5)
        self.g15 = Door(29, 25)
        self.g16 = Door(31, 5)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

        self.pillars = []

        self.walls = []

        self.level = Level_3(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level_3:
    def __init__(self, level_util):
        self.__util_level_3 = level_util
        self.players = self.__util_level_3.players