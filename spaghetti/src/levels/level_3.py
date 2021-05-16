from game_objects.player import Player
from game_objects.door import Door

class UtilLevel3:
    def __init__(self, util):
        self.util = util
        self.level_solved = False

        self.p_1 = Player(self, 1, 5)
        self.p_2 = Player(self, 3, 25)
        self.p_3 = Player(self, 5, 5)
        self.p_4 = Player(self, 7, 25)
        self.p_5 = Player(self, 9, 5)
        self.p_6 = Player(self, 11, 25)
        self.p_7 = Player(self, 13, 5)
        self.p_8 = Player(self, 15, 25)
        self.p_9 = Player(self, 17, 5)
        self.p_10 = Player(self, 19, 25)
        self.p_11 = Player(self, 21, 5)
        self.p_12 = Player(self, 23, 25)
        self.p_13 = Player(self, 25, 5)
        self.p_14 = Player(self, 27, 25)
        self.p_15 = Player(self, 29, 5)
        self.p_16 = Player(self, 31, 25)
        self.players = [self.p_1, self.p_2, self.p_3, self.p_4, self.p_5, self.p_6, self.p_7, self.p_8,
               self.p_9, self.p_10, self.p_11, self.p_12, self.p_13, self.p_14, self.p_15, self.p_16]

        self.g_1 = Door(1, 25)
        self.g_2 = Door(3, 5)
        self.g_3 = Door(5, 25)
        self.g_4 = Door(7, 5)
        self.g_5 = Door(9, 25)
        self.g_6 = Door(11, 5)
        self.g_7 = Door(13, 25)
        self.g_8 = Door(15, 5)
        self.g_9 = Door(17, 25)
        self.g_10 = Door(19, 5)
        self.g_11 = Door(21, 25)
        self.g_12 = Door(23, 5)
        self.g_13 = Door(25, 25)
        self.g_14 = Door(27, 5)
        self.g_15 = Door(29, 25)
        self.g_16 = Door(31, 5)
        self.doors = [self.g_1, self.g_2, self.g_3, self.g_4, self.g_5, self.g_6, self.g_7, self.g_8,
             self.g_9, self.g_10, self.g_11, self.g_12, self.g_13, self.g_14, self.g_15, self.g_16]

        self.pillars = []

        self.walls = []

        self.level = Level3(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level3:
    def __init__(self, level_util):
        self.__util_level_3 = level_util
        self.players = self.__util_level_3.players