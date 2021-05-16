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