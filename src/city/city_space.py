from city.lot import Lot
from city.lot_type import LotType
from city.road_system import RoadSystem
from city_graphics.city_space_graphics import CitySpaceGraphics
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
        definiuje pustą mapę, tworzy Loty
        zastąpić wczytywaniem z save'a
        '''
        self.lots = []
        if save_source is None:
            if map is not None:
                for x in range(self.width):
                    self.lots.append([])
                    for y in range(self.height):
                        self.lots[x].append(Lot(x, y, LotType(map[x][y])))

            else:
                for x in range(self.width):
                    self.lots.append([])
                    for y in range(self.height):
                        # if not ((self.width // 5 < x < 4*self.width//5) and (self.height // 5 < y < 4*self.height//5)):
                        #     self.lots[x].append(Lot(x, y, LotType.WATER))
                        if x == 0 or x == self.height-1 or y == 0 or y == self.width-1:
                            self.lots[x].append(Lot(x, y, LotType.WATER))
                        else:
                            self.lots[x].append(Lot(x, y, LotType.GRASS))

        else:
            for x in range(self.width):
                self.lots.append([])
                for y in range(self.height):
                    self.lots[x].append(
                        Lot(x, y, None, save_source=save_source[x][y]))

    def road_clicked(self):
        self.road_system.road_clicked()

    def add_to_zone(self, zone_type, clicked_lot):
        if clicked_lot.can_place(ConstructType.FAMILY_HOUSE):
            clicked_lot.set_zone(zone_type)
            self.zone.add(clicked_lot)
            return clicked_lot
        return None

    def bulldoze(self, clicked_lot):
        if clicked_lot.construct is None:
            return None

        clicked_lot.remove_construct()
        return clicked_lot

    def buy_construct(self, construct, clicked_lot) -> bool:
        '''zwraca True jeśli powiódł się zakup budynku'''
        if clicked_lot.can_place(construct):
            clicked_lot.set_construct(construct)
            return clicked_lot
        return None

    def compress2save(self):
        c2s = {
            'lots': [],
            'roads': self.road_system.compress2save()
        }
        for row in self.lots:
            c2s['lots'].append([])
            for lot in row:
                c2s['lots'][-1].append(lot.compress2save())

        return c2s
