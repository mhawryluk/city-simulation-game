from City.LotType import *
import pygame as pg
import os
from random import random, choice, seed


class CityImages:
    def __init__(self):
        self.main_images = {
            LotType.GRASS: pg.image.load(os.path.join('Assets', 'LotType', 'grass.png')),
            LotType.WATER: pg.image.load(os.path.join('Assets', 'LotType', 'water.png'))}

        self.additional_images = {
            LotType.GRASS: [
                pg.image.load(os.path.join('Assets', 'LotType', 'hills.png')),
                pg.image.load(os.path.join(
                    'Assets', 'LotType', 'flowers.png')),
                pg.image.load(os.path.join(
                    'Assets', 'LotType', 'small_hills.png')),
                pg.image.load(os.path.join('Assets', 'LotType', 'stones.png'))
            ],
            LotType.WATER: [
                pg.image.load(os.path.join('Assets', 'LotType', 'island.png'))
            ]}

        self.frequency = {
            LotType.GRASS: 0.1,
            LotType.WATER: 0.005
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
