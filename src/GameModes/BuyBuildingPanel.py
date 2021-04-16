from GameModes.Panel import *
import pygame_menu as pgmen
from Constructs.ConstructType import ConstructType


class BuyBuildingPanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.BUY_WINDOW_WIDTH = 500
        self.BUY_WINDOW_HEIGHT = 500
        self.BUY_WINDOW_POSITION = (100, 50)
        self.enabled_window = None
        self.game_window = game_window
        self.menu = pgmen.Menu(title='BUY A BUILDING',
                               width=width, height=height,
                               position=position,
                               rows=50, columns=2,
                               theme=self.get_theme(),
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        for construct in ConstructType:
            if not construct.value.get('zone', None):
                self.menu.add.button(
                    construct.name, self.building_window_function(construct))

    def building_window_function(self, construct):
        def func():
            if not self.enabled_window or self.enabled_window.construct != construct:
                if self.enabled_window:
                    self.enabled_window.disable()

                self.enabled_window = BuyBuildingWindow(
                    self.BUY_WINDOW_WIDTH, self.BUY_WINDOW_HEIGHT,
                    self.BUY_WINDOW_POSITION, self.game_window, construct)

            else:
                self.disable()

        return func

    def handle(self, event):
        super().handle(event)
        if self.enabled_window:
            self.enabled_window.handle(event)

    def disable(self):
        if self.enabled_window:
            self.enabled_window.disable()
            self.enabled_window = None

    def draw(self, window):
        super().draw(window)
        if self.enabled_window:
            self.enabled_window.draw(window)


class BuyBuildingWindow(Panel):
    def __init__(self, width, height, position, game_window, construct):
        super().__init__(width, height, game_window)
        self.construct = construct
        self.menu = pgmen.Menu(title=construct.value['level'][0]['name'], width=width,
                               height=height, position=position, rows=10, columns=1,
                               theme=self.get_theme(), enabled=True)
        self.menu.add.button('BUY', self.buy)

    def buy(self):
        pass

    def disable(self):
        self.menu.disable()
