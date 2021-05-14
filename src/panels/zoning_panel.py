from panels.panel import Panel
import pygame_menu as pgmen


class ZoningPanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.enabled_window = None
        self.game_window = game_window
        self.menu = pgmen.Menu(title='zoning',
                               width=width, height=height,
                               position=position,
                               rows=1, columns=50,
                               theme=self.get_theme(),
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        self.residential_zone_button = self.menu.add.button(
            "residential zone", self.residential_zone)
        self.industrial_zone_button = self.menu.add.button(
            "industrial zone", self.industrial_zone)
        self.commercial_zone_button = self.menu.add.button(
            "commercial zone", self.commercial_zone)

    def residential_zone(self):
        self.game_window.set_zoning("residential")

    def industrial_zone(self):
        self.game_window.set_zoning("industrial")

    def commercial_zone(self):
        self.game_window.set_zoning("commercial")
