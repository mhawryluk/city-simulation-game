class PlayerStatus:
    def __init__(self, save_source=None):
        self.data = save_source
        if save_source is None:
            self.data = {
                'money': 10000
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
