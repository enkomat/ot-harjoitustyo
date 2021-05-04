from util import Level_5
lvl5 = Level_5()

n = 0
for i in range(20000000):
    n += 1*1

lvl5.run()

def solve_level():
    for player in lvl5.players:
        dist_x = abs(player.get_position_x() - 15)
        dist_y = abs(player.get_position_y() - 15)
        
        for i in range(dist_x):
            if player.get_position_x() > 15:        
                player.move_left()
            else:
                player.move_right()
        
        for i in range(dist_y):
            if player.get_position_y() > 15:        
                player.move_up()
            else:
                player.move_down()

        player.interact()