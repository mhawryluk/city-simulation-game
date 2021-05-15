from game_engine_tools.player_status_tracker import PlayerStatus
from constructs.construct_type import ConstructType, get_zone_construct_type
from random import randint
from .simulation_tools import SIMULATIONS, calculate_happyness


class SimulationEngine:
    def __init__(self, city_space, save_data):
        world_state = save_data.get('world_state', {})
        self.data = world_state.get('world', {})
        self.player_status = PlayerStatus(world_state.get('player', None))
        self.city_space = city_space
        for row in self.city_space.lots:
            for lot in row:
                self.integrate_construct(lot)

    def simulate_cycle(self):
        self.data['resident_happyness'] = 1
        for row in self.city_space.lots:
            for lot in row:
                for simulation in SIMULATIONS:
                    simulation(lot)
                self.data['resident_happyness'] *= calculate_happyness(lot)

    def can_buy(self, construct=None, zone=None, level=0):
        building = construct
        if building is None:
            building = get_zone_construct_type(zone)
        return self.player_status.data['funds'] >= building.value['level'][level].get('upgrade_cost', building.value['cost'])

    def bought(self, construct):
        self.player_status['funds'] -= construct.type['cost']

    def upgraded(self, construct):
        self.player_status['funds'] -= construct.get('upgrade_cost', 0)

    def integrate_construct(self, lot, remove=False):
        construct = lot.construct
        
        if not construct is None:
            # print(construct.get('name', None), construct.get('range', 0))
            construct_range = int(construct.get('range', 0))
            pollution = float(construct.get('pollution', 0))
            happiness_multiplier = float(construct.get(
                'resident_happiness_multiplier', 1))

            ind = [
                (i, row.index(lot))
                for i, row in enumerate(self.city_space.lots)
                if lot in row
            ]
            row, col = ind[0]
            # print('-->', ind)
            size = len(self.city_space.lots)
            for r in range(row-construct_range, row+construct_range+1):
                for c in range(col-construct_range, col+construct_range+1):
                    if r >= 0 and row < size and c >= 0 and c < size and (r != row or c != col):
                        # print(r, c)
                        affected_lot = self.city_space.lots[r][c]
                        affected_lot.affected_by.add(construct)
                        if remove:
                            affected_lot.unpolluted /= (1-pollution)
                        else:
                            affected_lot.unpolluted *= (1-pollution)
                        if affected_lot.construct != None and affected_lot.construct.happiness != None:
                            if remove:
                                affected_lot.construct.happiness /= happiness_multiplier
                            else:
                                affected_lot.construct.happiness *= happiness_multiplier
        if not remove and (not lot.construct is None) and lot.construct.like('home'):
            for affecting_construct in list(lot.affected_by):
                lot.construct.happiness *= affecting_construct.get(
                    'resident_happiness_multiplier', 1)

    def change_taxes(self):
        # happiness
        # multipliers
        pass

    def get_data(self, key):
        data = self.data.get(key, None)
        if data is None:
            data = self.player_status.data.get(key, None)
        return data

    def compress2save(self):
        compressed_data = {
            'world': self.data,
            'player': self.player_status.compress2save()
        }
        return compressed_data
