import os
import pygame as pg

WINDOW_SIZE = (1200, 800)
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