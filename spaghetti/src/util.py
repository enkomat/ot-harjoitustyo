import pygame
import os

width, height = 8*64, 9*64
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("spaghetti")
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)
font_level_solved = pygame.font.SysFont('ComicSans MS', 32)

background_tile = pygame.image.load(
    "/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")
background_rect = background_tile.get_rect()
tile_pixel_size = 16
map_tiles = [pygame.image.load(
    "/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")] * 1024
background_color = (0, 0, 0)  # change from black to more grey

image_tiles = [pygame.image.load(
    "/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")] * 256

event_list = []
event_parameter_list = []

fps = 60


class Util:
    def load_tile_images():
        i = 0
        for filename in os.listdir("/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/"):
            path = "/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/" + filename
            if 'bmp' in path:
                image_tiles[i] = pygame.image.load(path)
                image_tiles[i].convert()
                i += 1

    def draw_text(text, x, y):
        text_surface = font.render(text, False, (255, 255, 255))
        window.blit(text_surface, (x, y))

    def draw_text_level_solved():
        text_surface = font_level_solved.render(
            'LEVEL SOLVED! :)', False, (255, 255, 255))
        window.blit(text_surface, (128, 256))

    def draw_coords():
        x = 0
        y = 64
        for i in range(32):
            Util.draw_text(str(i), x, y)
            x += 16
        x = 0
        for i in range(32):
            Util.draw_text(str(i), x, y)
            y += 16

    def draw_player(x, y):
        x *= tile_pixel_size
        y *= tile_pixel_size
        y += 64
        window.blit(image_tiles[140], (x, y))

    def draw_goal(x, y):
        x *= tile_pixel_size
        y *= tile_pixel_size
        y += 64
        window.blit(image_tiles[50], (x, y))

    def add_to_event_list(method_to_add):
        event_list.append(method_to_add)
        event_parameter_list.append(None)

    def add_to_event_list_with_parameter(method_to_add, parameter):
        event_list.append(method_to_add)
        event_parameter_list.append(parameter)

    def get_event_list():
        return event_list

    def execute_next_method_in_event_list():
        parameter = event_parameter_list.pop(0)
        if parameter is None:
            event_list.pop(0)()
        else:
            event_list.pop(0)(parameter[0], parameter[1])

    def quit():
        pygame.quit()


class Util_Level_1:
    def __init__(self, player_x=1, player_y=1, goal_x=30, goal_y=30):
        self.player_position_x = player_x
        self.player_position_y = player_y
        self.goal_position_x = goal_x
        self.goal_position_y = goal_y

    def move_player_left(self):
        self.player_position_x -= 1
        Util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_right(self):
        self.player_position_x += 1
        Util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_up(self):
        self.player_position_y -= 1
        Util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_down(self):
        self.player_position_y += 1
        Util.draw_player(self.player_position_x, self.player_position_y)

    def player_interact(self):
        if self.player_position_x == self.goal_position_x and self.player_position_y == self.goal_position_y:
            return True
        return False

    def draw_ui(self, amt):
        Util.draw_text('Level_1', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/59', 16, 32)

    def draw_map(self):
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x, y))
            x += tile_pixel_size
            if x >= width:
                x = 0
                y += tile_pixel_size

    def run(self, is_test=False):
        event_execution_amount = 0
        Util.load_tile_images()
        clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0
        run = True

        while run:
            if is_test and len(event_list) == 0:
                pygame.quit()

            clock.tick(fps)
            time_since_last_event_list_execute += clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if len(event_list) > 0 and time_since_last_event_list_execute > 40:
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            Util.draw_coords()
            Util.draw_goal(self.goal_position_x, self.goal_position_y)
            Util.draw_player(self.player_position_x, self.player_position_y)
            self.draw_ui(event_execution_amount)
            if(self.player_interact()):
                Util.draw_text_level_solved()

            pygame.display.update()

        pygame.quit()


class Level_1:
    def __init__(self):
        self.__util_level1 = Util_Level_1()

    def move_player_left(self):
        Util.add_to_event_list(self.__util_level1.move_player_left)

    def move_player_right(self):
        Util.add_to_event_list(self.__util_level1.move_player_right)

    def move_player_up(self):
        Util.add_to_event_list(self.__util_level1.move_player_up)

    def move_player_down(self):
        Util.add_to_event_list(self.__util_level1.move_player_down)

    def player_interact(self):
        Util.add_to_event_list(self.__util_level1.player_interact)

    def run(self, is_test=False):  # is_test should be removed from the main level class
        self.__util_level1.run(is_test)


class Player:
    def __init__(self, index, util):
        self.__index = index
        self.__util = util

    def move_player_left(self):
        Util.add_to_event_list_with_parameter(
            Util_Level_2.move_player_left, (self.__util, self.__index))

    def move_player_right(self):
        Util.add_to_event_list_with_parameter(
            Util_Level_2.move_player_right, (self.__util, self.__index))

    def move_player_up(self):
        Util.add_to_event_list_with_parameter(
            Util_Level_2.move_player_up, (self.__util, self.__index))

    def move_player_down(self):
        Util.add_to_event_list_with_parameter(
            Util_Level_2.move_player_down, (self.__util, self.__index))

    def interact(self):
        Util.add_to_event_list_with_parameter(
            Util_Level_2.player_interact, (self.__util, self.__index))


