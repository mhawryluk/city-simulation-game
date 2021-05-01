from game_engine_tools.player_status_tracker import PlayerStatus
from constructs.construct_type import get_zone_construct_type

class SimulationEngine:
    def __init__(self, cisty_space, save_data):
        world_state = save_data.get('world_state', {})
        self.data = world_state.get('world', None)
        self.player_status = PlayerStatus(world_state.get('player', None))

    def simulate_cycle(self):
        pass

    def can_buy(self, construct=None, zone=None, level=0):
        building = construct
        if building is None:
            building = get_zone_construct_type(zone)
        return self.player_status.data['funds'] >= building.value['level'][level].get('upgrade_cost', building.value['cost'])

    def bought(self, construct):
        self.player_status['funds'] -= construct.value['cost']

    def upgraded(self, construct):
        self.player_status['funds'] -= building.value['level'][level]['upgrade_cost']

    def integrate_cosntruct(self, construct, ):
        self.data['pollution'] 

    def random_event(self):
        pass

    def compress2save(self):
        compressed_data = {
            'world': self.data,
            'player':self.player_status.compress2save()
        }
        return compressed_data
