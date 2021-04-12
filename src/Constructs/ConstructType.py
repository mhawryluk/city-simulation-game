from enum import Enum, auto
from ZoneConstructs import *
from SpecialConstructs import *

class ConstructType:#(Enum):
    # FAMILY_HOUSE = auto()
    # BLOCK = auto()
    # SMALL_SHOP = auto()
    # SHOP = auto()
    # MALL = auto()
    # FACTORY = auto()

    # POLICE_OUTPOST = auto()
    # POLICE_STATION = auto()
    # COURTHOUSE = auto()
    # PRISON = auto()
    # FIRE_STATION = auto()
    # CLINIC = auto()
    # HOSPITAL = auto()
    # KINDERGARTEN = auto()
    # PRIMARY_SCHOOL = auto()
    # SECONDARY_SCHOOL = auto()
    # HIGH_SCHOOL = auto()
    # COLLEGE = auto()
    # UNIVERSITY = auto()
    # PUBLIC_LIBRARY = auto()

    # MUSEUM = auto()
    # PARK = auto()
    # WATER_PARK = auto()
    # DOG_PARK = auto()
    # STATUE = auto()
    # AMUSEMENT_PARK = auto()

    # LANDFILL = auto()
    # WASTE_STORAGE = auto()
    # WASTE_PROCESSING_PLANT = auto()
    # COAL_POWER_PLANT = auto()
    # WATER_POWER_PLANT = auto()
    # NUCLEAR_POWER_PLANT = auto()
    # DAM = auto()
    # WATER_PUMP = auto()
    # SWEWAGE_PUMP = auto()
    # SEWAGE_PROCESSING_STATION = auto()


    ATTRIBUTES = {
        FAMILY_HOUSE:{
            'max_level':2,
            'cost':1000,
        },
        BLOCK:{

        },
        SMALL_SHOP:{

        },
        SHOP:{},
        MALL:{},
        FACTORY:{},
        POLICE_OUTPOST:{},
        POLICE_STATION:{},
        COURTHOUSE:{},
        PRISON:{},
        FIRE_STATION:{},
        CLINIC:{},
        HOSPITAL:{},
        KINDERGARTEN:{},
        PRIMARY_SCHOOL:{},
        SECONDARY_SCHOOL:{},
        HIGH_SCHOOL:{},
        COLLEGE:{},
        UNIVERSITY:{},
        PUBLIC_LIBRARY:{},
        MUSEUM:{},
        PARK:{},
        WATER_PARK:{},
        DOG_PARK:{},
        STATUE:{},
        AMUSEMENT_PARK:{},
        LANDFILL:{},
        WASTE_STORAGE:{},
        WASTE_PROCESSING_PLANT:{},
        COAL_POWER_PLANT:{},
        WATER_POWER_PLANT:{},
        NUCLEAR_POWER_PLANT:{},
        DAM:{},
        WATER_PUMP:{},
        SWEWAGE_PUMP:{},
        SEWAGE_PROCESSING_STATION:{}

    }

    CONSTRUCTORS = {
        FAMILY_HOUSE:FamilyHouse
    }

    def get_info(self, type):
        return ATTRIBUTES[type]

    def new_object(self, type):
        return CONSTRUCTORS[type](ATTRIBUTES[type])








a = ConstructType()
print(a.ATTRIBUTES.keys())