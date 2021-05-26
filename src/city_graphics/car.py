from city import VERTICAL, HORIZONTAL, ROAD_WIDTH_RATIO
from math import floor
from random import choice, randint


class Car:
    def __init__(self, initial_road, initial_road_direction, road_system, image_type):
        self.x = initial_road[0]
        self.y = initial_road[1]
        self.road_direction = initial_road_direction
        self.direction = 1
        self.road_system = road_system
        self.image_type = image_type

    def move(self, amount):
        if self.road_direction == VERTICAL:
            self.y += self.direction*amount
        elif self.road_direction == HORIZONTAL:
            self.x += self.direction*amount

        if floor(self.x - amount) != floor(self.x) or floor(self.y - amount) != floor(self.y):
            return self.crossing()
        else:
            return True

    def crossing(self):
        x, y = round(self.x, self.y)
        available_roads = []
        road = self.road_system.get_road(x, y, VERTICAL)
        if road:
            available_roads.append((road, VERTICAL, 1))

        road = self.road_system.get_road(x, y, HORIZONTAL)
        if road:
            available_roads.append((road, HORIZONTAL, 1))

        road = self.road_system.get_road(x, y, VERTICAL)
        if road:
            available_roads.append((road, VERTICAL, -1))

        road = self.road_system.get_road(x, y, HORIZONTAL)
        if road:
            available_roads.append((road, HORIZONTAL, 1))

        if not available_roads:
            return False

        road, self.road_direction, self.direction = choice(available_roads)
        self.x = road[0]
        self.y = road[1]
        return True
