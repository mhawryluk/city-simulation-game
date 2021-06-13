import pygame_menu as pgmen

from city_graphics.city_images import CityImages
from game_engine_tools import WINDOW_SIZE
from panels.build_mode_panel import BuildModePanel
from panels.option_panel import OptionPanel
from panels.panel import Panel
from panels.stat_panel import StatPanel


class GameWindowPanel(Panel):
    """main panel on the left side"""
    city_images = CityImages()

    def __init__(self, width, height, game_window, position=(100, 100)):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='CITY SIMULATION GAME',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True)

        # BUILD MODE PANEL
        self.build_mode_panel = BuildModePanel(
            width=WINDOW_SIZE[0] - width, height=height // 15,
            position=position,
            game_window=game_window)

        # OPTIONS PANEL
        self.option_panel = OptionPanel(
            width=WINDOW_SIZE[0] // 2, height=WINDOW_SIZE[1] // 2, game_window=game_window)

        # STAT PANEL
        self.stat_panel = StatPanel(
            width=WINDOW_SIZE[0] // 2, height=WINDOW_SIZE[1] // 2, game_window=game_window)

        # BUTTONS
        scale = (0.1, 0.1)
        self.menu.add.image(self.city_images.get_icon(
            'play-button'), scale=scale, onselect=self.play)
        self.play_button = self.menu.add.button("play", self.play)
        self.play_button.set_controls()
        self.menu.add.label(' ')

        self.menu.add.image(self.city_images.get_icon('road'), scale=scale)
        self.road_button = self.menu.add.button("add roads", self.add_road)
        self.menu.add.label(' ')

        self.menu.add.image(self.city_images.get_icon('crane'), scale=scale)
        self.build_mode_button = self.menu.add.button(
            "build mode", self.build_mode)
        self.menu.add.label(' ')

        self.menu.add.image(self.city_images.get_icon(
            'mesh-network'), scale=scale)
        self.build_mode_button = self.menu.add.button(
            "access", self.access)
        self.menu.add.label(' ')

        self.menu.add.image(self.city_images.get_icon(
            'settings-knobs'), scale=scale)
        self.options_button = self.menu.add.button(
            "options", self.options)
        self.menu.add.label(' ')

    def play(self):
        self.game_window.mode = "game_mode"
        self.disable_subpanels()

    def add_road(self):
        self.disable_subpanels()

        if self.game_window.mode != "road_placing":
            self.game_window.mode = "road_placing"
        else:
            self.game_window.mode = "game_mode"
            self.unselect_selected_widget()

    def access(self):
        self.disable_subpanels()

        if self.game_window.mode != "access_highlighting":
            self.game_window.mode = "access_highlighting"
            self.game_window.city_graphics.select_lot(None)
        else:
            self.game_window.mode = "game_mode"
            self.unselect_selected_widget()

    def options(self):
        enabled = self.option_panel.is_enabled()

        self.disable_subpanels()

        if enabled:
            self.option_panel.disable()
            self.unselect_selected_widget()
        else:
            self.game_window.mode = "game_mode"
            self.option_panel.enable()

    def build_mode(self):
        enabled = self.build_mode_panel.is_enabled()
        self.disable_subpanels()

        if enabled:
            self.build_mode_panel.disable()
            self.unselect_selected_widget()
            self.game_window.mode = "game_mode"
        else:
            self.game_window.mode = "build_mode"
            self.build_mode_panel.enable()
            self.game_window.toggle_zone_highlighting(True)
            self.build_mode_panel.unselect_selected_widget()

    def get_subpanels(self):
        return [self.build_mode_panel, self.option_panel, self.stat_panel, self.game_window.upgrade_panel]

    def disable_subpanels(self):
        super().disable_subpanels()
        self.game_window.zoning = False
        self.game_window.bulldozing = False
        self.game_window.zoning_type = None
        self.game_window.toggle_zone_highlighting(False)
