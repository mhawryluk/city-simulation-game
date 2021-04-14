from enum import Enum, auto
from ZoneConstructs import *
from SpecialConstructs import *

class ConstructType(Enum):
    FAMILY_HOUSE = {
        'max_level':2,
        'cost':1000,
        'constructor':FamilyHouse,
        'type':{
            0:{
                'name':'small house',
                'capacity':3, #in people
                'base_resident_happiness':0.45, #in percentage
                'energy_consumption':3, #in units
                'water_consumption':5, #in units
                'waste_production':6.5, #in units
                'taxation':2000 #in dollars; per person; multiply by happiness to get actual income
            },
            1:{
                'name':'family house',
                'capacity':5,
                'base_resident_happiness':0.55,
                'energy_consumption':7,
                'water_consumption':10,
                'waste_production':10,
                'taxation':3000
            },
            2:{
                'name':'lerge residence',
                'capacity':7,
                'base_resident_happiness':0.65,
                'energy_consumption':14,
                'water_consumption':16,
                'waste_production':17,
                'taxation':4000
            }
        }
    }
    BLOCK = {
        'max_level':3,
        'cost':5000,
        'constructor':Block,
        'type':{
            0:{
                'name':'regular block',
                'capacity':90, #in people
                'base_resident_happiness':0.2, #in percentage
                'energy_consumption':99, #in units
                'water_consumption':90, #in units
                'waste_production':180, #in units
                'taxation':420 #in dollars; per person; multiply by happiness+1 to get actual income
            },
            1:{
                'name':'big block',
                'capacity':200,
                'base_resident_happiness':0.3,
                'energy_consumption':230,
                'water_consumption':200,
                'waste_production':400,
                'taxation':600,
                'upgrade_cost':10000
            },
            2:{
                'name':'high end block',
                'capacity':200,
                'base_resident_happiness':0.5,
                'energy_consumption':250,
                'water_consumption':210,
                'waste_production':400,
                'taxation':1000,
                'upgrade_cost':10000
            },
            3:{ #to balance
                'name':'lerge_residence',
                'capacity':50,
                'base_resident_happiness':0.85,
                'energy_consumption':400,
                'water_consumption':300,
                'waste_production':420,
                'taxation':10000,
                'upgrade_cost':500000
            }
        }
    }
    SHOP = {
        'max_level':4,
        'cost':1000,
        'constructor':SmallShop,
        'type':{
            0:{
                'name':'small shop',
                'description':'Small shop.',
                'employees':3,
                'income':1000,
                'energy_consumption':10,
                'water_consumption':5,
                'waste_production':20,
                'resident_happiness_multiplier':1.1
            },
            1:{
                'name':'shop',
                'description':'Larger shop.',
                'employees':10,
                'income':2000,
                'energy_consumption':20,
                'water_consumption':10,
                'waste_production':40,
                'resident_happiness_multiplier':1.2,
                'upgrade_cost':2000
            },
            2:{
                'name':'shopping mall',
                'description':'Medium size shopping mall.',
                'employees':50,
                'income':10000,
                'energy_consumption':100,
                'water_consumption':75,
                'waste_production':250,
                'resident_happiness_multiplier':1.35
            },
            3:{
                'name':'small_shop',
                'description':'Big and well known shopping mall.',
                'employees':200,
                'income':50000,
                'energy_consumption':500,
                'water_consumption':300,
                'waste_production':1000,
                'resident_happiness_multiplier':1.5
            }
        }
    }
    FACTORY = {
        'max_level':2,
        'cost':1000,
        'constructor':Factory
    }

    POLICE_OUTPOST = {
        'max_level':2,
        'cost':1000,
        'constructor':PoliceOutpost
    }
    POLICE_STATION = {
        'max_level':2,
        'cost':1000,
        'constructor':PoliceStation
    }
    COURTHOUSE = {
        'max_level':2,
        'cost':1000,
        'constructor':Courthouse
    }
    PRISON = {
        'max_level':2,
        'cost':1000,
        'constructor':Prison
    }
    FIRE_STATION = {
        'max_level':2,
        'cost':1000,
        'constructor':FireStation
    }
    CLINIC = {
        'max_level':2,
        'cost':1000,
        'constructor':Clinic
    }
    HOSPITAL = {
        'max_level':2,
        'cost':1000,
        'constructor':Hospital
    }
    NURSERY = {
        'max_level':2,
        'cost':1000,
        'constructor':Nursery
    }
    KINDERGARTEN = {
        'max_level':2,
        'cost':1000,
        'constructor':Kindergarten
    }
    PRIMARY_SCHOOL = {
        'max_level':2,
        'cost':1000,
        'constructor':PrimarySchool
    }
    SECONDARY_SCHOOL = {
        'max_level':2,
        'cost':1000,
        'constructor':SecondarySchool
    }
    HIGH_SCHOOL = {
        'max_level':2,
        'cost':1000,
        'constructor':HighSchool
    }
    COLLEGE = {
        'max_level':2,
        'cost':1000,
        'constructor':CollegeHouse
    }
    UNIVERSITY = {
        'max_level':2,
        'cost':1000,
        'constructor':UniversityHouse
    }
    PUBLIC_LIBRARY = {
        'max_level':2,
        'cost':1000,
        'constructor':PublicLibrary
    }

    MUSEUM = {
        'max_level':2,
        'cost':1000,
        'constructor':Museum
    }
    PARK = {
        'max_level':2,
        'cost':1000,
        'constructor':Park
    }
    WATER_PARK = {
        'max_level':2,
        'cost':1000,
        'constructor':WaterPark
    }
    DOG_PARK = {
        'max_level':2,
        'cost':1000,
        'constructor':DogPark
    }
    STATUE = {
        'max_level':2,
        'cost':1000,
        'constructor':Statue
    }
    AMUSEMENT_PARK = {
        'max_level':2,
        'cost':1000,
        'constructor':AmusementPark
    }

    LANDFILL = {
        'max_level':2,
        'cost':1000,
        'constructor':Landfill
    }
    WASTE_STORAGE = {
        'max_level':2,
        'cost':1000,
        'constructor':WasteStorage
    }
    WASTE_PROCESSING_PLANT = {
        'max_level':2,
        'cost':1000,
        'constructor':WasteProcessingPlant
    }
    POWER_PLANT = {
        'max_level':2,
        'cost':1000,
        'constructor':CoalPowerPlant,
        'types': {
            0:'coal',
            1:'oil',
            2:'nuclear'
        }
    }
    WATER_POWER_PLANT = {
        'max_level':2,
        'cost':1000,
        'constructor':CoalPowerPlant
    }
    DAM = {
        'max_level':2,
        'cost':1000,
        'constructor':Dam
    }
    WATER_PUMP = {
        'max_level':2,
        'cost':1000,
        'constructor':WaterPump
    }
    SWEWAGE_PUMP = {
        'max_level':2,
        'cost':1000,
        'constructor':SewagePump
    }
    SEWAGE_PROCESSING_STATION = {
        'max_level':2,
        'cost':1000,
        'constructor':SewageProcessingStation,
        'type': {
            0:{
                'name':'standard',
                'description':'Station destined to process sewage produced by cisty buildings.',
                'pollution_level':0.75,
                'range':5,
                'energy_consumption':1
            },
            1:{
                'name':'industrial',
                'description':'Expanded sewage treatement station with double the processing power of the regular variant.',
                'pollution_level':0.75,
                'range':10,
                'energy_consumption':2
            },
            2:{
                'name':'economical',
                'description':'More economical version of the sewage treatment station. Decreases pollution by one third.',
                'pollution_level':0.5,
                'range':10,
                'energy_consumption':4
            },
            3:{
                'name':'advanced_economical',
                'description':'State of the art seweage treatment facility - 20% larger processing power and 50% smaller pollution.',
                'pollution_level':0.25,
                'range':12,
                'energy_consumption':6
            }
        }
    }

    def get_info(type):
        return type.value

    def new_object(type):
        return type.value['constructor'](ConstructType.get_info(type))








a = ConstructType.new_object(ConstructType.FAMILY_HOUSE)
print(a.attributes)