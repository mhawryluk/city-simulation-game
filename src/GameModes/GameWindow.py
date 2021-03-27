from GameModes.GameMode import *
from City.CitySpace import *
from GameEngineTools.SaveManager import SaveManager
from GameModes.GameWindowPanel import *


class GameWindow(GameMode):
    def __init__(self, window, save, height, width):
        super().__init__(window, save)
        self.city_space = CitySpace(
            width, height, window.get_width(), window.get_height())
        self.SCROLL_SPEED = 5
        self.change_mode = False
        self.menu_panel = GameWindowPanel(
            120, self.window.get_height())

    def update(self):
        self.city_space.update()
        self.draw()

    def handle(self, event):
        self.menu_panel.handle(event)

        if event.type == pg.KEYDOWN:
            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                self.city_space.select_lot(pg.mouse.get_pos())
            if event.button == 4:
                self.city_space.zoom(self.SCROLL_SPEED)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.city_space.select_lot(pg.mouse.get_pos())
            # zooming out
            if event.button == 5:
                self.city_space.zoom(-self.SCROLL_SPEED)

        if event.type == pg.KEYUP:

            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))

    def draw(self):
        self.window.fill((0, 0, 0))
        self.city_space.draw(self.window)
        self.menu_panel.draw(self.window)
