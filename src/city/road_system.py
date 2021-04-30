import os
import pygame as pg
from random import randint
from city.lot import Lot
from city import ROAD_WIDTH_RATIO
from game_engine_tools import load_asset
from itertools import product

VERTICAL = 1
HORIZONTAL = -1


class RoadSystem:
    def __init__(self, map_width, map_height, save_source=None):
        self.vertical = set()
        self.horizontal = set()

        self.vertical_picture = load_asset('Streets', 'street_vertical.png')
        self.horizontal_picture = load_asset(
            'Streets', 'street_horizontal.png')
        self.map_width = map_width
        self.map_height = map_height
        self.hovered_road = None
        self.hovered_direction = VERTICAL

        if not save_source is None:
            for road in save_source['vertical']:
                self.vertical.add(tuple(road))
            for road in save_source['horizontal']:
                self.horizontal.add(tuple(road))

    def remove_road(self, direction, pos):
        if direction == VERTICAL:
            self.vertical.remove(pos)
        elif direction == HORIZONTAL:
            self.horizontal.remove(pos)

    def add_road(self, direction, pos):
        if direction == VERTICAL:
            self.vertical.add(pos)
        elif direction == HORIZONTAL:
            self.horizontal.add(pos)

    def draw(self, pov, scale, window):
        picture = pg.transform.scale(
            self.vertical_picture, self.get_vertical_size(scale))
        for pos_x, pos_y in self.vertical:
            self.draw_element(pos_x, pos_y, pov, scale, window, picture)

        picture = pg.transform.scale(
            self.horizontal_picture, self.get_horizontal_size(scale))

        for pos_x, pos_y in self.horizontal:
            self.draw_element(pos_x, pos_y, pov, scale, window, picture)

    def draw_element(self, pos_x, pos_y, pov, scale, window, element):
        x = pov[0] - scale*self.map_width//2 + scale*pos_x
        y = pov[1] - scale*self.map_height//2 + scale*pos_y
        if -scale < x < window.get_width() and -scale < y < window.get_height():
            window.blit(element, (x, y))

    def get_vertical_size(self, scale):
        return int(scale*ROAD_WIDTH_RATIO), int(scale+scale*ROAD_WIDTH_RATIO)

    def get_horizontal_size(self, scale):
        return int(scale+scale*ROAD_WIDTH_RATIO), int(scale*ROAD_WIDTH_RATIO)

    def highlight_roads(self, pov, scale, window):
        #vertical
        alpha = pg.Surface(self.get_vertical_size(scale))
        alpha_level = 100
        alpha.set_alpha(alpha_level)

        alpha.fill((220, 220, 220))
        for pos_x, pos_y in product(range(self.map_width), range(self.map_height)):
            if not (pos_x, pos_y) in self.vertical:
                self.draw_element(pos_x, pos_y, pov, scale, window, alpha)

        alpha.fill((0, 0, 255))
        for pos_x, pos_y in self.vertical:
            self.draw_element(pos_x, pos_y, pov, scale, window, alpha)

        # horizontal
        alpha = pg.Surface(self.get_horizontal_size(scale))
        alpha.set_alpha(alpha_level)

        alpha.fill((220, 220, 220))
        for pos_x, pos_y in product(range(self.map_width), range(self.map_height)):
            if not (pos_x, pos_y) in self.horizontal:
                self.draw_element(pos_x, pos_y, pov, scale, window, alpha)

        alpha.fill((0, 0, 255))
        for pos_x, pos_y in self.horizontal:
            self.draw_element(pos_x, pos_y, pov, scale, window, alpha)

        # hovered
        if self.hovered_road:
            if self.hovered_direction == HORIZONTAL:
                alpha.fill((255, 0, 0))
                self.draw_element(
                    self.hovered_road[0], self.hovered_road[1], pov, scale, window, alpha)
            elif self.hovered_direction == VERTICAL:
                alpha = pg.Surface(self.get_vertical_size(scale))
                alpha.set_alpha(alpha_level)
                alpha.fill((255, 0, 0))
                self.draw_element(
                    self.hovered_road[0], self.hovered_road[1], pov, scale, window, alpha)

    def road_clicked(self):
        if self.hovered_road is None:
            return
        if self.hovered_direction == VERTICAL and self.hovered_road in self.vertical:
            self.remove_road(VERTICAL, self.hovered_road)
        elif self.hovered_direction == HORIZONTAL and self.hovered_road in self.horizontal:
            self.remove_road(HORIZONTAL, self.hovered_road)
        else:
            self.add_road(self.hovered_direction, self.hovered_road)

    def compress2save(self):
        return {
            'vertical': list(self.vertical),
            'horizontal': list(self.horizontal)
        }
