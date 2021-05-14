import os
import pygame as pg
from random import randint
from city.lot import Lot
from city import ROAD_WIDTH_RATIO, VERTICAL, HORIZONTAL
from game_engine_tools import load_asset
from itertools import product


class RoadSystem:
    def __init__(self, map_width, map_height, save_source=None):
        self.vertical = set()
        self.horizontal = set()
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
