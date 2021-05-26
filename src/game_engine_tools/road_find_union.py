class RoadSystemUnion:
    def __init__(self, road_system):
        self.road_system = road_system
        self.rebuild = True
        self.change_list = self.generate_prime_change_list()
        self.build()
    
    def find(self, ind):
        pass

    def union(self, ind1, ind2):
        pass

    def generate_prime_change_list(self):
        return []

    def build(self):
        if self.rebuild:
            pass

    def add(self):
        pass

    def delete(self):
        pass