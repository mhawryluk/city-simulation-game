import os
import pygame as pg


def load_asset(*args):
    return pg.image.load(os.path.join('Assets', *args))


def get_asset_path(*args):
    return os.path.join('Assets', *args)
