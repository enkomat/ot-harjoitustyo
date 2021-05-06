import pygame
import os
import random
import math
from pymitter import EventEmitter

global event_emitter
event_emitter = EventEmitter()

class Image_Tile:
    def __init__(self, util):
        self.player = util.image_tiles[6]
        self.closed_door = util.image_tiles[32]
        self.open_door = util.image_tiles[33]
        self.background = util.image_tiles[15]

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

        self.image_tiles = []
        self.tile = None

        self.event_list = []
        self.event_parameter_list = []
        self.time_since_last_event_list_execute = 0.0
        self.event_execution_amount = 0

        self.fps = 60
    
    def load_tile_images(self):
        """Ladataan kaikki pelin grafiikat assets kansiosta image_tiles listaan ja järjestetään ne oikeaan järjestykseen.
        """
        i = 0
        asset_path = os.path.dirname(os.path.realpath(__file__)) + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'bmp' in path:
                new_bmp = pygame.image.load(path)
                new_bmp.convert()
                self.image_tiles.append(new_bmp)
        
        self.tile = Image_Tile(self) # create this object only after the tiles have been loaded

    # drawing related functions:

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
            x += 16
        x = 0
        for i in range(32):
            self.draw_text(str(i), x, y)
            y += 16

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

    def draw_ui(self, amt, level_name):
        self.draw_text(level_name, 16, 16)
        self.draw_text('call_amount=' + str(amt), 16, 32)

    def draw_map(self, level_util):
        self.window.fill(self.background_color)
        self.draw_background_tiles()
        self.draw_doors(level_util)
        self.draw_players(level_util)

    def draw_background_tiles(self):
        for x in range(32):
            for y in range(32):
                self.draw_tile(self.tile.background, x, y)

    def draw_doors(self, level_util):
        for door in level_util.doors:
            if door._Door__is_open:
                self.draw_tile(self.tile.open_door, door._Door__position_x, door._Door__position_y)
            else:
                self.draw_tile(self.tile.closed_door, door._Door__position_x, door._Door__position_y)
    
    def draw_players(self, level_util):
        for player in level_util.players:
            if player._Player__draw_player:
                self.draw_tile(self.tile.player, player._Player__position_x, player._Player__position_y)

    # current events:

    @event_emitter.on("move_player_left")
    def move_player_left(self, player):
        """Liikuttaa pelaajaa yhden ruudun vasemmalle.
        """
        player._Player__position_x -= 1

    @event_emitter.on("move_player_right")
    def move_player_right(self, player):
        """Liikuttaa pelaajaa yhden ruudun oikealle.
        """
        player._Player__position_x += 1

    @event_emitter.on("move_player_up")
    def move_player_up(self, player):
        """Liikuttaa pelaajaa yhden ruudun ylöspäin.
        """
        player._Player__position_y -= 1

    @event_emitter.on("move_player_down")
    def move_player_down(self, player):
        """Liikuttaa pelaajaa yhden ruudun alaspäin.
        """
        player._Player__position_y += 1
    
    @event_emitter.on("player_interact")
    def player_interact(self, player):
        """Laittaa pelaajan avaamaan oven, jos se on sen päällä. Jos pelaaja onnistuu avaamaan oven, päivitetään ovi avonaiseksi.

        Returns:
            bool: Palauttaa onko pelaaja avannut oven onnistuneesti.
        """
        if player._Player__level_util.interact_condition(player):
            player._Player__level_util.interact_action(player)

    # interactions with the world:

    def over_door(self, player):
        for door in player._Player__level_util.doors:
            if (door._Door__position_x == player._Player__position_x) and (door._Door__position_y == player._Player__position_y):
                return True
        return False

    def open_door(self, player):
        for door in player._Player__level_util.doors:
            if (door._Door__position_x == player._Player__position_x) and (door._Door__position_y == player._Player__position_y):
                door._Door__is_open = True
                player._Player__draw_player = False
                player._Player__has_interacted = True

    # main game loop and the methods that support it:

    def run(self, level_util, level_name, is_test=False, speed = 2):
        self.load_tile_images()
        clock = pygame.time.Clock()

        while self.should_run(is_test):
            # event execution related methods
            clock.tick(self.fps)
            self.time_since_last_event_list_execute += clock.tick(self.fps)
            self.execute_next_method_in_event_list(speed)
            
            # drawing related methods
            self.draw_map(level_util)
            self.draw_ui(self.event_execution_amount, level_name)
            self.draw_coords()
            if level_util.level_has_been_solved():
                self.draw_text_level_solved()
            
            pygame.display.update()

        # quit game after the game loop has been terminated
        pygame.quit()

    def should_run(self, is_test):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        if is_test and len(self.event_list) == 0:
            return False
        return True

    def execute_next_method_in_event_list(self, speed):
        """Suorittaa seuraavan metodin pelin aikana suoritettavien metodien listasta.
        """
        if(len(self.event_list) > 0 and self.time_since_last_event_list_execute > speed):
            method_parameter = self.event_parameter_list.pop(0)
            method_name = self.event_list.pop(0)
            event_emitter.emit(method_name, self, method_parameter)
            self.event_execution_amount += 1
            self.time_since_last_event_list_execute = 0

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
        self.__util.add_to_event_list("move_player_left", self)

    def move_right(self):
        self.__util.add_to_event_list("move_player_right", self)

    def move_up(self):
        self.__util.add_to_event_list("move_player_up", self)

    def move_down(self):
        self.__util.add_to_event_list("move_player_down", self)

    def interact(self):
        self.__util.add_to_event_list("player_interact", self)

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

