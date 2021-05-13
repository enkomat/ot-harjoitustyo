from game_objects import *
import random

class Util_Level_2:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        player_position_x = pelaajan paikka kartalla x suunnassa
        player_position_y = pelaajan paikka kartalla y suunnassa
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self, util):
        self.util = util
        
        self.player = Player(self, 27, 27)
        self.players = [self.player]
        
        self.doors = []

        self.walls = []

        random_x_left = random.randint(10, 15)
        random_x_right = random.randint(17, 25)
        random_y_top = random.randint(10, 15)
        random_y_bottom = random.randint(17, 25)

        self.p0 = Pillar(random_x_right, random_y_bottom)
        self.p1 = Pillar(random_x_left, random_y_bottom)
        self.p2 = Pillar(random_x_left, random_y_top)
        self.p3 = Pillar(random_x_right, random_y_top)
        self.pillars = [self.p0, self.p1, self.p2, self.p3]

        self.level = Level_2(self)

    def level_win_condition_satisfied(self):
        return False

class Level_2:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self, level_util):
        self.__util_level_2 = level_util
        self.player = self.__util_level_2.player
        self.pillars = self.__util_level_2.pillars