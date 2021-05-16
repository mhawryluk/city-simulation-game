from random import randint, random
from constructs.construct_type import ConstructType


def set_between(value, min_value, max_value):
    if max_value is None:
        max_value = value
    if min_value is None:
        min_value = value
    return max(min_value, min(max_value, value))


def fire(lot, player_status):
    if lot.construct != None:
        fire_protection = 0
        threshold = lot.construct.heat // HEAT_THRESHOLD
        # calculating buildings fire protection
        for affected_by in lot.affected_by:
            fire_protection += randint(0,
                                       affected_by.get('fire_protection', 0)//2) * 2
        fire_protection += lot.construct.get('fire_protection', 0)
        # adequately increasing temperature
        lot.construct.heat += lot.construct.get(
            'temperature_raise', DEFAULT_TEMPERATURE_RAISE) - fire_protection
        # if passed a threshold - expands additionaly
        if lot.construct.heat // HEAT_THRESHOLD > threshold:
            lot.construct.heat += randint(1, HEAT_EXPANSION)
        # setting heat to stay between min and max
        lot.construct.heat = set_between(
            lot.construct.heat, MIN_HEAT, MAX_HEAT)


def security(lot, player_status):
    if lot.construct != None:
        security = 0
        coefficient = lot.construct.get('burglary_appeal', 1)
        coefficient *= 1 if lot.construct.happiness is None else lot.construct.happiness
        crime_appeal = BURGLARY_APPEAL * coefficient
        for affected_by in lot.affected_by:
            security += randint(0, affected_by.get('security', 1))
        lot.construct.crime_level += crime_appeal - security
        lot.construct.crime_level = set_between(
            lot.construct.crime_level, MIN_CRIME, MAX_CRIME)


def energy(lot, player_status):
    if lot.construct != None:
        player_status.data['power'] += lot.construct.get('energy_change', 0)
        player_status.data['power'] = set_between(
            player_status.data['power'], MAX_POWER_DEMAND, MAX_POWER_SUPPLY)


def waste(lot, player_status):
    if lot.construct != None:
        player_status.data['waste'] += lot.construct.get('waste_change', 0)
        player_status.data['waste'] = set_between(
            player_status.data['waste'], MAX_WASTE_FREE_SPACE, MAX_WASTE_PILE_UP)


def water(lot, player_status):
    if lot.construct != None:
        player_status.data['water'] += lot.construct.get('water_change', 0)
        player_status.data['water'] = set_between(
            player_status.data['water'], MAX_WATER_DEMAND, MAX_WATER_SUPPLY)


def economy_change(lot, player_status):
    if lot.construct != None:
        money_change = lot.construct.get('taxation', 0)
        taxes_multiplier = min(lot.construct.happiness / HAPPYNESS_FOR_FULL_TAXES,
                               1) if not lot.construct.happiness is None else 1
        money_change *= (1 + player_status.data['taxation']) * taxes_multiplier
        money_change += lot.construct.get('income', 0)
        # print(money_change)
        player_status.data['funds'] += int(money_change)
        player_status.data['funds'] = set_between(
            player_status.data['funds'], MIN_MONEY, MAX_MONEY)


def health(lot, player_status):
    if lot.construct != None:
        player_status.data['health'] += lot.construct.people_involved * \
            player_status.density()
        player_status.data['health'] -= lot.construct.get(
            'patients', 0) * HEALING_FACTOR
        player_status.data['health'] = set_between(
            player_status.data['health'], MIN_HEALTH, None)
        if random() < PANDEMIC_CHANCE * player_status.density():
            for _ in range(PANDEMIC_SEVERITY):
                lot.current_events.append('pandemic')
            player_status.data['health'] *= 1 + PANDEMIC_COEF


def produce(lot, player_status):
    if lot.construct != None:
        player_status.data['produce'] += lot.construct.get('produce', 0)


def demand(lot, player_status):
    if lot.construct != None:
        player_status.data['demand'] += lot.construct.get('demand', 0)


def population(lot, player_status):
    if lot.construct != None:
        capacity = player_status.data['capacity']
        populus = player_status.data['population']
        happyness = player_status.data['resident_happyness']
        if populus < capacity and random() < POPULATION_HAPPYNESS_COEF * happyness:
            populus = randint(populus, set_between(
                capacity * POPULATION_HAPPYNESS_COEF * happyness,
                (population + capacity)//2,
                capacity
            )
            )
            player_status.data['population'] = populus
        if random() > happyness:
            player_status.data['population'] = int(
                player_status.data['population'] * POPULATION_REDUCTION)


def construct_specific_simulation(lot, player_status):
    if lot.construct != None:
        # sims common among all constructs
        def f(x, y):
            pass  # empty function
        function = lot.construct.get('simulation_handler', None)
        if function is None:
            function = f
        function(lot, player_status)


def update_events(lot, player_status):
    if lot.construct != None:
        lot.current_events = []

        if lot.construct.heat >= FIRE_THRESHOLD:
            print('BURN BABY BURN')
            lot.current_events.append('burning')
            lot.construct.multiply_happiness(1/HAPPYNES_DIVISOR)
        elif 'burning' in lot.current_events:
            lot.current_events.remove('burning')
            lot.construct.multiply_happiness(HAPPYNES_DIVISOR)
        if lot.construct.crime_level >= CRIME_THRESHOLD:
            lot.current_events.append('burglary')
            lot.construct.multiply_happiness(1/HAPPYNES_DIVISOR)
        elif 'burglary' in lot.current_events:
            lot.current_events.remove('burglary')
            lot.construct.multiply_happiness(HAPPYNES_DIVISOR)

        if 'pandemic' in lot.current_events:
            lot.current_events.remove('pandemic')


def satisfy_demand(player_status):
    normalize = min(player_status.data['produce'],
                    player_status.data['demand'])
    player_status.data['goods'] += int(normalize * PRODUCE_TO_GODS)
    player_status.data['produce'] -= normalize
    player_status.data['demand'] -= normalize


def calculate_demands(player_status):
    player_status.data['commercial demand'] = level_to_demand(
        player_status.data['produce'], PRODUCE_THRESHOLDS)
    player_status.data['industrial demand'] = level_to_demand(
        player_status.data['demand'], DEMAND_THRESHOLDS)
    player_status.data['population demand'] = 'Very high' if top_demand(player_status) else level_to_demand(
        player_status.data['population'] * GOODS_PER_PERSON - player_status.data['goods'], GOODS_THRESHOLDS)
    player_status.data['goods'] = max(
        0,  player_status.data['goods'] - player_status.data['population'] * GOODS_PER_PERSON)


def calculate_happyness(lot):
    return 1 if lot.construct is None or lot.construct.happiness is None else lot.construct.happiness


def level_to_demand(value, threshold):
    for i in range(len(DEMAND_LEVEL)):
        if value <= threshold * i or i == len(DEMAND_LEVEL)-1:
            return DEMAND_LEVEL[i]


def top_demand(player_status):
    top_demands = DEMAND_LEVEL[-2:]
    return player_status.data['commercial demand'] in top_demands and player_status.data['industrial demand'] in top_demands


SIMULATIONS = [
    fire,
    security,
    energy,
    waste,
    water,
    economy_change,
    health,
    produce,
    demand,
    population,
    update_events,
    construct_specific_simulation
]


# fire related constants
HEAT_THRESHOLD = 5
HEAT_EXPANSION = 2
MAX_HEAT = 15
MIN_HEAT = -5
DEFAULT_TEMPERATURE_RAISE = 1
FIRE_THRESHOLD = 10
HAPPYNES_DIVISOR = 2


# security constatnts
BURGLARY_APPEAL = 2
MIN_CRIME = 0
MAX_CRIME = 15
CRIME_THRESHOLD = 10


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


# health constatnts
HEALING_FACTOR = 5
MIN_HEALTH = 0
PANDEMIC_CHANCE = 0.1
PANDEMIC_COEF = 0.01
PANDEMIC_SEVERITY = 3


# population happynes coeficient
POPULATION_HAPPYNESS_COEF = 0.25
POPULATION_REDUCTION = 0.98


# buldoze constants
MONEY_RETURN_PERCENT = 0.78


# supply and demand constants
BASE_DEMAND = 10
PRODUCE_TO_GODS = 1.5
GOODS_PER_PERSON = 1.5
PRODUCE_THRESHOLDS = 25
DEMAND_THRESHOLDS = 45
GOODS_THRESHOLDS = 10


# demand levels
DEMAND_LEVEL = [
    'Very low',
    'Low',
    'Satisfyable',
    'Medium',
    'Medium high',
    'High',
    'Very high'
]