class Util_Level_1:
    """Pelin ensimmäisen tason työkalupakettiluokka.

    Attributes:
        util = Util olio
        player_position_x = pelaajan paikka kartalla x suunnassa
        player_position_y = pelaajan paikka kartalla y suunnassa
        door = tason ovi ja sen paikka parametreina konstruktorille
    """
    def __init__(self):
        self.util = Util()
        self.player = Player(self, 1, 1)
        self.players = [self.player]
        self.door = Door(30, 30)
        self.doors = [self.door]
        self.event_list = self.util.event_list

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)
    
    def level_has_been_solved(self):
        return self.player._Player__has_interacted

    def run(self, is_test=False):
        self.util.run(self, "Level_1", is_test, 40)

class Level_1:
    """Pelaajalle avoinna oleva luokka jonka kautta kutsutaan tason ratkaisemiseen tarkoitettuja metodeja.
    """
    def __init__(self):
        self.__util_level_1 = Util_Level_1()
        self.player = self.__util_level_1.player

    def run(self):
        """Laittaa pelin pyörimään. Poistaa pelaajalta mahdollisuuden suorittaa peliluuppi testimoodissa.
        """
        self.__util_level_1.run()

class Util_Level_2:
    """Toisen tason työkalupakkiluokka.

    Attributes:
        players: kaikki pelaajat listassa
        doors: kaikki ovet listassa
    """
    def __init__(self):
        self.util = Util()

        self.p1 = Player(self, 1, 1)
        self.p2 = Player(self, 3, 1)
        self.p3 = Player(self, 5, 1)
        self.p4 = Player(self, 7, 1)
        self.p5 = Player(self, 9, 1)
        self.p6 = Player(self, 11, 1)
        self.p7 = Player(self, 13, 1)
        self.p8 = Player(self, 15, 1)
        self.p9 = Player(self, 17, 1)
        self.p11 = Player(self, 21, 1)
        self.p10 = Player(self, 19, 1)
        self.p12 = Player(self, 23, 1)
        self.p13 = Player(self, 25, 1)
        self.p14 = Player(self, 27, 1)
        self.p15 = Player(self, 29, 1)
        self.p16 = Player(self, 31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = Door(1, 30)
        self.g2 = Door(3, 30)
        self.g3 = Door(5, 30)
        self.g4 = Door(7, 30)
        self.g5 = Door(9, 30)
        self.g6 = Door(11, 30)
        self.g7 = Door(13, 30)
        self.g8 = Door(15, 30)
        self.g9 = Door(17, 30)
        self.g10 = Door(19, 30)
        self.g11 = Door(21, 30)
        self.g12 = Door(23, 30)
        self.g13 = Door(25, 30)
        self.g14 = Door(27, 30)
        self.g15 = Door(29, 30)
        self.g16 = Door(31, 30)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)

    def level_has_been_solved(self):
        for player in self.players:
            if player._Player__has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        self.util.run(self, "Level_2", is_test)