class Player_Util:
    position_x = 0
    position_y = 0
    has_interacted = False

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.has_interacted = False


class Util_Level_2:
    def __init__(self):
        self.p1 = Player_Util(1, 1)
        self.p2 = Player_Util(3, 1)
        self.p3 = Player_Util(5, 1)
        self.p4 = Player_Util(7, 1)
        self.p5 = Player_Util(9, 1)
        self.p6 = Player_Util(11, 1)
        self.p7 = Player_Util(13, 1)
        self.p8 = Player_Util(15, 1)
        self.p9 = Player_Util(17, 1)
        self.p11 = Player_Util(21, 1)
        self.p10 = Player_Util(19, 1)
        self.p12 = Player_Util(23, 1)
        self.p13 = Player_Util(25, 1)
        self.p14 = Player_Util(27, 1)
        self.p15 = Player_Util(29, 1)
        self.p16 = Player_Util(31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = (1, 30)
        self.g2 = (3, 30)
        self.g3 = (5, 30)
        self.g4 = (7, 30)
        self.g5 = (9, 30)
        self.g6 = (11, 30)
        self.g7 = (13, 30)
        self.g8 = (15, 30)
        self.g9 = (17, 30)
        self.g10 = (19, 30)
        self.g11 = (21, 30)
        self.g12 = (23, 30)
        self.g13 = (25, 30)
        self.g14 = (27, 30)
        self.g15 = (29, 30)
        self.g16 = (31, 30)
        self.goals = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def draw_ui(self, amt):
        Util.draw_text('Level_2', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map(self):
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x, y))
            x += tile_pixel_size
            if x >= width:
                x = 0
                y += tile_pixel_size
        for goal in self.goals:
            Util.draw_goal(goal[0], goal[1])

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def player_interact(self, i):
        if self.over_goal(i):
            self.players[i].has_interacted = True

    def over_goal(self, i):
        for goal in self.goals:
            if (goal[0] == self.players[i].position_x) and (goal[1] == self.players[i].position_y):
                return True
        return False

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        if is_test and len(event_list) == 0:
            run = False

        event_execution_amount = 0
        Util.load_tile_images()
        clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            clock.tick(fps)
            time_since_last_event_list_execute += clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(event_list) > 0 and time_since_last_event_list_execute > 2):
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            Util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                Util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                Util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()


class Level_2:
    def __init__(self, players = []):
        self.__util_lvl2 = Util_Level_2()
        self.__p1 = Player(0, self.__util_lvl2)
        self.__p2 = Player(1, self.__util_lvl2)
        self.__p3 = Player(2, self.__util_lvl2)
        self.__p4 = Player(3, self.__util_lvl2)
        self.__p5 = Player(4, self.__util_lvl2)
        self.__p6 = Player(5, self.__util_lvl2)
        self.__p7 = Player(6, self.__util_lvl2)
        self.__p8 = Player(7, self.__util_lvl2)
        self.__p9 = Player(8, self.__util_lvl2)
        self.__p10 = Player(9, self.__util_lvl2)
        self.__p11 = Player(10, self.__util_lvl2)
        self.__p12 = Player(11, self.__util_lvl2)
        self.__p13 = Player(12, self.__util_lvl2)
        self.__p14 = Player(13, self.__util_lvl2)
        self.__p15 = Player(14, self.__util_lvl2)
        self.__p16 = Player(15, self.__util_lvl2)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_lvl2.run()

class Util_Level_3:
    def __init__(self):
        self.p1 = Player_Util(1, 1)
        self.p2 = Player_Util(3, 30)
        self.p3 = Player_Util(5, 1)
        self.p4 = Player_Util(7, 30)
        self.p5 = Player_Util(9, 1)
        self.p6 = Player_Util(11, 30)
        self.p7 = Player_Util(13, 1)
        self.p8 = Player_Util(15, 30)
        self.p9 = Player_Util(17, 1)
        self.p10 = Player_Util(19, 30)
        self.p11 = Player_Util(21, 1)
        self.p12 = Player_Util(23, 30)
        self.p13 = Player_Util(25, 1)
        self.p14 = Player_Util(27, 30)
        self.p15 = Player_Util(29, 1)
        self.p16 = Player_Util(31, 30)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = (1, 30)
        self.g2 = (3, 1)
        self.g3 = (5, 30)
        self.g4 = (7, 1)
        self.g5 = (9, 30)
        self.g6 = (11, 1)
        self.g7 = (13, 30)
        self.g8 = (15, 1)
        self.g9 = (17, 30)
        self.g10 = (19, 1)
        self.g11 = (21, 30)
        self.g12 = (23, 1)
        self.g13 = (25, 30)
        self.g14 = (27, 1)
        self.g15 = (29, 30)
        self.g16 = (31, 1)
        self.goals = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def draw_ui(self, amt):
        Util.draw_text('Level_4', 16, 16)
        Util.draw_text('call_amount=' + str(amt), 16, 32)

    def draw_map(self):
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x, y))
            x += tile_pixel_size
            if x >= width:
                x = 0
                y += tile_pixel_size
        for goal in self.goals:
            Util.draw_goal(goal[0], goal[1])

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def player_interact(self, i):
        if self.over_goal(i):
            self.players[i].has_interacted = True

    def over_goal(self, i):
        for goal in self.goals:
            if (goal[0] == self.players[i].position_x) and (goal[1] == self.players[i].position_y):
                return True
        return False

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        if is_test and len(event_list) == 0:
            run = False

        event_execution_amount = 0
        Util.load_tile_images()
        clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            clock.tick(fps)
            time_since_last_event_list_execute += clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(event_list) > 0 and time_since_last_event_list_execute > 2):
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            Util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                Util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                Util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()


