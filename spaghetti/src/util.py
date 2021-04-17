import pygame
import os

import pygame
import os

width, height = 8*64, 9*64
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("spaghetti_master")
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)
font_level_solved = pygame.font.SysFont('ComicSans MS', 32)

background_tile = pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti-master/src/assets/colored_tilemap_packed_140.bmp")
background_rect = background_tile.get_rect()
tile_pixel_size = 16
map_tiles = [pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti-master/src/assets/colored_tilemap_packed_140.bmp")] * 1024;
background_color = (0, 0, 0) # change from black to more grey

player_position_x = 1
player_position_y = 1

image_tiles = [pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti-master/src/assets/colored_tilemap_packed_140.bmp")] * 256;

event_list = []

fps = 60

class Level_1:
    def move_player_left():
        Util.add_to_event_list(Util.move_player_left)

    def move_player_right():
        Util.add_to_event_list(Util.move_player_right)

    def move_player_up():
        Util.add_to_event_list(Util.move_player_up)

    def move_player_down():
        Util.add_to_event_list(Util.move_player_down)

    def player_interact():
        Util.add_to_event_list(Util.player_interact_level1)

    def run():
        Util.run_level1()
        
class Util:
    def load_tile_images():
        i = 0
        for filename in os.listdir("/Users/mazi/Documents/ot-harjoitustyo/spaghetti-master/src/assets/"):
            path = "/Users/mazi/Documents/ot-harjoitustyo/spaghetti-master/src/assets/" + filename
            if 'bmp' in path: 
                image_tiles[i] = pygame.image.load(path)
                image_tiles[i].convert()
                i += 1

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

    def move_player_left():
        global player_position_x
        player_position_x -= 1
        Util.draw_player(player_position_x, player_position_y)

    def move_player_right():
        global player_position_x
        player_position_x += 1
        Util.draw_player(player_position_x, player_position_y)

    def move_player_up():
        global player_position_y
        player_position_y -= 1
        Util.draw_player(player_position_x, player_position_y)

    def move_player_down():
        global player_position_y
        player_position_y += 1
        Util.draw_player(player_position_x, player_position_y)

    def player_interact_level1():
        if(player_position_x == 30 and player_position_y == 30):
            return True
        else:
            return False

    def add_to_event_list(method_to_add):
        event_list.append(method_to_add)

    def execute_next_method_in_event_list():
        event_list.pop(0)()

    def run_level1():
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
            
            if(len(event_list) > 0 and time_since_last_event_list_execute > 40): 
                Util.execute_next_method_in_event_list()
                event_execution_amount += 1
                time_since_last_event_list_execute = 0
            
            Util.draw_map()
            Util.draw_coords()
            Util.draw_goal(30, 30)
            Util.draw_player(player_position_x, player_position_y)
            Util.draw_ui(event_execution_amount)
            if(Util.player_interact_level1()):
                Util.draw_text_level_solved()
                
            pygame.display.update()

        
        pygame.quit()

    def run():
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
            
            if(len(event_list) > 0 and time_since_last_event_list_execute > 50): 
                Util.execute_next_method_in_event_list()
                time_since_last_event_list_execute = 0
            
            Util.draw_map()
            Util.draw_coords()
            Util.draw_player(player_position_x, player_position_y)
                
            pygame.display.update()

        
        pygame.quit()
    
    def quit():
        pygame.quit()
    