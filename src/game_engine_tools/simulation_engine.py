from time import perf_counter
from game_engine_tools.player_status_tracker import PlayerStatus
from constructs.construct_type import ConstructType, get_zone_construct_type
from random import randint
from city_graphics.city_space_graphics import CitySpaceGraphics
from .simulation_tools import MONEY_RETURN_PERCENT, SIMULATIONS, calculate_happiness, satisfy_demand, calculate_demands
from math import inf
from .road_graph import RoadNetGraph


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
        self.road_graph = RoadNetGraph(self.city_space.road_system, self.city_space.lots)
        for row in self.city_space.lots:
            for lot in row:
                self.integrate_construct(lot, from_save=True)

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
                    self.player_status.data['resident_happyness'] *= calculate_happiness(lot)
            satisfy_demand(self.player_status)
            calculate_demands(self.player_status)
        else:
            self.fps_in_cycle += 1

    def can_buy(self, construct=None, zone=None, level=0):
        building = construct
        if building is None:
            building = get_zone_construct_type(zone)
        return self.player_status.data['funds'] >= building.value['level'][level].get('upgrade_cost', building.value['cost'])

    def funds_change_by(self, construct, multiplier=1.):
        self.player_status.data['funds'] -= construct.type['cost'] * multiplier

    def integrate_construct(self, lot, remove=False, from_save=False):
        construct = lot.construct
        
        if not construct is None:
            self.road_graph.update_lot(lot, remove)
            if not from_save:
                if construct.like('home'):
                    people_involved = construct.get('people_involved', 0)
                    self.player_status.data['capacity'] += people_involved if not remove else -people_involved
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
                r_size = len(self.city_space.lots)
                c_size = len(self.city_space.lots[0])
                for r in range(row-construct_range, row+construct_range+1):
                    for c in range(col-construct_range, col+construct_range+1):
                        if r >= 0 and r < r_size and c >= 0 and c < c_size and (r != row or c != col):
                            affected_lot = self.city_space.lots[r][c]
                            if remove:
                                affected_lot.unpolluted /= (1-pollution)
                            else:
                                affected_lot.unpolluted *= (1-pollution)
                            if affected_lot.construct != None and affected_lot.construct.happiness != None:
                                if remove:
                                    affected_lot.construct.happiness /= happiness_multiplier
                                else:
                                    affected_lot.construct.happiness *= happiness_multiplier
            
                if remove:
                    self.funds_change_by(lot.construct, -MONEY_RETURN_PERCENT)
                else:
                    self.funds_change_by(lot.construct)
                    if lot.construct.like('home'):
                        for affecting_construct in list(lot.affected_by):
                            lot.construct.happiness *= affecting_construct.get(
                                'resident_happiness_multiplier', 1)
    
    def change_speed(self, ind):
        self.fps_per_cycle = self.FPS_PER_CYCLE_OPTIONS[ind]
        CitySpaceGraphics.set_speed(ind)

    def change_taxes(self):
        # happiness
        # multipliers
        pass # to be implemented

    def get_data(self, key):
        return self.player_status.data.get(key, None)

    def compress2save(self):
        return self.player_status.compress2save()
