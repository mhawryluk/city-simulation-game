import os
import pygame as pg

WINDOW_SIZE = (1920, 1020)
FPS = 60


def load_asset(*args):
    return pg.image.load(os.path.join('Assets', *args))


def get_asset_path(*args):
    return os.path.join('Assets', *args)


def volume_up():
    volume = pg.mixer.music.get_volume()
    pg.mixer.music.set_volume(min(1, volume + 0.1))


def volume_down():
    volume = pg.mixer.music.get_volume()
    pg.mixer.music.set_volume(max(0, volume - 0.1))


def make_safe_range(minval, maxval):
    def safe_range(since, to):
        start = max(minval, since)
        end = min(maxval, to)
        return range(start, end)

    return safe_range


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