class Level_2:
    """Toisen tason ratkomiseen tarkoitettu luokka.
    """
    def __init__(self):
        self.__util_level_2 = Util_Level_2()
        self.players = self.__util_level_2.players

    def run(self):
        self.__util_level_2.run()

class Util_Level_3:
    def __init__(self):
        self.util = Util()
        
        self.p1 = Player(self, 1, 1)
        self.p2 = Player(self, 3, 30)
        self.p3 = Player(self, 5, 1)
        self.p4 = Player(self, 7, 30)
        self.p5 = Player(self, 9, 1)
        self.p6 = Player(self, 11, 30)
        self.p7 = Player(self, 13, 1)
        self.p8 = Player(self, 15, 30)
        self.p9 = Player(self, 17, 1)
        self.p10 = Player(self, 19, 30)
        self.p11 = Player(self, 21, 1)
        self.p12 = Player(self, 23, 30)
        self.p13 = Player(self, 25, 1)
        self.p14 = Player(self, 27, 30)
        self.p15 = Player(self, 29, 1)
        self.p16 = Player(self, 31, 30)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.g1 = Door(1, 30)
        self.g2 = Door(3, 1)
        self.g3 = Door(5, 30)
        self.g4 = Door(7, 1)
        self.g5 = Door(9, 30)
        self.g6 = Door(11, 1)
        self.g7 = Door(13, 30)
        self.g8 = Door(15, 1)
        self.g9 = Door(17, 30)
        self.g10 = Door(19, 1)
        self.g11 = Door(21, 30)
        self.g12 = Door(23, 1)
        self.g13 = Door(25, 30)
        self.g14 = Door(27, 1)
        self.g15 = Door(29, 30)
        self.g16 = Door(31, 1)
        self.doors = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8,
             self.g9, self.g10, self.g11, self.g12, self.g13, self.g14, self.g15, self.g16]

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)

    def level_has_been_solved(self):
        for player in self.players:
            if player._Player__has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        self.util.run(self, "Level_3", is_test)

class Level_3:
    def __init__(self):
        self.__util_level_3 = Util_Level_3()
        self.players = self.__util_level_3.players

    def run(self):
        self.__util_level_3.run()

class Util_Level_4:
    def __init__(self):
        self.util = Util()

        self.p1 = Player(self, 1, 1)
        self.p2 = Player(self, 3, 1)
        self.p3 = Player(self, 5, 1)
        self.p4 = Player(self, 7, 1)
        self.p5 = Player(self, 9, 1)
        self.p6 = Player(self, 11, 1)
        self.p7 = Player(self, 13, 1)
        self.p8 = Player(self, 15, 1)
        self.p9 = Player(self, 17, 1)
        self.p11 = Player(self, 21, 1)
        self.p10 = Player(self, 19, 1)
        self.p12 = Player(self, 23, 1)
        self.p13 = Player(self, 25, 1)
        self.p14 = Player(self, 27, 1)
        self.p15 = Player(self, 29, 1)
        self.p16 = Player(self, 31, 1)
        self.players = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8,
               self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]
        
        self.door = Door(15, 15)
        self.doors = [self.door]

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)

    def level_has_been_solved(self):
        for player in self.players:
            if player._Player__has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        self.util.run(self, "Level_4", is_test)

class Level_4:
    def __init__(self, players = []):
        self.__util_level_4 = Util_Level_4()
        self.players = self.__util_level_4.players

    def run(self):
        self.__util_level_4.run()

