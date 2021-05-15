import pygame
import math

from enum_types.state_type import State_Type

from utilities.game_graphics import Game_Graphics
from utilities.event_handler import Event_Handler
from utilities.game_sounds import Game_Sounds
from utilities.game_logic import Game_Logic

from levels.level_1 import Util_Level_1
from levels.level_2 import Util_Level_2
from levels.level_3 import Util_Level_3
from levels.level_4 import Util_Level_4
from levels.level_5 import Util_Level_5
from levels.level_6 import Util_Level_6

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
        
        self.levels = [Util_Level_1(self), Util_Level_2(self), Util_Level_3(self), Util_Level_4(self), Util_Level_5(self), Util_Level_6(self)]
        self.level_util = self.levels[0]
        self.level_index = 1
        self.game_paused = True
        self.game_state = State_Type.MAIN_MENU
        self.is_test = False
        self.solution = None
        
        self.run_game = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_speed = 40
        self.mouse_position = pygame.mouse.get_pos()
        
        self.logic = Game_Logic(self)
        self.event_handler = Event_Handler(self)
        self.gui = Game_Graphics(self)
        self.sounds = Game_Sounds()
        
        self.run()

    # -----------------------
    # main game loop:
    def run(self):
        while self.run_game:
            self.mouse_position = pygame.mouse.get_pos()
            
            if self.game_state == State_Type.MAIN_MENU:
                self.execute_main_menu()
            elif self.game_state == State_Type.PLAYING:
                self.execute_gameplay()
        # quit game after the game loop has been terminated
        pygame.quit()

    # -----------------------
    # methods that are called from main game loop

    def execute_main_menu(self):
        # if the quit button is pressed in events, the while loop should break
        self.handle_main_menu_keypresses()
        self.gui.draw_main_menu()

    def execute_gameplay(self):
        self.event_handler.time_since_last_event_execute += self.clock.tick(self.fps)
        self.handle_playing_keypresses()
        
        if not self.game_paused:
            self.event_handler.execute_next_method_in_event_list()
        
        if self.event_handler.all_events_have_been_executed():
            self.pause_game()
       
        self.gui.draw_current_level()

    def handle_playing_keypresses(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run_game = False
            elif event.type == pygame.MOUSEBUTTONUP:
                play_button_center = (381, 730)
                reset_button_center = (435, 735)
                menu_button_center = (736, 733)
                if self.distance(self.mouse_position, play_button_center) < 20:
                    self.play_button_pressed()
                elif self.distance(self.mouse_position, reset_button_center) < 20:
                    self.reset_button_pressed()
                elif self.distance(self.mouse_position, menu_button_center) < 20:
                    self.menu_button_pressed()

    def handle_main_menu_keypresses(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run_game = False
            elif event.type == pygame.MOUSEBUTTONUP:
                level_1_button_center = (227, 265)
                level_2_button_center = (323, 316)
                level_3_button_center = (396, 387)
                level_4_button_center = (493, 340)
                level_5_button_center = (444, 484)
                level_6_button_center = (491, 556)

                if self.distance(self.mouse_position, level_1_button_center) < 20:
                    self.go_to_level(self.levels[0], self.gui.tiles.level_backgrounds[1], 0)
                elif self.distance(self.mouse_position, level_2_button_center) < 20:
                    self.go_to_level(self.levels[1], self.gui.tiles.level_backgrounds[1], 1)
                elif self.distance(self.mouse_position, level_3_button_center) < 20:
                    self.go_to_level(self.levels[2], self.gui.tiles.level_backgrounds[1], 2)
                elif self.distance(self.mouse_position, level_4_button_center) < 20:
                    self.go_to_level(self.levels[3], self.gui.tiles.level_backgrounds[1], 3)
                elif self.distance(self.mouse_position, level_5_button_center) < 20:
                    self.go_to_level(self.levels[4], self.gui.tiles.level_backgrounds[0], 4)
                elif self.distance(self.mouse_position, level_6_button_center) < 20:
                    self.go_to_level(self.levels[5], self.gui.tiles.level_backgrounds[1], 5)
    
    def play_button_pressed(self):
        self.game_paused = not self.game_paused
        if self.game_paused:
            self.gui.play_button = self.gui.tiles.play_icon
        else:
            if self.event_handler.event_index == 0:
                self.event_handler.reload_events(self.level_index)
            self.gui.play_button = self.gui.tiles.pause_icon

    def reset_button_pressed(self):
        self.reset_game_state()

    def menu_button_pressed(self):
        self.game_state = State_Type.MAIN_MENU
        self.game_paused = True
        self.gui.play_button = self.gui.tiles.play_icon

    def pause_game(self):
        self.gui.play_button = self.gui.tiles.play_icon
        self.game_paused = True

    def go_to_level(self, level_util, background, level_index):
        self.game_state = State_Type.PLAYING
        self.level_util = level_util
        self.gui.level_background = background
        self.level_index = level_index
        self.reset_game_state()
        self.gui.draw_current_level()

    def get_game_state(self): 
        self.sounds.sound_on = False # hack to not hear the player moving while going thru events
        self.event_handler.execute_all_events()
        self.sounds.sound_on = True

    def reset_level(self):
        self.level_util.walls.clear()
        for player in self.level_util.players:
            player._Player__position_x = player._Player__original_x
            player._Player__position_y = player._Player__original_y
            player._Player__has_interacted = False
            player._Player__draw_player = True
        for door in self.level_util.doors:
            door._Door__is_open = False
        self.event_handler.event_index = 0
        self.event_execution_amount = 0
        self.level_util.level_solved = False

    def reset_game_state(self):
        self.level_util = self.levels[self.level_index]
        self.game_paused = True
        self.gui.play_button = self.gui.tiles.play_icon
        self.reset_level()    

    def distance(self, p1, p2):
        return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))