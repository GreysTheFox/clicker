from Settings import Settings
from text import Text
from button import Button

class LoginFrame:
    def __init__(self) -> None:
        self.objects = []
        self.label = Text([Settings.WIDTH//2 - 150, Settings.HEIGHT//2 - 225, 216, 40], 'Simple Clicker', 32, 'white', None)
        self.login = Button([Settings.WIDTH//2 -300, Settings.HEIGHT//2 - 125, 122, 38])
        self.register = Button([Settings.WIDTH//2 -300, Settings.HEIGHT//2 - 125, 122, 38])
        self.set_objects()

    def onClick(self):
        password = self.passField.text
        login = self.loginField.text

    def set_objects(self):
        self.objects.append(self.label)
        self.objects.append(self.loginField)
        self.objects.append(self.passField)

    def logic(self, event):
        for item in self.objects:
            item.logic(event)

    def draw(self, screen):
        for item in self.objects:
            item.update(screen)