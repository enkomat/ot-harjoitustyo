import pygame
import os
import random
import math
from enum import Enum

class Image_Tiles:
    def __init__(self):
        self.image_tiles = []
        self.load_tile_images()
        self.player = self.image_tiles[6]
        self.closed_door = self.image_tiles[32]
        self.open_door = self.image_tiles[33]
        self.background = self.image_tiles[15]
    
    def load_tile_images(self):
        """Ladataan kaikki pelin grafiikat assets kansiosta image_tiles listaan ja järjestetään ne oikeaan järjestykseen.
        """
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'bmp' in path:
                new_bmp = pygame.image.load(path)
                new_bmp.convert()
                self.image_tiles.append(new_bmp)

class Game_Event(Enum):
    MOVE_PLAYER_LEFT = 1
    MOVE_PLAYER_RIGHT = 2
    MOVE_PLAYER_UP = 3
    MOVE_PLAYER_DOWN = 4
    PLAYER_INTERACT = 5

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
        
        self.width = 8*64
        self.height = 9*64
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("spaghetti")
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 12)
        self.font_level_solved = pygame.font.SysFont('ComicSans MS', 32)
        self.font_playable = pygame.font.SysFont('Arial', 24)

        self.path = os.path.dirname(os.path.realpath(__file__))
        self.tile_pixel_size = 16
        self.background_color = (0, 0, 0)  # change from black to more grey

        self.tiles = Image_Tiles()

        self.event_list = []
        self.event_parameter_list = []
        self.event_execution_amount = 0
        self.time_since_last_event_list_execute = 0.0

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.level_util = level_util
        self.game_speed = game_speed
        self.level_name = level_name

    # drawing related methods:

    def draw_text(self, text, x, y):
        """Piirtää tekstiä Pygamen avulla mihin tahansa peli-ikkunaan.

        Args:
            text (str): Teksti joka piirretään
            x (int): Tekstin x kohta pikseleissä
            y (int): Tekstin y kohta pikseleissä
        """
        text_surface = self.font.render(text, False, (255, 255, 255))
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
        y = 64
        for i in range(32):
            self.draw_text(str(i), x, y)
            x += self.tile_pixel_size
        x = 0
        for i in range(32):
            self.draw_text(str(i), x, y)
            y += self.tile_pixel_size

    def draw_tile(self, tile, x, y):
        """Piirtää avoimen oven.

        Args:
            x (int): Oven kohta kartalla (ei pikseleissä) x suunnassa.
            y (int): Oven kohta kartalla (ei pikseleissä) y suunnassa.
        """
        x *= self.tile_pixel_size
        y *= self.tile_pixel_size
        y += 64
        self.window.blit(tile, (x, y))

    def draw_ui(self, amt):
        self.draw_text(self.level_name, 16, 16)
        self.draw_text('call_amount=' + str(amt), 16, 32)

    def draw_map(self):
        self.window.fill(self.background_color)
        self.draw_background_tiles()
        self.draw_doors()
        self.draw_players()

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

    # current events:

    def move_player_left(self, player):
        """Liikuttaa pelaajaa yhden ruudun vasemmalle.
        """
        player._Player__position_x -= 1

    def move_player_right(self, player):
        """Liikuttaa pelaajaa yhden ruudun oikealle.
        """
        player._Player__position_x += 1

    def move_player_up(self, player):
        """Liikuttaa pelaajaa yhden ruudun ylöspäin.
        """
        player._Player__position_y -= 1

    def move_player_down(self, player):
        """Liikuttaa pelaajaa yhden ruudun alaspäin.
        """
        player._Player__position_y += 1
    
    def player_interact(self, player):
        """Laittaa pelaajan avaamaan oven, jos se on sen päällä. Jos pelaaja onnistuu avaamaan oven, päivitetään ovi avonaiseksi.

        Returns:
            bool: Palauttaa onko pelaaja avannut oven onnistuneesti.
        """
        if self.over_door(player):
            self.open_door(player)

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
        for player in self.level_util.players:
            if player._Player__has_interacted == False:
                return False
        return True

    # event list addition:

    def add_to_event_list(self, method_name, method_parameter):
        """Lisää tietyn metodikutsun suoritettavien metodien listaan, eli event_list listaan.

        Args:
            method_to_add (metodikutsu): Mikä tahansa metodi joka halutaan lisätä suoritettavien metodien listaan.
            parameter (metodikutsun parametrin): Aiemman metodin parametri jota tarvitaan.
        """
        self.event_list.append(method_name)
        self.event_parameter_list.append(method_parameter)

    # main game loop:

    def run(self, is_test = False):
        while self.should_run(is_test):
            # timekeeping variables
            self.clock.tick(self.fps)
            self.time_since_last_event_list_execute += self.clock.tick(self.fps)
            
            # only update map if an event has been executed
            if self.execute_next_method_in_event_list():
                self.draw_new_frame()

        # quit game after the game loop has been terminated
        pygame.quit()

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
            
            self.event_execution_amount += 1
            self.time_since_last_event_list_execute = 0
            return True
        return False

    def draw_new_frame(self):
        self.draw_map()
        self.draw_ui(self.event_execution_amount)
        self.draw_coords()
        if self.level_has_been_solved():
            self.draw_text_level_solved()
        pygame.display.update()