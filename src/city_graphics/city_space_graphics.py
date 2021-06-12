from city_graphics import ROAD_WIDTH_RATIO
from city import VERTICAL
from game_engine_tools import WINDOW_SIZE
from city_graphics.lot_graphics import LotGraphics
from city_graphics.road_graphics import RoadGraphics
from city_graphics.city_images import CityImages
import pygame as pg


class CitySpaceGraphics:
    GRAY = (192, 192, 192)
    AFFECTS_COLOR = 0xf4acb7
    AFFECTED_COLOR = 0xffcad4

    def __init__(self, city_space, width, height):
        self.city_space = city_space
        self.city_images = CityImages()

        LotGraphics.map_dimensions = (width, height)
        RoadGraphics.map_dimensions = (width, height)
        RoadGraphics.reset()
        LotGraphics.reset()

        self.height = height  # amount of fields to height
        self.width = width  # amount of fields to width

        # pov - point of origin from which we're drawing
        self.pov_x = WINDOW_SIZE[0] // 2
        self.pov_y = WINDOW_SIZE[1] // 2
        self.scale = max([WINDOW_SIZE[1] // self.height + 1,
                         WINDOW_SIZE[0] // self.width + 1])  # defines the zoom
        self.move_speed = (0, 0)  # added to pov in each frame

        self.selected_lot = None  # square selected with lmb
        self.hovered_lot = None  # square above which the mouse is currently hovering

    def draw(self, mode, construct_to_buy, window):
        # rescaling
        self.city_images.rescale(self.scale)

        # draw lots
        for row in self.city_space.lots:
            for lot in row:
                LotGraphics.draw_background(
                    lot, self.scale, (self.pov_x, self.pov_y))

        # faded picture of a construct to be placed and bought
        if construct_to_buy:
            lot = self.get_clicked_lot(pg.mouse.get_pos())
            image = pg.image.load(
                construct_to_buy.value['level'][0]['images'][0])
            x, y = LotGraphics.get_draw_position(
                lot, (self.pov_x, self.pov_y), self.scale)

            offset = int(ROAD_WIDTH_RATIO*self.scale)
            scale = int(self.scale*(1 - ROAD_WIDTH_RATIO))
            width, height = image.get_width(), image.get_height()
            ratio = scale/width
            new_width, new_height = int(width*ratio), int(height*ratio)
            x = x + offset
            y = y - new_height + scale + offset
            image = pg.transform.scale(image, (new_width, new_height))

            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)

            if not lot.can_place(construct_to_buy):
                alpha.fill((255, 0, 0))
            else:
                alpha.fill((50, 50, 50))

            window.blit(image, (x, y))
            window.blit(alpha, (x, y))

        # roads
        RoadGraphics.draw(self.city_space.road_system,
                          (self.pov_x, self.pov_y), self.scale)

        # constructs
        for row in self.city_space.lots:
            for lot in row:
                LotGraphics.draw_construct(
                    lot, self.scale, (self.pov_x, self.pov_y))

        # cars
        RoadGraphics.animate_cars(
            self.city_space.road_system, (self.pov_x, self.pov_y), self.scale)

        # road placing drawing effect
        if mode == "road_placing":
            alpha = pg.Surface(WINDOW_SIZE)
            alpha.set_alpha(128)
            alpha.fill(self.GRAY)
            window.blit(alpha, (0, 0))
            RoadGraphics.highlight_roads(
                self.city_space.road_system, (self.pov_x, self.pov_y), self.scale)

        if mode == "access_highlighting":
            alpha = pg.Surface(WINDOW_SIZE)
            alpha.set_alpha(128)
            alpha.fill(self.GRAY)
            window.blit(alpha, (0, 0))
            self.highlight_access(window)

    def update(self):
        '''moves the map in each frame'''

        self.pov_x += self.move_speed[0]
        self.pov_y += self.move_speed[1]

        # border:
        self.pov_x = max(self.pov_x, WINDOW_SIZE[0] -
                         self.scale*self.width//2)
        self.pov_x = min(self.pov_x, self.scale*self.width//2)
        self.pov_y = min(self.pov_y, self.scale*self.height//2)
        self.pov_y = max(self.pov_y, WINDOW_SIZE[1] -
                         self.scale*self.height//2)

    def hovered(self, pos, mode):
        '''hovered lot highlighting:'''
        if mode == "road_placing":
            self.city_space.road_system.hovered(self.get_clicked_road(pos))

        else:
            if pos is None:
                if self.hovered_lot:
                    self.hovered_lot.hovered = False
                self.hovered_lot = None
                return

            hovered_lot = self.get_clicked_lot(pos)
            if hovered_lot:
                hovered_lot.hovered = True

                if self.hovered_lot and self.hovered_lot != hovered_lot:
                    self.hovered_lot.hovered = False

                self.hovered_lot = hovered_lot

    def add_move_speed(self, move_speed):
        self.move_speed = (
            self.move_speed[0] + move_speed[0], self.move_speed[1] + move_speed[1])

    def zoom(self, zoom_value):
        old_scale = self.scale
        self.scale = int(self.scale * zoom_value)
        self.scale = max([WINDOW_SIZE[1] // self.height + 1,
                         WINDOW_SIZE[0] // self.width + 1, self.scale])
        self.scale = min(self.scale, 500)

        mouse_x, mouse_y = pg.mouse.get_pos()
        self.pov_x -= int((mouse_x - self.pov_x)*(self.scale/old_scale - 1))
        self.pov_y -= int((mouse_y - self.pov_y)*(self.scale/old_scale - 1))

    def select_lot(self, mouse_pos):
        if self.selected_lot:
            self.selected_lot.selected = False
        clicked_lot = self.get_clicked_lot(mouse_pos)
        if clicked_lot:
            clicked_lot.selected = True
        self.selected_lot = clicked_lot

    def get_clicked_lot(self, mouse_pos):
        if mouse_pos is None:
            return None
        x = (mouse_pos[0] - self.pov_x +
             self.scale*self.width//2) // self.scale
        y = (mouse_pos[1] - self.pov_y +
             self.scale*self.height//2) // self.scale
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.city_space.lots[x][y]

    def get_clicked_road(self, mouse_pos):
        if mouse_pos is None:
            return
        x = (mouse_pos[0] - self.pov_x +
             self.scale*(self.width/2 - ROAD_WIDTH_RATIO/2)) / self.scale
        y = (mouse_pos[1] - self.pov_y +
             self.scale*(self.height/2 - ROAD_WIDTH_RATIO/2)) / self.scale
        return x, y

    def highlight_access(self, window):
        if self.selected_lot is None or self.selected_lot.construct is None:
            return

        LotGraphics.highlight_lot(
            self.selected_lot, (self.pov_x, self.pov_y), self.scale, self.AFFECTS_COLOR)

        for lot in self.selected_lot.affects:
            if lot == self.selected_lot:
                continue
            LotGraphics.highlight_lot(
                lot, (self.pov_x, self.pov_y), self.scale, self.AFFECTED_COLOR)

    @staticmethod
    def set_speed(speed):
        LotGraphics.animation_speed = 0.05*speed
        RoadGraphics.car_speed = 0.02*speed
