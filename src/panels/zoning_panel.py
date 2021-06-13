import pygame_menu as pgmen

from panels.panel import Panel


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
                               mouse_enabled=True)

        self.residential_zone_button = self.menu.add.button(
            "residential zone", self.set_zone('residential'))
        self.industrial_zone_button = self.menu.add.button(
            "industrial zone", self.set_zone('industrial'))
        self.commercial_zone_button = self.menu.add.button(
            "commercial zone", self.set_zone('commercial'))

        self.unselect_selected_widget()

    def set_zone(self, zone_type):
        def change_zoning():
            if not self.game_window.set_zoning(zone_type):
                self.unselect_selected_widget()

        return change_zoning
