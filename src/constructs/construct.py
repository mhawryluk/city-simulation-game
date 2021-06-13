from random import choice, seed
from time import time
import pygame as pg
from constructs.construct_type import ConstructType


class Construct:
    def __init__(self, construct_type=None, construct_state=None):
        self.image = None
        self.image_path = None

        if construct_state:
            self.construct_level = int(construct_state['construct_level'])
            self.type_name = construct_state['type']
            self.type = ConstructType[self.type_name].value

            self.happiness = None if construct_state['happiness'] is None else float(
                construct_state['happiness'])
            self.heat = bool(construct_state['heat'])
            self.crime_level = int(construct_state['crime_level'])
            self.waste = int(construct_state['waste'])

            self.past_images = construct_state['images']
            self.choose_image(path=self.past_images[-1])
        else:
            self.construct_level = 0
            self.type_name = ''.join(str(construct_type).split('.')[1])
            self.type = construct_type.value

            self.happiness = self.type['level'][0].get(
                'base_resident_happiness', None)
            self.heat = False
            self.crime_level = 0
            self.waste = 0

            self.past_images = []
            self.choose_image()

    def choose_image(self, path=None):
        if path is None:
            seed(time())
            path = choice(self.type['level'][self.construct_level]['images'])
            self.past_images.append(path)
        self.image = pg.image.load(path)
        self.image_path = path

    def level_up(self, level_up_by=1):
        prev = self.construct_level
        max_level = len(self.type['level']) - 1
        self.construct_level = min(
            max_level, self.construct_level + level_up_by)
        if self.construct_level != prev:
            self.choose_image()
        return self.construct_level - prev

    def level_down(self, level_down_by=1):
        prev = self.construct_level
        self.construct_level = max(0, self.construct_level - level_down_by)
        if self.construct_level != prev and self.construct_level >= 0:
            self.past_images.pop()
            self.image = pg.image.load(self.past_images[-1])
        return prev - self.construct_level

    def get(self, string, else_value):
        """retrieves specified info from the construct"""
        value = self.type.get(string, else_value)
        if value is else_value:
            level = self.get_level()
            value = level.get(
                string, else_value)
        return value

    def get_level(self):
        level = self.type['level'].get(self.construct_level, None)
        if level is None:
            level = self.type['level'].get(str(self.construct_level), None)
        if level is None:
            print("Error: invalid construct level structure")
            print(self.type)
        return level

    def likes(self, cmp_likeness):
        return cmp_likeness in self.get('likeness', [])

    def multiply_happiness(self, by):
        if self.happiness is not None:
            self.happiness *= by

    def compress2save(self):
        return {
            'construct_level': self.construct_level,
            'type': self.type_name,
            'happiness': self.happiness,
            'heat': self.heat,
            'crime_level': self.crime_level,
            'waste': self.waste,
            'images': self.past_images
        }
