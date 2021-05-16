from enum import Enum

class WallType(Enum):
    HORIZONTAL = 1
    VERTICAL_RIGHT = 2
    VERTICAL_LEFT = 3
    CORNER_LOWER_RIGHT = 4
    CORNER_LOWER_LEFT = 5
    CORNER_UPPER_RIGHT = 6
    CORNER_UPPER_LEFT = 7
    DOOR = 8