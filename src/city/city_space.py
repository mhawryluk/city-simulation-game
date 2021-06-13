from city.lot import Lot
from city.lot_type import LotType
from city.road_system import RoadSystem


class CitySpace:
    """main class representing the city"""

    def __init__(self, width, height, save_source=None, map=None):
        self.height = height  # amount of fields in height
        self.width = width  # amount of fields in width

        # roads
        self.road_system = RoadSystem(None if save_source is None else save_source['roads'])

        # lots
        self.lots = []
        self.reset_lots(
            None if save_source is None else save_source['lots'], map)

    def reset_lots(self, save_source=None, map=None):
        """
        If no save data available - creates new lot grid.
        Else - loads lots form memory.
        """

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
        """informs the road system that a road was clicked"""
        self.road_system.road_clicked()

    def compress2save(self):
        c2s = {
            'lots': [
                [lot.compress2save() for lot in row] for row in self.lots
            ],
            'roads': self.road_system.compress2save()
        }
        return c2s
