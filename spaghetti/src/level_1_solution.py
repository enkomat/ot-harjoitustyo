from levels.level_1 import Level_1

class Level_1_Solution:
    def __init__(self, level: Level_1):
        for i in range(4):
            level.player.move_left()
            level.player.build_wall()
        for i in range(4):
            level.player.move_up()
            level.player.build_wall()
        for i in range(6):
            level.player.move_left()
            level.player.build_wall()
        for i in range(6):
            level.player.move_up()
            level.player.build_wall()
        for i in range(10):
            level.player.move_right()
            level.player.build_wall()