import pygame

class TextInput:
    def __init__(self, font: str, text: str, baseText: str, pos: list):
        self.font = pygame.font.Font(font, 32)
        self.text = ''
        self.baseText = baseText
        self.isActive = False
        self.activeColor = pygame.Color('white')
        self.passiveColor = pygame.Color('gray15')
        self.color = self.passiveColor
        self.rect = pygame.Rect(pos[0], pos[1], 400, 32)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.isActive = True
            self.color = self.activeColor
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
            self.isActive = False
            self.color = self.passiveColor

    def text_add(self, event):
        if event.type == pygame.KEYDOWN and self.isActive:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.isActive = False
                self.color = self.passiveColor
            else:
                self.text += event.unicode

    def logic(self, event):
        self.clicked(event)
        if (self.text == self.baseText and self.isActive):
            self.text = ''
        elif (self.text != self.baseText and self.text != '' and not self.isActive):
            self.text = self.text
        elif (self.text != self.baseText and self.text == '' and not self.isActive):
            self.text = self.baseText
        if self.isActive:
            self.text_add(event)

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)

        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        self.rect.w = max(200, text_surface.get_width() + 10)
