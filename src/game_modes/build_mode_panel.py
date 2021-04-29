import pygame_menu as pgmen
import pygame as pg
from game_modes.panel import Panel
from game_modes.special_buildings_panel import BuySpecialBuildingPanel
from game_modes.zoning_panel import ZoningPanel
import os


class BuildModePanel(Panel):
    '''
    panel enabled after clicking build mode
    '''

    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)

        self.menu = pgmen.Menu(title='BUILD - BUY',
                               width=width, height=height,
                               position=position,
                               rows=1, columns=3,
                               theme=self.get_theme(),
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        # ZONING PANEL
        self.zone_building_panel = ZoningPanel(
            width=width,
            height=height,
            position=(100, 100-100*height/game_window.window.get_height()-0.3), game_window=game_window)

        # BUY A SPECIAL BUILDING PANEL
        self.special_building_panel = BuySpecialBuildingPanel(
            width=width,
            height=height,
            position=(100, 100-100*height/game_window.window.get_height()), game_window=game_window)

        # BUTTONS
        self.zoning_button = self.menu.add.button(
            "zone buildings", self.zone_buildings)
        self.buy_building_button = self.menu.add.button(
            "special buildings", self.special_buildings)
        self.bulldoze_button = self.menu.add.button(
            "bulldoze", self.bulldoze)

    def special_buildings(self):
        '''funkcja wywoływana przy przyciśnięciu przycisku "zone building"'''

        enabled = self.special_building_panel.is_enabled()
        self.disable_subpanels()

        if enabled:
            self.special_building_panel.disable()
        else:
            self.special_building_panel.enable()
            self.game_window.zoning = False

    def zone_buildings(self):
        '''funkcja wywoływana przy przyciśnięciu przycisku "special building"'''

        enabled = self.zone_building_panel.is_enabled()
        self.disable_subpanels()

        if enabled:
            self.zone_building_panel.disable()
        else:
            self.zone_building_panel.enable()

    def bulldoze(self):
        '''TODO'''
        pass

    def get_subpanels(self):
        return [self.special_building_panel, self.zone_building_panel]
