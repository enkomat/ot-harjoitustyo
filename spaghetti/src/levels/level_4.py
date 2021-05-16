from game_objects.player import Player
from game_objects.door import Door

class UtilLevel4:
    def __init__(self, util):
        self.util = util
        self.level_solved = False

        self.p_1 = Player(self, 1, 5)
        self.p_2 = Player(self, 3, 5)
        self.p_3 = Player(self, 5, 5)
        self.p_4 = Player(self, 7, 5)
        self.p_5 = Player(self, 9, 5)
        self.p_6 = Player(self, 11, 5)
        self.p_7 = Player(self, 13, 5)
        self.p_8 = Player(self, 15, 5)
        self.p_9 = Player(self, 17, 5)
        self.p_10 = Player(self, 19, 5)
        self.p_11 = Player(self, 21, 5)
        self.p_12 = Player(self, 23, 5)
        self.p_13 = Player(self, 25, 5)
        self.p_14 = Player(self, 27, 5)
        self.p_15 = Player(self, 29, 5)
        self.p_16 = Player(self, 31, 5)
        self.players = [self.p_1, self.p_2, self.p_3, self.p_4, self.p_5, self.p_6, self.p_7, self.p_8,
        self.p_9, self.p_10, self.p_11, self.p_12, self.p_13, self.p_14, self.p_15, self.p_16]

        self.door = Door(15, 15)
        self.doors = [self.door]

        self.pillars = []

        self.walls = []

        self.level = Level4(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level4:
    def __init__(self, level_util):
        self.__util_level_4 = level_util
        self.players = self.__util_level_4.players