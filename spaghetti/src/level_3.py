from util import Level_3

for i in range(16):
    for n in range(9):
        Level_3.players[i].move_player_down()

for i in range(16):
    for n in range(9):
        if i % 2 == 0:
            Level_3.players[i].move_player_down()

for i in range(16):
    for n in range(29):
        if i % 2 != 0:
            Level_3.players[i].move_player_down()

Level_3.run()