from levels.level_2 import Level2

class Level2TestSolution2:
    def __init__(self, level: Level2):
        for player in level.players:
            for i in range(10):
                player.move_down()
            player.interact()