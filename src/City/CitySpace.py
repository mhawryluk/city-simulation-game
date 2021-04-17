from City.Lot import *
from City.LotType import *
from City.CityImages import *
from City.RoadSystem import *
import pygame as pg


class CitySpace:

    def __init__(self, width, height, window_width, window_height):
        self.city_images = CityImages()
        Lot.city_images = self.city_images
        Lot.map_dimensions = (width, height)
        Lot.window_dimensions = (window_width, window_height)
        self.window_height = window_height
        self.window_width = window_width
        self.height = height
        self.width = width
        self.pov_x = window_width // 2
        self.pov_y = window_height // 2
        self.road_system = RoadSystem(width, height)
        self.scale = 50
        self.reset_lots()
        self.move_speed = (0, 0)
        self.selected_lot = None
        self.hovered_lot = None
        self.zone = set()

    def reset_lots(self):
        self.lots = []
        for x in range(self.width):
            self.lots.append([])
            for y in range(self.height):
                if not ((self.width // 5 < x < 4*self.width//5) and (self.height // 5 < y < 4*self.height//5)):
                    self.lots[x].append(Lot(x, y, LotType.WATER))
                else:
                    self.lots[x].append(Lot(x, y, LotType.GRASS))

    def update(self):
        self.pov_x += self.move_speed[0]
        self.pov_y += self.move_speed[1]

        # border:
        self.pov_x = max(self.pov_x, self.window_width -
                         self.scale*self.width//2)
        self.pov_x = min(self.pov_x, self.scale*self.width//2)
        self.pov_y = min(self.pov_y, self.scale*self.height//2)
        self.pov_y = max(self.pov_y, self.window_height -
                         self.scale*self.height//2)

    def hovered(self, pos, mode):
        '''hovered lot highlighting:'''
        if mode == "road_placing":
            self.road_system.hovered_road = self.get_clicked_road(pos)

        else:
            if pos is None:
                if self.hovered_lot:
                    self.hovered_lot.hovered = False
                self.hovered_lot = None
                return

            hovered_lot = self.get_clicked_lot(pos)
            hovered_lot.hovered = True

            if self.hovered_lot and self.hovered_lot != hovered_lot:
                self.hovered_lot.hovered = False

            self.hovered_lot = hovered_lot

    def draw(self, window, mode, construct_to_buy):
        self.city_images.rescale(self.scale)
        # draw lots
        for row in self.lots:
            for lot in row:
                lot.draw(self.scale, (self.pov_x, self.pov_y), window)

        self.road_system.draw((self.pov_x, self.pov_y), self.scale, window)

        if mode == "road_placing":
            alpha = pg.Surface((self.window_width, self.window_height))
            alpha.set_alpha(128)
            alpha.fill((192, 192, 192))
            window.blit(alpha, (0, 0))
            self.road_system.highlight_roads(
                (self.pov_x, self.pov_y), self.scale, window)

        # faded picture of a construct to be placed and bought
        elif construct_to_buy:
            lot = self.get_clicked_lot(pg.mouse.get_pos())
            image = construct_to_buy.value['level'][0]['image']
            image = pg.transform.scale(image, (self.scale, self.scale))
            window.blit(image, lot.get_draw_position(
                (self.pov_x, self.pov_y), self.scale))

            alpha = pg.Surface((self.scale, self.scale))
            alpha.set_alpha(128)

            if not lot.can_place():
                alpha.fill((255, 0, 0))
            else:
                alpha.fill((50, 50, 50))

            window.blit(alpha, lot.get_draw_position(
                (self.pov_x, self.pov_y), self.scale))

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
        x = (mouse_pos[0] - self.pov_x +
             self.scale*self.width//2) // self.scale
        y = (mouse_pos[1] - self.pov_y +
             self.scale*self.height//2) // self.scale
        return self.lots[x][y]

    def get_clicked_road(self, mouse_pos):
        if mouse_pos is None:
            return

        x = round((mouse_pos[0] - self.pov_x +
                  self.scale*self.width//2) / self.scale)
        y = round((mouse_pos[1] - self.pov_y +
                  self.scale*self.height//2) / self.scale)
        return (x, y)

    def road_clicked(self):
        self.road_system.road_clicked()

    def add_to_zone(self, zone_type):
        clicked_lot = self.get_clicked_lot(pg.mouse.get_pos())
        if clicked_lot.can_place():
            clicked_lot.set_zone(zone_type)
            self.zone.add(clicked_lot)

    def buy_construct(self, construct) -> bool:
        '''return True if managed to buy'''
        clicked_lot = self.get_clicked_lot(pg.mouse.get_pos())
        if clicked_lot.can_place():
            clicked_lot.set_construct(construct)
            return True
        return False
