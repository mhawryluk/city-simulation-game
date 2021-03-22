import pygame as pg
import os
import json as js
import GameModes.MainMenu as mm
from GameModes.GameWindow import *


class GameEngine:
    def __init__(self):
        self.running = False
        pg.init()
        pg.display.set_caption('City Simulation Game')

        self.MEASUREMENTS = (1000, 600)
        self.WINDOW = pg.display.set_mode(self.MEASUREMENTS)
        self.FPS = 60
        self.clock = pg.time.Clock()

        self.save_manager = SaveManager()
        self.game_mode = mm.MainMenu(self.WINDOW, self.save_manager)
        #self.game_mode = GameWindow(self.WINDOW, None, 50, 50)

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
        self.saves_list = []
        self.load_settings()

    def generate_base_settings(self, settings_file):
        settings = dict()
        settings['active_save'] = None
        settings['saves_amount'] = 0
        settings['max_saves_amount'] = 500
        with open(settings_file, 'w') as new_settings_file:
            js.dump(settings, new_settings_file)

    def generate_game_save_source(self):
        pass

    def load_settings(self):
        settings_file = os.path.join('SaveFiles', 'settings.json')

        if not os.path.isfile(settings_file):
            self.generate_base_settings(settings_file)

        with open(settings_file, 'r') as settings:
            self.active_settings = js.load(settings)

    def save_settings(self):
        pass

    def create_save(self, name):
        save_id = settings['saves_amount'] + 1
        if save_id >= settings['max_saves_amount']:
            #error
        else:
            settings['saves_amount'] = save_id
            self.active_save = {'name':name, 'id':save_id}

            self.save()

    def activate_save(self, save_id):
        self.active_settings['active_save'] = save_id

    def load_save(self, save_id):
        try:
            pass
        except:
            pass

    def save(self):
        save_id = self.activate_save['id']
        self.active_save['last_saved'] = pg.time.get_time()
        save_path = os.path.join('SaveFiles', 'save' + save_id + '.json')
        with open(save_path, 'w') as save_file:
            js.dump(self.activate_save, save_file)
