from city.lot_type import LotType
import pygame as pg
import os
from random import random, choice, seed
from game_engine_tools import load_asset, get_asset_path


class CityImages:
    '''scaled and original background lot images'''

    def __init__(self):
        self.main_images = {
            # LotType.GRASS: load_asset('LotType', 'grass.png'),
            LotType.GRASS: load_asset('LotType', 'PNG', 'rpgTile039.png'),
            # LotType.WATER: load_asset('LotType', 'water.png')
            LotType.WATER: load_asset('LotType', 'PNG', 'rpgTile029.png'),

            LotType.WATER_RIGHT: load_asset('LotType', 'PNG', 'rpgTile030.png'),
            LotType.WATER_LEFT: load_asset('LotType', 'PNG', 'rpgTile028.png'),
            LotType.WATER_UP: load_asset('LotType', 'PNG', 'rpgTile011.png'),
            LotType.WATER_DOWN: load_asset('LotType', 'PNG', 'rpgTile045.png'),

            LotType.WATER_CORNER_LEFT_UP: load_asset('LotType', 'PNG', 'rpgTile032.png'),
            LotType.WATER_CORNER_LEFT_DOWN: load_asset('LotType', 'PNG', 'rpgTile014.png'),
            LotType.WATER_CORNER_RIGHT_UP: load_asset('LotType', 'PNG', 'rpgTile031.png'),
            LotType.WATER_CORNER_RIGHT_DOWN: load_asset('LotType', 'PNG', 'rpgTile013.png'),

            LotType.WATER_IN_CORNER_LEFT_UP: load_asset('LotType', 'PNG', 'rpgTile010.png'),
            LotType.WATER_IN_CORNER_LEFT_DOWN: load_asset('LotType', 'PNG', 'rpgTile044.png'),
            LotType.WATER_IN_CORNER_RIGHT_UP: load_asset('LotType', 'PNG', 'rpgTile012.png'),
            LotType.WATER_IN_CORNER_RIGHT_DOWN: load_asset(
                'LotType', 'PNG', 'rpgTile046.png')
        }

        self.additional_images = {
            LotType.GRASS: [
                load_asset('LotType', 'PNG', 'rpgTile155.png'),
                load_asset('LotType', 'PNG', 'rpgTile156.png'),
                load_asset('LotType', 'PNG', 'rpgTile160.png'),
                load_asset('LotType', 'PNG', 'rpgTile158.png')
            ],
            LotType.WATER: [
                load_asset('LotType', 'island.png')
            ]}

        self.frequency = {
            LotType.GRASS: 0.1,
            LotType.WATER: 0.005
        }

        self.icons = {
            key: get_asset_path('Icons2', f'{key}.png') for key in [
                'play-button',
                'modern-city',
                'capitol',
                'bulldozer',
                'road',
                'crane',
                'settings-knobs',
                'banknote',
                'heart-inside',
                'person',
                'drop',
                'trash-can',
                'plug',
                'recycle',
                'house',
                'shop',
                'factory'
            ]
        }

        self.scaled_main_images = self.main_images
        self.scaled_additional_images = self.additional_images

    def rescale(self, scale):
        self.scaled_main_images = {k: pg.transform.scale(
            v, (scale, scale)) for k, v in self.main_images.items()}

        self.scaled_additional_images = {k: list(map(lambda x: pg.transform.scale(
            x, (scale, scale)), v)) for k, v in self.additional_images.items()}

    def get_images(self, lot_type, lot_seed):
        seed(lot_seed)
        images = [self.scaled_main_images[lot_type]]
        if lot_type in self.scaled_additional_images and random() < self.frequency[lot_type]:
            images += [choice(self.scaled_additional_images[lot_type])]
        return images

    def get_icon(self, icon):
        return self.icons[icon]


CITY_IMAGES = CityImages()
