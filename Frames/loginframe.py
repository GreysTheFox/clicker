import pygame
from textinput import TextInput
from text import Text
from Settings import Settings

class LoginFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2, Settings.HEIGHT//2, 216, 40], 'Simple Clicker', 32, 'white', None)
        self.loginField = TextInput(None, '', 'Enter your login...', [Settings.WIDTH//2, Settings.HEIGHT//2 - 100])
        self.passField = TextInput(None, '', 'Enter your password...', [Settings.WIDTH//2, Settings.HEIGHT//2 - 200])

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.loginField)
        self.objects.append(self.passField)

    def draw(self):
        for item in self.objects:
            item.update(self.screen)