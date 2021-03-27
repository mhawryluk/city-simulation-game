import pygame as pg
import pygame_menu as pgmen
from GameModes.GameWindow import *


class GameWindowPanel:
    def __init__(self, width, height, game_window):
        self.height = height
        self.width = width
        self.menu = pgmen.Menu(title='CITY SIMULATION GAME',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)
        self.play_button = self.menu.add.button("play", self.play)
        self.road_button = self.menu.add.button("add road", self.add_road)
        self.select_area_button = self.menu.add.button(
            "select area", self.select_area)
        self.stats_button = self.menu.add.button(
            "stats", self.stats)
        self.game_window = game_window

    def play(self):
        self.game_window.mode = "game_mode"

    def add_road(self):
        print("add road")
        self.game_window.mode = "road_placing"

    def select_area(self):
        print("select area")

    def stats(self):
        print("stats")

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
        #theme.widget_border_color = (220, 50, 60)
        #theme.widget_border_width = 5
        theme.widget_font_size = 20
        #theme.widget_padding = 5
        return theme
