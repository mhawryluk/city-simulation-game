import pygame as pg
import pygame_menu as pgmen
from GameModes.GameWindow import *


class GameWindowPanel:
    def __init__(self, width, height, game_window):
        self.height = height
        self.width = width
        self.game_window = game_window

        self.menu = pgmen.Menu(title='CITY SIMULATION GAME',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

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
        self.game_window.mode = "build_mode" if self.game_window.mode != "build_mode" else "game_mode"

    def save(self):
        pass
        # self.game_window.save_manager.save()

    def draw(self, window):
        self.menu.draw(window)

    def handle(self, event):
        self.menu.update([event])

    def get_theme(self):
        theme = pgmen.themes.THEME_DARK.copy()
        theme.title_font = pgmen.font.FONT_FRANCHISE
        theme.title_font_size = 30
        theme.title_background_color = (0, 0, 0)
        theme.background_color = (0, 0, 0, 50)
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_NONE
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (200, 75, 100)
        # theme.widget_border_color = (220, 50, 60)
        # theme.widget_border_width = 5
        theme.widget_font_size = 20
        # theme.widget_padding = 5
        return theme
