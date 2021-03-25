import pygame as pg
import os


class Lot:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.picture = Lot.city_images.get_image(type)
        self.selected = False

    def draw(self, scale, pov, window):
        x = pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x
        y = pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        if self.selected:
            pg.draw.rect(window,
                         (255, 0, 0), (x, y, scale, scale))
        else:
            picture = pg.transform.scale(self.picture, (scale, scale))
            window.blit(picture, (x, y))

        # border
        pg.draw.rect(window,
                     (0, 50, 0), (x, y, scale, scale), 2)
