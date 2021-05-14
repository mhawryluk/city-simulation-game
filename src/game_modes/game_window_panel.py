import pygame as pg
import pygame_menu as pgmen
from game_modes.build_mode_panel import BuildModePanel
from game_modes.option_panel import OptionPanel
from game_modes.stat_panel import StatPanel
from game_modes.panel import Panel
from game_engine_tools import WINDOW_SIZE


class GameWindowPanel(Panel):
    '''main panel on the left side'''

    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='CITY SIMULATION GAME',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

        # BUILD MODE PANEL
        self.build_mode_panel = BuildModePanel(
            width=WINDOW_SIZE[0] - width, height=height//15,
            position=(100, 100),
            game_window=game_window)

        # OPTIONS PANEL
        self.option_panel = OptionPanel(
            width=WINDOW_SIZE[0]//2, height=WINDOW_SIZE[1]//2, game_window=game_window)

        # STAT PANEL
        self.stat_panel = StatPanel(
            width=WINDOW_SIZE[0]//2, height=WINDOW_SIZE[1]//2, game_window=game_window)

        # BUTTONS
        self.play_button = self.menu.add.button("play", self.play)
        self.road_button = self.menu.add.button("add roads", self.add_road)
        self.build_mode_button = self.menu.add.button(
            "build mode", self.build_mode)
        self.stats_button = self.menu.add.button(
            "stats", self.stats)
        self.options_button = self.menu.add.button(
            "options", self.options)

    def play(self):
        self.game_window.mode = "game_mode"

        if self.game_window.zoning:
            self.game_window.zoning = False
            self.game_window.zoning_type = None

        self.game_window.toggle_zone_highlighting(False)
        self.game_window.upgrade_panel.disable()
        self.disable_subpanels()

    def add_road(self):
        self.disable_subpanels()
        self.game_window.mode = "road_placing" if self.game_window.mode != "road_placing" else "game_mode"
        self.game_window.zoning = False
        self.game_window.upgrade_panel.disable()

    def stats(self):
        enabled = self.stat_panel.is_enabled()
        self.game_window.mode = self.game_window.mode if self.game_window.mode != "road_placing" else "game_mode"
        self.game_window.upgrade_panel.disable()

        self.disable_subpanels()
        self.stat_panel.menu.toggle()

        if enabled:
            self.stat_panel.disable()
        else:
            self.stat_panel.enable()

    def options(self):
        enabled = self.option_panel.is_enabled()
        self.game_window.mode = self.game_window.mode if self.game_window.mode != "road_placing" else "game_mode"
        self.game_window.upgrade_panel.disable()

        self.disable_subpanels()
        if enabled:
            self.option_panel.disable()
        else:
            self.option_panel.enable()

    def build_mode(self):
        enabled = self.build_mode_panel.is_enabled()

        for panel in self.get_subpanels():
            panel.disable_all_panels()

        if enabled:
            self.build_mode_panel.disable()
        else:
            self.build_mode_panel.enable()

        self.game_window.upgrade_panel.disable()
        self.game_window.toggle_zone_highlighting()

        if self.game_window.mode == "build_mode":
            self.build_mode_panel.special_building_panel.disable()
            self.game_window.game_resume()
        else:
            self.game_window.mode = "build_mode"

    def get_subpanels(self):
        return [self.build_mode_panel, self.option_panel, self.stat_panel]
