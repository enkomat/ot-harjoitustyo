from enum_types.event_type import Event_Type

class Player:
    """Myöhemmissä tasoissa käytetty luokka, joka mahdollistaa sen, että tasoa ratkottaesta voi ohjata useampaa pelaajaa.
    """
    def __init__(self, level_util, position_x, position_y):
        self.__level_util = level_util
        self.__util = self.__level_util.util
        self.__original_x = position_x
        self.__original_y = position_y
        self.__position_x = position_x
        self.__position_y = position_y
        self.__has_interacted = False
        self.__draw_player = True

    def move_left(self):
        self.__util.event_handler.add_new_event(Event_Type.MOVE_PLAYER_LEFT, self)

    def move_right(self):
        self.__util.event_handler.add_new_event(Event_Type.MOVE_PLAYER_RIGHT, self)

    def move_up(self):
        self.__util.event_handler.add_new_event(Event_Type.MOVE_PLAYER_UP, self)

    def move_down(self):
        self.__util.event_handler.add_new_event(Event_Type.MOVE_PLAYER_DOWN, self)

    def interact(self):
        self.__util.event_handler.add_new_event(Event_Type.PLAYER_INTERACT, self)

    def build_wall(self):
        self.__util.event_handler.add_new_event(Event_Type.PLAYER_BUILD_WALL, self)
    
    def build_door(self):
        self.__util.event_handler.add_new_event(Event_Type.PLAYER_BUILD_DOOR, self)

    def get_position_x(self):
        self.__util.get_game_state()
        updated_position_x = self.__position_x
        self.__util.reset_level()
        return updated_position_x

    def get_position_y(self):
        self.__util.get_game_state()
        updated_position_y = self.__position_y
        self.__util.reset_level()
        return updated_position_y