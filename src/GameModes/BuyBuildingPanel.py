from .Panel import *
import pygame_menu as pgmen
from Constructs.ConstructType import ConstructType


class BuyBuildingPanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='BUY A BUILDING',
                               width=width, height=height,
                               position=position,
                               rows=50, columns=4,
                               theme=self.get_theme(),
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        for construct in ConstructType:
            self.menu.add.button(construct.name, None)
