import os
from random import random, choice, seed
from time import time_ns

import pygame as pg

from city import HORIZONTAL
from city.lot_type import LotType
from city_graphics import ROAD_WIDTH_RATIO
from game_engine_tools import load_asset, get_asset_path, Singleton


class CityImages(metaclass=Singleton):
    """scaled and original background lot images"""
    current_scale = -1

    def __init__(self):
        self.main_images = {
            LotType.GRASS: load_asset('LotType', 'PNG', 'rpgTile039.png'),
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
                load_asset('LotType', 'PNG', f'rpgTile{i}.png') for i in [155, 156, 158, 160]
            ],
            LotType.WATER: [
                load_asset('LotType', 'island.png')
            ]}

        # chance of adding an addition image on specific lot type:
        self.frequency = {
            LotType.GRASS: 0.1,
            LotType.WATER: 0.005
        }

        self.icons = {
            path.name.split('.')[-2]: path.path for path in os.scandir(get_asset_path("Icons2"))
        }

        self.warning_icons = {
            path.name.split('.')[-2]: path.path for path in os.scandir(get_asset_path("WarningIcons"))
        }

        self.vertical_road = load_asset('Streets', 'vertical.png')
        self.horizontal_road = load_asset('Streets', 'horizontal.png')

        self.cars = {
            key: load_asset('Cars', f'{key}.png') for key in [
                'mini-van', 'audi', 'mini-truck', 'taxi'
            ]
        }

        self.animation_images = {
            'fire': [load_asset('Animations', f'flame{i}.png') for i in range(5)],
            'unhappy': [load_asset('Status', 'icon_sad.png'), load_asset('Status', 'icon_cry.png')],
            'pandemic': [load_asset('Animations', f'coronavirus-red-rim-light-pulse_{i}.png') for i in range(7)],
            'burglary': [load_asset('Animations', 'Roll jump', f'rj_{i:03}.png') for i in range(37)]
        }

        self.scaled_main_images = self.main_images
        self.scaled_additional_images = self.additional_images
        self.scaled_cars = self.additional_images
        self.scaled_vertical = self.vertical_road
        self.scaled_horizontal = self.horizontal_road

    def rescale(self, scale):
        if scale == self.current_scale:
            return
        self.current_scale = scale

        self.scaled_main_images = {k: pg.transform.scale(
            v, (scale, scale)) for k, v in self.main_images.items()}

        self.scaled_cars = {k: pg.transform.scale(
            v, (int(scale * ROAD_WIDTH_RATIO * 1.1), int(scale * ROAD_WIDTH_RATIO * 1.1))) for k, v in
            self.cars.items()}

        self.scaled_additional_images = {k: list(map(lambda x: pg.transform.scale(
            x, (scale, scale)), v)) for k, v in self.additional_images.items()}

        self.scaled_vertical = pg.transform.scale(self.vertical_road, (int(scale * ROAD_WIDTH_RATIO), int(scale + scale * ROAD_WIDTH_RATIO)))
        self.scaled_horizontal = pg.transform.scale(self.horizontal_road, (int(scale + scale * ROAD_WIDTH_RATIO), int(scale * ROAD_WIDTH_RATIO)))

    def get_images(self, lot_type, lot_seed):
        seed(lot_seed)
        images = [self.scaled_main_images[lot_type]]
        if lot_type in self.scaled_additional_images and random() < self.frequency[lot_type]:
            images += [choice(self.scaled_additional_images[lot_type])]
        return images

    def get_icon(self, icon):
        return self.icons[icon]

    def get_warning_icon(self, icon):
        return self.warning_icons[icon]

    def get_scaled_car_image(self, car_type, road_direction, direction):
        image = self.scaled_cars[car_type]
        if road_direction == HORIZONTAL:
            image = pg.transform.rotate(image, -direction * 90)
        return image

    def get_random_car_type(self):
        seed(time_ns())
        return choice(list(self.cars.keys()))

    def get_animation_image(self, animation_type, frame, size):
        image = self.animation_images[animation_type][frame % len(
            self.animation_images[animation_type])]
        return pg.transform.scale(image, (size, size))
