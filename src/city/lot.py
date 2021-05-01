import pygame as pg
import os
from random import randint
from constructs.construct_type import ConstructType
from constructs.construct import Construct
from city.lot_type import LotType
from city import ROAD_WIDTH_RATIO


class Lot:
    zone_highlighting = False

    def __init__(self, x, y, type, save_source=None):
        self.type = type
        self.x = x
        self.y = y
        self.selected = False
        self.hovered = False
        self.seed = randint(0, 5000)
        self.zone_type_color = None
        self.construct = None
        self.construct_level = 0

        self.affected_by = set()
        self.unpolluted = 1

        if not save_source is None:
            self.type = LotType(save_source['type_value'])
            self.seed = save_source['seed']
            if not save_source['construct'] is None:
                self.construct = Construct(
                    None, construct_state=save_source['construct'])

    def draw_background(self, scale, pov, window):
        x, y = self.get_draw_position(pov, scale)

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        # lot type pictures
        for picture in Lot.city_images.get_images(self.type, self.seed):
            window.blit(picture, (x, y))

        # # mouse selection
        # if self.selected or self.hovered:
        #     alpha = pg.Surface((scale, scale))
        #     alpha.set_alpha(128)

        #     if self.hovered:
        #         alpha.fill((255, 255, 255))
        #     elif self.selected:
        #         alpha.fill((0, 0, 0))

        #     window.blit(alpha, (x, y))

    def draw_construct(self, scale, pov, window):
        x, y = self.get_draw_position(pov, scale)

        if not (-scale <= x < Lot.window_dimensions[0] and -scale <= y < Lot.window_dimensions[1]):
            return

        # construct
        if self.construct:
            offset = int(ROAD_WIDTH_RATIO*scale)
            new_scale = int(scale*(1 - ROAD_WIDTH_RATIO))
            image = self.construct.image
            width, height = image.get_width(), image.get_height()
            ratio = new_scale/width
            new_width, new_height = int(width*ratio), int(height*ratio)
            new_x = x + offset
            new_y = y - new_height + new_scale + offset
            pic = pg.transform.scale(
                self.construct.image, (new_width, new_height))
            window.blit(pic, (new_x, new_y))

        # zone highlighting
        if Lot.zone_highlighting and self.zone_type_color:
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)
            alpha.fill(self.zone_type_color)
            window.blit(alpha, (x, y))

    def get_draw_position(self, pov, scale):
        return pov[0] - scale*Lot.map_dimensions[0]//2 + scale*self.x, pov[1] - scale*Lot.map_dimensions[1]//2 + scale*self.y

    def set_zone(self, zone_type):
        if zone_type == 'residential':
            self.zone_type_color = (61, 143, 102)
            self.construct = Construct(ConstructType.FAMILY_HOUSE)

        elif zone_type == 'commercial':
            self.zone_type_color = (92, 153, 214)
            self.construct = Construct(ConstructType.SHOP)

        elif zone_type == 'industrial':
            self.zone_type_color = (173, 102, 31)
            self.construct = Construct(ConstructType.FACTORY)

    def set_construct(self, construct):
        self.construct = Construct(construct)
        self.zone_type_color = None

    def can_place(self):
        '''zwraca True jeśli można ustawić construct na tym polu'''
        return self.construct is None and self.type == LotType.GRASS

    def compress2save(self):
        return {
            'seed': self.seed,
            'type_value': self.type.value,
            'construct': None if self.construct is None else self.construct.compress2save()
        }
