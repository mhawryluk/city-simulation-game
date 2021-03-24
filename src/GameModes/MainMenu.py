from GameModes.GameMode import *
from GameEngineTools.SaveManager import SaveManager
import pygame as pg
import pygame_menu as pgmen
import os

class MainMenu(GameMode):
    def __init__(self, WINDOW, save: SaveManager):
        self.save_manager = save
        self.change_mode = False
        self.redraw = True
        self.WINDOW = WINDOW

        self.background = None
        self.menu = None
        self.play_button = None
        self.save_button = None

        self.create_menu_window()

    @classmethod
    def create_menu_window(self):
    
        width, height = self.WINDOW.get_size()

        self.background = pg.image.load(os.path.join('Assets', 'menu_background.jpg'))
        self.background = pg.transform.scale(self.background, self.WINDOW.get_size())

        self.menu = pgmen.Menu(title='City Simulation Game', width=width*0.6, height=height*0.85, theme=pgmen.themes.THEME_SOLARIZED, 
        mouse_enabled=True, mouse_motion_selection=True)

        if(self.save.has_active_save()):
            self.play_button = self.menu.add.button('Play', self.play)
            self.save_button = self.menu.add_button('Choose save', self.save_menu)
        else:
            self.play_button = None
            self.save_button = self.menu.add_button('Create save', self.save_menu)
    
    @classmethod
    def save_menu(self):
        print("Save")

    @classmethod
    def play(self):
        #configure save
        #self.change_mode = True  
        print("PLAY")  

    def update(self):
        self.draw()        

    def handle(self, event):
        if self.menu.is_enabled():
            self.menu.update([event])
            self.draw()

    def draw(self):
        self.WINDOW.blit(self.background, (0,0))
        self.menu.draw(self.WINDOW)
        pg.display.update()
