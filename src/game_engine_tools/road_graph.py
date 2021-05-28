class RoadGraph:
    def __init__(self, road_system, lots):
        self.road_system = road_system
        self.lots = lots
        self.rebuild_references()
    
    def rebuild_references(self):
        if self.road_system.changes:
            self.road_system.changes = False
            buildings = []
            r = -1
            for row in self.lots:
                r += 1
                c = -1
                for lot in row:
                    c += 1
                    if not lot.construct is None:
                        radius = lot.construct.get('range', 0)
                        horizontal, vertical = self.lot_adjecent_roads(r, c)
                        for i,j in vertical:
                            self.dfs(lot.construct, True, i, j, radius)
                        for i,j in horizontal:
                            self.dfs(lot.construct, False, i, j, radius)

    def dfs(self, construct, vertical, i, j, radius):
        pass

    def road_adjecent_lots(self, i, j, vertical):
        pass

    def edge_neighbors(self, i, j, vertical):
        pass
    
    def lot_adjecent_roads(self, lot_i, lot_j):
        # horizontal roads
        hor = []
        hor.append((lot_i, lot_j))
        hor.append((lot_i+1, lot_j))
        hor = [
            (i,j) for i,j in hor if 
            i >= 0 and i <= len(self.lots) and
            j >= 0 and j < len(self.lots) and
            (i, j) in self.road_system.horizontal
        ]

        # vertical roads
        ver = []
        ver.append((lot_i, lot_j))
        ver.append((lot_i, lot_j+1))
        ver = [
            (i,j) for i,j in ver if 
            i >= 0 and i < len(self.lots) and
            j >= 0 and j <= len(self.lots) and
            (i, j) in self.road_system.vertical
        ]

        return hor, ver