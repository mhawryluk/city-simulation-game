from random import randint


def fire(lot):
    fire_protection = 0
    threshold = lot.construct.heat // HEAT_THRESHOLD
    # calculating buildings fire protection
    for affected_by in lot.affected_by:
        fire_protection += randint(0, affected_by.get('fire_protection', 0))
    # adequately increasing temperature
    lot.construct.heat += lot.construct.get('temperature_raise', DEFAULT_TEMPERATURE_RAISE) - fire_protection
    # if passed a threshold - expands additionaly
    if lot.construct.heat // HEAT_THRESHOLD > threshold:
        lot.construct.heat += randint(1, HEAT_EXPANSION)
    # setting heat to stay between min and max
    lot.construct.heat = max(MIN_HEAT, min(MAX_HEAT, lot.construct.heat))


def security(lot):
    pass


def resource_management(lot):
    pass


def human_resource_management(lot):
    pass


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