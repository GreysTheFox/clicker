import pygame 

class Text:
    def __init__(self, rect, text, size, color, font):
        self.font = pygame.font.Font(font, 64)
        self.rect = rect
        self.text = text
        self.size = size
        self.color = pygame.Color(color)
        self.texture = None
    
    def logic(self):
        pass

    def update(self, screen):
        self.texture = self.font.render(self.text, True, self.color)
        screen.blit(self.text, (self.rect[0], self.rect[1]))