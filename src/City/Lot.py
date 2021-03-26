import pygame as pg
import os


class Lot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # todo: move picture loading and scaling
        self.picture = pg.image.load(
            os.path.join('Assets', 'field.png'))

        self.selected = False

    def draw(self, scale, pov, window):
        if not(-scale <= pov[0] + scale*self.x < window.get_width() and -scale <= pov[1]+scale*self.y < window.get_height()):
            return

        if self.selected:
            pg.draw.rect(window,
                         (255, 0, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))
        else:
            if self.picture is None:
                pg.draw.rect(window,
                             (0, 255, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))
            else:
                self.picture = pg.transform.scale(self.picture, (scale, scale))
                window.blit(
                    self.picture, (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale))

            # border
        pg.draw.rect(window,
                     (0, 0, 0), (pov[0] + scale*self.x, pov[1]+scale*self.y, scale, scale), 2)


