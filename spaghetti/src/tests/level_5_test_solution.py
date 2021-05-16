from levels.level_5 import Level5

class Level5TestSolution:
    def __init__(self, level: Level5):
        for i in range(4):
            level.player.move_left()
            if i == 1:
                level.player.build_door()
            else:
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
        for i in range(10):
            level.player.move_down()
            level.player.build_wall()
        level.player.move_down()
        level.player.move_left()
        level.player.move_left()
        level.player.move_up()
        level.player.move_up()
        level.player.move_up()
        level.player.move_up()
        level.player.move_up()
        level.player.move_right()
        level.player.build_wall()
        level.player.move_left()
        level.player.build_door()
        level.player.move_left()
        level.player.build_wall()
        level.player.move_down()
        level.player.move_down()