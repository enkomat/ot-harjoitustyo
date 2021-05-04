from util import Level_5
lvl5 = Level_5()

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

lvl5.run()

def solve_level():
    for player in lvl5.players:
        dist_x = abs(player.get_position_x - 15)
        dist_y = abs(player.get_position_y - 15)
    
    for i in range(dist_x):
        if player.position_x > 15:        
            player.move_player_left()
        else:
            player.move_player_right()
    
    for i in range(dist_y):
        if player.position_y > 15:        
            player.move_player_up()
        else:
            player.move_player_down()

    player.interact()