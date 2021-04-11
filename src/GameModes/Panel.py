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

    def draw(self, window):
        if self.menu.is_enabled():
            self.menu.draw(window)

    def handle(self, event):
        if self.menu.is_enabled():
            self.menu.update([event])

    def enable(self):
        self.menu.enable()

    def disable(self):
        self.menu.disable()

    def collide(self):
        if not self.menu.is_enabled():
            return False

        position = self.menu.get_position()
        mouse_pos = pg.mouse.get_pos()

        if position[0] < mouse_pos[0] < position[0] + self.menu.get_width() and position[1] <= mouse_pos[1] <= position[1] + self.menu.get_height():
            return True

        return False
