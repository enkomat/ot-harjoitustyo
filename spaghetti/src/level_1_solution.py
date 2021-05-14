from levels.level_1 import Level_1

class Level_1_Solution:
    def __init__(self, level: Level_1):
        self.level = level
        self.player = self.level.player
        self.move_in_direction(15, "right")
        self.move_in_direction(14, "down")

    def move_in_direction(self, amt, dir):
        for i in range(amt):
            if dir == "up":
                self.player.move_up()
            elif dir == "down":
                self.player.move_down()
            elif dir == "left":
                self.player.move_left()
            elif dir == "right":
                self.player.move_right()