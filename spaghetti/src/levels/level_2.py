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

        self.player = Player(self, 15, 15)
        self.players = [self.player]
        
        self.walls = []

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
