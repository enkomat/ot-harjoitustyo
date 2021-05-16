from levels.level_4 import Level4

class Level4TestSolution:
    def __init__(self, level: Level4):
        n = 14
        go_right = True
        for player in level.players:
            for y in range(10):
                player.move_down()
            for x in range(n):
                if go_right:
                    player.move_right()
                else:
                    player.move_left()
            if go_right:
                n -= 2
            else:
                n += 2
            if n == 0:
                go_right = False
            player.interact()