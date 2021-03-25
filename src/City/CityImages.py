from City.LotType import *
import pygame as pg
import os


class CityImages:
    def __init__(self):
        self.images = {
            LotType.GRASS: pg.image.load(
                os.path.join('Assets', 'grass.png')),
            LotType.WATER: pg.image.load(
                os.path.join('Assets', 'water.png'))}

    def get_image(self, lot_type):
        return self.images[lot_type]
