from util import Util, Game_Event

class Player:
    """Myöhemmissä tasoissa käytetty luokka, joka mahdollistaa sen, että tasoa ratkottaesta voi ohjata useampaa pelaajaa.
    """
    def __init__(self, level_util, position_x, position_y):
        self.__level_util = level_util
        self.__util = self.__level_util.util
        self.__position_x = position_x
        self.__position_y = position_y
        self.__has_interacted = False
        self.__draw_player = True

    def move_left(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_LEFT, self)

    def move_right(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_RIGHT, self)

    def move_up(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_UP, self)

    def move_down(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_DOWN, self)

    def interact(self):
        self.__util.add_to_event_list(Game_Event.PLAYER_INTERACT, self)

    def get_position_x(self):
        return self.__position_x

    def get_position_y(self):
        return self.__position_y

class Door:
    """Luo oven jonka paikan pelaaja voi hakea.
    """
    def __init__(self, position_x, position_y):
        self.__position_x = position_x
        self.__position_y = position_y
        self.__is_open = False
    
    def get_position_x(self):
        return self.__position_x
    
    def get_position_y(self):
        return self.__position_y