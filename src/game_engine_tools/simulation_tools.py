from random import randint


def fire(lot):
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
        lot.construct.heat = max(MIN_HEAT, min(MAX_HEAT, lot.construct.heat))


def security(lot):
    if lot.construct != None:
        security = 0
        coefficient = lot.construct.get('burglary_appeal', 1)
        coefficient *= 1 if lot.construct.happiness is None else lot.construct.happiness
        crime_appeal = BURGLARY_APPEAL * coefficient
        for affected_by in lot.affected_by:
            security += randint(0, affected_by.get('security', 1))
        lot.crime_level += crime_appeal - security
        lot.construct.crime_level = max(MIN_CRIME, min(MAX_CRIME, lot.construct.crime_level))


def resource_management(lot):
    pass  # to be implemented


def human_resource_management(lot):
    pass  # to be implemented


def gather_taxes(lot):
    pass  # to be implemented


def update_events(lot):
    if lot.construct != None:
        lot.current_events = []
        if lot.construct.heat > FIRE_THRESHOLD:
            lot.current_events.append('burning')
        if lot.construct.crime_level > CRIME_THRESHOLD:
            lot.current_events.append('burglary')


def calculate_happyness(lot):
    return 1


SIMULATIONS = [
    fire,
    security,
    resource_management,
    human_resource_management
]


# fire related constants
HEAT_THRESHOLD = 20
HEAT_EXPANSION = 3
MAX_HEAT = 60
MIN_HEAT = -5
DEFAULT_TEMPERATURE_RAISE = 2
FIRE_THRESHOLD = 50


BURGLARY_APPEAL = 2
MIN_CRIME = 0
MAX_CRIME = 50
CRIME_THRESHOLD = 40


# events name list
EVENTS = [
    'burning'
]
