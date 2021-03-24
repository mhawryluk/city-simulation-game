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
        self.window = WINDOW

        self.background = None
        self.menu = None
        self.save_menu = None
        self.save_menu_active = False
        self.play_button = None
        self.save_button = None

        self.create_menu_window()

    def create_menu_window(self):
        width, height = self.window.get_size()

        self.background = pg.image.load(os.path.join('Assets', 'menu_background.jpg'))
        self.background = pg.transform.scale(self.background, self.window.get_size())

        self.menu = pgmen.Menu(title='City Simulation Game', width=width*0.6, height=height*0.85, theme=self.get_theme(), 
        mouse_enabled=True, mouse_motion_selection=True)
        self.save_menu = pgmen.Menu(title='Saves', width=width*0.48, height=height*0.85, theme=self.get_theme(), 
        mouse_enabled=True, mouse_motion_selection=True)

        self.save_menu.add_button('Back', self.change_save_menu_status)

        if(not self.save_manager.has_active_save()):
            self.play_button = self.menu.add.button('Play', self.play)
            self.save_button = self.menu.add_button('Choose save', self.change_save_menu_status)
        else:
            self.play_button = None
            self.save_button = self.menu.add_button('Create save', self.change_save_menu_status)
    
    def change_save_menu_status(self):
        self.save_menu_active = not self.save_menu_active

    def play(self):
        self.change_mode = True 

    def update(self):
        self.draw()        

    def handle(self, event):
        if self.save_menu_active:
            self.save_menu.update([event])
        elif self.menu.is_enabled():
            self.menu.update([event])

        self.draw()

    def draw(self):
        self.window.blit(self.background, (0,0))
        if self.save_menu_active:
            self.save_menu.draw(self.window)
        else:
            self.menu.draw(self.window)
        
        pg.display.update()

    def get_theme(self):
        theme = pgmen.themes.THEME_SOLARIZED.copy()
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (0, 0, 0)
        theme.widget_border_color = (0, 0, 0)
        theme.widget_border_width = 2
        return theme

