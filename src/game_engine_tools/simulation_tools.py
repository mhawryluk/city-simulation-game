from random import randint
from constructs.construct_type import ConstructType


def set_between(value, min_value, max_value):
    return max(min_value, min(max_value, value))


def fire(lot, player_status):
    if lot.construct != None:
        fire_protection = 0
        threshold = lot.construct.heat // HEAT_THRESHOLD
        # calculating buildings fire protection
        for affected_by in lot.affected_by:
            fire_protection += randint(0,
                                       affected_by.get('fire_protection', 0))
        # adequately increasing temperature
        lot.construct.heat += lot.construct.get(
            'temperature_raise', DEFAULT_TEMPERATURE_RAISE) - fire_protection
        # if passed a threshold - expands additionaly
        if lot.construct.heat // HEAT_THRESHOLD > threshold:
            lot.construct.heat += randint(1, HEAT_EXPANSION)
        # setting heat to stay between min and max
        lot.construct.heat = set_between(lot.construct.heat, MIN_HEAT, MAX_HEAT)


def security(lot, player_status):
    if lot.construct != None:
        security = 0
        coefficient = lot.construct.get('burglary_appeal', 1)
        coefficient *= 1 if lot.construct.happiness is None else lot.construct.happiness
        crime_appeal = BURGLARY_APPEAL * coefficient
        for affected_by in lot.affected_by:
            security += randint(0, affected_by.get('security', 1))
        lot.construct.crime_level += crime_appeal - security
        lot.construct.crime_level = set_between(lot.construct.crime_level, MIN_CRIME, MAX_CRIME)


def energy(lot, player_status):
    if lot.construct != None:
        player_status.data['power'] += lot.construct.get('energy_change', 0)
        player_status.data['power'] = set_between(player_status.data['power'], MAX_POWER_DEMAND, MAX_POWER_SUPPLY)


def waste(lot, player_status):
    if lot.construct != None:
        player_status.data['waste'] += lot.construct.get('waste_change', 0)
        player_status.data['waste'] = set_between(player_status.data['waste'], MAX_WASTE_FREE_SPACE, MAX_WASTE_PILE_UP)


def water(lot, player_status):
    if lot.construct != None:
        player_status.data['water'] += lot.construct.get('water_change', 0)
        player_status.data['water'] = set_between(player_status.data['water'], MAX_WATER_DEMAND, MAX_WATER_SUPPLY)


def economy_change(lot, player_status):
    if lot.construct != None:
        money_change = lot.construct.get('taxation', 0)
        taxes_multiplier = min(lot.construct.happiness / HAPPYNESS_FOR_FULL_TAXES, 1) if not lot.construct.happiness is None else 1
        money_change *= (1 + player_status.data['taxation']) * taxes_multiplier
        money_change += lot.construct.get('income', 0)
        player_status.data['funds'] += int(money_change)
        player_status.data['funds'] = set_between(player_status.data['funds'], MIN_MONEY, MAX_MONEY)


def construct_specific_simulation(lot, player_status):
    if lot.construct != None:
        # sims common among all constructs
        def f(x, y):
            pass # empty function
        function = lot.construct.get('simulation_handler', None)
        if function is None:
            function = f
        function(lot, player_status)


def update_events(lot):
    if lot.construct != None:
        lot.current_events = []
        if lot.construct.heat > FIRE_THRESHOLD:
            lot.current_events.append('burning')
        if lot.construct.crime_level > CRIME_THRESHOLD:
            lot.current_events.append('burglary')


def calculate_happyness(lot):
    return 1 if lot.construct is None or lot.construct.happiness is None else lot.construct.happiness


SIMULATIONS = [
    fire,
    security,
    energy,
    waste, 
    water,
    construct_specific_simulation
]


# fire related constants
HEAT_THRESHOLD = 20
HEAT_EXPANSION = 3
MAX_HEAT = 60
MIN_HEAT = -5
DEFAULT_TEMPERATURE_RAISE = 2
FIRE_THRESHOLD = 50


# security constatnts
BURGLARY_APPEAL = 2
MIN_CRIME = 0
MAX_CRIME = 50
CRIME_THRESHOLD = 40


# power cosntsatnts
MAX_POWER_SUPPLY = 100000
MAX_POWER_DEMAND = -10000
COSTS_REDUCED_ABOVE_POWER_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_PWOER_BORDERVAL = 1.2
POWER_BORDERVAL = 0


# water constants
MAX_WATER_SUPPLY = 100000
MAX_WATER_DEMAND = -10000
COSTS_REDUCED_ABOVE_WATER_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_WATER_BORDERVAL = 1.2
WATER_BORDERVAL = 0


# waste constatnts
MAX_WASTE_PILE_UP = 100000
MAX_WASTE_FREE_SPACE = -10000
COSTS_REDUCED_ABOVE_WASTE_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_WASTE_BORDERVAL = 1.2
WASTE_BORDERVAL = 0


# hapynes to taxes calculator
HAPPYNESS_FOR_FULL_TAXES = 2
MIN_MONEY = 0
MAX_MONEY = 1e9


# events name list
EVENTS = [
    'burning'
]
