class PlayerStatus:
    def __init__(self, save_source=None):
        self.data = save_source
        if save_source is None:
            self.data = {
                'funds': 10000,
                'population': 0,
                'capacity': 0,
                'work places': 0,
                'produce': 0,
                'demand': 0,
                'health': 0,
                'resident_happyness': 1,
                'power': 0,
                'water': 0,
                'waste': 0,
                'pollution': 0,
                'taxation': 0.1,
                'residential demand': 'Very high',
                'commercial demand': 'Very low',
                'industrial demand': 'Very low'
            }

    def density(self):
        return self.data['population'] / (self.data['capacity'] + 1)

    def compress2save(self):
        return self.data

    def get_funds(self):
        pass

    def funds_change(self, event):
        pass

    def get_satisfaction(self):
        pass

    def get_satisfaction_color(self):
        pass
