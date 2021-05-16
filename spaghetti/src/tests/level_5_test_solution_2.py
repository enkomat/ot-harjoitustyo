from levels.level_5 import Level5

class Level5TestSolution2:
    def __init__(self, level: Level5):
        for i in range(15):
            level.player.move_left()
            level.player.build_wall()
        for i in range(15):
            level.player.move_right()
            level.player.build_wall()
        for i in range(15):
            level.player.move_up()
            level.player.build_wall()
        for i in range(15):
            level.player.move_down()
            level.player.build_wall()
