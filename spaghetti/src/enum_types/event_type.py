from enum import Enum

class EventType(Enum):
    MOVE_PLAYER_LEFT = 1
    MOVE_PLAYER_RIGHT = 2
    MOVE_PLAYER_UP = 3
    MOVE_PLAYER_DOWN = 4
    PLAYER_INTERACT = 5
    PLAYER_BUILD_WALL = 6
    PLAYER_BUILD_DOOR = 7