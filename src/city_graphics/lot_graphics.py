from math import floor

import pygame as pg

from city_graphics import ROAD_WIDTH_RATIO
from city_graphics.city_images import CityImages
from game_engine_tools import WINDOW_SIZE, Singleton


class LotGraphics(metaclass=Singleton):
    zone_colors = {'residential': 0x60d394,
                   'commercial': 0x8fb8ed,
                   'industrial': 0xffd97d}
    animation_speed = 0.05
    map_dimensions = None
    zone_highlighting = False
    city_images = CityImages()

    def __init__(self, map_dimensions):
        self.frame = 0
        LotGraphics.map_dimensions = map_dimensions

    @classmethod
    def reset(cls):
        cls.animation_speed = 0.05

    def draw_background(self, lot, scale, pov, window):
        x, y = self.get_draw_position(lot, pov, scale)

        if not (-scale <= x < WINDOW_SIZE[0] and -scale <= y < WINDOW_SIZE[1]):
            return

        # lot type pictures
        for picture in self.city_images.get_images(lot.type, lot.seed):
            window.blit(picture, (x, y))

    def draw_construct(self, lot, scale, pov, window):
        x, y = self.get_draw_position(lot, pov, scale)

        if not (-scale <= x < WINDOW_SIZE[0] and -scale <= y < WINDOW_SIZE[1]):
            return

        # constructs
        if lot.construct:
            offset = int(ROAD_WIDTH_RATIO * scale)
            new_scale = int(scale * (1 - ROAD_WIDTH_RATIO))
            image = lot.construct.image
            width, height = image.get_width(), image.get_height()
            ratio = new_scale / width
            new_width, new_height = int(width * ratio), int(height * ratio)
            new_x = x + offset
            new_y = y - new_height + new_scale + offset
            pic = pg.transform.scale(
                lot.construct.image, (new_width, new_height))
            window.blit(pic, (new_x, new_y))

            # simulation effects
            self.draw_simulation_effects(lot, pov, scale, window)

        # zone highlighting
        if self.zone_highlighting and lot.zone_type:
            self.highlight_lot(lot, pov, scale, self.zone_colors[lot.zone_type], window)

    @classmethod
    def get_draw_position(cls, lot, pov, scale):
        return pov[0] - scale * cls.map_dimensions[0] // 2 + scale * lot.x, pov[1] - scale * cls.map_dimensions[
            1] // 2 + scale * lot.y

    def highlight_lot(self, lot, pov, scale, color, window):
        x, y = self.get_draw_position(lot, pov, scale)
        x += int(scale * ROAD_WIDTH_RATIO // 2)
        y += int(scale * ROAD_WIDTH_RATIO // 2)
        alpha = pg.Surface((scale, scale))
        alpha.set_alpha(128)
        alpha.fill(color)
        window.blit(alpha, (x, y))

    def draw_simulation_effects(self, lot, pov, scale, window):
        self.frame += self.animation_speed

        events = lot.current_events
        x, y = self.get_draw_position(lot, pov, scale)

        if 'burning' in events:
            size = scale
            image = self.city_images.get_animation_image(
                'fire', floor(self.frame) // 5, size)
            window.blit(image, (x + scale / 2 - size / 2, y))

        if 'unhappy' in events:
            size = int(scale / 5)
            image = self.city_images.get_animation_image(
                'unhappy', floor(self.frame) // 10, size)
            window.blit(image, (x + scale / 2 - size / 2, y))

        if 'pandemic' in events:
            size = int(scale / 2)
            image = self.city_images.get_animation_image(
                'pandemic', floor(self.frame), size)
            window.blit(
                image, (x + scale / 2 - size / 2, y + scale / 2 - size / 2))

        if 'burglary' in events:
            size = int(scale / 2)
            image = self.city_images.get_animation_image(
                'burglary', floor(self.frame), size)
            window.blit(
                image, (x + scale / 2 - size / 2, y + scale / 2 - size / 2))
