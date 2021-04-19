import pygame
import os

width, height = 8*64, 9*64
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("spaghetti")
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)
font_level_solved = pygame.font.SysFont('ComicSans MS', 32)

background_tile = pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")
background_rect = background_tile.get_rect()
tile_pixel_size = 16
map_tiles = [pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")] * 1024;
background_color = (0, 0, 0) # change from black to more grey

image_tiles = [pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti/src/assets/colored_tilemap_packed_140.bmp")] * 256;

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
        text_surface = font_level_solved.render('LEVEL SOLVED! :)', False, (255, 255, 255))
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
        window.blit(image_tiles[140], (x,y))

    def draw_goal(x, y):
        x *= tile_pixel_size
        y *= tile_pixel_size
        y += 64
        window.blit(image_tiles[50], (x,y))

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
            event_list.pop(0)(parameter)
    
    def quit():
        pygame.quit()

class Util_Level_1:
    player_position_x = 1
    player_position_y = 1
    goal_position_x = 30
    goal_position_y = 30

    def move_player_left():
        Util_Level_1.player_position_x -= 1
        Util.draw_player(Util_Level_1.player_position_x, Util_Level_1.player_position_y)

    def move_player_right():
        Util_Level_1.player_position_x += 1
        Util.draw_player(Util_Level_1.player_position_x, Util_Level_1.player_position_y)

    def move_player_up():
        Util_Level_1.player_position_y -= 1
        Util.draw_player(Util_Level_1.player_position_x, Util_Level_1.player_position_y)

    def move_player_down():
        Util_Level_1.player_position_y += 1
        Util.draw_player(Util_Level_1.player_position_x, Util_Level_1.player_position_y)

    def player_interact():
        if Util_Level_1.player_position_x == Util_Level_1.goal_position_x and Util_Level_1.player_position_y == Util_Level_1.goal_position_y:
            return True
        else:
            return False
    
    def draw_ui(amt):
        Util.draw_text('Level_1', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/59', 16, 32)

    def draw_map():
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x,y))
            x += tile_pixel_size
            if(x >= width):
                x = 0 
                y += tile_pixel_size

    def run(isTest = False):
        event_execution_amount = 0
        Util.load_tile_images()
        clock = pygame.time.Clock()
        time_since_last_event_list_execute = 0.0
        run = True
        
        while run:
            if isTest and len(event_list) == 0:
                run = False

            clock.tick(fps)
            time_since_last_event_list_execute += clock.tick(fps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            if(len(event_list) > 0 and time_since_last_event_list_execute > 40): 
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0
            
            Util_Level_1.draw_map()
            Util.draw_coords()
            Util.draw_goal(Util_Level_1.goal_position_x, Util_Level_1.goal_position_y)
            Util.draw_player(Util_Level_1.player_position_x, Util_Level_1.player_position_y)
            Util_Level_1.draw_ui(event_execution_amount)
            if(Util_Level_1.player_interact()):
                Util.draw_text_level_solved()
                
            pygame.display.update()

        pygame.quit()

class Level_1:
    def move_player_left():
        Util.add_to_event_list(Util_Level_1.move_player_left)

    def move_player_right():
        Util.add_to_event_list(Util_Level_1.move_player_right)

    def move_player_up():
        Util.add_to_event_list(Util_Level_1.move_player_up)

    def move_player_down():
        Util.add_to_event_list(Util_Level_1.move_player_down)

    def player_interact():
        Util.add_to_event_list(Util_Level_1.player_interact)

    def run():
        Util_Level_1.run()

class Player:
    index = 0

    def __init__(self, index):
        self.index = index

    def move_player_left(self):
        Util.add_to_event_list_with_parameter(Util_Level_2.move_player_left, self.index)
    
    def move_player_right(self):
        Util.add_to_event_list_with_parameter(Util_Level_2.move_player_right, self.index)
    
    def move_player_up(self):
        Util.add_to_event_list_with_parameter(Util_Level_2.move_player_up, self.index)

    def move_player_down(self):
        Util.add_to_event_list_with_parameter(Util_Level_2.move_player_down, self.index)

    def interact(self):
        Util.add_to_event_list_with_parameter(Util_Level_2.player_interact, self.index)

class Player_Util:
    position_x = 0
    position_y = 0
    has_interacted = False

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.has_interacted = False

class Util_Level_2:
    p1 = Player_Util(1, 1)
    p2 = Player_Util(3, 1)
    p3 = Player_Util(5, 1)
    p4 = Player_Util(7, 1)
    p5 = Player_Util(9, 1)
    p6 = Player_Util(11, 1)
    p7 = Player_Util(13, 1)
    p8 = Player_Util(15, 1)
    p9 = Player_Util(17, 1)
    p11 = Player_Util(21, 1)
    p10 = Player_Util(19, 1)
    p12 = Player_Util(23, 1)
    p13 = Player_Util(25, 1)
    p14 = Player_Util(27, 1)
    p15 = Player_Util(29, 1)
    p16 = Player_Util(31, 1)
    players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

    g1 = (1,30)
    g2 = (3,30)
    g3 = (5,30)
    g4 = (7,30)
    g5 = (9,30)
    g6 = (11,30)
    g7 = (13,30)
    g8 = (15,30)
    g9 = (17,30)
    g10 = (19,30)
    g11 = (21,30)
    g12 = (23,30)
    g13 = (25,30)
    g14 = (27,30)
    g15 = (29,30)
    g16 = (31,30)
    goals = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16]

    def draw_ui(amt):
        Util.draw_text('Level_2', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map():
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x,y))
            x += tile_pixel_size
            if(x >= width):
                x = 0 
                y += tile_pixel_size
        for goal in Util_Level_2.goals:
            Util.draw_goal(goal[0], goal[1])

    def move_player_up(i):
        Util_Level_2.players[i].position_y -= 1
        Util.draw_player(Util_Level_2.players[i].position_x, Util_Level_2.players[0].position_x)
    
    def move_player_down(i):
        Util_Level_2.players[i].position_y += 1
        Util.draw_player(Util_Level_2.players[i].position_x, Util_Level_2.players[0].position_x)
    
    def move_player_left(i):
        Util_Level_2.players[i].position_x -= 1
        Util.draw_player(Util_Level_2.players[i].position_x, Util_Level_2.players[0].position_x)
    
    def move_player_right(i):
        Util_Level_2.players[i].position_x += 1
        Util.draw_player(Util_Level_2.players[i].position_x, Util_Level_2.players[0].position_x)

    def player_interact(i):
        if Util_Level_2.over_goal(i):
            Util_Level_2.players[i].has_interacted = True
    
    def over_goal(i):
        for goal in Util_Level_2.goals:
            if (goal[0] == Util_Level_2.players[i].position_x) and (goal[1] == Util_Level_2.players[i].position_y):
                return True
        return False
    
    def level_has_been_solved():
        for player in Util_Level_2.players:
            if player.has_interacted == False:
                return False
        return True

    def run(is_test = False):
        if isTest and len(event_list) == 0:
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
            
            Util_Level_2.draw_map()
            Util.draw_coords()
            Util_Level_2.draw_ui(event_execution_amount)
            for player in Util_Level_2.players:
                Util.draw_player(player.position_x, player.position_y)
            if Util_Level_2.level_has_been_solved():
                Util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()

