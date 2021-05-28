from game_engine_tools.player_status_tracker import PlayerStatus
from constructs.construct_type import ConstructType, get_zone_construct_type
from random import randint
from .simulation_tools import SIMULATIONS, calculate_happyness, satisfy_demand, calculate_demands
from math import inf
from .road_graph import RoadGraph


class SimulationEngine:

    FPS_PER_CYCLE_OPTIONS = [
        inf,
        60 * 2.5,
        60 * 1.5,
        60 * 0.5
    ]
    fps_per_cycle = 60 * 2.5

    def __init__(self, city_space, save_data):
        self.player_status = PlayerStatus(save_data.get('world_state', None))
        self.city_space = city_space
        self.fps_in_cycle = 0
        self.road_graph = RoadGraph(self.city_space.road_system, self.city_space.lots)
        for row in self.city_space.lots:
            for lot in row:
                self.integrate_construct(lot)

    def simulate_cycle(self):
        if self.fps_in_cycle >= self.fps_per_cycle:
            self.road_graph.rebuild_references()
            self.fps_in_cycle = 0
            self.player_status.data['resident_happyness'] = 1
            for row in self.city_space.lots:
                for lot in row:
                    for simulation in SIMULATIONS:
                        simulation(lot, self.player_status)
                    # construct_specific_simulation(lot, self.player_status)
                    self.player_status.data['resident_happyness'] *= calculate_happyness(lot)
            satisfy_demand(self.player_status)
            calculate_demands(self.player_status)
        else:
            self.fps_in_cycle += 1

    def can_buy(self, construct=None, zone=None, level=0):
        building = construct
        if building is None:
            building = get_zone_construct_type(zone)
        return self.player_status.data['funds'] >= building.value['level'][level].get('upgrade_cost', building.value['cost'])

    def funds_change_by(self, construct):
        self.player_status.data['funds'] -= construct.type['cost']

    def upgraded(self, construct):
        self.player_status.data['funds'] -= construct.get('upgrade_cost', 0)

    def integrate_construct(self, lot, remove=False):
        construct = lot.construct
        
        if not construct is None:
            if construct.like('home'):
                self.player_status.data['capacity'] += construct.people_involved if not remove else -construct.people_involved
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
                    if r >= 0 and r < size and c >= 0 and c < size and (r != row or c != col):
                        # print('-->', r, c, size)
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
                  
        if not remove and not lot.construct is None:
            self.funds_change_by(lot.construct)
            if lot.construct.like('home'):
                for affecting_construct in list(lot.affected_by):
                    lot.construct.happiness *= affecting_construct.get(
                        'resident_happiness_multiplier', 1)
    
    def change_speed(self, ind):
        self.fps_per_cycle = self.FPS_PER_CYCLE_OPTIONS[ind]

    def change_taxes(self):
        # happiness
        # multipliers
        pass

    def get_data(self, key):
        return self.player_status.data.get(key, None)

    def compress2save(self):
        return self.player_status.compress2save()
