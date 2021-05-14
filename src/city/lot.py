import pygame as pg
import os
from random import randint
from constructs.construct_type import ConstructType
from constructs.construct import Construct
from city.lot_type import LotType
from city import ROAD_WIDTH_RATIO


class Lot:
    def __init__(self, x, y, type, save_source=None):
        self.type = type
        self.x = x
        self.y = y
        self.selected = False
        self.hovered = False
        self.seed = randint(0, 5000)
        self.zone_type = None
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

    def set_zone(self, zone_type):
        self.zone_type = zone_type
        if zone_type == 'residential':
            self.construct = Construct(ConstructType.FAMILY_HOUSE)
        elif zone_type == 'commercial':
            self.construct = Construct(ConstructType.SHOP)
        elif zone_type == 'industrial':
            self.construct = Construct(ConstructType.FACTORY)

    def set_construct(self, construct):
        self.construct = Construct(construct)
        self.zone_type = None

    def remove_construct(self):
        self.construct = None
        self.construct_level = 0
        self.zone_type = None

    def can_place(self):
        '''zwraca True jeśli można ustawić construct na tym polu'''
        return self.construct is None and self.type == LotType.GRASS

    def compress2save(self):
        return {
            'seed': self.seed,
            'type_value': self.type.value,
            'construct': None if self.construct is None else self.construct.compress2save()
        }

    def show(self):
        return self.affected_by
