from random import randint
from constructs.construct_type import ConstructType
from constructs.construct import Construct
from city.lot_type import LotType


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
        self.affects = set()
        self.unpolluted = 1

        self.current_events = []

        if not save_source is None:
            self.type = LotType(save_source['type_value'])
            self.zone_type = save_source['zone_type']
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

    def set_construct(self, construct_type):
        self.construct = Construct(construct_type)
        self.zone_type = None

    def remove_construct(self):
        self.construct = None
        self.construct_level = 0
        self.current_events = []
        self.zone_type = None

    def can_place(self, construct):
        '''zwraca True jeśli można ustawić construct na tym polu'''
        construct = Construct(construct)
        type = LotType.GRASS
        if construct.like('water'):
            type = LotType.WATER

        return self.construct is None and self.type == type

    def compress2save(self):
        return {
            'seed': self.seed,
            'type_value': self.type.value,
            'construct': None if self.construct is None else self.construct.compress2save(),
            'zone_type': self.zone_type,
            'unpolluted': self.unpolluted
        }

    def get_current_events(self):
        return self.current_events

    def show(self):
        return self.affected_by
