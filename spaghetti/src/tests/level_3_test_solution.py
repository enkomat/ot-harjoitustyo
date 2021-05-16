from levels.level_3 import Level3

class Level3TestSolution:
    def __init__(self, level: Level3):
        for i in range(len(level.players)):
            for n in range(20):
                if i % 2 == 0:
                    level.players[i].move_down()
                else:
                    level.players[i].move_up()
            level.players[i].interact()