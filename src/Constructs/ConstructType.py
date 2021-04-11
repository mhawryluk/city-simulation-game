from enum import Enum, auto
from .ZoneConstructs import *
from .SpecialConstructs import *


class ConstructType(Enum):
    FAMILY_HOUSE = auto()
    BLOCK = auto()
    SMALL_SHOP = auto()
    SHOP = auto()
    MALL = auto()
    FACTORY = auto()

    POLICE_OUTPOST = auto()
    POLICE_STATION = auto()
    COURTHOUSE = auto()
    PRISON = auto()
    FIRE_STATION = auto()
    CLINIC = auto()
    HOSPITAL = auto()
    KINDERGARTEN = auto()
    PRIMARY_SCHOOL = auto()
    SECONDARY_SCHOOL = auto()
    HIGH_SCHOOL = auto()
    COLLEGE = auto()
    UNIVERSITY = auto()
    PUBLIC_LIBRARY = auto()

    MUSEUM = auto()
    PARK = auto()
    WATER_PARK = auto()
    DOG_PARK = auto()
    STATUE = auto()
    AMUSEMENT_PARK = auto()

    LANDFILL = auto()
    WASTE_STORAGE = auto()
    WASTE_PROCESSING_PLANT = auto()
    COAL_POWER_PLANT = auto()
    WATER_POWER_PLANT = auto()
    NUCLEAR_POWER_PLANT = auto()
    DAM = auto()
    WATER_PUMP = auto()
    SWEWAGE_PUMP = auto()
    SEWAGE_PROCESSING_STATION = auto()

    ATTRIBUTES = {
        FAMILY_HOUSE: {
            'max_level': 2
        }
    }

    CONSTRUCTORS = {
        FAMILY_HOUSE: FamilyHouse
    }

    def get_info(self, type):
        return ATTRIBUTES[type]

    def new_object(self, type):
        return CONSTRUCTORS[type](ATTRIBUTES[type])