class Level_3:
    def __init__(self, players = []):
        self.__util_lvl3 = Util_Level_3()
        self.__p1 = Player(0, self.__util_lvl3)
        self.__p2 = Player(1, self.__util_lvl3)
        self.__p3 = Player(2, self.__util_lvl3)
        self.__p4 = Player(3, self.__util_lvl3)
        self.__p5 = Player(4, self.__util_lvl3)
        self.__p6 = Player(5, self.__util_lvl3)
        self.__p7 = Player(6, self.__util_lvl3)
        self.__p8 = Player(7, self.__util_lvl3)
        self.__p9 = Player(8, self.__util_lvl3)
        self.__p10 = Player(9, self.__util_lvl3)
        self.__p11 = Player(10, self.__util_lvl3)
        self.__p12 = Player(11, self.__util_lvl3)
        self.__p13 = Player(12, self.__util_lvl3)
        self.__p14 = Player(13, self.__util_lvl3)
        self.__p15 = Player(14, self.__util_lvl3)
        self.__p16 = Player(15, self.__util_lvl3)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_lvl3.run()

class Util_Level_4:
    def __init__(self):
        self.p1 = Player_Util(1, 1)
        self.p2 = Player_Util(3, 1)
        self.p3 = Player_Util(5, 1)
        self.p4 = Player_Util(7, 1)
        self.p5 = Player_Util(9, 1)
        self.p6 = Player_Util(11, 1)
        self.p7 = Player_Util(13, 1)
        self.p8 = Player_Util(15, 1)
        self.p9 = Player_Util(17, 1)
        self.p11 = Player_Util(21, 1)
        self.p10 = Player_Util(19, 1)
        self.p12 = Player_Util(23, 1)
        self.p13 = Player_Util(25, 1)
        self.p14 = Player_Util(27, 1)
        self.p15 = Player_Util(29, 1)
        self.p16 = Player_Util(31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = (15, 15)

    def draw_ui(self, amt):
        Util.draw_text('Level_3', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map(self):
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x, y))
            x += tile_pixel_size
            if x >= width:
                x = 0
                y += tile_pixel_size
            Util.draw_goal(self.g1[0], self.g1[1])

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        Util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def player_interact(self, i):
        if self.over_goal(i):
            self.players[i].has_interacted = True

    def over_goal(self, i):
        if (self.g1[0] == self.players[i].position_x) and (self.g1[0] == self.players[i].position_y):
            return True
        return False

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        if is_test and len(event_list) == 0:
            run = False

        event_execution_amount = 0
        Util.load_tile_images()
        clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            clock.tick(fps)
            time_since_last_event_list_execute += clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(event_list) > 0 and time_since_last_event_list_execute > 2):
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            Util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                Util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                Util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()


class Level_4:
    def __init__(self, players = []):
        self.__util_lvl4 = Util_Level_4()
        self.__p1 = Player(0, self.__util_lvl4)
        self.__p2 = Player(1, self.__util_lvl4)
        self.__p3 = Player(2, self.__util_lvl4)
        self.__p4 = Player(3, self.__util_lvl4)
        self.__p5 = Player(4, self.__util_lvl4)
        self.__p6 = Player(5, self.__util_lvl4)
        self.__p7 = Player(6, self.__util_lvl4)
        self.__p8 = Player(7, self.__util_lvl4)
        self.__p9 = Player(8, self.__util_lvl4)
        self.__p10 = Player(9, self.__util_lvl4)
        self.__p11 = Player(10, self.__util_lvl4)
        self.__p12 = Player(11, self.__util_lvl4)
        self.__p13 = Player(12, self.__util_lvl4)
        self.__p14 = Player(13, self.__util_lvl4)
        self.__p15 = Player(14, self.__util_lvl4)
        self.__p16 = Player(15, self.__util_lvl4)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_lvl4.run()
