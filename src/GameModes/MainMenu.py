from GameModes.GameMode import *
import pygame as pg
import pygame_menu as pgmen
import os

class MainMenu(GameMode):
    def __init__(self, WINDOW, save):
        self.save_manager = save
        self.change_mode = False
        self.redraw = True
        self.WINDOW = WINDOW
        width, height = self.WINDOW.get_size()

        self.background = pg.image.load(os.path.join('Assets', 'menu_background.jpg'))
        self.background = pg.transform.scale(self.background, self.WINDOW.get_size())

        self.menu = pgmen.Menu(title='City Simulation Game', width=width*0.6, height=height*0.85, theme=pgmen.themes.THEME_SOLARIZED)

    def redraw_needed(self):
        self.redraw = not self.redraw
        return not self.redraw

    def update(self):
        self.WINDOW.blit(self.background, (0,0))
        self.menu.draw(self.WINDOW)
        pg.display.update()

            

    def handle(self, event):
        next_game_mode = self

    def draw(self):
        pass
