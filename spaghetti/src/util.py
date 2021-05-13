import pygame
import os
import math
import importlib
from enum import Enum

from game_event import Game_Event
from wall_type import Wall_Type
from game_objects import *

from levels.level_1 import Util_Level_1
from levels.level_2 import Util_Level_2
from levels.level_3 import Util_Level_3
from levels.level_4 import Util_Level_4
from levels.level_5 import Util_Level_5
from levels.level_6 import Util_Level_6
from level_1_solution import Level_1_Solution
from level_2_solution import Level_2_Solution
from level_3_solution import Level_3_Solution
from level_4_solution import Level_4_Solution
from level_5_solution import Level_5_Solution
from level_6_solution import Level_6_Solution

class Image_Tiles:
    def __init__(self, level_name):
        self.__image_tiles = []
        self.__load_tile_images()

        # all the types of tiles currently used in game, to be called from elsewhere:
        self.wall_horizontal = self.__image_tiles[1]
        self.wall_horizontal_2 = self.__image_tiles[58]
        self.wall_horizontal_3 = self.__image_tiles[59]
        self.wall_vertical_right = self.__image_tiles[17]
        self.wall_vertical_left = self.__image_tiles[14]
        self.wall_corner_lower_right = self.__image_tiles[31]
        self.wall_corner_lower_left = self.__image_tiles[28]
        self.wall_corner_upper_right = self.__image_tiles[3]
        self.wall_corner_upper_left = self.__image_tiles[0]

        self.pillar = self.__image_tiles[141]
        self.line_vertical = self.__image_tiles[143]
        self.line_horizontal = self.__image_tiles[142]

        self.player = self.__image_tiles[6]
        self.closed_door = self.__image_tiles[32]
        self.open_door = self.__image_tiles[33]
        self.background = self.__image_tiles[15]

        self.level_solved = self.__image_tiles[140]

        self.__icons = []
        self.__load_icons()
        self.play_icon = self.__icons[0]
        self.pause_icon = self.__icons[1]
        self.reset_icon = self.__icons[2]
        self.menu_icon = self.__icons[3]

        self.level_backgrounds = []
        self.__load_level_backgrounds()
    
    def __load_tile_images(self):
        """Ladataan kaikki pelin spritesheet grafiikat assets kansiosta image_tiles listaan ja järjestetään ne oikeaan järjestykseen.
        """
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.__image_tiles.append(new_png)
    
    def __load_icons(self):
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/icons/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.__icons.append(new_png)
    
    def __load_level_backgrounds(self):
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/level_backgrounds/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.level_backgrounds.append(new_png)

class Game_Sounds:
    def __init__(self):
        self.__sounds = []
        self.__load_game_sounds()
        self.build = self.__sounds[0]
        self.hit_wall = self.__sounds[1]
        self.level_win = self.__sounds[2]

    def __load_game_sounds(self):
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/sounds/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'ogg' in path:
                new_sound = pygame.mixer.Sound(path)
                self.__sounds.append(new_sound)

class Game_State(Enum):
    MAIN_MENU = 1
    PLAYING = 2

