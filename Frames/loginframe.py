import pygame
from textinput import TextInput
from text import Text
from button import Button
from Settings import Settings

class LoginFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 150, Settings.HEIGHT//2 - 225, 216, 40], 'Simple Clicker', 64, 'white', None)
        self.loginField = TextInput(None, '', 'Enter your login...', [Settings.WIDTH//2 - 300, Settings.HEIGHT//2 - 75])
        self.passField = TextInput(None, '', 'Enter your password...', [Settings.WIDTH//2 -300, Settings.HEIGHT//2 - 25])
        self.submit = Button([Settings.WIDTH//2 -300, Settings.HEIGHT//2 + 50, 122, 38], pygame.Color('white'), self.onClick, 'Login')
        self.set_objects()

    def onClick(self):
        #password = self.passField.text
        #login = self.loginField.text
        Settings.set_frame(3)

    def onRelease(self):
        pass

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.loginField)
        self.objects.append(self.passField)
        self.objects.append(self.submit)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)