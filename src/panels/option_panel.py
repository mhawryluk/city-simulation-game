import pygame_menu as pgmen

from game_engine_tools import volume_up, volume_down
from panels.panel import Panel


class OptionPanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='options',
                               width=width, height=height,
                               position=(50, 50),
                               theme=self.get_theme(),
                               mouse_enabled=True,
                               enabled=False)
        self.menu.add.button("save", self.save)
        self.menu.add.button("main menu", self.main_menu)

        self.menu.add.label('')
        self.menu.add.button('volume up', volume_up)
        self.menu.add.button('volume down', volume_down)
        self.menu.add.label('')

        self.unselect_selected_widget()

    def main_menu(self):
        self.game_window.change_mode = True

    def save(self):
        self.game_window.save()

    def get_theme(self):
        theme = super().get_theme()
        theme.title = True
        return theme
