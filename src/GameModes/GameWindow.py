from GameModes.GameMode import *
from City.CitySpace import *


class GameWindow(GameMode):
    def __init__(self, window, save, height, width):
        super().__init__(window, save)
        self.city_space = CitySpace(height, width)

    def update(self):
        self.draw()

    def handle(self, event):
        pass

    def draw(self):
        self.city_space.draw(self.window)
