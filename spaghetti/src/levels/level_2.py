from game_objects.player import Player
from game_objects.door import Door

class UtilLevel2:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        player_position_x = pelaajan paikka kartalla x suunnassa
        player_position_y = pelaajan paikka kartalla y suunnassa
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self, util):
        self.util = util
        self.level_solved = False

        self.player_1 = Player(self, 2, 21)
        self.player_2 = Player(self, 2, 18)
        self.player_3 = Player(self, 2, 15)
        self.player_4 = Player(self, 2, 12)
        self.player_5 = Player(self, 2, 9)
        self.players = [self.player_1, self.player_2, self.player_3, self.player_4, self.player_5]

        self.door_1 = Door(29, 21)
        self.door_2 = Door(29, 18)
        self.door_3 = Door(29, 15)
        self.door_4 = Door(29, 12)
        self.door_5 = Door(29, 9)
        self.doors = [self.door_1, self.door_2, self.door_3, self.door_4, self.door_5]

        self.walls = []

        self.pillars = []

        self.level = Level2(self)

    def level_win_condition_satisfied(self):
        for player in self.players:
            went_through_door = False
            for door in self.doors:
                if player._Player__position_x == door._Door__position_x and player._Player__position_y == door._Door__position_y and player._Player__has_interacted:
                    went_through_door = True
            if went_through_door == False:
                return False
        return True

class Level2:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self, level_util):
        self.__util_level_2 = level_util
        self.players = self.__util_level_2.players
        self.doors = self.__util_level_2.doors