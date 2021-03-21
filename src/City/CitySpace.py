from City.Lot import *


class CitySpace:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.pov_x = 0
        self.pov_y = 0
        self.roads = []
        self.scale = 20
        self.reset_lots()
        self.move_speed = (0, 0)

    def reset_lots(self):
        self.lots = []
        for x in range(self.width):
            self.lots.append([])
            for y in range(self.height):
                self.lots[x].append(Lot(x, y))

    def update(self):
        self.pov_x += self.move_speed[0]
        self.pov_y += self.move_speed[1]

    def draw(self, window):

        # draw lots
        for row in self.lots:
            for lot in row:
                lot.draw(self.scale, (self.pov_x, self.pov_y), window)

    def add_move_speed(self, move_speed):
        self.move_speed = (
            self.move_speed[0] + move_speed[0], self.move_speed[1] + move_speed[1])

    def zoom(self, zoom_value):
        self.scale += zoom_value
