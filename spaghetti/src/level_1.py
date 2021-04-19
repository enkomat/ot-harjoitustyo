# you always need to import the game and the level you want to play
from util import Level_1

# write your solution between the lines below
# you have the following methods to use to control the player:
# Level_1.move_player_down()
# Level_1.move_player_up()
# Level_1.move_player_left()
# Level_1.move_player_right()
# Level_1.player_interact()
# -------------------------------------

for i in range(29):
    Level_1.move_player_down()

for i in range(29):
    Level_1.move_player_right()

Level_1.player_interact()

# -------------------------------------

Level_1.run() # this runs the first level, always call run method last