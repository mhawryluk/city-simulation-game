import pygame_menu as pgmen
from panels.panel import Panel
from panels.special_buildings_panel import BuySpecialBuildingPanel
from panels.zoning_panel import ZoningPanel
from game_engine_tools import get_asset_path


class BuildModePanel(Panel):
    '''
    panel enabled after clicking build mode
    '''

    def __init__(self, width, height, position, game_window):
        super().__init__(width, height, game_window)

        self.menu = pgmen.Menu(title='BUILD - BUY',
                               width=width, height=height,
                               position=position,
                               theme=self.get_theme(),
                               columns=10, rows=1,
                               enabled=False,
                               mouse_enabled=True, mouse_motion_selection=True)

        # ZONING PANEL
        self.zone_building_panel = ZoningPanel(
            width=width,
            height=height,
            position=(100, 100-100*height/game_window.window.get_height()-0.3), game_window=game_window)

        # BUY A SPECIAL BUILDING PANEL
        self.special_building_panel = BuySpecialBuildingPanel(
            width=width,
            height=height,
            position=(100, 100-100*height/game_window.window.get_height()), game_window=game_window)

        # BUTTONS
        scale = (0.075, 0.075)
        self.menu.add.image(get_asset_path('Icons', 'modern-city.png'), scale=scale)
        self.zoning_button = self.menu.add.button(
            "zone buildings", self.zone_buildings)

        self.menu.add.label(' ')
        self.menu.add.label(' ')
        
        self.menu.add.image(get_asset_path('Icons', 'capitol.png'), scale=scale)
        self.buy_building_button = self.menu.add.button(
            "special buildings", self.special_buildings)

        self.menu.add.label(' ')
        self.menu.add.label(' ')

        self.menu.add.image(get_asset_path('Icons', 'bulldozer.png'), scale=scale)
        self.bulldoze_button = self.menu.add.button(
            "bulldoze", self.bulldoze)

    def special_buildings(self):
        '''funkcja wywoływana przy przyciśnięciu przycisku "special building"'''

        enabled = self.special_building_panel.is_enabled()
        self.disable_subpanels()

        if enabled:
            self.special_building_panel.disable()
        else:
            self.special_building_panel.enable()

    def zone_buildings(self):
        '''funkcja wywoływana przy przyciśnięciu przycisku "zone building"'''

        enabled = self.zone_building_panel.is_enabled()
        self.disable_subpanels()

        if enabled:
            self.zone_building_panel.disable()
        else:
            self.zone_building_panel.enable()

    def bulldoze(self):
        self.disable_subpanels()
        self.game_window.bulldozing = True

    def get_subpanels(self):
        return [self.special_building_panel, self.zone_building_panel]

    def disable_subpanels(self):
        super().disable_subpanels()
        self.game_window.zoning = False
        self.game_window.bulldozing = False
