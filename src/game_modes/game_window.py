from game_modes.game_mode import GameMode
from panels.game_window_panel import GameWindowPanel
from panels.toggle_menu import ToggleMenu
from panels.info_panel import InfoPanel
from panels.upgrade_panel import UpgradePanel
from panels.warning_panel import WarningPanel
from panels.speed_panel import SpeedPanel
from city.city_space import CitySpace
from city.lot import Lot
from city_graphics.lot_graphics import LotGraphics
from city_graphics.road_graphics import RoadGraphics
from city_graphics.city_space_graphics import CitySpaceGraphics
from game_engine_tools import WINDOW_SIZE
from game_engine_tools.save_manager import SaveManager
from game_engine_tools.simulation_engine import SimulationEngine
import pygame as pg


class GameWindow(GameMode):
    def __init__(self, window, save_manager, height, width, map=None):
        super().__init__(window, save_manager)

        saved_data = save_manager.get_gameplay_data()

        # constants
        self.SCROLL_SPEED = 15
        self.ZOOM_VALUE = 1.2

        LotGraphics.window = window
        RoadGraphics.window = window

        # current state variables
        self.change_mode = False
        self.mode = "game_mode"
        self.button_down = False
        self.zoning = False
        self.zoning_type = None
        self.bulldozing = False
        self.construct_to_buy = None  # construct - wciśnięto buy ale jeszcze nie postawiono

        # befriended classes
        self.city_space = CitySpace(
            width, height,
            save_source=saved_data.get('city_space', None), map=map)
        self.city_graphics = CitySpaceGraphics(self.city_space, width, height)

        self.simulator = SimulationEngine(self.city_space, saved_data)
        # self.player_status = PlayerStatus(save_source=saved_data.get('player_status', None))

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
            width=WINDOW_SIZE[0]//2, height=WINDOW_SIZE[1]//2, game_window=self, simulation=self.simulator)

        self.speed_panel = SpeedPanel(
            width=200, height=100, window=self, position=(99, 5), simulator=self.simulator)

        self.sub_panels = [self.menu_panel, self.toggle_menu,
                           self.info_panel, self.upgrade_panel, self.speed_panel]

    def update(self):
        self.simulator.simulate_cycle()
        self.city_graphics.update()
        self.draw()

    def handle(self, event):
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

        ##### only if mouse isn't above another panel #####

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

            # self.menu_panel.stat_panel.disable()

            if event.button == pg.BUTTON_LEFT:
                self.button_down = True
                if self.construct_to_buy:
                    lot = self.city_space.buy_construct(
                        self.construct_to_buy, self.city_graphics.get_clicked_lot(pg.mouse.get_pos()))
                    if lot:
                        self.simulator.integrate_construct(lot)
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
                    if not self.bulldozing and not bought:
                        self.set_upgrade_panel()

            # zooming out
            if event.button == 5:
                self.city_graphics.zoom(1/self.ZOOM_VALUE)

        if event.type == pg.MOUSEMOTION or event.type or event.type == pg.MOUSEBUTTONDOWN:
            if self.button_down:
                if self.zoning:
                    if self.simulator.can_buy(zone=self.zoning_type):
                        lot = self.city_space.add_to_zone(
                            self.zoning_type, self.city_graphics.get_clicked_lot(pg.mouse.get_pos()))
                        if lot:
                            self.simulator.integrate_construct(lot)

                elif self.bulldozing:
                    lot = self.city_space.bulldoze(
                        self.city_graphics.get_clicked_lot(pg.mouse.get_pos()))
                    if lot:
                        self.simulator.integrate_construct(lot, remove=True)

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

    def toggle_zone_highlighting(self, set=None):
        if not set is None:
            LotGraphics.zone_highlighting = set
        else:
            LotGraphics.zone_highlighting = not LotGraphics.zone_highlighting

    def set_upgrade_panel(self):
        lot = self.city_graphics.get_clicked_lot(pg.mouse.get_pos())
        if lot.construct:
            self.upgrade_panel.set_lot(lot)
            self.upgrade_panel.enable()
        else:
            self.upgrade_panel.disable()

    def game_resume(self):
        self.zoning = False
        self.game_mode = 'game_mode'

    def save(self):
        def compress2save():
            c2s = {}
            c2s['city_space'] = self.city_space.compress2save()
            c2s['world_state'] = self.simulator.compress2save()
            return c2s

        self.save_manager.save(compress2save())

    def show_warning(self, text):
        if self.warning_panel:
            self.warning_panel.disable()
            self.warning_panel = None
        self.warning_panel = WarningPanel(self, text)
