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
    fire_images = [load_asset('Animations', f'flame{i}.png') for i in range(5)]
    unhappy_images = [load_asset('Status', 'icon_sad.png'), load_asset(
        'Status', 'icon_cry.png')]
    pandemic_images = [load_asset(
        'Animations', f'coronavirus-red-rim-light-pulse_{i}.png') for i in range(7)]
    burglary_images = [load_asset(
        'Animations', 'Roll jump', f'rj_{i:03}.png') for i in range(37)]
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
            image = cls.fire_images[cls.frame //
                                    cls.animation_speed % len(cls.fire_images)]
            scaled_image = pg.transform.scale(image, (size, size))
            cls.window.blit(scaled_image, (x + scale/2 - size/2, y))

        if 'unhappy' in events:
            icon_size = int(scale/5)
            image = cls.unhappy_images[cls.frame //
                                       cls.animation_speed % len(cls.unhappy_images)]
            scaled_image = pg.transform.scale(image, (icon_size, icon_size))
            cls.window.blit(scaled_image, (x + scale/2 - icon_size/2, y))

        if 'pandemic' in events:
            icon_size = int(scale/2)
            image = cls.pandemic_images[cls.frame //
                                        cls.animation_speed % len(cls.pandemic_images)]
            scaled_image = pg.transform.scale(image, (icon_size, icon_size))
            cls.window.blit(scaled_image, (x + scale/2 -
                            icon_size/2, y + scale/2 - icon_size/2))

        if 'burglary' in events:
            icon_size = int(scale/2)
            image = cls.burglary_images[cls.frame//10 %
                                        len(cls.burglary_images)]
            scaled_image = pg.transform.scale(image, (icon_size, icon_size))
            cls.window.blit(scaled_image, (x + scale/2 -
                            icon_size/2, y + scale/2 - icon_size/2))
