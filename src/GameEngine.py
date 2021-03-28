from GameModes.GameWindow import *
from GameEngineTools.SaveManager import SaveManager
import pygame as pg
import os
import GameModes.MainMenu as mm


class GameEngine:
    def __init__(self):
        self.running = False
        pg.init()
        pg.display.set_caption('City Simulation Game')

        self.MEASUREMENTS = (1200, 800)
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
        self.game_mode = GameWindow(self.WINDOW, None, 50, 50)
