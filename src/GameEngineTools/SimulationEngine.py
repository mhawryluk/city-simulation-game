class SimulationEngine:
    def __init__(self):
        self.player_status = None

    def can_buy(self, construct=None, zone=None):
        return True

    def bought(self, construct):
        pass

    def upgraded(self, construct):
        pass

    def random_event(self):
        pass
