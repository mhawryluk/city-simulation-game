import pygame as pg
import pygame_menu as pgmen


class GameWindowPanel:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.panel = pg.Surface((width, height))
        self.panel.set_alpha(100)
        self.menu = pgmen.Menu(title='options',
                               width=width, height=height,
                               position=(0, 0),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

    def draw(self, window):
        self.panel.fill((255, 255, 255))
        self.menu.draw(self.panel)
        window.blit(self.panel, (window.get_width() - self.width, 0))

    def get_theme(self):
        theme = pgmen.themes.THEME_DARK.copy()
        # theme.title_font = pgmen.font.FONT_FRANCHISE
        theme.title_font_size = 1
        theme.title_background_color = (0, 0, 0)
        theme.background_color = (0, 0, 0, 50)
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_NONE
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (200, 75, 100)
        theme.widget_border_color = (220, 50, 60)
        theme.widget_border_width = 3
        theme.widget_font_size = 44
        theme.widget_padding = 20
        return theme
