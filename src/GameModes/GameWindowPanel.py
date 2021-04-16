import pygame as pg
import pygame_menu as pgmen
from GameModes.GameWindow import *
from GameModes.BuildModePanel import BuildModePanel
from GameModes.OptionPanel import OptionPanel
from GameModes.Panel import Panel


class GameWindowPanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='CITY SIMULATION GAME',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

        # BUILD MODE PANEL
        window_width = game_window.city_space.window_width
        window_height = game_window.city_space.window_height
        self.build_mode_panel = BuildModePanel(
            width=window_width - width, height=height//10,
            position=(100, 100),
            game_window=game_window)

        # OPTIONS PANEL
        self.option_panel = OptionPanel(
            width=window_width//2, height=window_height//2, game_window=game_window)

        # BUTTONS
        self.play_button = self.menu.add.button("play", self.play)
        self.road_button = self.menu.add.button("add roads", self.add_road)
        self.build_mode_button = self.menu.add.button(
            "build mode", self.build_mode)
        self.stats_button = self.menu.add.button(
            "stats", self.stats)
        self.options_button = self.menu.add.button(
            "options", self.options)
        self.save_button = self.menu.add.button(
            "save", self.save)
        self.main_menu_button = self.menu.add.button(
            "main menu", self.main_menu)

    def play(self):
        self.game_window.mode = "game_mode"
        if self.game_window.zoning:
            self.game_window.zoning = False
            self.game_window.zoning_type = None
            self.game_window.toggle_zone_highlighting()
        self.build_mode_panel.disable_all_panels()

    def add_road(self):
        self.game_window.mode = "road_placing" if self.game_window.mode != "road_placing" else "game_mode"
        self.game_window.zoning = False

    def select_area(self):
        pass

    def stats(self):
        pass

    def main_menu(self):
        self.game_window.change_mode = True

    def options(self):
        self.build_mode_panel.disable_all_panels()
        self.option_panel.menu.toggle()

    def build_mode(self):
        self.build_mode_panel.menu.toggle()
        self.game_window.toggle_zone_highlighting()

        if self.game_window.mode == "build_mode":
            self.build_mode_panel.buy_building_panel.disable()
            self.game_window.game_resume()
        else:
            self.game_window.mode = "build_mode"

    def save(self):
        self.game_window.save_manager.save()

    def get_subpanels(self):
        return [self.build_mode_panel, self.option_panel]
