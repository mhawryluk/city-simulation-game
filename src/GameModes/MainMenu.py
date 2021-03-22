from GameModes.GameMode import *
import pygame as pg
import os

class MainMenu(GameMode):
    def __init__(self, WINDOW, save):
        self.save_manager = save
        self.change_mode = False
        self.redraw = True
        self.WINDOW = WINDOW

        self.background = pg.image.load(os.path.join('Assets', 'menu_background.jpg'))
        self.background = pg.transform.scale(self.background, self.WINDOW.get_size())

    def redraw_needed(self):
        self.redraw = not self.redraw
        return not self.redraw

    def update(self):
        if self.redraw_needed():
            self.WINDOW.blit(self.background, (0,0))
            pg.display.update()

    def handle(self, event):
        next_game_mode = self

    def draw(self):
        pass
