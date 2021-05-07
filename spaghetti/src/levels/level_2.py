from util import Util
from gameobjects import *

class Util_Level_2:
    """Toisen tason työkalupakkiluokka.

    Attributes:
        players: kaikki pelaajat listassa
        doors: kaikki ovet listassa
    """
    def __init__(self):
        self.util = Util(self, "Level_2")

        self.p1 = Player(self, 1, 1)
        self.p2 = Player(self, 3, 1)
        self.p3 = Player(self, 5, 1)
        self.p4 = Player(self, 7, 1)
        self.p5 = Player(self, 9, 1)
        self.p6 = Player(self, 11, 1)
        self.p7 = Player(self, 13, 1)
        self.p8 = Player(self, 15, 1)
        self.p9 = Player(self, 17, 1)
        self.p11 = Player(self, 21, 1)
        self.p10 = Player(self, 19, 1)
        self.p12 = Player(self, 23, 1)
        self.p13 = Player(self, 25, 1)
        self.p14 = Player(self, 27, 1)
        self.p15 = Player(self, 29, 1)
        self.p16 = Player(self, 31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = Door(1, 30)
        self.g2 = Door(3, 30)
        self.g3 = Door(5, 30)
        self.g4 = Door(7, 30)
        self.g5 = Door(9, 30)
        self.g6 = Door(11, 30)
        self.g7 = Door(13, 30)
        self.g8 = Door(15, 30)
        self.g9 = Door(17, 30)
        self.g10 = Door(19, 30)
        self.g11 = Door(21, 30)
        self.g12 = Door(23, 30)
        self.g13 = Door(25, 30)
        self.g14 = Door(27, 30)
        self.g15 = Door(29, 30)
        self.g16 = Door(31, 30)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def run(self, is_test=False):
        self.util.run(is_test)

class Level_2:
    """Toisen tason ratkomiseen tarkoitettu luokka.
    """
    def __init__(self):
        self.__util_level_2 = Util_Level_2()
        self.players = self.__util_level_2.players

    def run(self):
        self.__util_level_2.run()
