# you always need to import the game and the level you want to play
from util import Level_2

# write your solution between the lines below
# -------------------------------------

for n in range(29):
    for i in range(16):
        Level_2.players[i].move_player_down()

for i in range(16):
    Level_2.players[i].interact()

# -------------------------------------

Level_2.run() # always call run method last