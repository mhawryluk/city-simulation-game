from game_engine_tools.player_status_tracker import PlayerStatus


class SimulationEngine:
    def __init__(self, save_data):
        self.player_status = PlayerStatus(save_data.get('player_status', None))

    def simulate_cycle(self):
        pass

    def can_buy(self, construct=None, zone=None):
        return True

    def bought(self, construct):
        pass

    def upgraded(self, construct):
        pass

    def random_event(self):
        pass

    def compress2save(self):
        return self.player_status.compress2save()
