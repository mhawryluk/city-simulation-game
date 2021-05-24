from game_engine_tools import WINDOW_SIZE
from city_graphics import ROAD_WIDTH_RATIO
from city_graphics.city_images import CITY_IMAGES
import game_engine_tools.simulation_tools as sim_consts
from game_engine_tools import load_asset
import pygame as pg


class LotGraphics:
    frame = 0
    zone_highlighting = False
    zone_colors = {'residential': (61, 143, 102),
                   'commercial': (92, 153, 214),
                   'industrial': (173, 102, 31)}
    animation_speed = 50

    @classmethod
    def draw_background(cls, lot, scale, pov):
        x, y = cls.get_draw_position(lot, pov, scale)

        if not (-scale <= x < WINDOW_SIZE[0] and -scale <= y < WINDOW_SIZE[1]):
            return

        # lot type pictures
        for picture in CITY_IMAGES.get_images(lot.type, lot.seed):
            cls.window.blit(picture, (x, y))

    @classmethod
    def draw_construct(cls, lot, scale, pov):
        x, y = cls.get_draw_position(lot, pov, scale)

        if not (-scale <= x < WINDOW_SIZE[0] and -scale <= y < WINDOW_SIZE[1]):
            return

        # construct
        if lot.construct:
            offset = int(ROAD_WIDTH_RATIO*scale)
            new_scale = int(scale*(1 - ROAD_WIDTH_RATIO))
            image = lot.construct.image
            width, height = image.get_width(), image.get_height()
            ratio = new_scale/width
            new_width, new_height = int(width*ratio), int(height*ratio)
            new_x = x + offset
            new_y = y - new_height + new_scale + offset
            pic = pg.transform.scale(
                lot.construct.image, (new_width, new_height))
            cls.window.blit(pic, (new_x, new_y))

            # simulation effects
            cls.draw_simulation_effects(lot, pov, scale)

        # zone highlighting
        if cls.zone_highlighting and lot.zone_type:
            alpha = pg.Surface((scale, scale))
            alpha.set_alpha(128)
            alpha.fill(cls.zone_colors[lot.zone_type])
            cls.window.blit(alpha, (x, y))

    @classmethod
    def get_draw_position(cls, lot, pov, scale):
        return pov[0] - scale*cls.map_dimensions[0]//2 + scale*lot.x, pov[1] - scale*cls.map_dimensions[1]//2 + scale*lot.y

    @classmethod
    def draw_simulation_effects(cls, lot, pov, scale):
        cls.frame += 1
        events = lot.get_current_events()
        x, y = cls.get_draw_position(lot, pov, scale)

        if 'burning' in events:
            size = scale
            image = CITY_IMAGES.get_animation_image(
                'fire', cls.frame//cls.animation_speed, size)
            cls.window.blit(image, (x + scale/2 - size/2, y))

        if 'unhappy' in events:
            size = int(scale/5)
            image = CITY_IMAGES.get_animation_image(
                'unhappy', cls.frame//cls.animation_speed, size)
            cls.window.blit(image, (x + scale/2 - size/2, y))

        if 'pandemic' in events:
            size = int(scale/2)
            image = CITY_IMAGES.get_animation_image(
                'pandemic', cls.frame//cls.animation_speed, size)
            cls.window.blit(
                image, (x + scale/2 - size/2, y + scale/2 - size/2))

        if 'burglary' in events:
            size = int(scale/2)
            image = CITY_IMAGES.get_animation_image(
                'burglary', cls.frame//10, size)
            cls.window.blit(
                image, (x + scale/2 - size/2, y + scale/2 - size/2))
