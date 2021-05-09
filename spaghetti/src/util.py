import pygame
import os
import random
import math
from enum import Enum

class Image_Tiles:
    def __init__(self):
        self.__image_tiles = []
        self.__load_tile_images()

        # all the types of tiles currently used in game, to be called from elsewhere:
        self.wall_horizontal = self.__image_tiles[1]
        self.wall_vertical_right = self.__image_tiles[17]
        self.wall_vertical_left = self.__image_tiles[14]
        self.wall_corner_lower_right = self.__image_tiles[31]
        self.wall_corner_lower_left = self.__image_tiles[28]
        self.wall_corner_upper_right = self.__image_tiles[3]
        self.wall_corner_upper_left = self.__image_tiles[0]

        self.player = self.__image_tiles[6]
        self.closed_door = self.__image_tiles[32]
        self.open_door = self.__image_tiles[33]
        self.background = self.__image_tiles[15]
        self.level_background = None
        self.__load_level_background()
    
    def __load_tile_images(self):
        """Ladataan kaikki pelin grafiikat assets kansiosta image_tiles listaan ja järjestetään ne oikeaan järjestykseen.
        """
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.__image_tiles.append(new_png)
    
    def __load_level_background(self):
        """Ladataan kaikki pelin grafiikat assets kansiosta image_tiles listaan ja järjestetään ne oikeaan järjestykseen.
        """
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/level_backgrounds/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'level_1' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.level_background = new_png

class Wall_Type(Enum):
    HORIZONTAL = 1
    VERTICAL_RIGHT = 2
    VERTICAL_LEFT = 3
    CORNER_LOWER_RIGHT = 4
    CORNER_LOWER_LEFT = 5
    CORNER_UPPER_RIGHT = 6
    CORNER_UPPER_LEFT = 7

class Game_Event(Enum):
    MOVE_PLAYER_LEFT = 1
    MOVE_PLAYER_RIGHT = 2
    MOVE_PLAYER_UP = 3
    MOVE_PLAYER_DOWN = 4
    PLAYER_INTERACT = 5
    PLAYER_BUILD_WALL = 6

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
    def __init__(self, level_util, level_name, game_speed = 2):
        pygame.init()

        self.tile_pixel_size = 24
        self.width = self.tile_pixel_size * 32
        self.height = self.tile_pixel_size * 32
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("spaghetti")
        self.ui_height = self.tile_pixel_size * 2
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 12)
        self.font_level_solved = pygame.font.SysFont('ComicSans MS', 32)
        self.font_playable = pygame.font.SysFont('Arial', 24)

        self.path = os.path.dirname(os.path.realpath(__file__))
        self.background_color = (0, 0, 0)  # change from black to more grey

        self.tiles = Image_Tiles()

        self.event_list = []
        self.event_parameter_list = []
        self.event_execution_amount = 0
        self.time_since_last_event_list_execute = 0.0

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_speed = game_speed

        self.level_util = level_util
        self.level_name = level_name

    # -----------------------
    # main game loop:
    def run(self, is_test = False):
        self.draw_new_frame() # starting frame is drawn before any event is processed, otherwise screen will be black

        while self.should_run(is_test):
            # timekeeping variables
            self.clock.tick(self.fps)
            self.time_since_last_event_list_execute += self.clock.tick(self.fps)
            
            # only update map if an event has been executed
            if self.execute_next_method_in_event_list():
                self.draw_new_frame()

        # quit game after the game loop has been terminated
        pygame.quit()

    # -----------------------
    # methods that are called from main game loop:

    def should_run(self, is_test):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if is_test and len(self.event_list) == 0:
            return False
        return True

    def execute_next_method_in_event_list(self):
        """Suorittaa seuraavan metodin pelin aikana suoritettavien metodien listasta.
        """
        if(len(self.event_list) > 0 and self.time_since_last_event_list_execute > self.game_speed):
            event_type = self.event_list.pop(0)
            player_reference = self.event_parameter_list.pop(0)
            
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
            
            self.event_execution_amount += 1
            self.time_since_last_event_list_execute = 0
            return True
        return False

    def draw_new_frame(self):
        self.draw_map()
        #self.draw_ui(self.event_execution_amount)
        #self.draw_coords()
        if self.level_has_been_solved():
            self.draw_text_level_solved()
        pygame.display.update()

    # -----------------------
    # drawing related methods:

    def draw_map(self):
        self.window.fill(self.background_color)
        # self.draw_background_tiles()
        self.draw_level_background()
        self.draw_pillar_texts()
        self.draw_walls()
        self.draw_doors()
        self.draw_players()
        self.draw_coords()

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
            self.draw_text(str(i), pillar.get_position_x() * self.tile_pixel_size + 9, pillar.get_position_y() * self.tile_pixel_size + 4, (0, 0, 0))
            i += 1

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

    def draw_ui(self, amt):
        self.draw_text(self.level_name, 16, 16)
        self.draw_text('call_amount=' + str(amt), 16, 32)


    def draw_level_background(self):
        self.window.blit(self.tiles.level_background, (0, 0))

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
            tile_to_draw = self.tiles.wall_horizontal
            
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
            
            self.draw_tile(tile_to_draw, wall.get_position_x(), wall.get_position_y())

    # -----------------------
    # player event related methods:
    # maybe move to play class?

    def move_player_left(self, player):
        """Liikuttaa pelaajaa yhden ruudun vasemmalle.
        """
        if self.get_wall_in_position(player.get_position_x() - 1, player.get_position_y()):
            return
        player._Player__position_x -= 1

    def move_player_right(self, player):
        """Liikuttaa pelaajaa yhden ruudun oikealle.
        """
        if self.get_wall_in_position(player.get_position_x() + 1, player.get_position_y()):
            return
        player._Player__position_x += 1

    def move_player_up(self, player):
        """Liikuttaa pelaajaa yhden ruudun ylöspäin.
        """
        if self.get_wall_in_position(player.get_position_x(), player.get_position_y() - 1):
            return
        player._Player__position_y -= 1

    def move_player_down(self, player):
        """Liikuttaa pelaajaa yhden ruudun alaspäin.
        """
        if self.get_wall_in_position(player.get_position_x(), player.get_position_y() + 1):
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
        new_wall = Wall(player.get_position_x(), player.get_position_y())
        self.level_util.walls.append(new_wall)
        self.set_correct_wall_type(new_wall)

    # -----------------------
    # interactions with the world:

    def over_door(self, player):
        for door in self.level_util.doors:
            if (door.get_position_x() == player.get_position_x()) and (door.get_position_y() == player.get_position_y()):
                return True
        return False

    def open_door(self, player):
        for door in self.level_util.doors:
            if (door.get_position_x() == player.get_position_x()) and (door.get_position_y() == player.get_position_y()):
                door._Door__is_open = True
                player._Player__draw_player = False
                player._Player__has_interacted = True

    def level_has_been_solved(self):
        for player in self.level_util.players:
            if player._Player__has_interacted == False:
                return False
        return True

    def set_correct_wall_type(self, new_wall):
        x = new_wall.get_position_x()
        y = new_wall.get_position_y()
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

        if wall_left and wall_down_left:
            new_wall.type = Wall_Type.HORIZONTAL
            wall_left.type = Wall_Type.CORNER_UPPER_LEFT

        if not wall_right and wall_left and wall_up:
            new_wall.type = Wall_Type.CORNER_LOWER_RIGHT
        
        if wall_down and wall_down.type == Wall_Type.VERTICAL_LEFT:
            new_wall.type = Wall_Type.VERTICAL_LEFT
        
        """
        if not wall_right and not wall_left and wall_down and wall_down_left:
            new_wall.type = Wall_Type.VERTICAL_RIGHT
            wall_down.type = Wall_Type.CORNER_LOWER_RIGHT
        """
    
    def get_wall_in_position(self, x, y):
        for wall in self.level_util.walls:
            if wall.get_position_x() == x and wall.get_position_y() == y:
                return wall

    # event list addition:

    def add_to_event_list(self, method_name, method_parameter):
        """Lisää tietyn metodikutsun suoritettavien metodien listaan, eli event_list listaan.

        Args:
            method_to_add (metodikutsu): Mikä tahansa metodi joka halutaan lisätä suoritettavien metodien listaan.
            parameter (metodikutsun parametrin): Aiemman metodin parametri jota tarvitaan.
        """
        self.event_list.append(method_name)
        self.event_parameter_list.append(method_parameter)

