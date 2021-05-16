from levels.level_1 import Level1

class Level1TestSolution2:
    def __init__(self, level: Level1):
        for i in range(10):
            level.player.move_right()
            if i < 10:
                level.player.move_down()
        level.player.interact()