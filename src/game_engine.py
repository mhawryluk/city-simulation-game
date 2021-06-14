import json as js
import os

import pygame as pg

from game_engine_tools import FPS, WINDOW_SIZE, load_asset
from game_engine_tools.save_manager import SaveManager
from game_modes.gameplay_mode import GameplayMode
from game_modes.main_menu import MainMenu


class GameEngine:
    """main class that runs the game"""

    def __init__(self):
        self.running = False
        pg.init()
        pg.display.set_caption('City Simulation Game')
        pg.display.set_icon(load_asset('House', 'H01.png'))
        try:
            pg.mixer.music.load(os.path.join(
                'Assets', 'Music', 'background_music.ogg'))
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play()
        except Exception as e:
            print("couldn't play the music")
            print(e)
            pass  # if music drivers don't work - don't play the music

        self.window = pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.save_manager = SaveManager()
        self.game_mode = MainMenu(self.window, self.save_manager)
        self.map_name = 'map2'

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(FPS)
            pg.display.update()
            self.game_mode.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                else:
                    self.game_mode.handle(event)
                    if self.game_mode.change_mode:
                        self.change_mode()

    @staticmethod
    def get_map(map_name):
        with open(f'Maps/{map_name}.json', 'r') as f:
            return js.load(f)

    def change_mode(self):
        if isinstance(self.game_mode, MainMenu):
            map_ = self.get_map(self.map_name)
            if map_ is None:
                self.game_mode = GameplayMode(
                    self.window, self.save_manager, 10, 10)
            else:
                self.game_mode = GameplayMode(
                    self.window, self.save_manager, map_['height'], map_['width'], map_['map'])
        else:
            self.game_mode = MainMenu(self.window, self.save_manager)
