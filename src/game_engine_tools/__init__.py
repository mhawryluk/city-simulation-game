import os
import pygame as pg

WINDOW_SIZE = (1200, 800)
FPS = 60


def load_asset(*args):
    return pg.image.load(os.path.join('Assets', *args))


def get_asset_path(*args):
    return os.path.join('Assets', *args)
