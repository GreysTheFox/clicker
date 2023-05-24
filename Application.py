import pygame, pymysql

from SQL import send_score

from Settings import Settings
from Frames.loadframe import LoadFrame
from Frames.loginframe import LoginFrame
from Frames.registerframe import RegisterFrame
from Frames.clickerframe import ClickerFrame

class Application:
    def __init__(self, screen):
        self.screen = screen
        self.isSending = False
        self.frames = [
            LoadFrame(),
            LoginFrame(),
            RegisterFrame(),
            ClickerFrame()
        ]

    def main_loop(self):
        self.draw_objects()
        self.scene_events()


    def draw_objects(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.frames[Settings.frameNumber].draw(self.screen)
        pygame.display.flip()

    def scene_events(self):
        for event in pygame.event.get():
            self.application_exit(event)
            self.frames[Settings.frameNumber].logic(event)

    def application_exit(self, event):
        if event.type != pygame.QUIT:
            return
        if event.type == pygame.QUIT and Settings.frameNumber == 3:
            send_score(Settings.name, Settings.password, Settings.score)
            Settings.end = True
        Settings.end = True

    def run(self):
        while not Settings.end:
            self.main_loop()
    