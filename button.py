import pygame as pg


class Button:
    def __init__(self, rect, color, function, text):
        self.rect = pg.Rect(rect)
        self.font = pg.font.Font(None, 24)
        self.color = color
        self.function = function
        self.texture = None
        self.text = text
        self.clicked = False

    def logic(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            self.function()
            self.clicked = False


    def update(self, screen):
        pg.draw.rect(screen, self.color, self.rect, 1)

        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, ((self.rect.x + 10, self.rect.y + 10)))
