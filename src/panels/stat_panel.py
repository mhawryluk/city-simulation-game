import pygame_menu as pgmen

from panels.panel import Panel


class StatPanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='game stats',
                               width=width, height=height,
                               position=(50, 50),
                               theme=self.get_theme(),
                               mouse_enabled=True,
                               enabled=False)

    def get_theme(self):
        theme = super().get_theme()
        theme.title = True
        return theme
