class RoadNetGraph:
    """ class used as to find connection between lots through road system"""

    def __init__(self, road_system, lots):
        self.road_system = road_system
        self.lots = lots
        self.rebuild_references(force=True)

    def rebuild_references(self, force=False):
        if self.road_system.changes or force:
            self.road_system.changes = False
            lots_with_buildings = self.preprocess_lots()
            for lot in lots_with_buildings:
                self.update_lot(lot)

    def preprocess_lots(self):
        lots_with_buildings = []
        for row in self.lots:
            for lot in row:
                lot.affected_by = set()
                lot.affects = set()
                if not (lot.construct is None or lot.construct.get('range', 0) == 0):
                    lots_with_buildings.append(lot)
        return lots_with_buildings

    def update_lot(self, lot, remove=False):
        row, col = lot.y, lot.x
        i, j = row + 1, col
        radius = lot.construct.get('range', 0)
        if (j, i) in self.road_system.horizontal:
            visited = dict()
            self.dfs(lot, False, i, j, radius, remove, visited)

    def dfs(self, lot, vertical, i, j, radius, remove, visited):
        visited[(i, j, vertical)] = radius
        construct = lot.construct
        if radius > 0:
            radius -= 1
            hor_neighbors, ver_neighbors = self.edge_neighbors(i, j, vertical)
            lot1, lot2 = self.road_adjacent_lots(i, j, vertical)

            if remove:
                if construct in lot1.affected_by:
                    lot1.affected_by.remove(construct)
                if lot1 in lot.affects:
                    lot.affects.remove(lot1)

                if lot2 is not None:
                    if construct in lot2.affected_by:
                        lot2.affected_by.remove(construct)
                    if lot2 in lot.affects:
                        lot.affects.remove(lot2)
            else:
                lot1.affected_by.add(construct)
                lot.affects.add(lot1)
                if lot2 is not None:
                    lot2.affected_by.add(construct)
                    lot.affects.add(lot2)

            for row, col in hor_neighbors:
                if visited.get((row, col, False), 0) <= radius:
                    self.dfs(lot, False, row, col, radius, remove, visited)
            for row, col in ver_neighbors:
                if visited.get((row, col, True), 0) <= radius:
                    self.dfs(lot, True, row, col, radius, remove, visited)

    def road_adjacent_lots(self, i, j, vertical):
        second_lot = None
        if vertical:
            if j - 1 >= 0:
                second_lot = self.lots[j - 1][i]
        else:
            if i - 1 >= 0:
                second_lot = self.lots[j][i - 1]

        return self.lots[j][i], second_lot

    def edge_neighbors(self, i, j, vertical):
        ver, hor = [(i - 1, j)], [(i, j - 1)]
        if vertical:
            ver += [
                (i + 1, j)
            ]
            hor += [
                (i, j),
                (i + 1, j - 1),
                (i + 1, j)
            ]
        else:
            ver += [
                (i - 1, j + 1),
                (i, j),
                (i, j + 1)
            ]
            hor += [
                (i, j + 1)
            ]
        return self.filter_neighbor_roads(hor, ver)

    def filter_neighbor_roads(self, hor=None, ver=None):
        if ver is None:
            ver = []
        if hor is None:
            hor = []

        horizontal = [
            (i, j) for i, j in hor if (j, i) in self.road_system.horizontal
        ]
        vertical = [
            (i, j) for i, j in ver if (j, i) in self.road_system.vertical
        ]
        return horizontal, vertical
