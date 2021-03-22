from City.Lot import *


class CitySpace:

    def __init__(self, width, height, window_width, window_height):
        self.window_height = window_height
        self.window_width = window_width
        self.height = height
        self.width = width
        self.pov_x = -height // 2
        self.pov_y = -width // 2
        self.roads = []
        self.scale = 50
        self.reset_lots()
        self.move_speed = (0, 0)
        self.selected_lot = None

    def reset_lots(self):
        self.lots = []
        for x in range(self.width):
            self.lots.append([])
            for y in range(self.height):
                self.lots[x].append(Lot(x, y))

    def update(self):
        self.pov_x += self.move_speed[0]
        self.pov_y += self.move_speed[1]
        self.pov_x = max(self.window_width - self.width*self.scale, self.pov_x)
        self.pov_x = min(0, self.pov_x)
        self.pov_y = max(self.window_height - self.height *
                         self.scale, self.pov_y)
        self.pov_y = min(0, self.pov_y)

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
        self.scale = max([self.window_height // self.height + 1,
                         self.window_width // self.width + 1, self.scale])

    def select_lot(self, mouse_pos):
        if self.selected_lot:
            self.selected_lot.selected = False
        self.get_clicked_lot(mouse_pos).selected = True
        self.selected_lot = self.get_clicked_lot(mouse_pos)

    def get_clicked_lot(self, mouse_pos):
        return self.lots[(mouse_pos[0] - self.pov_x) // self.scale][(mouse_pos[1] - self.pov_y) // self.scale]
