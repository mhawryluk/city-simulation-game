import pygame as pg

from city.city_space import CitySpace
from city_graphics.city_space_graphics import CitySpaceGraphics
from city_graphics.lot_graphics import LotGraphics
from game_engine_tools import WINDOW_SIZE
from game_engine_tools.simulation_engine import SimulationEngine
from game_modes.game_mode import GameMode
from panels.game_window_panel import GameWindowPanel
from panels.info_panel import InfoPanel
from panels.speed_panel import SpeedPanel
from panels.toggle_menu import ToggleMenu
from panels.upgrade_panel import UpgradePanel
from panels.warning_panel import WarningPanel


class GameplayMode(GameMode):
    """main engine for the game mode, which is the main part of the game"""

    def __init__(self, window, save_manager, height, width, map_=None):
        super().__init__(window, save_manager)

        saved_data = save_manager.get_gameplay_data()

        # constants
        self.SCROLL_SPEED = 15
        self.ZOOM_VALUE = 1.2

        # current state variables
        self.change_mode = False
        self.mode = "game_mode"
        self.button_down = False
        self.zoning = False
        self.zoning_type = None
        self.bulldozing = False
        # construct - buy button pressed, but the purchase is not yet confirmed
        self.construct_to_buy = None

        # befriended classes
        self.city_space = CitySpace(
            width, height, save_source=saved_data.get('city_space', None), map=map_)
        self.city_graphics = CitySpaceGraphics(self.city_space, width, height)
        self.simulator = SimulationEngine(self.city_space, saved_data)

        # panels
        menu_panel_width = 97
        menu_panel_height = self.window.get_height()

        self.menu_panel = GameWindowPanel(
            menu_panel_width, menu_panel_height, self)

        self.toggle_menu = ToggleMenu(
            width=menu_panel_width, height=50, game_window=self, position=(0, 100), panel=self.menu_panel)

        self.info_panel = InfoPanel(
            250, 400, (99, 50), self, self.simulator)

        self.warning_panel = WarningPanel(self, 'hello!')

        self.upgrade_panel = UpgradePanel(
            width=WINDOW_SIZE[0] // 2, height=WINDOW_SIZE[1] // 2, game_window=self, simulation=self.simulator)

        self.speed_panel = SpeedPanel(
            width=250, height=100, window=self, position=(99, 8), simulator=self.simulator)

        self.sub_panels = [self.menu_panel, self.toggle_menu,
                           self.info_panel, self.upgrade_panel, self.speed_panel]

    def update(self):
        """run every frame"""
        self.simulator.simulate_cycle()
        self.city_graphics.update()
        self.draw()

    def handle(self, event):
        """mouse and key events"""
        for panel in self.sub_panels:
            panel.handle(event)

        # KEY EVENTS
        if event.type == pg.KEYDOWN:
            # moving across the map
            if event.key == pg.K_d:
                self.city_graphics.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_graphics.add_move_speed((0, -self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_graphics.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_graphics.add_move_speed((0, self.SCROLL_SPEED))

        if event.type == pg.KEYUP:
            # moving across the map
            if event.key == pg.K_d:
                self.city_graphics.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_graphics.add_move_speed((0, self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_graphics.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_graphics.add_move_speed((0, -self.SCROLL_SPEED))

        # MOUSE EVENTS
        for panel in self.sub_panels:
            if panel.collide():
                self.city_graphics.hovered(None, self.mode)
                self.button_down = False
                return

        # !!! only if mouse isn't above another panel !!!#

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == pg.BUTTON_LEFT:
                self.button_down = False

            # zooming in
            if event.button == 4:
                self.city_graphics.zoom(self.ZOOM_VALUE)

        if event.type == pg.MOUSEBUTTONDOWN:
            bought = False
            self.menu_panel.option_panel.disable()
            if self.warning_panel:
                self.warning_panel.disable()
                self.warning_panel = None

            if event.button == pg.BUTTON_LEFT:
                self.button_down = True
                if self.construct_to_buy:
                    clicked_lot = self.city_graphics.get_clicked_lot(
                        pg.mouse.get_pos())
                    if clicked_lot.set_construct(self.construct_to_buy):
                        self.simulator.integrate_construct(clicked_lot)
                        self.construct_to_buy = None
                        bought = True

            if self.mode == 'road_placing':
                if event.button == pg.BUTTON_RIGHT:
                    self.city_space.road_system.hovered_direction *= -1
                elif event.button == pg.BUTTON_LEFT:
                    self.city_space.road_clicked()

            elif not self.zoning:
                if event.button == pg.BUTTON_LEFT:
                    self.city_graphics.select_lot(pg.mouse.get_pos())
                    if not self.bulldozing and not bought and self.mode != 'access_highlighting':
                        self.set_upgrade_panel()

            # zooming out
            if event.button == 5:
                self.city_graphics.zoom(1 / self.ZOOM_VALUE)

        if event.type == pg.MOUSEMOTION or event.type or event.type == pg.MOUSEBUTTONDOWN:
            clicked_lot = self.city_graphics.get_clicked_lot(
                pg.mouse.get_pos())
            if self.button_down:
                if self.zoning and self.simulator.can_buy(zone=self.zoning_type):
                    if clicked_lot and clicked_lot.set_zone(self.zoning_type):
                        self.simulator.integrate_construct(clicked_lot)

                elif self.bulldozing:
                    if clicked_lot and clicked_lot.remove_construct():
                        self.simulator.integrate_construct(
                            clicked_lot, remove=True)

            else:
                self.city_graphics.hovered(
                    pg.mouse.get_pos(), self.mode)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.city_graphics.draw(mode=self.mode,
                                construct_to_buy=self.construct_to_buy, window=self.window)

        for panel in self.sub_panels:
            panel.draw(self.window)

        if self.warning_panel:
            self.warning_panel.draw(self.window)

    def set_zoning(self, zoning_type):
        LotGraphics.zone_highlighting = True
        if not self.zoning:
            self.zoning = True
            self.zoning_type = zoning_type
        elif self.zoning_type != zoning_type:
            self.zoning_type = zoning_type
        else:
            self.zoning = False

        return self.zoning

    @staticmethod
    def toggle_zone_highlighting(enabled=None):
        if enabled is not None:
            LotGraphics.zone_highlighting = enabled
        else:
            LotGraphics.zone_highlighting = not LotGraphics.zone_highlighting

    def set_upgrade_panel(self):
        """display a panel showing construct info with an upgrade option"""
        lot = self.city_graphics.get_clicked_lot(pg.mouse.get_pos())
        if lot.construct:
            self.upgrade_panel.set_lot(lot)
            self.upgrade_panel.enable()
        else:
            self.upgrade_panel.disable()

    def show_warning(self, text):
        """display warning popup with specified text"""
        if self.warning_panel:
            self.warning_panel.disable()
            self.warning_panel = None
        self.warning_panel = WarningPanel(self, text)

    def save(self):
        def compress2save():
            c2s = {'city_space': self.city_space.compress2save(
            ), 'world_state': self.simulator.compress2save()}
            return c2s

        self.save_manager.save(compress2save())
