import pygame_menu as pgmen
from GameModes.Panel import Panel


class OptionPanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='options',
                               width=width, height=height,
                               position=(50, 50),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True,
                               enabled=False)
        self.save_button = self.menu.add.button(
            "save", self.save)
        self.main_menu_button = self.menu.add.button(
            "main menu", self.main_menu)

    def main_menu(self):
        self.game_window.change_mode = True

    def save(self):
        self.game_window.save_manager.save()

    def get_theme(self):
        theme = super().get_theme()
        theme.title = True
        return theme
