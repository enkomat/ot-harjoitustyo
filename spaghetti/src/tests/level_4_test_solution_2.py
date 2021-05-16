from levels.level_4 import Level4

class Level4TestSolution2:
    def __init__(self, level: Level4):
        for player in level.players:
            for y in range(10):
                player.move_down()
            player.interact()