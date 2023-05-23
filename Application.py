import pygame

from Settings import Settings
from Frames.loadframe import LoadFrame
from Frames.loginframe import LoginFrame

class Application:
    def __init__(self, screen):
        self.screen = screen
        self.frames = [
            #LoadFrame(),
            LoginFrame(),
            #RegisterFrame(),
            #ClickerFrame()
        ]
    
    

    def main_loop(self):
        pass

    def draw_objects(self):
        self.scenes[Settings.frameNumber].draw(self.screen)

    def scene_events(self):
        for event in pygame.event.get():
            self.scenes[Settings.scene_index].logic(event)

    def run(self):
        while not Settings.end:
            self.main_loop()
    