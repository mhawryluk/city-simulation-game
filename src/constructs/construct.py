from random import choice, seed
from time import time
from constructs.construct_type import ConstructType
import pygame as pg


class Construct:
    def __init__(self, construct_type, construct_state=None):
        if construct_type is None:
            self.construct_level = construct_state['construct_level']
            self.human_resources = construct_state['human_resouces']
            self.users = construct_state['users']
            self.type = construct_state['type_value']

            self.happyness = construct_state['happyness']
            self.burning = construct_state['burning']
            self.crime_level = construct_state['crime_level']
            self.waste = construct_state['waste']

            self.image = None
            self.past_images = construct_state['images']
            self.choose_image(path=self.past_images[-1])
        else:
            self.construct_level = 0
            self.human_resources = 0
            self.users = 0
            self.type = construct_type.value

            self.happyness = self.type['level'][0].get('base_resident_happiness', None)
            self.burning = False
            self.crime_level = 0
            self.waste = 0

            self.image = None
            self.past_images = []
            self.choose_image()

    def choose_image(self, path=None):
        if path is None:
            seed(time())
            path = choice(self.type['level'][self.construct_level]['images'])
            self.past_images.append(path)
        self.image = pg.image.load(path)

    def level_up(self, level_up_by):
        prev = self.construct_level
        self.construct_level = min(
            self.attributes['max_level'], self.construct_level + level_up_by)
        if self.construct_level != prev:
            self.choose_image()
        return self.construct_level - prev

    def delevel(self, delevel_by):
        prev = self.construct_level
        self.construct_level = max(0, self.construct_level - delevel_by)
        if self.construct_level != prev and self.construct_level >= 0:
            self.past_images.pop()
            self.image = pg.image.load(self.past_images[-1])
        return prev - self.construct_level

    def compress2save(self):
        return {
            'construct_level': self.construct_level,
            'human_resouces': self.human_resources,
            'users': self.users,
            'type_value': self.type,
            'happyness': self.happyness,
            'burning': self.burning,
            'crime_level': self.crime_level,
            'waste': self.waste,
            'images': self.past_images
        }

    def get(self, string, else_value):
        value = self.type.get(string, else_value)
        if value is else_value:
            value = self.type['level'][self.construct_level].get(string, else_value)
        return value