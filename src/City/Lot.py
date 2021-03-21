import pygame as pg


class Lot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = None

    def draw(self, scale, pov, window):
        if self.picture is None:
            pg.draw.rect(window,
                         (0, 255, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))
            pg.draw.rect(window,
                         (0, 0, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale), 2)
