import pygame as pg
import os
from random import randint
from Constructs.ConstructType import ConstructType
from City.LotType import LotType


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
        self.construct = None
        self.construct_level = 0

    def draw_background(self, scale, pov, window):
        x, y = self.get_draw_position(pov, scale)

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        # lot type pictures
        for picture in Lot.city_images.get_images(self.type, self.seed):
            window.blit(picture, (x, y))

        # zone highlighting
        if Lot.zone_highlighting and self.zone_type_color:
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)
            alpha.fill(self.zone_type_color)
            window.blit(alpha, (x, y))

        # mouse selection
        if self.selected or self.hovered:
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)

            if self.selected:
                alpha.fill((0, 0, 0))
            elif self.hovered:
                alpha.fill((255, 255, 255))

            window.blit(alpha, (x, y))

    def draw_construct(self, scale, pov, window):
        x, y = self.get_draw_position(pov, scale)

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        # construct
        if self.construct:
            pic = pg.transform.scale(
                self.construct.value['level'][self.construct_level]['image'], (scale, scale))
            window.blit(pic, (x, y))

    def get_draw_position(self, pov, scale):
        return pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x, pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

    def set_zone(self, zone_type):
        if zone_type == 'residential':
            self.zone_type_color = (61, 143, 102)
            self.construct = ConstructType.FAMILY_HOUSE

        elif zone_type == 'commercial':
            self.zone_type_color = (92, 153, 214)
            # self.construct = ConstructType.SHOP

        elif zone_type == 'industrial':
            self.zone_type_color = (173, 102, 31)

    def set_construct(self, construct):
        self.construct = construct
        self.zone_type_color = None

    def can_place(self):
        return self.construct is None and self.type == LotType.GRASS
