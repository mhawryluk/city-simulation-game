import pygame as pg
import os


class Lot:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.pictures = Lot.city_images.get_images(type)
        self.selected = False
        self.hovered = False

    def draw(self, scale, pov, window):
        x = pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x
        y = pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        for picture in self.pictures:
            pic = pg.transform.scale(picture, (scale, scale))
            window.blit(pic, (x, y))

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
