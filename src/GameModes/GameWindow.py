from GameModes.GameMode import GameMode
from GameModes.GameWindowPanel import GameWindowPanel
from GameModes.ToggleMenu import ToggleMenu
from City.CitySpace import CitySpace
from City.Lot import Lot
from GameEngineTools.SaveManager import SaveManager
from GameEngineTools.SimulationEngine import *
from GameEngineTools.PlayerStatusTracker import *
import pygame as pg


class GameWindow(GameMode):
    def __init__(self, window, save, height, width):
        super().__init__(window, save)
        self.city_space = CitySpace(
            width, height, window.get_width(), window.get_height())
        self.SCROLL_SPEED = 15
        self.change_mode = False
        self.menu_panel = GameWindowPanel(
            120, self.window.get_height(), self)
        self.mode = "game_mode"
        self.button_down = False
        self.zoning = False
        self.zoning_type = None
        self.simulator = SimulationEngine()
        self.player_status = PlayerStatus()
        self.toggle_menu = ToggleMenu(
            width=120, height=window.get_height()//15, game_window=self, position=(0, 100), panel=self.menu_panel)

    def update(self):
        self.city_space.update()
        self.draw()

    def handle(self, event):
        self.menu_panel.handle(event)
        self.toggle_menu.handle(event)

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
        if self.menu_panel.collide() or self.toggle_menu.collide():
            self.city_space.hovered(None, self.mode)
            self.button_down = False
            return

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == pg.BUTTON_LEFT:
                self.button_down = False
            if event.button == 4:
                self.city_space.zoom(self.SCROLL_SPEED)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                self.button_down = True

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
                self.city_space.hovered(pg.mouse.get_pos(), self.mode)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.city_space.draw(self.window, mode=self.mode)
        self.menu_panel.draw(self.window)
        self.toggle_menu.draw(self.window)

    def set_zoning(self, zoning_type):
        if not self.zoning:
            self.zoning = True
            self.zoning_type = zoning_type
        elif self.zoning_type != zoning_type:
            self.zoning_type = zoning_type
        else:
            self.zoning = False

    def game_resume(self):
        self.zoning = False
        self.game_mode = 'game_mode'

    def toggle_zone_highlighting(self):
        Lot.zone_highlighting = not Lot.zone_highlighting
