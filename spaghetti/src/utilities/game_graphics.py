import pygame

from utilities.image_tiles import ImageTiles
from enum_types.wall_type import WallType

class GameGraphics:
    def __init__(self, util):
        self.util = util

        self.tile_pixel_size = 24
        self.width = self.tile_pixel_size * 32
        self.height = self.tile_pixel_size * 32
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Spaghetti Master")
        self.background_color = (0, 0, 0)

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 12)
        self.font_level_solved = pygame.font.SysFont('ComicSans MS', 32)

        self.tile_pixel_size = 24
        self.tiles = ImageTiles()
        self.level_background = self.tiles.level_backgrounds[0]
        self.play_button = self.tiles.play_icon # swaps between pause and play
        
        center_x = self.width / 2
        self.play_button_position = (center_x - 25, self.height - 60)
        self.reset_button_position = (center_x + 25, self.height - 60)
        self.menu_button_position = (self.width - 60, self.height - 60)

    def draw_map(self):
        self.window.fill(self.background_color)
        # self.draw_background_tiles()
        self.draw_level_background()
        self.draw_construction_lines()
        self.draw_pillars()
        self.draw_doors()
        self.draw_walls()
        self.draw_players()

    def draw_text(self, text, x, y, color = (255, 255, 255)):
        """Piirtää tekstiä Pygamen avulla mihin tahansa peli-ikkunaan.

        Args:
            text (str): Teksti joka piirretään
            x (int): Tekstin x kohta pikseleissä
            y (int): Tekstin y kohta pikseleissä
        """
        text_surface = self.font.render(text, False, color)
        self.window.blit(text_surface, (x, y))

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
        for pillar in self.util.level_util.pillars:
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
        for pillar in self.util.level_util.pillars:
            self.draw_tile(self.tiles.pillar, pillar._Pillar__position_x, pillar._Pillar__position_y)
        self.draw_pillar_texts()

    def draw_construction_lines(self):
        for i in range(len(self.util.level_util.pillars)):
            if i == len(self.util.level_util.pillars)-1:
                start_x = self.util.level_util.pillars[i]._Pillar__position_x
                end_x = self.util.level_util.pillars[0]._Pillar__position_x
            else:
                start_x = self.util.level_util.pillars[i]._Pillar__position_x
                end_x = self.util.level_util.pillars[i+1]._Pillar__position_x
            if start_x == end_x:
                if i == len(self.util.level_util.pillars)-1:
                    start_y = self.util.level_util.pillars[i]._Pillar__position_y
                    end_y = self.util.level_util.pillars[0]._Pillar__position_y
                else:
                    start_y = self.util.level_util.pillars[i]._Pillar__position_y
                    end_y = self.util.level_util.pillars[i+1]._Pillar__position_y
                y = start_y
                while y != end_y:
                    self.draw_tile(self.tiles.line_vertical, start_x, y)
                    if end_y > y:
                        y += 1
                    else:
                        y -= 1
            else:
                start_y = self.util.level_util.pillars[i]._Pillar__position_y
                x = start_x
                while x != end_x:
                    self.draw_tile(self.tiles.line_horizontal, x, start_y)
                    if end_x > x:
                        x += 1
                    else:
                        x -= 1

    def draw_level_background(self):
        self.window.blit(self.level_background, (0, 0))

    def draw_background_tiles(self):
        for x in range(32):
            for y in range(32):
                self.draw_tile(self.tiles.background, x, y)

    def draw_doors(self):
        for door in self.util.level_util.doors:
            if door._Door__is_open:
                self.draw_tile(self.tiles.open_door, door._Door__position_x, door._Door__position_y)
            else:
                self.draw_tile(self.tiles.closed_door, door._Door__position_x, door._Door__position_y)
    
    def draw_players(self):
        for player in self.util.level_util.players:
            if player._Player__draw_player:
                self.draw_tile(self.tiles.player, player._Player__position_x, player._Player__position_y)

    def draw_walls(self):
        for wall in self.util.level_util.walls:
            tile_to_draw = None
            
            if wall.type == WallType.HORIZONTAL:
                tile_to_draw = self.tiles.wall_horizontal
            elif wall.type == WallType.DOOR:
                tile_to_draw = self.tiles.open_door
            if wall.type == WallType.VERTICAL_LEFT:
                tile_to_draw = self.tiles.wall_vertical_left
            elif wall.type == WallType.VERTICAL_RIGHT:
                tile_to_draw = self.tiles.wall_vertical_right
            elif wall.type == WallType.CORNER_LOWER_LEFT:
                tile_to_draw = self.tiles.wall_corner_lower_left
            elif wall.type == WallType.CORNER_UPPER_LEFT:
                tile_to_draw = self.tiles.wall_corner_upper_left
            elif wall.type == WallType.CORNER_LOWER_RIGHT:
                tile_to_draw = self.tiles.wall_corner_lower_right
            elif wall.type == WallType.CORNER_UPPER_RIGHT:
                tile_to_draw = self.tiles.wall_corner_upper_right

            if tile_to_draw:
                self.draw_tile(tile_to_draw, wall._Wall__position_x, wall._Wall__position_y)

    def draw_current_level(self):
        self.draw_map()
        self.draw_coords()
        self.draw_buttons()
        if self.util.logic.level_has_been_solved():
            self.draw_tile(self.tiles.level_solved, 13, 14)
        pygame.display.update()

    def draw_main_menu(self):
        self.window.blit(self.tiles.level_backgrounds[2], (0, 0))
        pygame.display.update()