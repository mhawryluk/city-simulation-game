from GameModes.Panel import Panel
from Constructs.ConstructType import ConstructType
import pygame_menu as pgmen


class BuySpecialBuildingPanel(Panel):
    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)
        self.BUY_WINDOW_WIDTH = 500
        self.BUY_WINDOW_HEIGHT = 500
        self.BUY_WINDOW_POSITION = (100, 50)

        self.enabled_window = None
        self.game_window = game_window
        self.menu = pgmen.Menu(title='special building',
                               width=width, height=height,
                               position=position,
                               rows=1, columns=4,
                               theme=self.get_theme(),
                               enabled=False, mouse_motion_selection=True)
        for construct in ConstructType:
            if not construct.value.get('zone', None):
                self.menu.add.button(
                    construct.name, self.building_window_function(construct))

    def building_window_function(self, construct):
        '''zwraca funkcje wywoływane przy kilnięciu na przycisk'''
        def func():
            if not self.enabled_window or self.enabled_window.construct != construct:
                if self.enabled_window:
                    self.enabled_window.disable()

                self.enabled_window = BuyBuildingWindow(
                    self.BUY_WINDOW_WIDTH, self.BUY_WINDOW_HEIGHT,
                    self.BUY_WINDOW_POSITION, self.game_window, construct, self)

            else:
                self.disable()

        return func

    def disable(self):
        super().disable()
        self.enabled_window = None

    def get_subpanels(self):
        return [self.enabled_window]


class BuyBuildingWindow(Panel):
    def __init__(self, width, height, position, game_window, construct, panel):
        super().__init__(width, height, game_window)
        self.construct = construct
        self.parent_panel = panel
        self.menu = pgmen.Menu(title=construct.value['level'][0]['name'], width=width,
                               height=height, position=position, rows=15, columns=1,
                               theme=self.get_theme(), enabled=True)

        # IMAGE & INFO
        info = construct.value['level'][0]
        self.menu.add.image(info['image_path'], scale=(0.5, 0.5))

        for key, value in info.items():
            if key == 'image' or key == 'image_path':
                continue
            self.menu.add.label(f'{key.replace("_", " ")}: {value}')

        self.menu.add.label(f'COST: {construct.value["cost"]}')

        # BUTTONS
        self.menu.add.button('BUY', self.buy)

    def buy(self):
        if self.game_window.simulator.can_buy(self.construct):
            self.game_window.construct_to_buy = self.construct
            self.parent_panel.disable_all_panels()
            self.parent_panel.enabled_window = None

    def disable(self):
        self.menu.disable()
