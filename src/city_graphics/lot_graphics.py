from game_engine_tools import WINDOW_SIZE
from city_graphics import ROAD_WIDTH_RATIO
import game_engine_tools.simulation_tools as sim_consts
import pygame as pg


class LotGraphics:
    frame = 0
    zone_highlighting = False
    zone_colors = {'residential': (61, 143, 102),
                   'commercial': (92, 153, 214),
                   'industrial': (173, 102, 31)}

    @classmethod
    def draw_background(cls, lot, scale, pov):
        x, y = cls.get_draw_position(lot, pov, scale)

        if not (-scale <= x < WINDOW_SIZE[0] and -scale <= y < WINDOW_SIZE[1]):
            return

        # lot type pictures
        for picture in cls.city_images.get_images(lot.type, lot.seed):
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
        events = lot.construct.get_current_events()
