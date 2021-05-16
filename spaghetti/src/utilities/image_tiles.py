import pygame
import os
import re

class ImageTiles:
    def __init__(self):
        
        directory = os.path.dirname(os.path.realpath(__file__))
        self.directory_path = re.sub('/utilities', '', directory)
        self.__image_tiles = []
        self.__load_tile_images()

        # all the enum_types of tiles currently used in game, to be called from elsewhere:
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
        asset_path = self.directory_path + "/assets/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.__image_tiles.append(new_png)

    def __load_icons(self):
        asset_path = self.directory_path + "/assets/icons/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'png' in path:
                new_png = pygame.image.load(path)
                new_png.convert()
                self.__icons.append(new_png)

    def __load_level_backgrounds(self):
        asset_paths = []
        asset_paths.append(self.directory_path + "/assets/level_backgrounds/Level_1.png")
        asset_paths.append(self.directory_path + "/assets/level_backgrounds/Level_2.png")
        asset_paths.append(self.directory_path + "/assets/level_backgrounds/Level_3.png")
        for path in asset_paths:
            new_png = pygame.image.load(path)
            new_png.convert()
            self.level_backgrounds.append(new_png)
