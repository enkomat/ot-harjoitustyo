import pygame
import os

class Util:
    def __init__(self):
        pygame.init()
        self.width = 8*64
        self.height = 9*64
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("spaghetti")
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 12)
        self.font_level_solved = pygame.font.SysFont('ComicSans MS', 32)

        self.path = os.path.dirname(os.path.realpath(__file__))
        self.tile_pixel_size = 16
        self.map_tiles = [pygame.image.load(
            self.path + "/assets/colored_tilemap_packed_140.bmp")] * 1024
        self.background_color = (0, 0, 0)  # change from black to more grey

        self.image_tiles = []

        self.event_list = []
        self.event_parameter_list = []

        self.fps = 60

    def load_tile_images(self):
        i = 0
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'bmp' in path:
                new_bmp = pygame.image.load(path)
                new_bmp.convert()
                self.image_tiles.append(new_bmp)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, False, (255, 255, 255))
        self.window.blit(text_surface, (x, y))

    def draw_text_level_solved(self):
        self.text_surface = self.font_level_solved.render(
            'LEVEL SOLVED! :)', False, (255, 255, 255))
        self.window.blit(self.text_surface, (128, 256))

    def draw_coords(self):
        x = 0
        y = 64
        for i in range(32):
            self.draw_text(str(i), x, y)
            x += 16
        x = 0
        for i in range(32):
            self.draw_text(str(i), x, y)
            y += 16

    def draw_player(self, x, y):
        x *= self.tile_pixel_size
        y *= self.tile_pixel_size
        y += 64
        self.window.blit(self.image_tiles[6], (x, y))

    def draw_closed_door(self, x, y):
        x *= self.tile_pixel_size
        y *= self.tile_pixel_size
        y += 64
        self.window.blit(self.image_tiles[32], (x, y))

    def draw_open_door(self, x, y):
        x *= self.tile_pixel_size
        y *= self.tile_pixel_size
        y += 64
        self.window.blit(self.image_tiles[33], (x, y))

    def add_to_event_list(self, method_to_add):
        self.event_list.append(method_to_add)
        self.event_parameter_list.append(None)

    def add_to_event_list_with_parameter(self, method_to_add, parameter):
        self.event_list.append(method_to_add)
        self.event_parameter_list.append(parameter)

    def get_event_list(self):
        return self.event_list

    def execute_next_method_in_event_list(self):
        parameter = self.event_parameter_list.pop(0)
        if parameter is None:
            self.event_list.pop(0)()
        else:
            self.event_list.pop(0)(parameter)

    def quit(self):
        pygame.quit()

class Door_Util:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.is_open = False

