from enum_types.wall_type import WallType

class Wall:
    def __init__(self, position_x, position_y, wall_type = WallType.HORIZONTAL):
        self.__position_x = position_x
        self.__position_y = position_y
        self.type = wall_type
    
    def get_position_x(self):
        return self.__position_x
    
    def get_position_y(self):
        return self.__position_y