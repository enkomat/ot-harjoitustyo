from util import Util, Player, Door

class Util_Level_1:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        player_position_x = pelaajan paikka kartalla x suunnassa
        player_position_y = pelaajan paikka kartalla y suunnassa
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self):
        self.util = Util(self, "Level_1", 40)
        
        self.player = Player(self, 1, 1)
        self.players = [self.player]
        
        self.door = Door(30, 30)
        self.doors = [self.door]

    def run(self, is_test=False):
        self.util.run(is_test)

class Level_1:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self):
        self.__util_level_1 = Util_Level_1()
        self.player = self.__util_level_1.player

    def run(self):
        """Laittaa pelin pyörimään. Poistaa pelaajalta mahdollisuuden suorittaa peliluuppi testimoodissa.
        """
        self.__util_level_1.run()