class Util_Level_1:
    def __init__(self, player_x=1, player_y=1):
        self.util = Util()
        self.player_position_x = player_x
        self.player_position_y = player_y
        self.door = Door_Util(30, 30)
        self.event_list = self.util.event_list

    def move_player_left(self):
        self.player_position_x -= 1
        self.util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_right(self):
        self.player_position_x += 1
        self.util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_up(self):
        self.player_position_y -= 1
        self.util.draw_player(self.player_position_x, self.player_position_y)

    def move_player_down(self):
        self.player_position_y += 1
        self.util.draw_player(self.player_position_x, self.player_position_y)

    def player_interact(self):
        if self.player_position_x == self.door.position_x and self.player_position_y == self.door.position_y:
            self.door.is_open = True
            return True
        return False

    def draw_ui(self, amt):
        self.util.draw_text('Level_1', 16, 16)
        self.util.draw_text('call_amount=' + str(amt) + '/59', 16, 32)

    def draw_map(self):
        self.util.window.fill(self.util.background_color)
        x = 0
        y = 64
        for tile in self.util.map_tiles:
            self.util.window.blit(self.util.image_tiles[15], (x, y))
            x += self.util.tile_pixel_size
            if x >= self.util.width:
                x = 0
                y += self.util.tile_pixel_size

    def run(self, is_test=False):
        event_execution_amount = 0
        self.util.load_tile_images()
        self.clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0
        run = True

        while run:
            if is_test and len(self.event_list) == 0:
                pygame.quit()
                return None

            self.clock.tick(self.util.fps)
            time_since_last_event_list_execute += self.clock.tick(self.util.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if len(self.event_list) > 0 and time_since_last_event_list_execute > 40:
                self.util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            self.util.draw_coords()
            
            if self.door.is_open:
                self.util.draw_open_door(self.door.position_x, self.door.position_y)
            else:
                self.util.draw_closed_door(self.door.position_x, self.door.position_y)
            
            self.draw_ui(event_execution_amount)
            
            if(self.player_interact()):
                self.util.draw_text_level_solved()
            else:
                self.util.draw_player(self.player_position_x, self.player_position_y)

            pygame.display.update()

        pygame.quit()


class Level_1:
    def __init__(self):
        self.__util_level_1 = Util_Level_1()

    def move_player_left(self):
        self.__util_level_1.util.add_to_event_list(self.__util_level_1.move_player_left)

    def move_player_right(self):
        self.__util_level_1.util.add_to_event_list(self.__util_level_1.move_player_right)

    def move_player_up(self):
        self.__util_level_1.util.add_to_event_list(self.__util_level_1.move_player_up)

    def move_player_down(self):
        self.__util_level_1.util.add_to_event_list(self.__util_level_1.move_player_down)

    def player_interact(self):
        self.__util_level_1.util.add_to_event_list(self.__util_level_1.player_interact)

    def run(self):
        self.__util_level_1.run()

class Player:
    def __init__(self, index, util):
        self.__index = index
        self.__util = util

    def move_player_left(self):
        self.__util.util.add_to_event_list_with_parameter(
            self.__util.move_player_left, self.__index)

    def move_player_right(self):
        self.__util.util.add_to_event_list_with_parameter(
            self.__util.move_player_right, self.__index)

    def move_player_up(self):
        self.__util.util.add_to_event_list_with_parameter(
            self.__util.move_player_up, self.__index)

    def move_player_down(self):
        self.__util.util.add_to_event_list_with_parameter(
            self.__util.move_player_down, self.__index)

    def interact(self):
        self.__util.util.add_to_event_list_with_parameter(
            self.__util.player_interact, self.__index)

class Player_Util:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.has_interacted = False
        self.draw_player = True

class Util_Level_2:
    def __init__(self):
        self.util = Util()

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
        
        self.g1 = Door_Util(1, 30)
        self.g2 = Door_Util(3, 30)
        self.g3 = Door_Util(5, 30)
        self.g4 = Door_Util(7, 30)
        self.g5 = Door_Util(9, 30)
        self.g6 = Door_Util(11, 30)
        self.g7 = Door_Util(13, 30)
        self.g8 = Door_Util(15, 30)
        self.g9 = Door_Util(17, 30)
        self.g10 = Door_Util(19, 30)
        self.g11 = Door_Util(21, 30)
        self.g12 = Door_Util(23, 30)
        self.g13 = Door_Util(25, 30)
        self.g14 = Door_Util(27, 30)
        self.g15 = Door_Util(29, 30)
        self.g16 = Door_Util(31, 30)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def draw_ui(self, amt):
        self.util.draw_text('Level_2', 16, 16)
        self.util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map(self):
        self.util.window.fill(self.util.background_color)
        x = 0
        y = 64
        for tile in self.util.map_tiles:
            self.util.window.blit(self.util.image_tiles[15], (x, y))
            x += self.util.tile_pixel_size
            if x >= self.util.width:
                x = 0
                y += self.util.tile_pixel_size
        for door in self.doors:
            if door.is_open:
                self.util.draw_open_door(door.position_x, door.position_y)
            else:
                self.util.draw_closed_door(door.position_x, door.position_y)

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def player_interact(self, i):
        if self.over_door(i):
            self.open_door(i)
            self.players[i].has_interacted = True
            self.players[i].draw_player = False

    def over_door(self, i):
        for door in self.doors:
            if (door.position_x == self.players[i].position_x) and (door.position_y == self.players[i].position_y):
                return True
        return False

    def open_door(self, i):
        for door in self.doors:
            if (door.position_x == self.players[i].position_x) and (door.position_y == self.players[i].position_y):
                door.is_open = True

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        event_execution_amount = 0
        self.util.load_tile_images()
        self.clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            if is_test and len(self.util.event_list) == 0:
                run = False
                return None

            self.clock.tick(self.util.fps)
            time_since_last_event_list_execute += self.clock.tick(self.util.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(self.util.event_list) > 0 and time_since_last_event_list_execute > 2):
                self.util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            self.util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                if player.draw_player:
                    self.util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                self.util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()

class Level_2:
    def __init__(self, players = []):
        self.__util_level_2 = Util_Level_2()
        self.__p1 = Player(0, self.__util_level_2)
        self.__p2 = Player(1, self.__util_level_2)
        self.__p3 = Player(2, self.__util_level_2)
        self.__p4 = Player(3, self.__util_level_2)
        self.__p5 = Player(4, self.__util_level_2)
        self.__p6 = Player(5, self.__util_level_2)
        self.__p7 = Player(6, self.__util_level_2)
        self.__p8 = Player(7, self.__util_level_2)
        self.__p9 = Player(8, self.__util_level_2)
        self.__p10 = Player(9, self.__util_level_2)
        self.__p11 = Player(10, self.__util_level_2)
        self.__p12 = Player(11, self.__util_level_2)
        self.__p13 = Player(12, self.__util_level_2)
        self.__p14 = Player(13, self.__util_level_2)
        self.__p15 = Player(14, self.__util_level_2)
        self.__p16 = Player(15, self.__util_level_2)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_level_2.run()

class Util_Level_3:
    def __init__(self):
        self.util = Util()
        
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
        
        self.g1 = Door_Util(1, 30)
        self.g2 = Door_Util(3, 1)
        self.g3 = Door_Util(5, 30)
        self.g4 = Door_Util(7, 1)
        self.g5 = Door_Util(9, 30)
        self.g6 = Door_Util(11, 1)
        self.g7 = Door_Util(13, 30)
        self.g8 = Door_Util(15, 1)
        self.g9 = Door_Util(17, 30)
        self.g10 = Door_Util(19, 1)
        self.g11 = Door_Util(21, 30)
        self.g12 = Door_Util(23, 1)
        self.g13 = Door_Util(25, 30)
        self.g14 = Door_Util(27, 1)
        self.g15 = Door_Util(29, 30)
        self.g16 = Door_Util(31, 1)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def draw_ui(self, amt):
        self.util.draw_text('Level_3', 16, 16)
        self.util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map(self):
        self.util.window.fill(self.util.background_color)
        x = 0
        y = 64
        for tile in self.util.map_tiles:
            self.util.window.blit(self.util.image_tiles[15], (x, y))
            x += self.util.tile_pixel_size
            if x >= self.util.width:
                x = 0
                y += self.util.tile_pixel_size
        for door in self.doors:
            if door.is_open:
                self.util.draw_open_door(door.position_x, door.position_y)
            else:
                self.util.draw_closed_door(door.position_x, door.position_y)

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[i].position_y)

    def player_interact(self, i):
        if self.over_door(i):
            self.open_door(i)
            self.players[i].has_interacted = True
            self.players[i].draw_player = False

    def over_door(self, i):
        for door in self.doors:
            if (door.position_x == self.players[i].position_x) and (door.position_y == self.players[i].position_y):
                return True
        return False
    
    def open_door(self, i):
        for door in self.doors:
            if (door.position_x == self.players[i].position_x) and (door.position_y == self.players[i].position_y):
                door.is_open = True

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        event_execution_amount = 0
        self.util.load_tile_images()
        self.clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            if is_test and len(self.util.event_list) == 0:
                run = False
                return None

            self.clock.tick(self.util.fps)
            time_since_last_event_list_execute += self.clock.tick(self.util.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(self.util.event_list) > 0 and time_since_last_event_list_execute > 2):
                self.util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            self.util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                if player.draw_player:
                    self.util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                self.util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()


