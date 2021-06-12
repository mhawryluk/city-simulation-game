from city.lot import Lot
from city.lot_type import LotType
from city.road_system import RoadSystem
from constructs.construct_type import ConstructType


class CitySpace:
    '''main class representing the city'''

    def __init__(self, width, height, save_source=None, map=None):
        self.height = height  # amount of fields to height
        self.width = width  # amount of fields to width

        self.road_system = RoadSystem(
            width, height, None if save_source is None else save_source['roads'])
        self.reset_lots(
            None if save_source is None else save_source['lots'], map)
        self.zone = set()

    def reset_lots(self, save_source=None, map=None):
        '''
        If no save data avaliable - creates new lot grid.
        Else - loads lots form memory.
        '''
        self.lots = []

        if save_source is None:
            if map is not None:
                self.lots = [
                    [Lot(x, y, LotType(map[x][y])) for y in range(self.height)] for x in range(self.width)
                ]

            else:
                self.lots = [
                    [Lot(x, y,
                         LotType.WATER if x == 0 or x == self.height - 1 or y == 0 or y == self.width - 1 else LotType.GRASS)
                     for y in range(self.height)] for x in range(self.width)
                ]

        else:
            self.lots = [
                [Lot(x, y, None, save_source=save_source[x][y]) for y in range(self.height)] for x in range(self.width)
            ]

    def road_clicked(self):
        self.road_system.road_clicked()

    def add_to_zone(self, zone_type, clicked_lot):
        if clicked_lot.can_place(ConstructType.FAMILY_HOUSE):
            clicked_lot.set_zone(zone_type)
            self.zone.add(clicked_lot)
            return clicked_lot
        return None

    def buy_construct(self, construct, clicked_lot):
        if clicked_lot.can_place(construct):
            clicked_lot.set_construct(construct)
            return clicked_lot
        return None

    def compress2save(self):
        c2s = {
            'lots': [
                [lot.compress2save() for lot in row] for row in self.lots
            ],
            'roads': self.road_system.compress2save()
        }

        return c2s
