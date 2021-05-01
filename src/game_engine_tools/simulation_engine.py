from game_engine_tools.player_status_tracker import PlayerStatus
from constructs.construct_type import get_zone_construct_type

class SimulationEngine:
    def __init__(self, city_space, save_data):
        world_state = save_data.get('world_state', {})
        self.data = world_state.get('world', None)
        self.player_status = PlayerStatus(world_state.get('player', None))
        self.city_space = city_space
        for row in self.city_space.lots:
            for lot in row:
                self.integrate_cosntruct(lot)

    def simulate_cycle(self):
        pass

    def can_buy(self, construct=None, zone=None, level=0):
        building = construct
        if building is None:
            building = get_zone_construct_type(zone)
        return self.player_status.data['funds'] >= building.value['level'][level].get('upgrade_cost', building.value['cost'])

    def bought(self, construct):
        self.player_status['funds'] -= construct.type['cost']

    def upgraded(self, construct):
        self.player_status['funds'] -= construct.type['level'][level]['upgrade_cost']

    def integrate_cosntruct(self, lot, remove=False):
        construct = lot.construct
        if not construct is None:
            construct_range = construct.get('range', 0)
            pollution = construct.get('pollution', 0)
            happyness_multiplier = construct.get('resident_happiness_multiplier', 1)

            row, col = self.city_space.lots.index(lot)
            size = len(self.city_space.lots)
            for r in range(row-construct_range, row+construct_range+1):
                for c in range(col-construct_range, col+construct_range+1):
                    if r >= 0 and row < size and c >= 0 and c < size and (r != row or c != col):
                        affected_lot = self.city_space.lots[r][c]
                        affected_lot.affected_by.add(construct)
                        if remove:
                            affected_lot.unpolluted /= (1-pollution)
                        else:
                            affected_lot.unpolluted *= (1-pollution)
                        if affected_lot.construct != None and affected_lot.construct.happyness != None:
                            if remove:
                                affected_lot.construct.happyness /= happyness_multiplier
                            else:
                                affected_lot.construct.happyness *= happyness_multiplier
        if not remove:
            for affecting_constructs in list(lot.affected_by):
                pass

    def compress2save(self):
        compressed_data = {
            'world': self.data,
            'player':self.player_status.compress2save()
        }
        return compressed_data
