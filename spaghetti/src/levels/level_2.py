from util import *
import random

class Util_Level_2:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        player_position_x = pelaajan paikka kartalla x suunnassa
        player_position_y = pelaajan paikka kartalla y suunnassa
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self):
        self.util = Util(self, "Level_2", 40)
        
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
        self.level_win_condition_satisfied()

    def level_win_condition_satisfied(self):
        return False

    def run(self, is_test=False):
        self.util.run(is_test)

class Level_2:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self):
        self.__util_level_2 = Util_Level_2()
        self.player = self.__util_level_2.player
        self.pillars = self.__util_level_2.pillars

    def run(self):
        """Laittaa pelin pyörimään. Poistaa pelaajalta mahdollisuuden suorittaa peliluuppi testimoodissa.
        """
        self.__util_level_2.run()
