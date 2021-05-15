from game_objects.player import Player
from game_objects.pillar import Pillar

level_solution = """
20
22
Wall_Type.HORIZONTAL
---------
19
22
Wall_Type.DOOR
---------
18
22
Wall_Type.HORIZONTAL
---------
17
22
Wall_Type.CORNER_LOWER_LEFT
---------
17
21
Wall_Type.VERTICAL_LEFT
---------
17
20
Wall_Type.VERTICAL_LEFT
---------
17
19
Wall_Type.VERTICAL_LEFT
---------
17
18
Wall_Type.CORNER_UPPER_LEFT
---------
16
18
Wall_Type.HORIZONTAL
---------
15
18
Wall_Type.HORIZONTAL
---------
14
18
Wall_Type.HORIZONTAL
---------
13
18
Wall_Type.HORIZONTAL
---------
12
18
Wall_Type.HORIZONTAL
---------
11
18
Wall_Type.CORNER_LOWER_LEFT
---------
11
17
Wall_Type.VERTICAL_LEFT
---------
11
16
Wall_Type.VERTICAL_LEFT
---------
11
15
Wall_Type.VERTICAL_LEFT
---------
11
14
Wall_Type.VERTICAL_LEFT
---------
11
13
Wall_Type.VERTICAL_LEFT
---------
11
12
Wall_Type.CORNER_UPPER_LEFT
---------
12
12
Wall_Type.HORIZONTAL
---------
13
12
Wall_Type.HORIZONTAL
---------
14
12
Wall_Type.HORIZONTAL
---------
15
12
Wall_Type.HORIZONTAL
---------
16
12
Wall_Type.HORIZONTAL
---------
17
12
Wall_Type.HORIZONTAL
---------
18
12
Wall_Type.HORIZONTAL
---------
19
12
Wall_Type.HORIZONTAL
---------
20
12
Wall_Type.HORIZONTAL
---------
21
12
Wall_Type.CORNER_UPPER_RIGHT
---------
21
13
Wall_Type.VERTICAL_RIGHT
---------
21
14
Wall_Type.VERTICAL_RIGHT
---------
21
15
Wall_Type.VERTICAL_RIGHT
---------
21
16
Wall_Type.VERTICAL_RIGHT
---------
21
17
Wall_Type.VERTICAL_RIGHT
---------
21
18
Wall_Type.CORNER_UPPER_RIGHT
---------
21
19
Wall_Type.VERTICAL_RIGHT
---------
21
20
Wall_Type.VERTICAL_RIGHT
---------
21
21
Wall_Type.VERTICAL_RIGHT
---------
21
22
Wall_Type.CORNER_LOWER_RIGHT
---------
20
18
Wall_Type.HORIZONTAL
---------
19
18
Wall_Type.DOOR
---------
18
18
Wall_Type.HORIZONTAL
---------
"""

class Util_Level_5:
    def __init__(self, util):
        self.util = util

        self.player = Player(self, 21, 22)
        self.players = [self.player]
        
        self.doors = []

        self.walls = []

        self.p0 = Pillar(21, 22)
        self.p1 = Pillar(17, 22)
        self.p2 = Pillar(17, 18)
        self.p3 = Pillar(11, 18)
        self.p4 = Pillar(11, 12)
        self.p5 = Pillar(21, 12)
        self.p6 = Pillar(21, 18)
        self.pillars = [self.p0, self.p1, self.p2, self.p3, self.p4, self.p5, self.p6] 

        self.level = Level_5(self)

    def level_win_condition_satisfied(self):
        level_solution_list = level_solution.splitlines()
        index = 0
        x = 0
        y = 0
        wall_type = None
        solution_coordinates = []
        # check all needed walls exist
        for line in level_solution_list:

            if index == 1:
                x = int(line)
            elif index == 2:
                y = int(line)
            elif index == 3:
                pass

            index += 1
            
            if index == 4:
                solution_coordinates.append((x, y))
                index = 0

        for coord in solution_coordinates:
            wall_found_in_position = False
            for wall in self.walls:
                if coord[0] == wall.get_position_x() and coord[1] == wall.get_position_y():
                    wall_found_in_position = True
            if wall_found_in_position == False:
                    return False

        # check if a wall exists in wrong place
        for wall in self.walls:
            wall_in_wrong_place = True
            current_x = wall.get_position_x()
            current_y = wall.get_position_y()
            for coordinate in solution_coordinates:
                if coordinate[0] == current_x and coordinate[1] == current_y:
                    wall_in_wrong_place = False
                    break
            if wall_in_wrong_place:
                return False
    
        return True

class Level_5:
    def __init__(self, level_util):
        self.__util_level_5 = level_util
        self.player = self.__util_level_5.player
        self.pillars = self.__util_level_5.pillars
