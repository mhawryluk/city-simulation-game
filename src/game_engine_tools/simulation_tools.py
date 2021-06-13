from random import randint, random

import numpy as np


def set_between(value, min_value, max_value):
    if max_value is None:
        max_value = value
    if min_value is None:
        min_value = value
    return max(min_value, min(max_value, value))


def fire(lot, player_status):
    if lot.construct is not None:
        fire_protection = 0
        threshold = lot.construct.heat // HEAT_THRESHOLD
        # calculating buildings fire protection
        for affected_by in lot.affected_by:
            fire_protection += affected_by.get('fire_protection', 0)
        fire_protection += lot.construct.get('fire_protection', 0)
        # adequately increasing temperature
        lot.construct.heat += lot.construct.get(
            'temperature_raise', DEFAULT_TEMPERATURE_RAISE) - fire_protection
        # if passed a threshold - expands additionally
        if lot.construct.heat // HEAT_THRESHOLD > threshold:
            lot.construct.heat += randint(1, HEAT_EXPANSION)
        # setting heat to stay between min and max
        lot.construct.heat = set_between(
            lot.construct.heat, MIN_HEAT, MAX_HEAT)


def security(lot, player_status):
    if lot.construct is not None:
        security = 0
        coefficient = lot.construct.get('burglary_appeal', 0.5)
        coefficient *= 1 if lot.construct.happiness is None else lot.construct.happiness
        crime_appeal = BURGLARY_APPEAL * coefficient
        for affected_by in lot.affected_by:
            security += affected_by.get('security', 0.05)
        security += lot.construct.get('security', 0.05)
        lot.construct.crime_level += crime_appeal - security
        lot.construct.crime_level = set_between(
            lot.construct.crime_level, MIN_CRIME, MAX_CRIME)


def energy(lot, player_status):
    if lot.construct is not None:
        player_status.data['power'] += lot.construct.get('energy_change', 0)
        player_status.data['power'] = set_between(
            player_status.data['power'], MAX_POWER_DEMAND, MAX_POWER_SUPPLY)


def waste(lot, player_status):
    if lot.construct is not None:
        player_status.data['waste'] += lot.construct.get('waste_change', 0)
        player_status.data['waste'] = set_between(
            player_status.data['waste'], MAX_WASTE_FREE_SPACE, MAX_WASTE_PILE_UP)


def water(lot, player_status):
    if lot.construct is not None:
        player_status.data['water'] += lot.construct.get('water_change', 0)
        player_status.data['water'] = set_between(
            player_status.data['water'], MAX_WATER_DEMAND, MAX_WATER_SUPPLY)


def calculate_income(construct, player_status):
    income = construct.get('income', 0)
    if income > 0:
        income /= 1 + np.abs(player_status.data['goods'] - player_status.data['population'] * GOODS_PER_PERSON) / max(
            player_status.data['population'] * GOODS_PER_PERSON, 1)
    return income


def economy_change(lot, player_status):
    if lot.construct is not None:
        money_change = lot.construct.get('taxation', 0)
        taxes_multiplier = min(lot.construct.happiness / HAPPYNESS_FOR_FULL_TAXES,
                               1) if not lot.construct.happiness is None else 1
        money_change *= (1 + player_status.data['taxation']) * taxes_multiplier
        money_change += calculate_income(lot.construct, player_status)
        player_status.data['funds'] += int(money_change)
        player_status.data['funds'] = set_between(
            player_status.data['funds'], MIN_MONEY, MAX_MONEY)


def health(lot, player_status):
    if lot.construct is not None:
        player_status.data['health'] += lot.construct.get('people_involved', 0) * player_status.density()
        player_status.data['health'] -= lot.construct.get('patients', 0) * HEALING_FACTOR
        player_status.data['health'] = set_between(
            player_status.data['health'], MIN_HEALTH, None)
        if random() < PANDEMIC_CHANCE * player_status.density():
            for _ in range(PANDEMIC_SEVERITY):
                if len(lot.current_events) < EVENTS_LIMIT:
                    lot.current_events.append('pandemic')
            player_status.data['health'] *= 1 + PANDEMIC_COEF


def produce(lot, player_status):
    if lot.construct is not None:
        player_status.data['produce'] += lot.construct.get('produce', 0)


def demand(lot, player_status):
    if lot.construct is not None:
        player_status.data['demand'] += lot.construct.get('demand', 0)


def population(lot, player_status):
    if lot.construct is not None:
        capacity = player_status.data['capacity']
        populus = player_status.data['population']
        happyness = player_status.data['resident_happyness']
        if populus < capacity and random() < POPULATION_HAPPINESS_COEF * happyness:
            populus = randint(populus, int(set_between(
                capacity * POPULATION_HAPPINESS_COEF * happyness,
                (populus + capacity) // 2,
                capacity
            ))
                              )
            player_status.data['population'] = populus
        if random() > happyness:
            player_status.data['population'] = int(
                player_status.data['population'] * POPULATION_REDUCTION)


