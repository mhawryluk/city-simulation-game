import pygame_menu as pgmen
import pygame as pg


class Panel:
    def __init__(self, width, height, game_window):
        self.width = width
        self.height = height
        self.game_window = game_window

    def get_theme(self):
        theme = pgmen.themes.THEME_DARK.copy()
        theme.widget_font = pg.font.SysFont("segoeuisymbol", 80)
        theme.title_font = pgmen.font.FONT_FRANCHISE
        theme.title_font_size = 40
        theme.title_background_color = (0, 0, 0)
        theme.background_color = (0, 0, 0, 70)
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_NONE
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (200, 75, 100)
        # theme.widget_border_color = (220, 50, 60)
        # theme.widget_border_width = 5
        theme.widget_font_size = 30
        # theme.widget_padding = 5
        return theme