class Player:
    """Myöhemmissä tasoissa käytetty luokka, joka mahdollistaa sen, että tasoa ratkottaesta voi ohjata useampaa pelaajaa.
    """
    def __init__(self, level_util, position_x, position_y):
        self.__level_util = level_util
        self.__util = self.__level_util.util
        self.__position_x = position_x
        self.__position_y = position_y
        self.__has_interacted = False
        self.__draw_player = True

    def move_left(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_LEFT, self)

    def move_right(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_RIGHT, self)

    def move_up(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_UP, self)

    def move_down(self):
        self.__util.add_to_event_list(Game_Event.MOVE_PLAYER_DOWN, self)

    def interact(self):
        self.__util.add_to_event_list(Game_Event.PLAYER_INTERACT, self)

    def build_wall(self):
        self.__util.add_to_event_list(Game_Event.PLAYER_BUILD_WALL, self)

    def get_position_x(self):
        return self.__position_x

    def get_position_y(self):
        return self.__position_y

class Door:
    """Luo oven jonka paikan pelaaja voi hakea.
    """
    def __init__(self, position_x, position_y):
        self.__position_x = position_x
        self.__position_y = position_y
        self.__is_open = False
    
    def get_position_x(self):
        return self.__position_x
    
    def get_position_y(self):
        return self.__position_y

class Wall:
    def __init__(self, position_x, position_y, wall_type = Wall_Type.HORIZONTAL):
        self.__position_x = position_x
        self.__position_y = position_y
        self.type = wall_type
    
    def get_position_x(self):
        return self.__position_x
    
    def get_position_y(self):
        return self.__position_y

class Pillar:
    def __init__(self, position_x, position_y):
        self.__position_x = position_x
        self.__position_y = position_y
    
    def get_position_x(self):
        return self.__position_x
    
    def get_position_y(self):
        return self.__position_y