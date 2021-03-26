import os
import pygame as pg


class RoadSystem:
    def __init__(self, map_width, map_height):
        self.vertical = {(20, 20), (21, 20)}
        self.horizontal = {(20, 20), (21, 20), (22, 20)}
        self.vertical_picture = pg.image.load(
            os.path.join('Assets', 'street_vertical.png'))
        self.horizontal_picture = pg.image.load(
            os.path.join('Assets', 'street_horizontal.png'))
        self.map_width = map_width
        self.map_height = map_height

    def remove_rode(self, direction, pos):
        if direction == "vertical":
            self.vertical.remove(pos)
        elif direction == "horizontal":
            self.horizontal.remove(pos)

    def add_rode(self, direction, pos):
        if direction == "vertical":
            self.vertical.add(pos)
        elif direction == "horizontal":
            self.horizontal.add(pos)

    def draw(self, pov, scale, window):
        picture = pg.transform.scale(self.vertical_picture, (scale//5, scale))
        for pos_x, pos_y in self.vertical:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            window.blit(picture, (x, y))

        picture = pg.transform.scale(
            self.horizontal_picture, (scale, scale//5))

        for pos_x, pos_y in self.horizontal:
            x = pov[0] - scale*self.map_width//2 + scale*pos_x
            y = pov[1] - scale*self.map_height//2 + scale*pos_y
            window.blit(picture, (x, y))
