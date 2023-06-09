import pygame
from text import Text
from button import Button
from Settings import Settings

class ClickerFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 250, 25, 92, 18], 'Simple Clicker', 24, 'white', None)
        self.count = Text([Settings.WIDTH//2 - 10, 25, 92, 18], '', 48, 'white', None)
        self.count.text = str(Settings.score)
        self.click = Button([Settings.WIDTH//2-75, Settings.HEIGHT//2, 150, 150], pygame.Color('white'), self.onClick, 'click')
        self.set_objects()

    def onClick(self):
        Settings.set_score()
        self.count.text = str(Settings.score)

    def onRelease(self):
        pass

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.count)
        self.objects.append(self.click)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)