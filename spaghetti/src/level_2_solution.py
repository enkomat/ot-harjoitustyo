from levels.level_2 import Level_2

class Level_2_Solution:
    def __init__(self, level: Level_2):
        for player in level.players:
            for i in range(15):
                player.move_right()
            player.interact()