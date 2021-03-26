from City.LotType import *
import pygame as pg
import os
from random import random, choice


class CityImages:
    def __init__(self):
        self.main_images = {
            LotType.GRASS: pg.image.load(os.path.join('Assets', 'grass.png')),
            LotType.WATER: pg.image.load(os.path.join('Assets', 'water.png'))}

        self.additional_images = {
            LotType.GRASS: [
                pg.image.load(os.path.join('Assets', 'hills.png')),
                pg.image.load(os.path.join('Assets', 'flowers.png')),
                pg.image.load(os.path.join('Assets', 'small_hills.png')),
                pg.image.load(os.path.join('Assets', 'stones.png'))
            ],
            LotType.WATER: [
                pg.image.load(os.path.join('Assets', 'island.png'))
            ]}

        self.frequency = {
            LotType.GRASS: 0.1,
            LotType.WATER: 0.005
        }

    def get_images(self, lot_type):
        images = [self.main_images[lot_type]]
        if lot_type in self.additional_images and random() < self.frequency[lot_type]:
            images += [choice(self.additional_images[lot_type])]
        return images
