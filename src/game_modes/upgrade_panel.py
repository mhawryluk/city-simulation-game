from game_modes.panel import Panel
from game_engine_tools import WINDOW_SIZE
import pygame_menu as pgmen


class UpgradePanel(Panel):
    def __init__(self, width, height, game_window):
        super().__init__(width, height, game_window)
        self.menu = pgmen.Menu(title='LOT', width=width,
                               height=height, position=(50, 50), rows=50, columns=1,
                               theme=self.get_theme(), enabled=False)

    def set_lot(self, lot):
        self.lot = lot
        self.menu.clear()

        # IMAGE & INFO
        info = lot.construct.type['level'][str(lot.construct_level)]
        self.menu.add.image(
            info['images'][lot.construct_level], scale=(0.5, 0.5))

        for key, value in info.items():
            if key == 'images':
                continue
            self.menu.add.label(
                f'{key.replace("_", " ")}: {value}', max_char=30)

        self.menu.add.label(
            f'COST: {lot.construct.type["cost"]}')

        # BUTTONS
        self.menu.add.button('UPGRADE', self.upgrade)

        self.menu.force_surface_cache_update()

    def upgrade(self):
        pass
