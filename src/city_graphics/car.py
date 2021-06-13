from math import floor
from random import choice, seed
from time import time
from city import VERTICAL, HORIZONTAL


class Car:
    """class representing vehicles on the roads"""

    def __init__(self, initial_road, initial_road_direction, road_system, image_type):
        # setting initial position
        self.x = initial_road[0]
        self.y = initial_road[1]

        self.road_direction = initial_road_direction  # VERTICAL OR HORIZONTAL
        self.car_direction = 1  # 1 or -1 (left or right)/(up or down)

        self.road_system = road_system
        self.image_type = image_type

    def move(self, amount):
        """called with each animation frame"""

        if self.road_direction == VERTICAL:
            self.y += self.car_direction * amount
            if floor(self.y - self.car_direction * amount) != floor(self.y):
                self.crossing()
                if self.road_direction == VERTICAL:
                    self.y += 2 * self.car_direction * amount
                elif self.road_direction == HORIZONTAL:
                    self.x += 2 * self.car_direction * amount
        elif self.road_direction == HORIZONTAL:
            self.x += self.car_direction * amount
            if floor(self.x - self.car_direction * amount) != floor(self.x):
                self.crossing()
                if self.road_direction == VERTICAL:
                    self.y += 2 * self.car_direction * amount
                elif self.road_direction == HORIZONTAL:
                    self.x += 2 * self.car_direction * amount

    def crossing(self):
        """ called when reached the end of a single part of road """
        x, y = floor(self.x), floor(self.y)

        if self.car_direction == -1:
            if self.road_direction == VERTICAL:
                y += 1
            elif self.road_direction == HORIZONTAL:
                x += 1

        possible_turns = [[x, y, VERTICAL, 1], [x, y, HORIZONTAL, 1], [x, y - 1, VERTICAL, -1],
                          [x - 1, y, HORIZONTAL, -1]]
        available_turns = [
            (x, y, turn[2], turn[3]) for turn in possible_turns
            if self.road_system.has_road(turn[0], turn[1], turn[2]) and turn[2:] != [self.road_direction, -self.car_direction]
        ]

        if not available_turns:
            self.car_direction *= -1
        else:
            seed(time())
            self.x, self.y, self.road_direction, self.car_direction = choice(available_turns)
