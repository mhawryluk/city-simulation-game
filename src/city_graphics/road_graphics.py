from city_graphics import ROAD_WIDTH_RATIO
from city_graphics.car import Car
from city_graphics.city_images import CITY_IMAGES
from city import HORIZONTAL, VERTICAL
from itertools import product
import pygame as pg
from random import choice


class RoadGraphics:
    HIGHLIGHT_COLOR = 0x6d597a
    PLACE_COLOR = 0xf7b267
    BLANK_COLOR = 0xeee2df

    CARS_TO_ROADS_RATIO = 0.1

    cars = set()
    car_speed = 0.04

    @classmethod
    def draw(cls, roads, pov, scale):
        picture = CITY_IMAGES.get_vertical_road(cls.get_vertical_size(scale))
        for pos_x, pos_y in roads.vertical:
            cls.draw_element(pos_x, pos_y, pov, scale, picture)

        picture = CITY_IMAGES.get_horizontal_road(
            cls.get_horizontal_size(scale))
        for pos_x, pos_y in roads.horizontal:
            cls.draw_element(pos_x, pos_y, pov, scale, picture)

    @classmethod
    def draw_element(cls, pos_x, pos_y, pov, scale, element):
        x = pov[0] - scale*cls.map_dimensions[0]//2 + scale*pos_x
        y = pov[1] - scale*cls.map_dimensions[1]//2 + scale*pos_y
        if -scale < x < cls.window.get_width() and -scale < y < cls.window.get_height():
            cls.window.blit(element, (x, y))

    @staticmethod
    def get_vertical_size(scale):
        return int(scale*ROAD_WIDTH_RATIO), int(scale+scale*ROAD_WIDTH_RATIO)

    @staticmethod
    def get_horizontal_size(scale):
        return int(scale+scale*ROAD_WIDTH_RATIO), int(scale*ROAD_WIDTH_RATIO)

    @classmethod
    def highlight_roads(cls, roads, pov, scale):
        # vertical
        alpha = pg.Surface(cls.get_vertical_size(scale))
        alpha_level = 150
        alpha.set_alpha(alpha_level)

        alpha.fill(cls.BLANK_COLOR)
        for pos_x, pos_y in product(range(cls.map_dimensions[0]), range(cls.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.vertical:
                cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        alpha.fill(cls.HIGHLIGHT_COLOR)
        for pos_x, pos_y in roads.vertical:
            cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        # horizontal
        alpha = pg.Surface(cls.get_horizontal_size(scale))
        alpha.set_alpha(alpha_level)

        alpha.fill(cls.BLANK_COLOR)
        for pos_x, pos_y in product(range(cls.map_dimensions[0]), range(cls.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.horizontal:
                cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        alpha.fill(cls.HIGHLIGHT_COLOR)
        for pos_x, pos_y in roads.horizontal:
            cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        # hovered
        if roads.hovered_road:
            if roads.hovered_direction == HORIZONTAL:
                alpha.fill(cls.PLACE_COLOR)
                cls.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha)
            elif roads.hovered_direction == VERTICAL:
                alpha = pg.Surface(cls.get_vertical_size(scale))
                alpha.set_alpha(alpha_level)
                alpha.fill(cls.PLACE_COLOR)
                cls.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha)

    @classmethod
    def animate_cars(cls, roads, pov, scale):
        cls.update_cars()
        if len(cls.cars) < cls.CARS_TO_ROADS_RATIO*(roads.get_road_count()):
            cls.add_car(roads)

        if len(cls.cars) > 2*cls.CARS_TO_ROADS_RATIO*(roads.get_road_count()):
            cls.cars.pop()

        for car in cls.cars:
            image = CITY_IMAGES.get_scaled_car_image(
                car.image_type, car.road_direction, car.direction)
            cls.draw_element(car.x, car.y, pov, scale, image)

    @classmethod
    def update_cars(cls):
        for car in cls.cars:
            car.move(cls.car_speed)

    @classmethod
    def add_car(cls, roads, car_type=None, road=None, road_direction=None):
        if car_type is None:
            car_type = CITY_IMAGES.get_random_car_type()
        if road is None:
            if (road_direction is None or road_direction == VERTICAL) and roads.vertical:
                road = choice(list(roads.vertical))
                cls.cars.add(Car(road, VERTICAL, roads, car_type))
            elif (road_direction is None or road_direction == HORIZONTAL) and roads.horizontal:
                road = choice(list(roads.horizontal))
                cls.cars.add(Car(road, HORIZONTAL, roads, car_type))
        else:
            cls.cars.add(Car(road, road_direction, roads, car_type))
