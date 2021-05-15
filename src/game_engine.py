from game_modes.game_window import GameWindow
from game_engine_tools.save_manager import SaveManager
import pygame as pg
from game_modes.main_menu import MainMenu
from game_engine_tools import FPS, WINDOW_SIZE


class GameEngine:
    def __init__(self):
        self.running = False
        pg.init()
        pg.display.set_caption('City Simulation Game')

        self.window = pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.save_manager = SaveManager()
        self.game_mode = MainMenu(self.window, self.save_manager)

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

    def change_mode(self):
        if isinstance(self.game_mode, MainMenu):
            self.game_mode = GameWindow(self.window, self.save_manager, 10, 10)
        else:
            self.game_mode = MainMenu(self.window, self.save_manager)
