from GameModes.GameMode import *
from City.CitySpace import *


class GameWindow(GameMode):
    def __init__(self, window, save, height, width):
        super().__init__(window, save)
        self.city_space = CitySpace(height, width)
        self.SCROLL_SPEED = 5

    def update(self):
        self.city_space.update()
        self.draw()

    def handle(self, event):
        if event.type == pg.KEYDOWN:
            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))

        if event.type == pg.KEYUP:
            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))

    def draw(self):
        self.window.fill((0, 0, 0))
        self.city_space.draw(self.window)
