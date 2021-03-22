import pygame as pg


class Lot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = None
        self.selected = False

    def draw(self, scale, pov, window):
        if not(-scale <= pov[0] + scale*self.x < window.get_width() and -scale <= pov[1]+scale*self.y < window.get_height()):
            return

        if self.picture is None:
            if self.selected:
                pg.draw.rect(window,
                             (255, 0, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))
            else:
                pg.draw.rect(window,
                             (0, 255, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))

            # border
            pg.draw.rect(window,
                         (0, 0, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale), 2)
