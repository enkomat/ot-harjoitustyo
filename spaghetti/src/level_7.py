from util import Level_7
import math
lvl7 = Level_7()

# get biggest distance between two players
biggest_dist = 0
leader1 = lvl7.players[0]
leader2 = lvl7.players[0]
for player1 in lvl7.players:
    player1_xy = [player1.get_position_x(), player1.get_position_y()]
    for player2 in lvl7.players:
        if player1 == player2:
            continue
        player2_xy = [player2.get_position_x(), player2.get_position_y()]
        dist = math.dist(player1_xy, player2_xy)
        if(dist > biggest_dist):
            biggest_dist = dist
            leader1 = player1
            leader2 = player2

leader1_xy = [leader1.get_position_x(), leader1.get_position_y()]

distances = []
players_grp1 = []
for player in lvl7.players:
    if player == leader1:
        continue

    player_xy = [player.get_position_x(), player.get_position_y()]
    dist = math.dist(leader1_xy, player_xy)
    distances.append(dist)
    players_grp1.append(player)

zipped_pairs = zip(distances, players_grp1)
sorted_players = sorted(zipped_pairs, key = lambda x: x[0])

group1 = [leader1]
for i in range(7):
    group1.append(sorted_players[i][1])
    


lvl7.run()

def move_players():
    for player in group1:
        dist_x = abs(player.get_position_x() - 10)
        dist_y = abs(player.get_position_y() - 15)
        
        for i in range(dist_x):
            if player.get_position_x() > 10:        
                player.move_left()
            else:
                player.move_right()
        
        for i in range(dist_y):
            if player.get_position_y() > 15:        
                player.move_up()
            else:
                player.move_down()

        player.interact()