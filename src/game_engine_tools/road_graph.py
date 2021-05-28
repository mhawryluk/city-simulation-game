class RoadGraph:
    def __init__(self, road_system, lots):
        self.road_system = road_system
        self.lots = lots
        self.update = True
        self.rebuild_references()
    
    def rebuild_references(self):
        if self.update:
            self.update = False
            # update references