import pygame as pg
<<<<<<< HEAD
import os
import json as js
import GameModes.MainMenu as mm
=======
from GameModes.MainMenu import *
from GameModes.GameWindow import *

>>>>>>> a8348588cf2c08e76e1718a09ae930b3fe0101d3

class GameEngine:
    def __init__(self):
        self.running = False
        pg.init()
        pg.display.set_caption('City Simulation Game')

        self.MEASUREMENTS = (1000, 600)
        self.WINDOW = pg.display.set_mode(self.MEASUREMENTS)
        self.FPS = 60
        self.clock = pg.time.Clock()

<<<<<<< HEAD
        self.save_manager = SaveManager()
        self.game_mode = mm.MainMenu(self.WINDOW, self.save_manager)
=======
        #self.game_mode = MainMenu(self.WINDOW)
        self.game_mode = GameWindow(self.WINDOW, None, 50, 50)
>>>>>>> a8348588cf2c08e76e1718a09ae930b3fe0101d3

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(self.FPS)
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

    def change_mode(self):
        pass


class SaveManager:
    def __init__(self):
        self.active_save = None
        self.active_settings = None

        settings_file = os.path.join('SaveFiles', 'settings.json')

        if not os.path.isfile(settings_file):
            self.generate_base_settings(settings_file)
       
        with open(settings_file, 'r') as settings:
            self.active_settings = js.load(settings)
            
        self.load_save(self.active_settings.get('active_save', None))

    def generate_base_settings(self, settings_file):
        settings = dict()
        settings['active_save'] = None
        with open(settings_file, 'w') as new_settings_file:
            js.dump(settings, new_settings_file)

    def generate_game_save_source(self):
        pass

    def load_settings(self):
        pass

    def save_settings(self):
        pass

    def load_save(self, save_id):
        if save_id != None:
            pass

    def save(self):
        pass

