import pygame

from Settings import Settings
from text import Text
from button import Button

class LoadFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 150, Settings.HEIGHT//2 - 225, 216, 40], 'Simple Clicker', 32, 'white', None)
        self.login = Button([Settings.WIDTH//2 -50, Settings.HEIGHT//2 + 50, 122, 38], pygame.Color('white'), self.onClickLogin, 'Login')
        self.register = Button([Settings.WIDTH//2 -50, Settings.HEIGHT//2 + 100, 122, 38], pygame.Color('white'), self.onClickRegister, 'Register')
        self.set_objects()

    def onClickLogin(self):
        Settings.set_frame(1)
        print(Settings.frameNumber)

    def onClickRegister(self):
        Settings.set_frame(2)
        print(Settings.frameNumber)

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.login)
        self.objects.append(self.register)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)