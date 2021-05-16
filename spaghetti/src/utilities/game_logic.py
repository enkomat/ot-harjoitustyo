from enum_types.wall_type import WallType
from game_objects.wall import Wall

class GameLogic:
    def __init__(self, util):
        self.util = util
        self.level_util = util.level_util

    # -----------------------
    # player event related methods:

    def move_player_left(self, player):
        """Liikuttaa pelaajaa yhden ruudun vasemmalle.
        """
        if self.collision_in_position(player._Player__position_x - 1, player._Player__position_y):
            return
        player._Player__position_x -= 1

    def move_player_right(self, player):
        """Liikuttaa pelaajaa yhden ruudun oikealle.
        """
        if self.collision_in_position(player._Player__position_x + 1, player._Player__position_y):
            return
        player._Player__position_x += 1

    def move_player_up(self, player):
        """Liikuttaa pelaajaa yhden ruudun ylöspäin.
        """
        if self.collision_in_position(player._Player__position_x, player._Player__position_y - 1):
            return
        player._Player__position_y -= 1

    def move_player_down(self, player):
        """Liikuttaa pelaajaa yhden ruudun alaspäin.
        """
        if self.collision_in_position(player._Player__position_x, player._Player__position_y + 1):
            return
        player._Player__position_y += 1

    def player_interact(self, player):
        """Laittaa pelaajan avaamaan oven, jos se on sen päällä. Jos pelaaja onnistuu avaamaan oven, päivitetään ovi avonaiseksi.

        Returns:
            bool: Palauttaa onko pelaaja avannut oven onnistuneesti.
        """
        if self.over_door(player):
            self.open_door(player)

    def player_build_wall(self, player):
        if self.get_wall_in_position(player._Player__position_x,player._Player__position_y):
            return
        self.util.sounds.play_sound(self.util.sounds.build)
        new_wall = Wall(player._Player__position_x, player._Player__position_y)
        self.level_util.walls.append(new_wall)
        self.set_correct_wall_type(new_wall)

    def player_build_door(self, player):
        self.util.sounds.play_sound(self.util.sounds.build)
        new_door = Wall(player._Player__position_x, player._Player__position_y)
        new_door.type = WallType.DOOR
        self.level_util.walls.append(new_door)

    def player_get_position_x(self, player):
        return player._Player__position_x

    def player_get_position_y(self, player):
        return player._Player__position_y

    # -----------------------
    # interactions with the world:

    def over_door(self, player):
        for door in self.level_util.doors:
            if (door._Door__position_x == player._Player__position_x) and (door._Door__position_y == player._Player__position_y):
                return True
        return False

    def open_door(self, player):
        for door in self.level_util.doors:
            if (door._Door__position_x == player._Player__position_x) and (door._Door__position_y == player._Player__position_y):
                door._Door__is_open = True
                player._Player__draw_player = False
                player._Player__has_interacted = True

    def level_has_been_solved(self):
        if self.level_util.level_win_condition_satisfied():
            if self.level_util.level_solved == False:
                self.util.sounds.play_sound(self.util.sounds.level_win)
                self.level_util.level_solved = True
            return True
        return False

    def collision_in_position(self, x, y):
        collidable_wall = self.get_wall_in_position(x, y)
        if collidable_wall and collidable_wall.type is not WallType.DOOR:
            self.util.sounds.play_sound(self.util.sounds.hit_wall)
            return True
        return False

    def set_correct_wall_type(self, new_wall):
        x = new_wall._Wall__position_x
        y = new_wall._Wall__position_y
        wall_right = self.get_wall_in_position(x+1, y)
        wall_left = self.get_wall_in_position(x-1, y)
        wall_up = self.get_wall_in_position(x, y-1)
        wall_down = self.get_wall_in_position(x, y+1)
        wall_up_left = self.get_wall_in_position(x-1, y-1)
        wall_up_right = self.get_wall_in_position(x+1, y-1)
        wall_down_left = self.get_wall_in_position(x-1, y+1)
        wall_down_right = self.get_wall_in_position(x+1, y+1)

        if not wall_right and not wall_left and not wall_up and not wall_down:
            new_wall.type = WallType.HORIZONTAL

        if not wall_right and not wall_left and wall_up and wall_up.type == WallType.VERTICAL_RIGHT:
            new_wall.type = WallType.VERTICAL_RIGHT
        if not wall_right and not wall_left and wall_down and wall_down.type == WallType.VERTICAL_RIGHT:
            new_wall.type = WallType.VERTICAL_RIGHT
        if not wall_right and not wall_left and wall_up and wall_up.type == WallType.VERTICAL_LEFT:
            new_wall.type = WallType.VERTICAL_LEFT
        if not wall_right and not wall_left and wall_down and wall_down.type == WallType.VERTICAL_LEFT:
            new_wall.type = WallType.VERTICAL_LEFT

        if not wall_right and not wall_left and not wall_up and wall_down and wall_down_right:
            new_wall.type = WallType.VERTICAL_LEFT
            wall_down.type = WallType.CORNER_LOWER_LEFT
        if not wall_right and not wall_left and wall_up and wall_up_left:
            new_wall.type = WallType.VERTICAL_RIGHT
            wall_up.type = WallType.CORNER_UPPER_RIGHT
        if wall_right and wall_down_right and wall_down_right.type == WallType.VERTICAL_RIGHT:
            new_wall.type = WallType.HORIZONTAL
            wall_right.type = WallType.CORNER_UPPER_RIGHT

        if wall_left and wall_down_left:
            new_wall.type = WallType.HORIZONTAL
            wall_left.type = WallType.CORNER_UPPER_LEFT

        if not wall_right and wall_left and wall_up:
            new_wall.type = WallType.CORNER_LOWER_RIGHT

        if wall_down and wall_down.type == WallType.VERTICAL_LEFT:
            new_wall.type = WallType.VERTICAL_LEFT

        if not wall_right and not wall_left and not wall_up and not wall_down_right and wall_down and wall_down_left:
            new_wall.type = WallType.VERTICAL_RIGHT
            wall_down.type = WallType.CORNER_LOWER_RIGHT

    def get_wall_in_position(self, x, y):
        for wall in self.level_util.walls:
            if wall._Wall__position_x == x and wall._Wall__position_y == y:
                return wall
