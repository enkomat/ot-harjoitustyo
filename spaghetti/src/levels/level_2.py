from game_objects.player import Player
from game_objects.door import Door

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
        
        self.player1 = Player(self, 2, 21)
        self.player2 = Player(self, 2, 18)
        self.player3 = Player(self, 2, 15)
        self.player4 = Player(self, 2, 12)
        self.player5 = Player(self, 2, 9)
        self.players = [self.player1, self.player2, self.player3, self.player4, self.player5]
        
        self.door1 = Door(29, 21)
        self.door2 = Door(29, 18)
        self.door3 = Door(29, 15)
        self.door4 = Door(29, 12)
        self.door5 = Door(29, 9)
        self.doors = [self.door1, self.door2, self.door3, self.door4, self.door5]

        self.walls = []

        self.pillars = []

        self.level = Level_2(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level_2:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self, level_util):
        self.__util_level_2 = level_util
        self.players = self.__util_level_2.players
        self.doors = self.__util_level_2.doors