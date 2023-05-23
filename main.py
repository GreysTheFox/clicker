import pygame, sys
from textinput import TextInput

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([640, 480])

    text1 = TextInput(None, '', 'insert joke here', [100, 200])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            text1.state_change(event)
        screen.fill((0, 0, 0))

        text1.update(screen)
        
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
