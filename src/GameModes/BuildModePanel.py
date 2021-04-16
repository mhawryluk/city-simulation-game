import pygame_menu as pgmen
import pygame as pg
from GameModes.Panel import *
from GameModes.BuyBuildingPanel import BuyBuildingPanel
import os


class BuildModePanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)

        self.menu = pgmen.Menu(title='BUILD - BUY',
                               width=width, height=height,
                               position=position,
                               rows=1, columns=15,
                               theme=self.get_theme(),
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        # BUY A BUILDING PANEL
        self.buy_building_panel = BuyBuildingPanel(
            width=game_window.city_space.window_width/2,
            height=game_window.city_space.window_height/2,
            position=(50, 50), game_window=game_window)

        # BUTTONS
        self.residential_zone_button = self.menu.add.button(
            "residential zone", self.residential_zone)
        self.industrial_zone_button = self.menu.add.button(
            "industrial zone", self.industrial_zone)
        self.commercial_zone_button = self.menu.add.button(
            "commercial zone", self.commercial_zone)
        self.buy_building_button = self.menu.add.button(
            "buy a building", self.buy_building)
        self.bulldoze_button = self.menu.add.button(
            "bulldoze", self.bulldoze)

    def residential_zone(self):
        self.game_window.set_zoning("residential")

    def industrial_zone(self):
        self.game_window.set_zoning("industrial")

    def commercial_zone(self):
        self.game_window.set_zoning("commercial")

    def buy_building(self):
        if self.buy_building_panel.is_enabled():
            self.buy_building_panel.disable()
        else:
            self.buy_building_panel.enable()

    def bulldoze(self):
        pass

    def get_subpanels(self):
        return [self.buy_building_panel]
