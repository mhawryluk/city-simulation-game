from itertools import product
from random import choice

import pygame as pg

from city import HORIZONTAL, VERTICAL
from city_graphics import ROAD_WIDTH_RATIO
from city_graphics.car import Car
from city_graphics.city_images import CityImages
from game_engine_tools import Singleton


class RoadGraphics(metaclass=Singleton):
    HIGHLIGHT_COLOR = 0x6d597a
    PLACE_COLOR = 0xf7b267
    BLANK_COLOR = 0xeee2df

    CARS_TO_ROADS_RATIO = 0.1

    cars = set()
    car_speed = 0.04
    city_images = CityImages()
    map_dimensions = None

    def __init__(self, map_dimensions):
        self.map_dimensions = map_dimensions

    @classmethod
    def reset(cls):
        cls.cars = set()
        cls.car_speed = 0.04

    def draw(self, roads, pov, scale, window):
        picture = self.city_images.scaled_vertical
        for pos_x, pos_y in roads.vertical:
            self.draw_element(pos_x, pos_y, pov, scale, picture, window)

        picture = self.city_images.scaled_horizontal
        for pos_x, pos_y in roads.horizontal:
            self.draw_element(pos_x, pos_y, pov, scale, picture, window)

    def draw_element(self, pos_x, pos_y, pov, scale, element, window):
        x = pov[0] - scale * self.map_dimensions[0] // 2 + scale * pos_x
        y = pov[1] - scale * self.map_dimensions[1] // 2 + scale * pos_y
        if -scale < x < window.get_width() and -scale < y < window.get_height():
            window.blit(element, (x, y))

    @staticmethod
    def get_vertical_size(scale):
        return int(scale * ROAD_WIDTH_RATIO), int(scale + scale * ROAD_WIDTH_RATIO)

    @staticmethod
    def get_horizontal_size(scale):
        return int(scale + scale * ROAD_WIDTH_RATIO), int(scale * ROAD_WIDTH_RATIO)

    def highlight_roads(self, roads, pov, scale, window):
        # vertical
        alpha = pg.Surface(self.get_vertical_size(scale))
        alpha_level = 150
        alpha.set_alpha(alpha_level)

        # road outline
        alpha.fill(self.BLANK_COLOR)
        for pos_x, pos_y in product(range(self.map_dimensions[0]), range(self.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.vertical:
                self.draw_element(pos_x, pos_y, pov, scale, alpha, window)

        alpha = pg.Surface(self.get_horizontal_size(scale))
        alpha.set_alpha(alpha_level)
        alpha.fill(self.BLANK_COLOR)
        for pos_x, pos_y in product(range(self.map_dimensions[0]), range(self.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.horizontal:
                self.draw_element(pos_x, pos_y, pov, scale, alpha, window)

        # highlight
        alpha = pg.Surface(self.get_vertical_size(scale))
        alpha.set_alpha(alpha_level)
        alpha.fill(self.HIGHLIGHT_COLOR)
        for pos_x, pos_y in roads.vertical:
            self.draw_element(pos_x, pos_y, pov, scale, alpha, window)

        alpha = pg.Surface(self.get_horizontal_size(scale))
        alpha.set_alpha(alpha_level)

        alpha.fill(self.HIGHLIGHT_COLOR)
        for pos_x, pos_y in roads.horizontal:
            self.draw_element(pos_x, pos_y, pov, scale, alpha, window)

        # hovered
        if roads.hovered_road:
            if roads.hovered_direction == HORIZONTAL:
                alpha.fill(self.PLACE_COLOR)
                self.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha, window)
            elif roads.hovered_direction == VERTICAL:
                alpha = pg.Surface(self.get_vertical_size(scale))
                alpha.set_alpha(alpha_level)
                alpha.fill(self.PLACE_COLOR)
                self.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha, window)

    def animate_cars(self, roads, pov, scale, window):
        self.update_cars()
        if len(self.cars) < self.CARS_TO_ROADS_RATIO * (roads.get_road_count()):
            self.add_car(roads)

        if len(self.cars) > 2 * self.CARS_TO_ROADS_RATIO * (roads.get_road_count()):
            self.cars.pop()

        for car in self.cars:
            image = self.city_images.get_scaled_car_image(
                car.image_type, car.road_direction, car.car_direction)
            self.draw_element(car.x, car.y, pov, scale, image, window)

    def update_cars(self):
        for car in self.cars:
            car.move(self.car_speed)

    def add_car(self, roads, car_type=None, road=None, road_direction=None):
        if car_type is None:
            car_type = self.city_images.get_random_car_type()
        if road is None:
            if (road_direction is None or road_direction == VERTICAL) and roads.vertical:
                road = choice(list(roads.vertical))
                self.cars.add(Car(road, VERTICAL, roads, car_type))
            elif (road_direction is None or road_direction == HORIZONTAL) and roads.horizontal:
                road = choice(list(roads.horizontal))
                self.cars.add(Car(road, HORIZONTAL, roads, car_type))
        else:
            self.cars.add(Car(road, road_direction, roads, car_type))
