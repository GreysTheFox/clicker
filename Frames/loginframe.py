import pygame
from textinput import TextInput
from text import Text
from Settings import Settings

class LoginFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 150, Settings.HEIGHT//2 - 225, 216, 40], 'Simple Clicker', 32, 'white', None)
        self.loginField = TextInput(None, '', 'Enter your login...', [Settings.WIDTH//2 - 300, Settings.HEIGHT//2 - 25])
        self.passField = TextInput(None, '', 'Enter your password...', [Settings.WIDTH//2 -300, Settings.HEIGHT//2 - 75])
        self.set_objects()

    def set_objects(self):
        print('here')
        self.objects.append(self.label)
        self.objects.append(self.loginField)
        self.objects.append(self.passField)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)