class Level_2:
    p1 = Player(0)
    p2 = Player(1)
    p3 = Player(2)
    p4 = Player(3)
    p5 = Player(4)
    p6 = Player(5)
    p7 = Player(6)
    p8 = Player(7)
    p9 = Player(8)
    p10 = Player(9)
    p11 = Player(10)
    p12 = Player(11)
    p13 = Player(12)
    p14 = Player(13)
    p15 = Player(14)
    p16 = Player(15)
    players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
        
    def run():
        Util_Level_2.run()

class Util_Level_3:
    p1 = Player_Util(1, 1)
    p2 = Player_Util(3, 30)
    p3 = Player_Util(5, 1)
    p4 = Player_Util(7, 30)
    p5 = Player_Util(9, 1)
    p6 = Player_Util(11, 30)
    p7 = Player_Util(13, 1)
    p8 = Player_Util(15, 30)
    p9 = Player_Util(17, 1)
    p10 = Player_Util(19, 30)
    p11 = Player_Util(21, 1)
    p12 = Player_Util(23, 30)
    p13 = Player_Util(25, 1)
    p14 = Player_Util(27, 30)
    p15 = Player_Util(29, 1)
    p16 = Player_Util(31, 30)
    players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

    g1 = (1,30)
    g2 = (3,1)
    g3 = (5,30)
    g4 = (7,1)
    g5 = (9,30)
    g6 = (11,1)
    g7 = (13,30)
    g8 = (15,1)
    g9 = (17,30)
    g10 = (19,1)
    g11 = (21,30)
    g12 = (23,1)
    g13 = (25,30)
    g14 = (27,1)
    g15 = (29,30)
    g16 = (31,1)
    goals = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16]

    def draw_ui(amt):
        Util.draw_text('Level_3', 16, 16)
        Util.draw_text('call_amount=' + str(amt) + '/480', 16, 32)

    def draw_map():
        window.fill(background_color)
        x = 0
        y = 64
        for tile in map_tiles:
            window.blit(image_tiles[141], (x,y))
            x += tile_pixel_size
            if(x >= width):
                x = 0 
                y += tile_pixel_size
        for goal in Util_Level_3.goals:
            Util.draw_goal(goal[0], goal[1])

    def move_player_up(i):
        Util_Level_3.players[i].position_y -= 1
        Util.draw_player(Util_Level_3.players[i].position_x, Util_Level_3.players[0].position_x)
    
    def move_player_down(i):
        Util_Level_3.players[i].position_y += 1
        Util.draw_player(Util_Level_3.players[i].position_x, Util_Level_3.players[0].position_x)
    
    def move_player_left(i):
        Util_Level_3.players[i].position_x -= 1
        Util.draw_player(Util_Level_3.players[i].position_x, Util_Level_3.players[0].position_x)
    
    def move_player_right(i):
        Util_Level_3.players[i].position_x += 1
        Util.draw_player(Util_Level_3.players[i].position_x, Util_Level_3.players[0].position_x)

    def player_interact(i):
        if Util_Level_3.over_goal(i):
            Util_Level_3.players[i].has_interacted = True
    
    def over_goal(i):
        for goal in Util_Level_3.goals:
            if (goal[0] == Util_Level_3.players[i].position_x) and (goal[1] == Util_Level_3.players[i].position_y):
                return True
        return False
    
    def level_has_been_solved():
        for player in Util_Level_3.players:
            if player.has_interacted == False:
                return False
        return True

    def run():
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
            
            Util_Level_3.draw_map()
            Util.draw_coords()
            Util_Level_3.draw_ui(event_execution_amount)
            for player in Util_Level_3.players:
                Util.draw_player(player.position_x, player.position_y)
            if Util_Level_3.level_has_been_solved():
                Util.draw_text_level_solved()
            pygame.display.update()

        pygame.quit()

class Level_3:
    p1 = Player(0)
    p2 = Player(1)
    p3 = Player(2)
    p4 = Player(3)
    p5 = Player(4)
    p6 = Player(5)
    p7 = Player(6)
    p8 = Player(7)
    p9 = Player(8)
    p10 = Player(9)
    p11 = Player(10)
    p12 = Player(11)
    p13 = Player(12)
    p14 = Player(13)
    p15 = Player(14)
    p16 = Player(15)
    players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
        
    def run():
        Util_Level_3.run()
    