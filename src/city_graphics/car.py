from city import VERTICAL, HORIZONTAL
from math import floor
from random import choice, randint, seed
from time import time


class Car:
    def __init__(self, initial_road, initial_road_direction, road_system, image_type):
        self.x = initial_road[0]
        self.y = initial_road[1]
        self.road_direction = initial_road_direction
        self.direction = 1
        self.road_system = road_system
        self.image_type = image_type

    def move(self, amount):
        # print(self.x, self.y)
        if self.road_direction == VERTICAL:
            self.y += self.direction*amount
            if floor(self.y - self.direction*amount) != floor(self.y):
                # print(self.x-amount, self.x)
                self.crossing()
                if self.road_direction == VERTICAL:
                    self.y += 2*self.direction*amount
                elif self.road_direction == HORIZONTAL:
                    self.x += 2*self.direction*amount
        elif self.road_direction == HORIZONTAL:
            self.x += self.direction*amount
            if floor(self.x - self.direction*amount) != floor(self.x):
                self.crossing()
                if self.road_direction == VERTICAL:
                    self.y += 2*self.direction*amount
                elif self.road_direction == HORIZONTAL:
                    self.x += 2*self.direction*amount

    def crossing(self):
        x, y = floor(self.x), floor(self.y)

        if self.direction == -1:
            if self.road_direction == VERTICAL:
                y += 1
            elif self.road_direction == HORIZONTAL:
                x += 1

        possible_turns = [[x, y, VERTICAL, 1], [x, y, HORIZONTAL, 1], [
            x, y-1, VERTICAL, -1], [x-1, y, HORIZONTAL, -1]]
        available_turns = []

        for turn in possible_turns:
            if self.road_system.has_road(turn[0], turn[1], turn[2]) and turn[2:] != [self.road_direction, -self.direction]:
                available_turns.append((x, y, turn[2], turn[3]))

        if not available_turns:
            self.direction *= -1
        else:
            seed(time())
            self.x, self.y, self.road_direction, self.direction = choice(
                available_turns)