class Level_3:
    def __init__(self, players = []):
        self.__util_level_3 = Util_Level_3()

        self.__p1 = Player(0, self.__util_level_3)
        self.__p2 = Player(1, self.__util_level_3)
        self.__p3 = Player(2, self.__util_level_3)
        self.__p4 = Player(3, self.__util_level_3)
        self.__p5 = Player(4, self.__util_level_3)
        self.__p6 = Player(5, self.__util_level_3)
        self.__p7 = Player(6, self.__util_level_3)
        self.__p8 = Player(7, self.__util_level_3)
        self.__p9 = Player(8, self.__util_level_3)
        self.__p10 = Player(9, self.__util_level_3)
        self.__p11 = Player(10, self.__util_level_3)
        self.__p12 = Player(11, self.__util_level_3)
        self.__p13 = Player(12, self.__util_level_3)
        self.__p14 = Player(13, self.__util_level_3)
        self.__p15 = Player(14, self.__util_level_3)
        self.__p16 = Player(15, self.__util_level_3)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_level_3.run()

class Util_Level_4:
    def __init__(self):
        self.util = Util()

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
        
        self.door = Door_Util(15, 15)

    def draw_ui(self, amt):
        self.util.draw_text('Level_4', 16, 16)
        self.util.draw_text('call_amount=' + str(amt) + '/368', 16, 32)

    def draw_map(self):
        self.util.window.fill(self.util.background_color)
        x = 0
        y = 64
        for tile in self.util.map_tiles:
            self.util.window.blit(self.util.image_tiles[15], (x, y))
            x += self.util.tile_pixel_size
            if x >= self.util.width:
                x = 0
                y += self.util.tile_pixel_size
            if self.door.is_open:
                self.util.draw_open_door(self.door.position_x, self.door.position_y)
            else:
                self.util.draw_closed_door(self.door.position_x, self.door.position_y)

    def move_player_up(self, i):
        self.players[i].position_y -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_down(self, i):
        self.players[i].position_y += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_left(self, i):
        self.players[i].position_x -= 1
        self.util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def move_player_right(self, i):
        self.players[i].position_x += 1
        self.util.draw_player(
            self.players[i].position_x, self.players[0].position_x)

    def player_interact(self, i):
        if self.over_goal(i):
            self.door.is_open = True
            self.players[i].has_interacted = True
            self.players[i].draw_player = False

    def over_goal(self, i):
        if (self.door.position_x == self.players[i].position_x) and (self.door.position_y == self.players[i].position_y):
            return True
        return False

    def level_has_been_solved(self):
        for player in self.players:
            if player.has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        event_execution_amount = 0
        self.util.load_tile_images()
        self.clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0

        run = True
        while run:
            if is_test and len(self.util.event_list) == 0:
                run = False
                return None

            self.clock.tick(self.util.fps)
            time_since_last_event_list_execute += self.clock.tick(self.util.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if(len(self.util.event_list) > 0 and time_since_last_event_list_execute > 2):
                self.util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0

            self.draw_map()
            self.util.draw_coords()
            self.draw_ui(event_execution_amount)
            for player in self.players:
                if player.draw_player:
                    self.util.draw_player(player.position_x, player.position_y)
            if self.level_has_been_solved():
                self.util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()


class Level_4:
    def __init__(self, players = []):
        self.__util_level_4 = Util_Level_4()

        self.__p1 = Player(0, self.__util_level_4)
        self.__p2 = Player(1, self.__util_level_4)
        self.__p3 = Player(2, self.__util_level_4)
        self.__p4 = Player(3, self.__util_level_4)
        self.__p5 = Player(4, self.__util_level_4)
        self.__p6 = Player(5, self.__util_level_4)
        self.__p7 = Player(6, self.__util_level_4)
        self.__p8 = Player(7, self.__util_level_4)
        self.__p9 = Player(8, self.__util_level_4)
        self.__p10 = Player(9, self.__util_level_4)
        self.__p11 = Player(10, self.__util_level_4)
        self.__p12 = Player(11, self.__util_level_4)
        self.__p13 = Player(12, self.__util_level_4)
        self.__p14 = Player(13, self.__util_level_4)
        self.__p15 = Player(14, self.__util_level_4)
        self.__p16 = Player(15, self.__util_level_4)
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
                self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def run(self):
        self.__util_level_4.run()