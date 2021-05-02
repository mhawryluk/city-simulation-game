from game_modes.game_mode import GameMode
from game_modes.game_window_panel import GameWindowPanel
from game_modes.toggle_menu import ToggleMenu
from game_modes.info_panel import InfoPanel
from city.city_space import CitySpace
from city.lot import Lot
from game_engine_tools.save_manager import SaveManager
from game_engine_tools.simulation_engine import SimulationEngine
# from game_engine_tools.player_status_tracker import *
import pygame as pg


class GameWindow(GameMode):
    def __init__(self, window, save_manager, height, width):
        super().__init__(window, save_manager)

        saved_data = save_manager.get_gameplay_data()

        # constants
        self.SCROLL_SPEED = 15

        # current state variables
        self.change_mode = False
        self.mode = "game_mode"
        self.button_down = False
        self.zoning = False
        self.zoning_type = None
        self.construct_to_buy = None  # construct - wciśnięto buy ale jeszcze nie postawiono

        # befriended classes
        self.city_space = CitySpace(
            width, height, window.get_width(), window.get_height(),
            save_source=saved_data.get('city_space', None))
        self.simulator = SimulationEngine(self.city_space, saved_data)
        # self.player_status = PlayerStatus(save_source=saved_data.get('player_status', None))

        # panels
        self.menu_panel = GameWindowPanel(
            120, self.window.get_height(), self)
        self.toggle_menu = ToggleMenu(
            width=120, height=window.get_height()//15, game_window=self, position=(0, 100), panel=self.menu_panel)
        self.info_panel = InfoPanel(260, 120, (100, 0), self, self.simulator)

        self.sub_panels = [self.menu_panel, self.toggle_menu, self.info_panel]

    def update(self):
        self.simulator.simulate_cycle()
        self.city_space.update()
        self.draw()

    def handle(self, event):
        for panel in self.sub_panels:
            panel.handle(event)

        # KEY EVENTS
        if event.type == pg.KEYDOWN:
            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))

        if event.type == pg.KEYUP:
            # moving across the map
            if event.key == pg.K_d:
                self.city_space.add_move_speed((self.SCROLL_SPEED, 0))
            elif event.key == pg.K_s:
                self.city_space.add_move_speed((0, self.SCROLL_SPEED))
            elif event.key == pg.K_a:
                self.city_space.add_move_speed((-self.SCROLL_SPEED, 0))
            elif event.key == pg.K_w:
                self.city_space.add_move_speed((0, -self.SCROLL_SPEED))

        # MOUSE EVENTS
        for panel in self.sub_panels:
            if panel.collide():
                self.city_space.hovered(None, self.mode)
                self.button_down = False
                return

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == pg.BUTTON_LEFT:
                self.button_down = False

            # zooming in
            if event.button == 4:
                self.city_space.zoom(self.SCROLL_SPEED)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                self.button_down = True
                if self.construct_to_buy:
                    if self.city_space.buy_construct(self.construct_to_buy):
                        self.construct_to_buy = None

            if self.mode == 'road_placing':
                if event.button == pg.BUTTON_RIGHT:
                    self.city_space.road_system.hovered_direction *= -1
                elif event.button == pg.BUTTON_LEFT:
                    self.city_space.road_clicked()

            elif not self.zoning:
                if event.button == pg.BUTTON_LEFT:
                    self.city_space.select_lot(pg.mouse.get_pos())

            # zooming out
            if event.button == 5:
                self.city_space.zoom(-self.SCROLL_SPEED)

        if event.type == pg.MOUSEMOTION:
            if self.zoning:
                if self.button_down:
                    if self.simulator.can_buy(zone=self.zoning_type):
                        self.city_space.add_to_zone(self.zoning_type)
            else:
                self.city_space.hovered(
                    pg.mouse.get_pos(), self.mode)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.city_space.draw(self.window, mode=self.mode,
                             construct_to_buy=self.construct_to_buy)

        for panel in self.sub_panels:
            panel.draw(self.window)

    def set_zoning(self, zoning_type):
        Lot.zone_highlighting = True
        if not self.zoning:
            self.zoning = True
            self.zoning_type = zoning_type
        elif self.zoning_type != zoning_type:
            self.zoning_type = zoning_type
        else:
            self.zoning = False

    def toggle_zone_highlighting(self, set=None):
        if set:
            Lot.zone_highlighting = set
        else:
            Lot.zone_highlighting = not Lot.zone_highlighting

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
