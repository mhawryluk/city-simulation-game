import pygame_menu as pgmen
from .Panel import *


class BuildModePanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)

        self.menu = pgmen.Menu(title='BUILD MODE',
                               width=width, height=height,
                               position=position,
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

        # BUTTONS
        self.residential_zone_button = self.menu.add.button(
            "residential zone", self.residential_zone)
        self.industrial_zone_button = self.menu.add.button(
            "industrial zone", self.industrial_zone)
        self.commercial_zone_button = self.menu.add.button(
            "commercial zone", self.commercial_zone)

    def draw(self, window):
        if self.menu.is_enabled():
            self.menu.draw(window)

    def handle(self, event):
        if self.menu.is_enabled():
            return self.menu.update([event])

    def disable(self):
        self.menu.disable()

    def enable(self):
        self.menu.enable()

    def residential_zone(self):
        pass

    def industrial_zone(self):
        pass

    def commercial_zone(self):
        print("commercial")
        pass
