from panels.panel import Panel
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
        info = lot.construct.get_level()

        self.menu.add.image(
            lot.construct.image_path, scale=(0.5, 0.5))

        for key, value in info.items():
            if key == 'images':
                continue
            self.menu.add.label(
                f'{key.replace("_", " ")}: {value}', max_char=30)

        self.menu.add.label(
            f'COST: {lot.construct.type["cost"]}')

        if str(lot.construct_level + 1) in lot.construct.type['level']:
            self.menu.add.label(
                f'upgrade cost: {lot.construct.type["level"][str(lot.construct_level + 1)]["upgrade_cost"]}')
            self.menu.add.button('UPGRADE', self.upgrade)

        self.menu.force_surface_cache_update()

    def upgrade(self):
        pass

    def get_theme(self):
        theme = super().get_theme()
        theme.widget_font_size = 25
        return theme
