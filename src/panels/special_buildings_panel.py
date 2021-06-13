import pygame as pg
import pygame_menu as pgmen

from constructs.construct_type import ConstructType
from panels.panel import Panel


class BuySpecialBuildingPanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.BUY_WINDOW_WIDTH = 500
        self.BUY_WINDOW_HEIGHT = 500
        self.BUY_WINDOW_POSITION = (50, 50)

        self.enabled_window = None
        self.game_window = game_window
        scroll_bar_height = 4
        position = (position[0], position[1] - 100 *
                    scroll_bar_height / game_window.window.get_height())
        self.menu = pgmen.Menu(title='special building',
                               width=width, height=height + scroll_bar_height,
                               position=position,
                               rows=1, columns=41,
                               theme=self.get_theme(),
                               enabled=False)
        for construct in ConstructType:
            if not construct.value.get('zone', None):
                self.menu.add.button(
                    construct.name.replace('_', ' '), self.building_window_function(construct))
        self.unselect_selected_widget()

    def building_window_function(self, construct):
        """returns function called upon the clicking of the button"""

        def func():
            if not self.enabled_window or self.enabled_window.construct != construct:
                if self.enabled_window:
                    self.enabled_window.disable()

                self.enabled_window = BuyBuildingWindow(
                    self.BUY_WINDOW_WIDTH, self.BUY_WINDOW_HEIGHT,
                    self.BUY_WINDOW_POSITION, self.game_window, construct, self)

            else:
                self.enabled_window.disable()
                self.enabled_window = None
                self.unselect_selected_widget()

        return func

    def get_subpanels(self):
        return [self.enabled_window]


class BuyBuildingWindow(Panel):
    IMAGE_SIZE = 100

    def __init__(self, width, height, position, game_window, construct, panel):
        super().__init__(width, height, game_window)
        self.construct = construct
        self.parent_panel = panel
        self.menu = pgmen.Menu(title=construct.value['level'][0]['name'], width=width,
                               height=height, position=position,
                               theme=self.get_theme(), enabled=True)

        # IMAGE & INFO
        info = construct.value['level'][0]
        image_width, image_height = pg.image.load(
            info['images'][0]).get_rect().size
        self.menu.add.image(info['images'][0],
                            scale=(self.IMAGE_SIZE / image_width,
                                   self.IMAGE_SIZE / image_height)
                            )

        self.menu.add.label(f'|{info["name"]}|', max_char=30)
        self.menu.add.label(' ')
        if "description" in info:
            self.menu.add.label(f'{info["description"]}', max_char=30)
        self.menu.add.label(' ')

        # BUY
        self.menu.add.label(f'COST: {construct.value["cost"]}')
        self.menu.add.button('BUY', self.buy)
        self.menu.add.label(' ')

        for key, value in info.items():
            if key == 'images' or key == 'name' or key == 'description':
                continue
            self.menu.add.label(
                f'{key.replace("_", " ")}: {value}', max_char=30)

    def buy(self):
        if self.game_window.simulator.can_buy(self.construct):
            self.game_window.construct_to_buy = self.construct
            self.parent_panel.disable_all_panels()
            self.parent_panel.enabled_window = None
