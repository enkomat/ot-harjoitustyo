import pygame
import os
import re

class GameSounds:
    def __init__(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        self.directory_path = re.sub('/utilities', '', directory)
        self.__sounds = []
        self.__load_game_sounds()
        self.build = self.__sounds[0]
        self.hit_wall = self.__sounds[1]
        self.level_win = self.__sounds[2]
        self.sound_on = True

    def __load_game_sounds(self):
        
        asset_path = self.directory_path + "/assets/sounds/"
        for filename in sorted(os.listdir(asset_path)):
            path = asset_path + filename
            if 'ogg' in path:
                new_sound = pygame.mixer.Sound(path)
                self.__sounds.append(new_sound)

    def play_sound(self, sound):
        if self.sound_on:
            pygame.mixer.Sound.play(sound)
