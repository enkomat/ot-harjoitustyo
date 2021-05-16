from levels.level_2 import Level2

class Level2TestSolution:
    def __init__(self, level: Level2):
        for player in level.players:
            for i in range(27):
                player.move_right()
            player.interact()