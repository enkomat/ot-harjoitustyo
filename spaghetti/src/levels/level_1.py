from game_objects.player import Player
from game_objects.door import Door

class UtilLevel1:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self, util):
        self.util = util
        self.level_solved = False

        self.player = Player(self, 1, 1)
        self.players = [self.player]

        self.door = Door(29, 15)
        self.doors = [self.door]

        self.walls = []

        self.pillars = []

        self.level = Level1(self)

    def level_win_condition_satisfied(self):
        return self.player._Player__position_x == self.doors[0]._Door__position_x and self.player._Player__position_y == self.doors[0]._Door__position_y and self.player._Player__has_interacted

class Level1:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self, level_util):
        self.__util_level_1 = level_util
        self.player = self.__util_level_1.player
        self.door = self.__util_level_1.door

