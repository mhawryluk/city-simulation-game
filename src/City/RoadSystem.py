import os
import pygame as pg
from random import randint

VERTICAL = 1
HORIZONTAL = -1


class RoadSystem:
    def __init__(self, map_width, map_height):
        self.vertical = set()
        self.horizontal = set()
        self.road_width_ratio = 0.1666

        self.vertical_picture = pg.image.load(
            os.path.join('Assets', 'Streets', 'street_vertical.png'))
        self.horizontal_picture = pg.image.load(
            os.path.join('Assets', 'Streets', 'street_horizontal.png'))
        self.map_width = map_width
        self.map_height = map_height
        self.hovered_road = None
        self.hovered_direction = VERTICAL

    def remove_rode(self, direction, pos):
        if direction == VERTICAL:
            self.vertical.remove(pos)
        elif direction == HORIZONTAL:
            self.horizontal.remove(pos)

    def add_rode(self, direction, pos):
        if direction == VERTICAL:
            self.vertical.add(pos)
        elif direction == HORIZONTAL:
            self.horizontal.add(pos)

    def draw(self, pov, scale, window):
        picture = pg.transform.scale(
            self.vertical_picture, (int(scale*self.road_width_ratio), int(scale+scale*self.road_width_ratio)))
        for pos_x, pos_y in self.vertical:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(picture, (x, y))

        picture = pg.transform.scale(
            self.horizontal_picture, (int(scale + scale*self.road_width_ratio), int(scale*self.road_width_ratio)))

        for pos_x, pos_y in self.horizontal:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(picture, (x, y))

    def highlight_roads(self, pov, scale, window):
        alpha = pg.Surface((scale//5, scale))
        alpha.set_alpha(100)

        alpha.fill((220, 220, 220))
        for pos_x in range(self.map_width):
            for pos_y in range(self.map_height):
                if not (pos_x, pos_y) in self.vertical:
                    x = pov[0] - scale*self.map_width//2 + scale*pos_x
                    y = pov[1] - scale*self.map_height//2 + scale*pos_y
                    if -scale < x < window.get_width() and -scale < y < window.get_height():
                        window.blit(alpha, (x, y))

        alpha.fill((105, 105, 105))
        for pos_x, pos_y in self.vertical:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))

        alpha = pg.Surface((scale, scale//5))
        alpha.set_alpha(100)

        alpha.fill((220, 220, 220))
        for pos_x in range(self.map_width):
            for pos_y in range(self.map_height):
                if not (pos_x, pos_y) in self.horizontal:
                    x = pov[0] - scale*self.map_width//2 + scale*pos_x
                    y = pov[1] - scale*self.map_height//2 + scale*pos_y
                    if -scale < x < window.get_width() and -scale < y < window.get_height():
                        window.blit(alpha, (x, y))

        alpha.fill((105, 105, 105))
        for pos_x, pos_y in self.horizontal:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))

        # hovered
        if self.hovered_road and self.hovered_direction == HORIZONTAL:
            alpha.fill((255, 0, 0))
            x = pov[0] - scale*self.map_width//2 + scale*self.hovered_road[0]
            y = pov[1] - scale*self.map_height//2 + scale*self.hovered_road[1]
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))

        alpha = pg.Surface((scale//5, scale))
        alpha.set_alpha(100)
        alpha.fill((255, 0, 0))
        if self.hovered_road and self.hovered_direction == VERTICAL:
            alpha.fill((255, 0, 0))
            x = pov[0] - scale*self.map_width//2 + scale*self.hovered_road[0]
            y = pov[1] - scale*self.map_height//2 + scale*self.hovered_road[1]
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))

    def road_clicked(self):
        if self.hovered_road is None:
            return
        if self.hovered_direction == VERTICAL and self.hovered_road in self.vertical:
            self.remove_rode(VERTICAL, self.hovered_road)
        elif self.hovered_direction == HORIZONTAL and self.hovered_road in self.horizontal:
            self.remove_rode(HORIZONTAL, self.hovered_road)
        else:
            self.add_rode(self.hovered_direction, self.hovered_road)