def update_events(lot, player_status):
    if lot.construct is not None:
        if lot.construct.heat >= FIRE_THRESHOLD:
            if len(lot.current_events) < EVENTS_LIMIT:
                lot.current_events.append('burning')
            lot.construct.multiply_happiness(1 / HAPPYNES_DIVISOR)
        elif 'burning' in lot.current_events:
            lot.current_events.remove('burning')
            lot.construct.multiply_happiness(HAPPYNES_DIVISOR)
        if lot.construct.crime_level >= CRIME_THRESHOLD:
            if len(lot.current_events) < EVENTS_LIMIT:
                lot.current_events.append('burglary')
            lot.construct.multiply_happiness(1 / HAPPYNES_DIVISOR)
        elif 'burglary' in lot.current_events:
            lot.current_events.remove('burglary')
            lot.construct.multiply_happiness(HAPPYNES_DIVISOR)
        if 'pandemic' in lot.current_events:
            lot.current_events.remove('pandemic')


def satisfy_demand(player_status):
    normalize = min(player_status.data['produce'],
                    player_status.data['demand'])
    player_status.data['goods'] = max(0,
                                      player_status.data['goods'] - player_status.data['population'] * GOODS_PER_PERSON)
    player_status.data['goods'] += int(normalize * PRODUCE_TO_GOODS)
    player_status.data['produce'] -= normalize
    player_status.data['demand'] -= normalize


def calculate_demands(player_status):
    player_status.data['commercial demand'] = level_to_demand(
        player_status.data['produce'] + max(0, player_status.data['population'] * GOODS_PER_PERSON - player_status.data[
            'goods']) / PRODUCE_TO_GOODS, PRODUCE_THRESHOLDS)
    player_status.data['industrial demand'] = level_to_demand(
        player_status.data['demand'], DEMAND_THRESHOLDS)
    player_status.data['residential demand'] = 'Very high' if top_demand(player_status) else level_to_demand(
        player_status.data['goods'] - player_status.data['population'] * GOODS_PER_PERSON, GOODS_THRESHOLDS)


def calculate_happiness(lot):
    return 0 if lot.construct is None or lot.construct.happiness is None else lot.construct.happiness


def level_to_demand(value, threshold):
    for i in range(len(DEMAND_LEVEL)):
        if value <= threshold * i or i == len(DEMAND_LEVEL) - 1:
            return DEMAND_LEVEL[i]


def top_demand(player_status):
    top_demands = DEMAND_LEVEL[-2:]
    return player_status.data['commercial demand'] in top_demands and player_status.data[
        'industrial demand'] in top_demands


def normalize_happiness(happiness, old_happiness):
    happiness = (happiness * NEW_PERCENT_WEIGHT + old_happiness * CURRENT_PERCENT_WEIGHT) / (
            NEW_PERCENT_WEIGHT + CURRENT_PERCENT_WEIGHT)
    happiness = (happiness + 1) ** 0.25
    happiness = -1 / happiness + 1
    if happiness >= 0.9994:
        happiness = 1
    return happiness


# constant listing all simulation functions to be called in a complete cycle
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
    update_events
]

# event limit
EVENTS_LIMIT = 10

# fire related constants
HEAT_THRESHOLD = 5
HEAT_EXPANSION = 2
MAX_HEAT = 15
MIN_HEAT = -5
DEFAULT_TEMPERATURE_RAISE = 1
FIRE_THRESHOLD = 7
HAPPYNES_DIVISOR = 2

# security related constants
BURGLARY_APPEAL = 0.4
MIN_CRIME = 0
MAX_CRIME = 15
CRIME_THRESHOLD = 7

# power related constants
MAX_POWER_SUPPLY = 100000
MAX_POWER_DEMAND = -10000
COSTS_REDUCED_ABOVE_POWER_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_POWER_BORDERVAL = 1.2
POWER_BORDERVAL = 0

# water related constants
MAX_WATER_SUPPLY = 100000
MAX_WATER_DEMAND = -10000
COSTS_REDUCED_ABOVE_WATER_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_WATER_BORDERVAL = 1.2
WATER_BORDERVAL = 0

# waste related constants
MAX_WASTE_PILE_UP = 100000
MAX_WASTE_FREE_SPACE = -10000
COSTS_REDUCED_ABOVE_WASTE_BORDERVAL = 0.5
COSTS_INCREASED_BELOW_WASTE_BORDERVAL = 1.2
WASTE_BORDERVAL = 0

# health related constants
HEALING_FACTOR = 5
MIN_HEALTH = 0
PANDEMIC_CHANCE = 0.1
PANDEMIC_COEF = 0.01
PANDEMIC_SEVERITY = 3

# population happiness constants
POPULATION_HAPPINESS_COEF = 0.25
POPULATION_REDUCTION = 0.98
CURRENT_PERCENT_WEIGHT = 7
NEW_PERCENT_WEIGHT = 1

# happiness and taxes correlation constants
HAPPYNESS_FOR_FULL_TAXES = 3
MIN_MONEY = 0
MAX_MONEY = 1e9

# bulldozing related constants
MONEY_RETURN_PERCENT = 0.78

# supply and demand balance related constants
BASE_DEMAND = 10
PRODUCE_TO_GOODS = 2
GOODS_PER_PERSON = 1
PRODUCE_THRESHOLDS = 25
DEMAND_THRESHOLDS = 45
GOODS_THRESHOLDS = 10

# demand levels in verbose
DEMAND_LEVEL = [
    'Very low',
    'Low',
    'Satisfiable',
    'Medium',
    'Medium high',
    'High',
    'Very high'
]
