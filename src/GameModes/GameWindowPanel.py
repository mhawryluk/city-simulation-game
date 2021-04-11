import pygame as pg
import pygame_menu as pgmen
from .GameWindow import *
from .BuildModePanel import BuildModePanel
from .Panel import Panel


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
            width=window_width - width, height=height//8,
            position=(100, 100),
            game_window=game_window)
        self.build_mode_panel.disable()

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

    def add_road(self):
        self.game_window.mode = "road_placing" if self.game_window.mode != "road_placing" else "game_mode"

    def select_area(self):
        pass

    def stats(self):
        pass

    def main_menu(self):
        self.game_window.change_mode = True

    def options(self):
        pass

    def build_mode(self):
        if self.game_window.mode == "build_mode":
            self.game_window.mode = "game_mode"
            self.build_mode_panel.disable()
            self.build_mode_panel.buy_building_panel.disable()
        else:
            self.game_window.mode = "build_mode"
            self.build_mode_panel.enable()

    def save(self):
        pass
        # self.game_window.save_manager.save()

    def draw(self, window):
        super().draw(window)
        self.build_mode_panel.draw(window)

    def handle(self, event):
        super().handle(event)
        self.build_mode_panel.handle(event)

    def collide(self):
        if super().collide():
            return True

        return self.build_mode_panel.collide()
