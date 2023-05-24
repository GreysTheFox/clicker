import pygame
from textinput import TextInput
from text import Text
from button import Button
from Settings import Settings
from SQL import initialize, new_member

class RegisterFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 150, Settings.HEIGHT//2 - 225, 216, 40], 'Simple Clicker', 64, 'white', None)
        self.loginField = TextInput(None, '', 'Enter your login...', [Settings.WIDTH//2 - 300, Settings.HEIGHT//2 - 75])
        self.passField = TextInput(None, '', 'Enter your password...', [Settings.WIDTH//2 -300, Settings.HEIGHT//2 - 25])
        self.passRepeatField = TextInput(None, '', 'Repeat your password...', [Settings.WIDTH//2 -300, Settings.HEIGHT//2 + 25])
        self.submit = Button([Settings.WIDTH//2 -300, Settings.HEIGHT//2 + 75, 122, 38], pygame.Color('white'), self.onClick, 'Register')
        self.connection = initialize()
        self.set_objects()

    def onClick(self):
        if self.passField.text == self.passRepeatField.text:
            new_member(self.loginField.text, self.passField.text)
            Settings.set_frame(3)

    def onRelease(self):
        pass

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.loginField)
        self.objects.append(self.passField)
        self.objects.append(self.passRepeatField)
        self.objects.append(self.submit)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)