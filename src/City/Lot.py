import pygame as pg
import os
from random import randint


class Lot:
    def __init__(self, x, y, type):
        self.type = type
        self.x = x
        self.y = y
        self.selected = False
        self.hovered = False
        self.seed = randint(0, 5000)

    def draw(self, scale, pov, window):
        x = pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x
        y = pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        for picture in Lot.city_images.get_images(self.type, self.seed):
            window.blit(picture, (x, y))

        if self.selected or self.hovered:
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)
            if self.selected:
                alpha.fill((0, 0, 0))
            elif self.hovered:
                alpha.fill((255, 255, 255))
            window.blit(alpha, (x, y))

        # border
        # pg.draw.rect(window,
        #              (0, 50, 0), (x, y, scale, scale), 2)
