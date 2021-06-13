import pygame_menu as pgmen

from city_graphics.city_images import CityImages
from panels.panel import Panel
from panels.special_buildings_panel import BuySpecialBuildingPanel
from panels.zoning_panel import ZoningPanel


class BuildModePanel(Panel):
    """ panel enabled after clicking the build mode button"""

    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.city_images = CityImages()

        self.menu = pgmen.Menu(title='BUILD - BUY',
                               width=width, height=height,
                               position=position,
                               theme=self.get_theme(),
                               columns=11, rows=1,
                               enabled=False,
                               mouse_enabled=True)

        # ZONING PANEL
        self.zone_building_panel = ZoningPanel(
            width=width,
            height=height,
            position=(100, 100 - 100 * height / game_window.window.get_height() - 0.3), game_window=game_window)

        # BUY A SPECIAL BUILDING PANEL
        self.special_building_panel = BuySpecialBuildingPanel(
            width=width,
            height=height,
            position=(100, 100 - 100 * height / game_window.window.get_height()), game_window=game_window)

        # BUTTONS
        scale = (0.075, 0.075)
        self.menu.add.image(self.city_images.get_icon(
            'modern-city'), scale=scale)
        self.zoning_button = self.menu.add.button(
            "zone buildings", self.zone_buildings)

        self.zoning_button.select(False)

        self.menu.add.label(' ')
        self.menu.add.label(' ')

        self.menu.add.image(self.city_images.get_icon('capitol'), scale=scale)
        self.buy_building_button = self.menu.add.button(
            "special buildings", self.special_buildings)

        self.menu.add.label(' ')
        self.menu.add.label(' ')

        self.menu.add.image(
            self.city_images.get_icon('bulldozer'), scale=scale)
        self.bulldoze_button = self.menu.add.button(
            "bulldoze", self.bulldoze)

        self.menu.add.label(' ')

    def special_buildings(self):
        """runs after the button tagged "special building" is pressed"""

        enabled = self.special_building_panel.is_enabled()
        self.disable_subpanels()
        self.special_building_panel.unselect_selected_widget()

        if enabled:
            self.special_building_panel.disable()
            self.unselect_selected_widget()
        else:
            self.special_building_panel.enable()
            self.game_window.bulldozing = False
            self.game_window.zoning = False

    def zone_buildings(self):
        """runs after the button tagged "zone building" is pressed"""

        enabled = self.zone_building_panel.is_enabled()
        self.disable_subpanels()
        self.zone_building_panel.unselect_selected_widget()

        if enabled:
            self.zone_building_panel.disable()
            self.game_window.zoning = False
            self.unselect_selected_widget()
        else:
            self.zone_building_panel.enable()
            self.game_window.bulldozing = False
            self.game_window.zoning = False

    def bulldoze(self):
        """function called by bulldoze button"""
        self.disable_subpanels()
        if not self.game_window.bulldozing:
            self.game_window.bulldozing = True
            self.game_window.zoning = False
        else:
            self.game_window.bulldozing = False
            self.unselect_selected_widget()

    def get_subpanels(self):
        """overrides one from Panel"""
        return [self.special_building_panel, self.zone_building_panel]

    def disable(self):
        """overrides one from Panel"""
        super().disable()
        self.unselect_selected_widget()
        self.zone_building_panel.unselect_selected_widget()
        self.special_building_panel.unselect_selected_widget()
