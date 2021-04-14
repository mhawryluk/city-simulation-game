import pygame as pg
import os
from random import randint


class Lot:
    zone_highlighting = False

    def __init__(self, x, y, type, arguments=None):
        if arguments:
            pass
        self.type = type
        self.x = x
        self.y = y
        self.selected = False
        self.hovered = False
        self.seed = randint(0, 5000)
        self.zone_type_color = None

    def draw(self, scale, pov, window):
        x = pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x
        y = pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        for picture in Lot.city_images.get_images(self.type, self.seed):
            window.blit(picture, (x, y))

        if self.selected or self.hovered or (Lot.zone_highlighting and self.zone_type_color):
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)

            if Lot.zone_highlighting and self.zone_type_color:
                alpha.fill(self.zone_type_color)
            elif self.selected:
                alpha.fill((0, 0, 0))
            elif self.hovered:
                alpha.fill((255, 255, 255))

            window.blit(alpha, (x, y))

    def set_zone(self, zone_type):
        if zone_type == 'residential':
            self.zone_type_color = (0, 255, 0)
        elif zone_type == 'commercial':
            self.zone_type_color = (0, 0, 255)
        elif zone_type == 'industrial':
            self.zone_type_color = (255, 0, 0)
