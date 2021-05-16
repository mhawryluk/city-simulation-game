from panels.panel import Panel
import pygame_menu as pgmen


class WarningPanel(Panel):
    def __init__(self, window, text):
        width = 500
        height = 100
        super().__init__(width, height, window)
        self.menu = pgmen.Menu(title='warning', width=width,
                               height=height, position=(50, 50),
                               theme=self.get_theme(), enabled=True)
        self.menu.add.label(text)
