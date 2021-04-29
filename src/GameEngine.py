from GameModes.GameWindow import GameWindow
from GameEngineTools.SaveManager import SaveManager
import pygame as pg
import os
from GameModes.MainMenu import MainMenu


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
        self.game_mode = MainMenu(self.WINDOW, self.save_manager)

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
        if isinstance(self.game_mode, MainMenu):
            self.game_mode = GameWindow(
                self.WINDOW, self.save_manager, 50, 50)
        else:
            self.game_mode = MainMenu(self.WINDOW, self.save_manager)
