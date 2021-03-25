from City.LotType import *
import pygame as pg
import os
from random import random, choice


class CityImages:
    def __init__(self):
        self.images = {
            LotType.GRASS: {
                "main": pg.image.load(os.path.join('Assets', 'grass.png')),
                "additional": [
                    pg.image.load(os.path.join('Assets', 'hills.png')),
                    pg.image.load(os.path.join('Assets', 'flowers.png'))
                ],
            },
            LotType.WATER: {
                "main": pg.image.load(os.path.join('Assets', 'water.png')),
                "additional": [pg.image.load(os.path.join('Assets', 'island.png'))]
            }}

    def get_images(self, lot_type):
        images = [self.images[lot_type]["main"]]
        if self.images[lot_type]["additional"] and random() < 0.1:
            images += [choice(self.images[lot_type]["additional"])]
        return images