class Util:
    """Hallinnoi pelin ja pelimoottorin kaikki perustoiminnallisuuksia. Jokaisen tason luokasta referoidaan tätä luokkaa perustoiminallisuuksia varten.

    Attributes:
        width = peli-ikkunan leveys
        height = peli-ikkunan korkeus
        window = referenssi pygamen avulla luotuun peli-ikkunaan
        font = pelin perusfontti
        font_level_solved = isompi fontti joka näkyy kun taso ratkaistaan tai hävitään
        font_playable = pelin kartan sisään piirrettävä fontti, mahdollista tulevaa tasoa varten
        path = reitti pelin hakemistoon
        tile_pixel_size = yhden pelipalikan koko kartalla, pikseleissä
        map_tiles = kartalla olevat 1024 palikkaa, eli 32*32 kokoinen kartta
        background_color = oletustaustaväri, joka ei pitäisi olla näkyvillä kun renderöinti onnistuu
        image_tiles = kaikki pelin grafiikat tässä listassa, joka koostuu spriteistä
        event_list = pelimoottori kerää kaikki pelaajan koodaamat metodikutsut tähän listaan, ja suorittaa ne kun peli lähtee pyörimään
        event_parameter_list = tähän listaan voi syöttää mahdollisia parametreja tiettyyn metodikutsuun joka tulee pelaajan koodista
        fps = pelin frames per second
    """
    def __init__(self):
        pygame.init()
        level_name = "Level_1" # get this from level util
        self.tile_pixel_size = 24
        self.width = self.tile_pixel_size * 32
        self.height = self.tile_pixel_size * 32
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Spaghetti Master")
        self.ui_height = self.tile_pixel_size * 2
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 12)
        self.font_level_solved = pygame.font.SysFont('ComicSans MS', 32)
        self.font_playable = pygame.font.SysFont('Arial', 24)

        self.path = os.path.dirname(os.path.realpath(__file__))
        self.background_color = (0, 0, 0)  # change from black to more grey

        self.tiles = Image_Tiles(level_name)
        self.sounds = Game_Sounds()
        self.sound_on = True

        self.event_list = []
        self.event_parameter_list = []
        self.event_execution_amount = 0
        self.time_since_last_event_list_execute = 0.0
        self.event_index = 0

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_speed = 40

        self.levels = [Util_Level_1(self), Util_Level_2(self), Util_Level_3(self), Util_Level_4(self), Util_Level_5(self), Util_Level_6(self)]

        self.level_util = self.levels[0]
        self.level_name = level_name
        self.level_background = self.tiles.level_backgrounds[0]
        self.level_solved = False
        self.game_paused = True
        self.play_button = self.tiles.play_icon # swaps between pause and play
        self.game_state = Game_State.MAIN_MENU

        center_x = self.width / 2
        self.play_button_position = (center_x - 25, self.height - 60)
        self.reset_button_position = (center_x + 25, self.height - 60)
        self.menu_button_position = (self.width - 60, self.height - 60)

        self.solution = Level_1_Solution(self.level_util.level)
        
        self.run()

    # -----------------------
    # main game loop:
    def run(self, is_test = False):
        run = True
        while run:
            if self.game_state == Game_State.MAIN_MENU:
                self.draw_main_menu()
                # if the quit button is pressed in events, the while loop should break
                if self.handle_main_menu_events() == False:
                    break
            elif self.game_state == Game_State.PLAYING:
                if self.should_run(is_test): # automatic window closing for tests
                    # timekeeping variables
                    self.clock.tick(self.fps)
                    self.time_since_last_event_list_execute += self.clock.tick(self.fps)
                     # if the quit button is pressed in events, the while loop should break
                    if self.handle_playing_events():
                        self.draw_current_level() # view is updated so buttons can be updated
                    else:
                        break
                    # only update map if an event has been executed
                    if self.execute_next_method_in_event_list():
                        self.draw_current_level()
                else:
                    break
        # quit game after the game loop has been terminated
        pygame.quit()

    # -----------------------
    # methods that are called from main game loop:

    def should_run(self, is_test):
        if is_test and len(self.event_list) == 0:
            return False
        return True

    def handle_playing_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                # currently defined button positions are their upper left corner, so center is new variable
                play_button_center = (381, 730)
                reset_button_center = (435, 735)
                menu_button_center = (736, 733)
                if self.distance(mouse_position, play_button_center) < 20:
                    self.game_paused = not self.game_paused
                    if self.game_paused:
                        self.play_button = self.tiles.play_icon
                    else:
                        self.play_button = self.tiles.pause_icon
                elif self.distance(mouse_position, reset_button_center) < 20:
                    self.reload_events()
                    self.reset_game_state()
                elif self.distance(mouse_position, menu_button_center) < 20:
                    self.game_state = Game_State.MAIN_MENU
                    self.game_paused = True
                    self.play_button = self.tiles.play_icon
        return True
    
    def handle_main_menu_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                # currently defined button positions are their upper left corner, so center is new variable
                level_1_button_center = (45, 35)
                level_2_button_center = (45, 60)
                level_3_button_center = (450, 60)
                level_4_button_center = (450, 60)
                level_5_button_center = (450, 60)
                level_6_button_center = (450, 60)
                print(mouse_position)
                if self.distance(mouse_position, level_1_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[0]
                    self.level_background = self.tiles.level_backgrounds[0]
                    self.solution = Level_1_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
                elif self.distance(mouse_position, level_2_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[1]
                    self.level_background = self.tiles.level_backgrounds[1]
                    self.solution = Level_2_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
                elif self.distance(mouse_position, level_3_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[2]
                    self.level_background = self.tiles.level_backgrounds[2]
                    self.solution = Level_3_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
                elif self.distance(mouse_position, level_4_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[3]
                    self.level_background = self.tiles.level_backgrounds[3]
                    self.solution = Level_4_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
                elif self.distance(mouse_position, level_5_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[4]
                    self.level_background = self.tiles.level_backgrounds[4]
                    self.solution = Level_5_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
                elif self.distance(mouse_position, level_6_button_center) < 20:
                    self.game_state = Game_State.PLAYING
                    self.level_util = self.levels[5]
                    self.level_background = self.tiles.level_backgrounds[5]
                    self.solution = Level_6_Solution(self.level_util.level)
                    self.reload_events()
                    self.draw_current_level()
        return True

    def reload_events(self):
        if self.level_util == self.levels[0]:
            self.reload_level_1_events()
        elif self.level_util == self.levels[1]:
            self.reload_level_2_events()

    def reload_level_1_events(self):
        self.event_list.clear()
        import level_1_solution
        importlib.reload(level_1_solution)
        from level_1_solution import Level_1_Solution
        self.solution = Level_1_Solution(self.level_util.level)

    def reload_level_2_events(self):
        self.event_list.clear()
        import level_2_solution
        importlib.reload(level_2_solution)
        from level_2_solution import Level_2_Solution
        self.solution = Level_2_Solution(self.level_util.level)

    def reload_level_3_events(self):
        self.event_list.clear()
        import level_3_solution
        importlib.reload(level_3_solution)
        from level_3_solution import Level_3_Solution
        self.solution = Level_3_Solution(self.level_util.level)

    def reload_level_4_events(self):
        self.event_list.clear()
        import level_4_solution
        importlib.reload(level_4_solution)
        from level_4_solution import Level_2_Solution
        self.solution = Level_4_Solution(self.level_util.level)

    def reload_level_5_events(self):
        self.event_list.clear()
        import level_5_solution
        importlib.reload(level_5_solution)
        from level_5_solution import Level_5_Solution
        self.solution = Level_5_Solution(self.level_util.level)

    def reload_level_6_events(self):
        self.event_list.clear()
        import level_6_solution
        importlib.reload(level_6_solution)
        from level_6_solution import Level_6_Solution
        self.solution = Level_6_Solution(self.level_util.level)

    def execute_next_method_in_event_list(self):
        """Suorittaa seuraavan metodin pelin aikana suoritettavien metodien listasta.
        """
        if self.game_paused:
            return

        if self.event_index < len(self.event_list) and self.time_since_last_event_list_execute > self.game_speed:
            event_type = self.event_list[self.event_index]
            player_reference = self.event_parameter_list[self.event_index]
            if event_type is Game_Event.MOVE_PLAYER_RIGHT:
                self.move_player_right(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_LEFT:
                self.move_player_left(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_UP:
                self.move_player_up(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_DOWN:
                self.move_player_down(player_reference)
            elif event_type is Game_Event.PLAYER_INTERACT:
                self.player_interact(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_WALL:
                self.player_build_wall(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_DOOR:
                self.player_build_door(player_reference)
            
            self.event_execution_amount += 1
            self.time_since_last_event_list_execute = 0
            self.event_index += 1
            return True
        # when all the events have executed, the game is paused
        if self.event_index == len(self.event_list):
            self.play_button = self.tiles.play_icon
            self.game_paused = True
            self.draw_current_level()
        return False

    def draw_current_level(self):
        self.draw_map()
        #self.draw_ui(self.event_execution_amount)
        #self.draw_coords()
        if self.level_has_been_solved():
            self.draw_tile(self.tiles.level_solved, 13, 14)
        pygame.display.update()

    def draw_main_menu(self):
        self.window.fill(self.background_color)
        self.draw_text("Level 1", 25, 25)
        self.draw_text("Level 2", 25, 50)
        self.draw_text("Level 3", 25, 75)
        self.draw_text("Level 4", 25, 100)
        self.draw_text("Level 5", 25, 125)
        self.draw_text("Level 6", 25, 150)
        pygame.display.update()

    # -----------------------
    # drawing related methods:

    def draw_map(self):
        self.window.fill(self.background_color)
        # self.draw_background_tiles()
        self.draw_level_background()
        self.draw_construction_lines()
        self.draw_pillars()
        self.draw_doors()
        self.draw_walls()
        self.draw_players()
        self.draw_coords()
        self.draw_buttons()

    def draw_text(self, text, x, y, color = (255, 255, 255)):
        """Piirtää tekstiä Pygamen avulla mihin tahansa peli-ikkunaan.

        Args:
            text (str): Teksti joka piirretään
            x (int): Tekstin x kohta pikseleissä
            y (int): Tekstin y kohta pikseleissä
        """
        text_surface = self.font.render(text, False, color)
        self.window.blit(text_surface, (x, y))

    def draw_text_level_solved(self):
        """Piirtää tekstin kun tietty taso on selvitetty.
        """
        text_surface = self.font_level_solved.render(
            'LEVEL SOLVED! :)', False, (255, 255, 255))
        self.window.blit(text_surface, (128, 256))

    def draw_text_level_failed(self):
        """Piirtää tekstin kun jokin taso on hävitty.
        """
        text_surface = self.font_level_solved.render(
            'level failed... :(', False, (255, 255, 255))
        self.window.blit(text_surface, (128, 256))

    def draw_coords(self):
        """Piirtää koordinaatit numeroina pelin kartan reunoille, jotta pelaajan on helpompi hahmottaa missä elementit ovat.
        """
        x = 0
        y = 0
        for i in range(32):
            self.draw_text(str(i), x, y)
            x += self.tile_pixel_size
        x = 0
        for i in range(32):
            self.draw_text(str(i), x, y)
            y += self.tile_pixel_size

    def draw_pillar_texts(self):
        i = 0
        for pillar in self.level_util.pillars:
            self.draw_text(str(i), pillar._Pillar__position_x * self.tile_pixel_size + 9, pillar._Pillar__position_y * self.tile_pixel_size + 4, (0, 0, 0))
            i += 1

    def draw_buttons(self):
        self.window.blit(self.play_button, (self.play_button_position[0], self.play_button_position[1]))
        self.window.blit(self.tiles.reset_icon, (self.reset_button_position[0], self.reset_button_position[1]))
        self.window.blit(self.tiles.menu_icon, (self.menu_button_position[0], self.menu_button_position[1]))

    def draw_tile(self, tile, x, y):
        """Piirtää avoimen oven.
        Args:
            x (int): Oven kohta kartalla (ei pikseleissä) x suunnassa.
            y (int): Oven kohta kartalla (ei pikseleissä) y suunnassa.
        """
        x *= self.tile_pixel_size
        y *= self.tile_pixel_size
        #y += self.ui_height
        self.window.blit(tile, (x, y))

    def draw_pillars(self):
        for pillar in self.level_util.pillars:
            self.draw_tile(self.tiles.pillar, pillar._Pillar__position_x, pillar._Pillar__position_y)
        self.draw_pillar_texts()

    def draw_construction_lines(self):
        for i in range(len(self.level_util.pillars)):
            if i == len(self.level_util.pillars)-1:
                start_x = self.level_util.pillars[i]._Pillar__position_x
                end_x = self.level_util.pillars[0]._Pillar__position_x
            else:
                start_x = self.level_util.pillars[i]._Pillar__position_x
                end_x = self.level_util.pillars[i+1]._Pillar__position_x
            if start_x == end_x:
                if i == len(self.level_util.pillars)-1:
                    start_y = self.level_util.pillars[i]._Pillar__position_y
                    end_y = self.level_util.pillars[0]._Pillar__position_y
                else:
                    start_y = self.level_util.pillars[i]._Pillar__position_y
                    end_y = self.level_util.pillars[i+1]._Pillar__position_y
                y = start_y
                while y != end_y:
                    self.draw_tile(self.tiles.line_vertical, start_x, y)
                    if end_y > y:
                        y += 1
                    else:
                        y -= 1
            else:
                start_y = self.level_util.pillars[i]._Pillar__position_y
                x = start_x
                while x != end_x:
                    self.draw_tile(self.tiles.line_horizontal, x, start_y)
                    if end_x > x:
                        x += 1
                    else:
                        x -= 1

    def draw_ui(self, amt):
        self.draw_text(self.level_name, 16, 16)
        self.draw_text('call_amount=' + str(amt), 16, 32)

    def draw_level_background(self):
        self.window.blit(self.level_background, (0, 0))

    def draw_background_tiles(self):
        for x in range(32):
            for y in range(32):
                self.draw_tile(self.tiles.background, x, y)

    def draw_doors(self):
        for door in self.level_util.doors:
            if door._Door__is_open:
                self.draw_tile(self.tiles.open_door, door._Door__position_x, door._Door__position_y)
            else:
                self.draw_tile(self.tiles.closed_door, door._Door__position_x, door._Door__position_y)
    
    def draw_players(self):
        for player in self.level_util.players:
            if player._Player__draw_player:
                self.draw_tile(self.tiles.player, player._Player__position_x, player._Player__position_y)

    def draw_walls(self):
        for wall in self.level_util.walls:
            tile_to_draw = None
            
            if wall.type == Wall_Type.HORIZONTAL:
                tile_to_draw = self.tiles.wall_horizontal
            elif wall.type == Wall_Type.DOOR:
                tile_to_draw = self.tiles.open_door
            if wall.type == Wall_Type.VERTICAL_LEFT:
                tile_to_draw = self.tiles.wall_vertical_left
            elif wall.type == Wall_Type.VERTICAL_RIGHT:
                tile_to_draw = self.tiles.wall_vertical_right
            elif wall.type == Wall_Type.CORNER_LOWER_LEFT:
                tile_to_draw = self.tiles.wall_corner_lower_left
            elif wall.type == Wall_Type.CORNER_UPPER_LEFT:
                tile_to_draw = self.tiles.wall_corner_upper_left
            elif wall.type == Wall_Type.CORNER_LOWER_RIGHT:
                tile_to_draw = self.tiles.wall_corner_lower_right
            elif wall.type == Wall_Type.CORNER_UPPER_RIGHT:
                tile_to_draw = self.tiles.wall_corner_upper_right

            if tile_to_draw:
                self.draw_tile(tile_to_draw, wall._Wall__position_x, wall._Wall__position_y)

    # -----------------------
    # player event related methods:
    # maybe move to play class?

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
        self.play_sound(self.sounds.build)
        new_wall = Wall(player._Player__position_x, player._Player__position_y)
        self.level_util.walls.append(new_wall)
        self.set_correct_wall_type(new_wall)

    def player_build_door(self, player):
        self.play_sound(self.sounds.build)
        new_door = Wall(player._Player__position_x, player._Player__position_y)
        new_door.type = Wall_Type.DOOR
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
            if self.level_solved == False:
                self.play_sound(self.sounds.level_win)
                self.level_solved = True
            return True
        return False        

    def collision_in_position(self, x, y):
        collidable_wall = self.get_wall_in_position(x, y)
        if collidable_wall and collidable_wall.type is not Wall_Type.DOOR:
            self.play_sound(self.sounds.hit_wall)
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
            new_wall.type = Wall_Type.HORIZONTAL
        
        if not wall_right and not wall_left and wall_up and wall_up.type == Wall_Type.VERTICAL_RIGHT:
            new_wall.type = Wall_Type.VERTICAL_RIGHT
        if not wall_right and not wall_left and wall_down and wall_down.type == Wall_Type.VERTICAL_RIGHT:
            new_wall.type = Wall_Type.VERTICAL_RIGHT
        if not wall_right and not wall_left and wall_up and wall_up.type == Wall_Type.VERTICAL_LEFT:
            new_wall.type = Wall_Type.VERTICAL_LEFT
        if not wall_right and not wall_left and wall_down and wall_down.type == Wall_Type.VERTICAL_LEFT:
            new_wall.type = Wall_Type.VERTICAL_LEFT
        
        if not wall_right and not wall_left and not wall_up and wall_down and wall_down_right:
            new_wall.type = Wall_Type.VERTICAL_LEFT
            wall_down.type = Wall_Type.CORNER_LOWER_LEFT
        if not wall_right and not wall_left and wall_up and wall_up_left:
            new_wall.type = Wall_Type.VERTICAL_RIGHT
            wall_up.type = Wall_Type.CORNER_UPPER_RIGHT
        if wall_right and wall_down_right and wall_down_right.type == Wall_Type.VERTICAL_RIGHT:
            new_wall.type = Wall_Type.HORIZONTAL
            wall_right.type = Wall_Type.CORNER_UPPER_RIGHT

        if wall_left and wall_down_left:
            new_wall.type = Wall_Type.HORIZONTAL
            wall_left.type = Wall_Type.CORNER_UPPER_LEFT

        if not wall_right and wall_left and wall_up:
            new_wall.type = Wall_Type.CORNER_LOWER_RIGHT
        
        if wall_down and wall_down.type == Wall_Type.VERTICAL_LEFT:
            new_wall.type = Wall_Type.VERTICAL_LEFT
        
        if not wall_right and not wall_left and not wall_up and not wall_down_right and wall_down and wall_down_left:
            new_wall.type = Wall_Type.VERTICAL_RIGHT
            wall_down.type = Wall_Type.CORNER_LOWER_RIGHT
    
    def get_wall_in_position(self, x, y):
        for wall in self.level_util.walls:
            if wall._Wall__position_x == x and wall._Wall__position_y == y:
                return wall

    def play_sound(self, sound):
        if self.sound_on: 
            pygame.mixer.Sound.play(sound)

    # event list addition:

    def add_to_event_list(self, method_name, method_parameter):
        """Lisää tietyn metodikutsun suoritettavien metodien listaan, eli event_list listaan.

        Args:
            method_to_add (metodikutsu): Mikä tahansa metodi joka halutaan lisätä suoritettavien metodien listaan.
            parameter (metodikutsun parametrin): Aiemman metodin parametri jota tarvitaan.
        """
        self.event_list.append(method_name)
        self.event_parameter_list.append(method_parameter)

    def get_game_state(self): 
        self.sound_on = False
        for i in range(len(self.event_list)):
            event_type = self.event_list[i]
            player_reference = self.event_parameter_list[i]
            
            if event_type is Game_Event.MOVE_PLAYER_RIGHT:
                self.move_player_right(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_LEFT:
                self.move_player_left(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_UP:
                self.move_player_up(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_DOWN:
                self.move_player_down(player_reference)
            elif event_type is Game_Event.PLAYER_INTERACT:
                self.player_interact(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_WALL:
                self.player_build_wall(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_DOOR:
                self.player_build_door(player_reference)
        self.sound_on = True

    def reset_game_state(self):
        self.game_paused = True
        self.play_button = self.tiles.play_icon
        self.level_util.walls.clear()
        for player in self.level_util.players:
            player._Player__position_x = player._Player__original_x
            player._Player__position_y = player._Player__original_y
        self.event_index = 0

    def distance(self, p1, p2):
        return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))