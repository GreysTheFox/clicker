import pygame

class Settings:
    WIDTH = 640
    HEIGHT = 480
    frameNumber = 0
    BACKGROUND_COLOR = pygame.Color('black')
    end = False

    @staticmethod
    def set_scene(index):
        Settings.scene_index = index