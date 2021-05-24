from city_graphics import ROAD_WIDTH_RATIO
from city_graphics.city_images import CITY_IMAGES
from city import HORIZONTAL, VERTICAL
from itertools import product
import pygame as pg


class RoadGraphics:

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
        alpha_level = 100
        alpha.set_alpha(alpha_level)

        alpha.fill((220, 220, 220))
        for pos_x, pos_y in product(range(cls.map_dimensions[0]), range(cls.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.vertical:
                cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        alpha.fill((0, 0, 255))
        for pos_x, pos_y in roads.vertical:
            cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        # horizontal
        alpha = pg.Surface(cls.get_horizontal_size(scale))
        alpha.set_alpha(alpha_level)

        alpha.fill((220, 220, 220))
        for pos_x, pos_y in product(range(cls.map_dimensions[0]), range(cls.map_dimensions[1])):
            if not (pos_x, pos_y) in roads.horizontal:
                cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        alpha.fill((0, 0, 255))
        for pos_x, pos_y in roads.horizontal:
            cls.draw_element(pos_x, pos_y, pov, scale, alpha)

        # hovered
        if roads.hovered_road:
            if roads.hovered_direction == HORIZONTAL:
                alpha.fill((255, 0, 0))
                cls.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha)
            elif roads.hovered_direction == VERTICAL:
                alpha = pg.Surface(cls.get_vertical_size(scale))
                alpha.set_alpha(alpha_level)
                alpha.fill((255, 0, 0))
                cls.draw_element(
                    roads.hovered_road[0], roads.hovered_road[1], pov, scale, alpha)
