import pygame_menu as pgmen
from panels.panel import Panel
from test import test
import pygame as pg


class OptionPanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='options',
                               width=width, height=height,
                               position=(50, 50),
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True,
                               enabled=False)
        self.menu.add.button("save", self.save)
        self.menu.add.button("main menu", self.main_menu)

        self.menu.add.label('')
        self.menu.add.button('volume up', self.volume_up)
        self.menu.add.button('volume down', self.volume_down)
        self.menu.add.label('')

        self.menu.add.button("test", test(game_window))

    def main_menu(self):
        self.game_window.change_mode = True
    
    def volume_up(self):
        volume = pg.mixer.music.get_volume()
        pg.mixer.music.set_volume(min(1, volume + 0.1))
    
    def volume_down(self):
        volume = pg.mixer.music.get_volume()
        pg.mixer.music.set_volume(max(0, volume - 0.1))

    def save(self):
        self.game_window.save()

    def get_theme(self):
        theme = super().get_theme()
        theme.title = True
        return theme
