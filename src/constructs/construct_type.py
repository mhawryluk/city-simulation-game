from enum import Enum
from game_engine_tools import get_asset_path


class ConstructType(Enum):
    FAMILY_HOUSE = {
        'likeness': ['home'],
        'cost': 1000,
        'zone': 'residential',
        'level': {
            0: {
                'name': 'small house',
                'people_involved': 5,  # in people
                'base_resident_happiness': 0.45,  # in percentage
                'energy_change': -3,  # in units 
                'water_consumption': 3,  # in units (UNIFY)
                'waste_change': 3,  # in units 
                'taxation': 1200,  # in dollars; per person; multiply by happiness to get actual income
                'images': [get_asset_path('House', 'Hs01.png'), get_asset_path('House', 'Hs02.png'),
                           get_asset_path('House', 'Hs03.png'),
                           get_asset_path('House', 'Hs00.png')]
            },
            1: {
                'name': 'family house',
                'people_involved': 8,
                'base_resident_happiness': 0.55,
                'energy_change': -6,
                'water_consumption': 5,
                'waste_change': 5,
                'taxation': 1800,
                'upgrade_cost': 800,
                'images': [get_asset_path('House', 'H05.png')]
            },
            2: {
                'name': 'large residence',
                'people_involved': 10,
                'base_resident_happiness': 0.65,
                'energy_change': -10,
                'water_consumption': 10,
                'waste_change': 8,
                'taxation': 2300,
                'upgrade_cost': 1000,
                'images': [get_asset_path('House', 'H04.png'), get_asset_path('House', 'H06.png')]
            }
        }
    }

    BLOCK = {
        'likeness': ['home'],
        'cost': 5000,
        'level': {
            0: {
                'name': 'regular block',
                'people_involved': 90,  # in people
                'base_resident_happiness': 0.2,  # in percentage
                'energy_change': -99,  # in units
                'water_consumption': 90,  # in units
                'waste_change': 180,  # in units
                'taxation': 420,  # in dollars; per person; multiply by happiness+1 to get actual income
                'temperature_raise': 2,
                'images': [get_asset_path('House', 'block0.png'), get_asset_path('House', 'block1.png')]
            },
            1: {
                'name': 'big block',
                'people_involved': 200,
                'base_resident_happiness': 0.3,
                'energy_change': -230,
                'water_consumption': 200,
                'waste_change': 400,
                'taxation': 600,
                'upgrade_cost': 10000,
                'temperature_raise': 2,
                'images': [get_asset_path('House', 'block3.png')]
            },
            2: {
                'name': 'high end block',
                'people_involved': 200,
                'base_resident_happiness': 0.5,
                'energy_change': -250,
                'water_consumption': 210,
                'waste_change': 400,
                'taxation': 1000,
                'upgrade_cost': 10000,
                'temperature_raise': 3,
                'images': [get_asset_path('House', 'block4.png')]
            }
        }
    }

    SHOP = {
        'cost': 1000,
        'zone': 'commercial',
        'level': {
            0: {
                'name': 'small shop',
                'people_involved': 3,
                'income': 700,
                'demand': 5,
                'energy_change': -10,
                'water_consumption': 5,
                'waste_change': 20,
                'resident_happiness_multiplier': 1.1,
                'images': [get_asset_path('Shop', 'SH0.png'), get_asset_path('Shop', 'SH1.png'),
                           get_asset_path('Shop', 'SH2.png')]
            },
            1: {
                'name': 'small shop',
                'people_involved': 3,
                'income': 700,
                'demand': 5,
                'energy_change': -10,
                'water_consumption': 5,
                'waste_change': 20,
                'upgrade_cost': 2000,
                'resident_happiness_multiplier': 1.1,
                'images': [get_asset_path('Shop', 'SH0.png'), get_asset_path('Shop', 'SH1.png'),
                           get_asset_path('Shop', 'SH2.png')]
            },
            2: {
                'name': 'shop',
                'description': 'Larger shop, meant to sustain a larger neighbourhood, be it of houses of city blocks.',
                'people_involved': 10,
                'income': 1700,
                'demand': 10,
                'energy_change': -20,
                'water_consumption': 10,
                'waste_change': 40,
                'resident_happiness_multiplier': 1.2,
                'upgrade_cost': 2000,
                'images': [get_asset_path('Shop', 'SH3.png')]
            }
        }
    }

    FACTORY = {
        'cost': 1000,
        'zone': 'industrial',
        'level': {
            0: {
                'name': 'factory',
                'people_involved': 50,
                'income': -1250,
                'produce': 25,
                'energy_change': -100,
                'water_consumption': 20,
                'waste_change': 70,
                'resident_happiness_multiplier': 0.35,
                'pollution': 0.6,
                'temperature_raise': 4,
                'images': [get_asset_path('Factory', 'factory-s-1.png'), get_asset_path('Factory', 'factory-s-2.png')]
            }
        }
    }

    HOSPITAL = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'clinic',
                'description': 'Small clinic.',
                'people_involved': 10,
                'income': -450,
                'energy_change': -50,
                'water_consumption': 30,
                'waste_change': 100,
                'resident_happiness_multiplier': 1.6,
                'range': 10,
                'images': [get_asset_path('SpecialBuildings', 'hospital.png')]
            },
            1: {
                'name': 'hospital',
                'description': 'Small hospital. Can house more people.',
                'people_involved': 200,
                'income': -4500,
                'energy_change': -500,
                'water_consumption': 300,
                'waste_change': 1000,
                'resident_happiness_multiplier': 1.9,
                'upgrade_cost': 10000,
                'range': 18,
                'images': [get_asset_path('SpecialBuildings', 'hospital.png')]
            }
        }
    }

    POLICE_STATION = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'Police outpost.',
                'description': 'Smaller scale police outpost.',
                'people_involved': 5,
                'income': 250,
                'energy_change': -10,
                'water_consumption': 5,
                'waste_change': 5,
                'resident_happiness_multiplier': 1.7,
                'range': 8,
                'fire_protection': 1,
                'security': 5,
                'images': [get_asset_path('SpecialBuildings', 'police0.png')]
            },
            1: {
                'name': 'Police station',
                'description': 'Local police headquarters.',
                'people_involved': 20,
                'income': 550,
                'energy_change': -50,
                'water_consumption': 20,
                'waste_change': 20,
                'resident_happiness_multiplier': 1.8,
                'range': 15,
                'upgrade_cost': 10000,
                'fire_protection': 2,
                'security': 10,
                'images': [get_asset_path('SpecialBuildings', 'police1.png')]
            }
        }
    }

    FIRE_STATION = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'fire station',
                'description': 'A fire station. Keeps people happy that there is a way for their house to be saved '
                               'from burning down.',
                'people_involved': 20,
                'income': -600,
                'energy_change': -80,
                'water_consumption': 400,
                'waste_change': 80,
                'range': 10,
                'upgrade_cost': 10000,
                'resident_happiness_multiplier': 1.9,
                'fire_protection': 7,
                'temperature_raise': 0,
                'images': [get_asset_path('SpecialBuildings', 'firestation.png')]
            }
        }
    }

    SCHOOL = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'school',
                'description': 'Building that houses kindergarten, primary and secondary school as well as a high '
                               'school.',
                'people_involved': 150,
                'income': -500,
                'energy_change': -500,
                'water_consumption': 500,
                'waste_change': 500,
                'range': 5,
                'city_income_multiplier': 1.01,
                'resident_happiness_multiplier': 2,
                'images': [get_asset_path('SpecialBuildings', 'school0.png')]
            }
        }
    }

    UNIVERSITY = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'school',
                'description': 'Building that houses kindergarten, primary and secondary school as well as a high '
                               'school.',
                'people_involved': 300,
                'income': -7500,
                'energy_change': -1000,
                'water_consumption': 1000,
                'waste_change': 1000,
                'city_income_multiplier': 1.05,
                'resident_happiness_multiplier': 3.5,
                'temperature_raise': 2,
                'range': 20,
                'images': [get_asset_path('SpecialBuildings', 'school1.png')]
            }
        }
    }

    PARK = {  # upgraded to dog park
        'cost': 1000,
        'level': {
            0: {
                'name': 'park',
                'description': 'A perfect place for people to relax.',
                'people_involved': 2,
                'income': -200,
                'energy_change': -2,
                'water_consumption': 100,
                'waste_change': 50,
                'resident_happiness_multiplier': 1.5,
                'range': 5,
                'images': [get_asset_path('SpecialBuildings', 'park0.png')]
            },
            1: {
                'name': 'dog park',
                'description': 'Perfect place to relax and walk your pupils <3',
                'people_involved': 5,
                'income': -200,
                'energy_change': -5,
                'water_consumption': 110,
                'waste_change': 60,
                'resident_happiness_multiplier': 2,
                'upgrade_cost': 8000,
                'temperature_raise': 2,
                'range': 15,
                'images': [get_asset_path('SpecialBuildings', 'park1.png')]
            }
        }
    }

    STATUE = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'statue',
                'description': 'Beautiful statue - truly a sight to behold.',
                'resident_happiness_multiplier': 1.6,
                'temperature_raise': 0,
                'range': 10,
                'images': [
                    get_asset_path('SpecialBuildings', 'statue0.png'),
                    get_asset_path('SpecialBuildings', 'statue1.png'),
                    get_asset_path('SpecialBuildings', 'statue2.png'),
                    get_asset_path('SpecialBuildings', 'statue3.png')
                ]
            }
        }
    }

    LANDFILL = {  # upgraded to waste processing plant
        'cost': 1000,
        'level': {
            0: {
                'name': 'landfill',
                'description': 'Building to store the waste.',
                'people_involved': 10,
                'income': -750,
                'waste_change': -1000,
                'resident_happiness_multiplier': 0.2,
                'pollution': 0.9,
                'fire_protection': -1,
                'temperature_raise': 6,
                'range': 15,
                'images': [get_asset_path('SpecialBuildings', 'landfill.png')]
            },
            1: {
                'name': 'waste processing station',
                'description': 'Disposes of the waste and turns it into power.',
                'people_involved': 50,
                'income': -3500,
                'energy_change': 1000,
                'waste_change': -2000,
                'resident_happiness_multiplier': 1.0,
                'pollution': 0.2,
                'fire_protection': -1,
                'upgrade_cost': 50000,
                'temperature_raise': 3,
                'range': 15,
                'images': [get_asset_path('SpecialBuildings', 'wasteprocess.png')]
            }
        }
    }

    POWER_PLANT = {
        'cost': 5000,
        'level': {
            0: {
                'name': 'coal power plant',
                'description': 'A power plant which uses coal and converts heat to electrical power.',
                'people_involved': 50,
                'income': -1000,
                'energy_change': 2000,
                'resident_happiness_multiplier': 0.5,
                'range': 20,
                'images': [get_asset_path('SpecialBuildings', 'power_plant.png')]
            }
        }
    }

    WATER_PUMP = {
        'cost': 1000,
        'level': {
            0: {
                'name': 'water pump',
                'description': 'Increases water amount in the storage and provides water for all residents in range.',
                'income': -500,
                'energy_change': -100,
                'water_production': 1000,
                'resident_happiness_multiplier': 1.1,
                'fire_protection': 1,
                'temperature_raise': 0,
                'range': 10,
                'images': [get_asset_path('SpecialBuildings', 'waterpipe.png')]
            }
        }
    }


def get_zone_construct_type(zone_type):
    if zone_type == 'residential':
        return ConstructType.FAMILY_HOUSE
    if zone_type == 'commercial':
        return ConstructType.SHOP
    if zone_type == 'industrial':
        return ConstructType.FACTORY
