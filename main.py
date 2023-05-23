import pygame, sys

from Settings import Settings
from Application import Application

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WIDTH, Settings.HEIGHT])
    app = Application(screen)
    app.run()

if __name__ == "__main__":
    main()
