import pygame_menu as pgmen
from panels.panel import Panel


class ToggleMenu(Panel):
    '''menu with one button that hides GamewindowPanel (that one on the left)'''

    def __init__(self, width, height, position, game_window, panel):
        super().__init__(width, height, game_window)
        self.subpanel = panel
        self.menu = pgmen.Menu(
            title="toggle", theme=self.get_theme(), width=width, height=height, position=position)
        self.menu.add.button("SHOW MENU", self.toggle)

    def toggle(self):
        self.subpanel.disable_subpanels()
        self.subpanel.menu.toggle()
        self.game_window.info_panel.menu.toggle()

    def get_theme(self):
        theme = super().get_theme()
        theme.background_color = (0, 0, 0, 0)
        return theme
