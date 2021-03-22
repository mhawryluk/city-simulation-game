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

        self.background = None
        self.menu = None
        self.play_button = None

        self.create_menu_window()

    def create_menu_window(self):
    
        width, height = self.WINDOW.get_size()

        self.background = pg.image.load(os.path.join('Assets', 'menu_background.jpg'))
        self.background = pg.transform.scale(self.background, self.WINDOW.get_size())

        self.menu = pgmen.Menu(title='City Simulation Game', width=width*0.6, height=height*0.85, theme=pgmen.themes.THEME_SOLARIZED, 
        mouse_enabled=True, mouse_motion_selection=True)

        self.play_button = self.menu.add.button('Play', self.play)

    def redraw_needed(self):
        self.redraw = not self.redraw
        return not self.redraw

    def update(self):
        self.draw()
        

    def play(self):
        #configure save
        #self.change_mode = True  
        print("PLAY")          

    def handle(self, event):
        if self.menu.is_enabled():
            self.menu.update([event])
            self.draw()

    def draw(self):
        self.WINDOW.blit(self.background, (0,0))
        self.menu.draw(self.WINDOW)
        pg.display.update()
