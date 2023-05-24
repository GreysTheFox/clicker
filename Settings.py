import pygame

class Settings:
    WIDTH = 640
    HEIGHT = 480
    frameNumber = 0
    BACKGROUND_COLOR = pygame.Color('black')
    name = ''
    password = ''
    score = 0
    end = False

    @staticmethod
    def set_frame(index):
        Settings.frameNumber = index

    @staticmethod
    def set_score():
        Settings.score += 1