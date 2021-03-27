import os
import pygame as pg
from random import randint

VERTICAL = 1
HORIZONTAL = -1

class RoadSystem:
    def __init__(self, map_width, map_height):
        self.vertical = set()
        self.horizontal = set()

        # random streets (to delete later!)
        x = 25
        y = 25
        for _ in range(80):
            self.add_rode("vertical", (x, y))
            self.add_rode("horizontal", (x, y))
            x += randint(-1, 1)
            y += randint(-1, 1)
            if x > 39:
                x = 39
            if x < 11:
                x = 11
            if y > 39:
                y = 39
            if y < 11:
                y = 11

        self.vertical_picture = pg.image.load(
            os.path.join('Assets', 'street_vertical.png'))
        self.horizontal_picture = pg.image.load(
            os.path.join('Assets', 'street_horizontal.png'))
        self.map_width = map_width
        self.map_height = map_height
        self.hovered_road = None
        self.hovered_direction = VERTICAL

    def remove_rode(self, direction, pos):
        if direction == "vertical":
            self.vertical.remove(pos)
        elif direction == "horizontal":
            self.horizontal.remove(pos)

    def add_rode(self, direction, pos):
        if direction == VERTICAL:
            self.vertical.add(pos)
        elif direction == HORIZONTAL:
            self.horizontal.add(pos)

    def draw(self, pov, scale, window):
        picture = pg.transform.scale(self.vertical_picture, (scale//5, scale))
        for pos_x, pos_y in self.vertical:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(picture, (x, y))

        picture = pg.transform.scale(
            self.horizontal_picture, (scale, scale//5))

        for pos_x, pos_y in self.horizontal:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(picture, (x, y))

    def highlight_roads(self, pov, scale, window):
        alpha = pg.Surface((scale//4, scale))
        alpha.set_alpha(100)

        alpha.fill((220,220,220))
        for pos_x in range(self.map_width):
            for pos_y in range(self.map_height):
                if not (pos_x, pos_y) in self.vertical:
                    x = pov[0] - scale*self.map_width//2 + scale*pos_x
                    y = pov[1] - scale*self.map_height//2 + scale*pos_y
                    if -scale < x < window.get_width() and -scale < y < window.get_height():
                        window.blit(alpha, (x, y))
        
        alpha.fill((105,105,105))
        for pos_x, pos_y in self.vertical:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))

        alpha = pg.Surface((scale, scale//4))
        alpha.set_alpha(100)

        alpha.fill((220,220,220))
        for pos_x in range(self.map_width):
            for pos_y in range(self.map_height):
                if not (pos_x, pos_y) in self.horizontal:
                    x = pov[0] - scale*self.map_width//2 + scale*pos_x
                    y = pov[1] - scale*self.map_height//2 + scale*pos_y
                    if -scale < x < window.get_width() and -scale < y < window.get_height():
                        window.blit(alpha, (x, y))

        alpha.fill((105,105,105))
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

        alpha = pg.Surface((scale//4, scale))
        alpha.set_alpha(100)
        alpha.fill((255,0,0))
        if self.hovered_road and self.hovered_direction == VERTICAL:
            alpha.fill((255, 0, 0))
            x = pov[0] - scale*self.map_width//2 + scale*self.hovered_road[0]
            y = pov[1] - scale*self.map_height//2 + scale*self.hovered_road[1]
            if -scale < x < window.get_width() and -scale < y < window.get_height():
                window.blit(alpha, (x, y))


