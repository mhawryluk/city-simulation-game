class PlayerStatus:
    def __init__(self, save_source=None):
        self.data = save_source
        if save_source is None:
            self.data = {
                'funds': 10000,
                'resident_happyness': 1,
                'power': 0,
                'water': 0,
                'sewage': 0,
                'pollution': 0
            }

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