class Util_Level_5:
    def __init__(self):
        self.util = Util()
        
        self.random_positions = []
        for i in range(16):
            x = random.choice([i for i in range(1,30) if i not in [15]])
            y = random.choice([i for i in range(1,30) if i not in [15]])
            self.random_positions.append((x, y))

        self.__p1 = Player(self, self.random_positions[0][0], self.random_positions[0][1])
        self.__p2 = Player(self, self.random_positions[1][0], self.random_positions[1][1])
        self.__p3 = Player(self, self.random_positions[2][0], self.random_positions[2][1])
        self.__p4 = Player(self, self.random_positions[3][0], self.random_positions[3][1])
        self.__p5 = Player(self, self.random_positions[4][0], self.random_positions[4][1])
        self.__p6 = Player(self, self.random_positions[5][0], self.random_positions[5][1])
        self.__p7 = Player(self, self.random_positions[6][0], self.random_positions[6][1])
        self.__p8 = Player(self, self.random_positions[7][0], self.random_positions[7][1])
        self.__p9 = Player(self, self.random_positions[8][0], self.random_positions[8][1])
        self.__p10 = Player(self, self.random_positions[9][0], self.random_positions[9][1])
        self.__p11 = Player(self, self.random_positions[10][0], self.random_positions[10][1])
        self.__p12 = Player(self, self.random_positions[11][0], self.random_positions[11][1])
        self.__p13 = Player(self, self.random_positions[12][0], self.random_positions[11][1])
        self.__p14 = Player(self, self.random_positions[13][0], self.random_positions[12][1])
        self.__p15 = Player(self, self.random_positions[14][0], self.random_positions[13][1])
        self.__p16 = Player(self, self.random_positions[15][0], self.random_positions[14][1])
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
               self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

        self.door = Door(15, 15)
        self.doors = [self.door]

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)

    def level_has_been_solved(self):
        for player in self.players:
            if player._Player__has_interacted == False:
                return False
        return True

    def run(self, is_test=False):
        self.util.run(self, "Level_5", is_test)

class Level_5:
    def __init__(self, players = []):
        self.__util_level_5 = Util_Level_5()
        self.players = self.__util_level_5.players

    def run(self):
        self.__util_level_5.run()

class Util_Level_6:
    def __init__(self):
        self.util = Util()
        door_x = random.randint(1, 30)
        door_y = random.randint(1, 30)
        self.door = Door(door_x, door_y)
        self.doors = [self.door]
        
        self.random_positions = []
        for i in range(16):
            x = random.choice([i for i in range(1,30) if i not in [door_x]])
            y = random.choice([i for i in range(1,30) if i not in [door_y]])
            self.random_positions.append((x, y))

        self.__p1 = Player(self, self.random_positions[0][0], self.random_positions[0][1])
        self.__p2 = Player(self, self.random_positions[1][0], self.random_positions[1][1])
        self.__p3 = Player(self, self.random_positions[2][0], self.random_positions[2][1])
        self.__p4 = Player(self, self.random_positions[3][0], self.random_positions[3][1])
        self.__p5 = Player(self, self.random_positions[4][0], self.random_positions[4][1])
        self.__p6 = Player(self, self.random_positions[5][0], self.random_positions[5][1])
        self.__p7 = Player(self, self.random_positions[6][0], self.random_positions[6][1])
        self.__p8 = Player(self, self.random_positions[7][0], self.random_positions[7][1])
        self.__p9 = Player(self, self.random_positions[8][0], self.random_positions[8][1])
        self.__p10 = Player(self, self.random_positions[9][0], self.random_positions[9][1])
        self.__p11 = Player(self, self.random_positions[10][0], self.random_positions[10][1])
        self.__p12 = Player(self, self.random_positions[11][0], self.random_positions[11][1])
        self.__p13 = Player(self, self.random_positions[12][0], self.random_positions[11][1])
        self.__p14 = Player(self, self.random_positions[13][0], self.random_positions[12][1])
        self.__p15 = Player(self, self.random_positions[14][0], self.random_positions[13][1])
        self.__p16 = Player(self, self.random_positions[15][0], self.random_positions[14][1])
        self.players = [self.__p1, self.__p2, self.__p3, self.__p4, self.__p5, self.__p6, self.__p7, self.__p8,
               self.__p9, self.__p10, self.__p11, self.__p12, self.__p13, self.__p14, self.__p15, self.__p16]

    def interact_condition(self, player):
        return self.util.over_door(player)

    def interact_action(self, player):
        self.util.open_door(player)

    def run(self, is_test=False):
        self.util.run(self, "Level_6", is_test)

class Level_6:
    def __init__(self, players = []):
        self.__util_level_6 = Util_Level_6()
        self.players = self.__util_level_6.players
        self.door = self.__util_level_6.door

    def run(self):
        self.__util_level_6.run()