from enum import Enum
from game_engine_tools import get_asset_path


def get_zone_construct_type(zone_type):
    if zone_type == 'residential':
        return ConstructType.FAMILY_HOUSE
    if zone_type == 'commercial':
        return ConstructType.SHOP
    if zone_type == 'industrial':
        return ConstructType.FACTORY


class ConstructType(Enum):
    FAMILY_HOUSE = {
        'likeness': ['home'],
        'max_level': 2,
        'cost': 1000,
        'simulation_handler': None,
        'zone': 'residential',
        'level': {
            0: {
                'name': 'small house',
                'capacity': 3,  # in people
                'base_resident_happiness': 0.45,  # in percentage
                'energy_consumption': 3,  # in units
                'water_consumption': 3,  # in units
                'waste_production': 3,  # in units
                'taxation': 2000,  # in dollars; per person; multiply by happiness to get actual income
                'images': [get_asset_path('House', 'H01.png'), get_asset_path('House', 'H02.png'), get_asset_path('House', 'H03.png')]
            },
            1: {
                'name': 'family house',
                'capacity': 5,
                'base_resident_happiness': 0.55,
                'energy_consumption': 6,
                'water_consumption': 5,
                'waste_production': 5,
                'taxation': 3000,
                'upgrade_cost': 800,
                'images': [get_asset_path('House', 'H05.png')]
            },
            2: {
                'name': 'large residence',
                'capacity': 7,
                'base_resident_happiness': 0.65,
                'energy_consumption': 10,
                'water_consumption': 10,
                'waste_production': 8,
                'taxation': 4000,
                'upgrade_cost': 1000,
                'images': [get_asset_path('House', 'H04.png'), get_asset_path('House', 'H06.png')]
            }
        }
    }
    BLOCK = {
        'likeness': ['home'],
        'max_level': 3,
        'cost': 5000,
        'level': {
            0: {
                'name': 'regular block',
                'capacity': 90,  # in people
                'base_resident_happiness': 0.2,  # in percentage
                'energy_consumption': 99,  # in units
                'water_consumption': 90,  # in units
                'waste_production': 180,  # in units
                'taxation': 420,  # in dollars; per person; multiply by happiness+1 to get actual income
                'images': [get_asset_path('House', 'block0.png'), get_asset_path('House', 'block1.png')]
            },
            1: {
                'name': 'big block',
                'capacity': 200,
                'base_resident_happiness': 0.3,
                'energy_consumption': 230,
                'water_consumption': 200,
                'waste_production': 400,
                'taxation': 600,
                'upgrade_cost': 10000,
                'images': [get_asset_path('House', 'block3.png')]
            },
            2: {
                'name': 'high end block',
                'capacity': 200,
                'base_resident_happiness': 0.5,
                'energy_consumption': 250,
                'water_consumption': 210,
                'waste_production': 400,
                'taxation': 1000,
                'upgrade_cost': 10000,
                'images': [get_asset_path('House', 'block4.png')]
            }
        }
    }
    SHOP = {
        'max_level': 4,
        'cost': 1000,
        'zone': 'commercial',
        'level': {
            0: {
                'name': 'small shop',
                'employees': 3,
                'income': 1000,
                'products': 2,
                'energy_consumption': 10,
                'water_consumption': 5,
                'waste_production': 20,
                'resident_happiness_multiplier': 1.1,
                'images': [get_asset_path('Shop', 'SH0.png'), get_asset_path('Shop', 'SH1.png'), get_asset_path('Shop', 'SH2.png')]
            },
            1: {
                'name': 'shop',
                'description': 'Larger shop, meant to sustain a larger neighbourhood, be it of houses of city blocks.',
                'employees': 10,
                'income': 2000,
                'products': 5,
                'energy_consumption': 20,
                'water_consumption': 10,
                'waste_production': 40,
                'resident_happiness_multiplier': 1.2,
                'upgrade_cost': 2000,
                'images': [get_asset_path('Shop', 'SH3.png')]
            }
        }
    }
    FACTORY = {
        'max_level': 0,
        'cost': 1000,
        'zone': 'industrial',
        'level': {
            0: {
                'name': 'factory',
                'employees': 50,
                'income': -6000,
                'products': 15,
                'energy_consumption': 100,
                'water_consumption': 20,
                'waste_production': 70,
                'resident_happiness_multiplier': 0.35,
                'pollution': 0.6,
                'images': [get_asset_path('Factory', 'factory.png')]
            }
        }
    }

    HOSPITAL = {
        'max_level': 1,
        'cost': 1000,
        'level': {
            0: {
                'name': 'clinic',
                'description': 'Small clinic.',
                'patients': 10,
                'income': -1000,
                'energy_consumption': 50,
                'water_consumption': 30,
                'waste_production': 100,
                'resident_happiness_multiplier': 1.6,
                'images': [get_asset_path('SpecialBuildings', 'hospital.png')]
            },
            1: {
                'name': 'hospital',
                'description': 'Small hospital. Can house more people.',
                'patients': 200,
                'income': -10000,
                'energy_consumption': 500,
                'water_consumption': 300,
                'waste_production': 1000,
                'resident_happiness_multiplier': 1.9,
                'upgrade_cost': 10000,
                'image': [get_asset_path('SpecialBuildings', 'hospital.png')]
            }
        }
    }

    POLICE_STATION = {
        'max_level': 1,
        'cost': 1000,
        'level': {
            0: {
                'name': 'Police outpost.',
                'description': 'Smaller scale police outpost.',
                'policemen': 5,
                'income': 500,
                'energy_consumption': 10,
                'water_consumption': 5,
                'waste_production': 5,
                'resident_happiness_multiplier': 1.7,
                'images': [get_asset_path('SpecialBuildings', 'police0.png')]
            },
            1: {
                'name': 'Police station',
                'description': 'Local police headquarters.',
                'policemen': 20,
                'income': 1000,
                'energy_consumption': 50,
                'water_consumption': 20,
                'waste_production': 20,
                'resident_happiness_multiplier': 1.8,
                'upgrade_cost': 10000,
                'images': [get_asset_path('SpecialBuildings', 'police1.png')]
            }
        }
    }
    # PRISON = {
    #     'max_level': 0,
    #     'cost': 1000,
    #     'level':{
    #         0:{
    #             'name':'prison',
    #             'employees': 50,
    #             'inmates': 200,
    #             'income': -5000,
    #             'energy_consumption': 150,
    #             'water_consumption': 250,
    #             'waste_production': 200,
    #             'resident_happiness_multiplier': 1.7
    #         }
    #     }
    # }
    FIRE_STATION = {
        'max_level': 0,
        'cost': 1000,
        'level': {
            0: {
                'name': 'fire station',
                'description': 'A fire station. Keeps people hape that tere is a way for their house to be saved from nurning down.',
                'firemen': 20,
                'income': -2000,
                'energy_consumption': 80,
                'water_consumption': 400,
                'waste_production': 80,
                'range': 3,
                'upgrade_cost': 10000,
                'resident_happiness_multiplier': 1.9,
                'images': [get_asset_path('SpecialBuildings', 'firestation.png')]
            }
        }
    }

    SCHOOL = {
        'max_level': 0,
        'cost': 1000,
        'level': {
            0: {
                'name': 'school',
                'description': 'Building that houses kindergarten, primary and secondary school as well as a high school.',
                'teachers': 30,
                'students': 4000,
                'income': -1000,
                'energy_consumption': 500,
                'water_consumption': 500,
                'waste_production': 500,
                'range': 3,
                'city_income_multiplier': 1.01,
                'resident_happiness_multiplier': 1.5,
                'images': [get_asset_path('SpecialBuildings', 'school0.png')]
            }
        }
    }
    UNIVERSITY = {
        'max_level': 0,
        'cost': 1000,
        'level': {
            0: {
                'name': 'school',
                'description': 'Building that houses kindergarten, primary and secondary school as well as a high school.',
                'teachers': 500,
                'students': 40000,
                'income': -10000,
                'energy_consumption': 1000,
                'water_consumption': 1000,
                'waste_production': 1000,
                'city_income_multiplier': 1.05,
                'resident_happiness_multiplier': 1.9,
                'images': [get_asset_path('SpecialBuildings', 'school1.png')]
            }
        }
    }

    # MUSEUM = {
    #     'max_level': 0,
    #     'cost': 1000,
    #     'level':{
    #         0:{
    #             'name': 'museum',
    #             'description': 'A multi-themed museum.',
    #             'employees': 50,
    #             'income': 10000,
    #             'energy_consumption': 100,
    #             'water_consumption': 50,
    #             'waste_production': 60,
    #             'resident_happiness_multiplier': 1.7,
    #             'images': []
    #         }
    #     }
    # }
    PARK = {  # upgraded to dog park
        'max_level': 1,
        'cost': 1000,
        'level': {
            0: {
                'name': 'park',
                'description': 'A perfect place for people to relax.',
                'gardeners': 2,
                'income': -200,
                'energy_consumption': 2,
                'water_consumption': 100,
                'waste_production': 50,
                'resident_happiness_multiplier': 1.5,
                'images': [get_asset_path('SpecialBuildings', 'park0.png')]
            },
            1: {
                'name': 'dog park',
                'description': 'Perfect place to rela and walk your pupils <3',
                'gardeners': 5,
                'income': -200,
                'energy_consumption': 5,
                'water_consumption': 110,
                'waste_production': 60,
                'resident_happiness_multiplier': 2,
                'upgrade_cost': 8000,
                'images': [get_asset_path('SpecialBuildings', 'park1.png')]
            }
        }
    }
    STATUE = {
        'max_level': 0,
        'cost': 1000,
        'level': {
            0: {
                'name': 'statue',
                'description': 'Beauftiful statue - truly a sight to behold.',
                'resident_happiness_multiplier': 1.6,
                'images': [
                    get_asset_path('SpecialBuildings', 'statue0.png'),
                    get_asset_path('SpecialBuildings', 'statue1.png'),
                    get_asset_path('SpecialBuildings', 'statue2.png'),
                    get_asset_path('SpecialBuildings', 'statue3.png')
                ]
            }
        }
    }
    # AMUSEMENT_PARK = { #upgraded to water park
    #     'max_level': 1,
    #     'cost': 1000,
    #     'level':{
    #         0:{
    #             'name': 'amusement park',
    #             'description': 'An amusement park - increases resident happiness.',
    #             'employees': 100,
    #             'customers': 1000,
    #             'income': 50000,
    #             'energy_consumption': 5000,
    #             'water_consumption': 1000,
    #             'waste_production': ,
    #             'resident_happiness_multiplier': 2,
    #             'images': []
    #         },
    #         0:{
    #             'name': 'water park',
    #             'description': 'An amusement park enriched with big pools and water slides - greatly increases resident happiness.',
    #             'employees': 100,
    #             'customers': 1000,
    #             'income': 100000,
    #             'energy_consumption': 5000,
    #             'water_consumption': 10000,
    #             'waste_production': 1200,
    #             'resident_happiness_multiplier': 3,
    #             'upgrade_cost': 100000,
    #             'images': []
    #         }
    #     }
    # }

    LANDFILL = {  # upgraded to waste processing plant
        'max_level': 1,
        'cost': 1000,
        'level': {
            0: {
                'name': 'landfill',
                'description': 'Building to store the waste.',
                'employees': 10,
                'income': -1000,
                'waste_consumption': 500,
                'resident_happiness_multiplier': 0.2,
                'pollution': 0.9,
                'images': [get_asset_path('SpecialBuildings', 'landfill.png')]
            },
            0: {
                'name': 'waste processing station',
                'description': 'Disposes of the waste and turns it into power.',
                'employees': [50],
                'income': -5000,
                'energy_production': 1000,
                'waste_consumption': 1000,
                'resident_happiness_multiplier': 1.0,
                'pollution': 0.2,
                'upgrade_cost': 50000,
                'images': [get_asset_path('SpecialBuildings', 'wasteprocess.png')]
            }
        }
    }
    # POWER_PLANT = {
    #     'max_level': 2,
    #     'cost': 5000,
    #     'constructor': CoalPowerPlant,
    #     'types': {
    #         0: {
    #             'name': 'coal power plant',
    #             'description': 'A power plant which uses coal and converts heat to electrical power.',
    #             'maintenance': 50,
    #             'income': -1000,
    #             'energy_production': 1000,
    #             'resident_happiness_multiplier': 0.5,
    #             'images': []
    #         },
    #         1: {
    #             'name': 'sun power plant',
    #             'description': "Much more economical power plant with increased energy production - uses sunlight to create electricity.",
    #             'maintenance': 50,
    #             'income': -10000,
    #             'energy_production': 8000,
    #             'resident_happiness_multiplier': 1.5,
    #             'upgrade_cost': 100000,
    #             'images': []
    #         },
    #         2: {
    #             'name': 'nuclear power plant',
    #             'description': "High tech, state of the art facility. Produces large amounts of energy but reduces residents happiness and risks critical failure.",
    #             'income': -100000,
    #             'maintenance': 100,
    #             'energy_production': 100000,
    #             'upgrade_cost': 1000000,
    #             'resident_happiness_multiplier': 0.8,
    #             'images': []
    #         }
    #     }
    # }
    WATER_PUMP = {
        'max_level': 2,
        'cost': 1000,
        'level': {
            0: {
                'name': 'water pump',
                'description': 'Increases water amount in the storage and provides water for all residents in range.',
                'income': -1000,
                'energy_consumption': 100,
                'water_productioin': 1000,
                'resident_happiness_multiplier': 1.1,
                'images': [get_asset_path('SpecialBuildings', 'waterpipe.png')]
            }
        }
    }
    # SWEWAGE_PUMP = {
    #     'max_level': 2,
    #     'cost': 1000,
    #     'level':{
    #         0:{
    #             'name': ,
    #             'description': ,
    #             'patients': ,
    #             'income': ,
    #             'energy_consumption': ,
    #             'water_consumption': ,
    #             'waste_production': ,
    #             'resident_happiness_multiplier': ,
    #             'images': [get_asset_path('SpecialBuildings', 's.png')]
    #         }
    #     }
    # }
    # SEWAGE_PROCESSING_STATION = {
    #     'max_level': 2,
    #     'cost': 1000,
    #     'constructor': SewageProcessingStation,
    #     'type': {
    #         0: {
    #             'name': 'standard',
    #             'description': 'Station destined to process sewage produced by cisty buildings.',
    #             'pollution_level': 0.75,
    #             'range': 5,
    #             'energy_consumption': 1
    #         },
    #         1: {
    #             'name': 'industrial',
    #             'description': 'Expanded sewage treatement station with double the processing power of the regular variant.',
    #             'pollution_level': 0.75,
    #             'range': 10,
    #             'energy_consumption': 2,
    #             'upgrade_cost': 10000,
    #             'images': []
    #         },
    #         2: {
    #             'name': 'economical',
    #             'description': 'More economical version of the sewage treatment station. Decreases pollution by one third.',
    #             'pollution_level': 0.5,
    #             'range': 10,
    #             'energy_consumption': 4,
    #             'upgrade_cost': 50000,
    #             'images': []
    #         }
    #     }
    # }

    def get_info(self, type):
        return type.value
